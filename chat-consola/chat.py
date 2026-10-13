"""Chat final del asesor de «Turismo Colombia (simulada)»: todo lo del Nivel 1 en un solo programa.

Une streaming (3.3), costos (3.4), parámetros (3.5), modelo (3.6), memoria por cliente (3.7) y
reglas contra inventar (3.8). Resuelve los dos problemas del 3.7: la memoria se guarda en la base
del piloto (no se pierde al cerrar) y se envía con ventana (no crece sin límite).

Uso:  python chat.py                      chat en consola; /cliente N elige un cliente del piloto
      python chat.py --piloto             atiende a los 10 clientes con su guion (paso D.2)
      python chat.py --sonda-completa     misma pregunta de cierre, pero con el historial completo
Comandos dentro del chat: /ayuda  /cliente N  /tokens  /historial  /reset  /salir
"""
import argparse
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent / "etapas"))
import base_piloto as bd  # noqa: E402
from caso_simulado import construir_system, costo_usd  # noqa: E402

# ============================================================
# 1. CONFIGURACION
# ============================================================
load_dotenv()

MODEL = os.getenv("CHAT_MODEL", "claude-haiku-5-5")  # 3.6: Haiku dio la misma cifra por 20 a 41 veces menos
MAX_TOKENS = 2048          # 3.5: holgado; un tope bajo deja al asesor sin responder
EFFORT = "low"             # 3.5: en preguntas de catálogo el esfuerzo no cambió las cifras
SYSTEM_PROMPT = construir_system(con_reglas=True)   # 3.8: catálogo + reglas contra inventar
MAX_TURNS = 5              # 3.4: ventana de 5 turnos, −16 % calculado
CONFIG = "reglas|ventana5|low"   # etiqueta con la que se guardan los mensajes de este chat
EJEC = {"effort": EFFORT, "ventana": str(MAX_TURNS), "catalogo": "completo"}

# Pregunta de cierre para medir la memoria: ¿el asesor conserva el dato clave del cliente?
PREGUNTA_CIERRE = ("antes de seguir, me confirmas los datos de mi viaje que te he dado? "
                   "personas, fechas y cualquier cosa importante que te haya dicho")
DATO_CLAVE = {   # cliente_id -> patrón que debe aparecer en la respuesta si lo recuerda
    1: r"14 de febrero", 2: r"4.{0,12}7.{0,12}11", 3: r"\b6\b|seis", 4: r"movilidad",
    5: r"3 (al|y el|de) 6 de noviembre|3 de noviembre", 6: r"carne|vegetarian",
    7: r"Piedra Azul", 8: r"3 millones|3\.000\.000|tres millones", 9: r"man[ií]",
    10: r"480\.000|Casa Naranja",
}

# ============================================================
# 2. MEMORIA (en la base del piloto, con ventana)
# ============================================================
def cargar_historial(con, cliente_id: int, config: str = CONFIG) -> list[dict]:
    """Todo lo que el cliente ha hablado con el asesor en esta configuración."""
    return bd.historial(con, cliente_id, config=config)


def guardar_turno(con, cliente_id: int, turno: int, texto: str, respuesta: str, config: str = CONFIG) -> None:
    con.execute("insert or replace into mensajes (cliente_id, config, turno, rol, contenido) values (?, ?, ?, 'cliente', ?)",
                (cliente_id, config, turno, texto))
    con.execute("insert or replace into mensajes (cliente_id, config, turno, rol, contenido) values (?, ?, ?, 'asesor', ?)",
                (cliente_id, config, turno, respuesta))
    con.commit()


def recortar(messages: list[dict], max_turns: int = MAX_TURNS) -> list[dict]:
    """Ventana deslizante: conserva los últimos max_turns turnos y empieza siempre en 'user'."""
    messages = messages[-max_turns * 2:]
    while messages and messages[0]["role"] != "user":
        messages = messages[1:]
    return messages

# ============================================================
# 3. LLAMADA AL MODELO
# ============================================================
def construir_peticion(messages: list[dict]) -> dict:
    """Parámetros comunes: se usan para enviar y para contar tokens, así nunca se desalinean."""
    return {"model": MODEL, "system": SYSTEM_PROMPT, "messages": messages,
            "output_config": {"effort": EFFORT}}


def responder(client, messages: list[dict], mostrar: bool = True):
    """Envía la ventana con streaming; devuelve (texto, mensaje_final). Reintenta si hay límite de velocidad."""
    for intento in range(8):
        try:
            partes = []
            with client.messages.stream(max_tokens=MAX_TOKENS, **construir_peticion(messages)) as stream:
                for evento in stream:
                    if evento.type == "text":
                        if mostrar:
                            print(evento.text, end="", flush=True)
                        partes.append(evento.text)
                final = stream.get_final_message()
            if mostrar:
                print()
            return "".join(partes), final
        except anthropic.RateLimitError:
            if mostrar:
                raise
            time.sleep(15 + 10 * intento)
    raise RuntimeError("demasiados reintentos por límite de velocidad")


def registrar(con, cliente_id: int, turno: int, final, segundos: float, ejec: dict = EJEC) -> float:
    u = final.usage
    razon = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", 0) or 0
    costo = costo_usd(MODEL, u.input_tokens, u.output_tokens)
    con.execute(
        "insert or replace into ejecuciones (cliente_id, turno, modelo, effort, ventana, catalogo, tokens_entrada, "
        "tokens_salida, tokens_razonamiento, costo_usd, segundos, stop_reason) values (?,?,?,?,?,?,?,?,?,?,?,?)",
        (cliente_id, turno, MODEL, ejec["effort"], ejec["ventana"], ejec["catalogo"], u.input_tokens,
         u.output_tokens, razon, costo, segundos, final.stop_reason))
    con.commit()
    return costo


def atender_turno(client, con, cliente_id: int, texto: str, mostrar: bool = True):
    """Un turno completo: cargar → agregar → recortar → enviar → guardar → registrar."""
    completo = cargar_historial(con, cliente_id)
    turno = len(completo) // 2 + 1
    ventana = recortar(completo + [{"role": "user", "content": texto}])
    inicio = time.perf_counter()
    respuesta, final = responder(client, ventana, mostrar)
    segundos = time.perf_counter() - inicio
    if final.stop_reason == "max_tokens":
        print("  (respuesta cortada: se alcanzó MAX_TOKENS)")
    guardar_turno(con, cliente_id, turno, texto, respuesta or "(sin respuesta)")
    return respuesta, final, registrar(con, cliente_id, turno, final, segundos)

# ============================================================
# 4. COMANDOS
# ============================================================
AYUDA = """Comandos:
  /cliente N  atender al cliente N del piloto (1 a 10)
  /tokens     tamaño de lo que se enviará en la próxima llamada y costo de la sesión
  /historial  la ventana que se reenvía (los últimos turnos)
  /reset      borra la memoria de este cliente en esta configuración
  /salir      termina (la memoria ya queda guardada en la base)"""


def mostrar_tokens(client, con, cliente_id, total):
    ventana = recortar(cargar_historial(con, cliente_id))
    if ventana:
        n = client.messages.count_tokens(**construir_peticion(ventana)).input_tokens
        print(f"Próxima llamada: {n} tokens de entrada + el mensaje nuevo ({len(ventana)} mensajes en la ventana)")
    print(f"Sesión: {total[0]:.5f} USD")


def mostrar_historial(con, cliente_id):
    ventana = recortar(cargar_historial(con, cliente_id))
    if not ventana:
        print("(memoria vacía)")
    for i, m in enumerate(ventana, 1):
        quien = "Cliente" if m["role"] == "user" else "Asesor"
        t = m["content"].replace("\n", " ")
        print(f"{i:>3}. {quien}: {t[:90]}{'...' if len(t) > 90 else ''}")

# ============================================================
# 5. BUCLE PRINCIPAL (consola)
# ============================================================
def main(client=None) -> None:
    if client is None:
        if not os.getenv("ANTHROPIC_API_KEY"):
            sys.exit("Falta ANTHROPIC_API_KEY. Crea el archivo .env (mira .env.example).")
        client = anthropic.Anthropic()
    con = bd.conectar()
    clientes = {c["id"]: c["nombre"] for c in bd.cargar_clientes(con)}
    cliente_id, total = 1, [0.0]
    print(f"Asesor de Turismo Colombia (simulada) · {MODEL} · ventana {MAX_TURNS} turnos · escribe /ayuda")
    print(f"Atendiendo a {clientes[cliente_id]} ({len(cargar_historial(con, cliente_id)) // 2} turnos guardados)")

    while True:
        try:
            texto = input(f"\n{clientes[cliente_id]}: ").strip()
        except (EOFError, KeyboardInterrupt):
            texto = "/salir"
        if not texto:
            continue
        if texto == "/salir":
            print("\nLa memoria de cada cliente queda en la base del piloto. Hasta luego.")
            break
        if texto == "/ayuda":
            print(AYUDA)
            continue
        if texto.startswith("/cliente"):
            try:
                cliente_id = int(texto.split()[1]) if int(texto.split()[1]) in clientes else cliente_id
            except (IndexError, ValueError):
                pass
            print(f"Atendiendo a {clientes[cliente_id]} ({len(cargar_historial(con, cliente_id)) // 2} turnos guardados)")
            continue
        if texto == "/reset":
            con.execute("delete from mensajes where cliente_id = ? and config = ?", (cliente_id, CONFIG))
            con.commit()
            print("Memoria de este cliente borrada.")
            continue
        if texto == "/historial":
            mostrar_historial(con, cliente_id)
            continue
        if texto == "/tokens":
            try:
                mostrar_tokens(client, con, cliente_id, total)
            except anthropic.APIError as e:
                print(f"[No se pudo contar: {e}]")
            continue

        print("Asesor: ", end="", flush=True)
        try:
            _, _, costo = atender_turno(client, con, cliente_id, texto)
            total[0] += costo
        except anthropic.AuthenticationError:
            print("\n[API key inválida. Revisa tu .env]")
        except anthropic.RateLimitError:
            print("\n[Límite de uso alcanzado. Espera un momento y reintenta]")
        except anthropic.APIConnectionError:
            print("\n[Sin conexión con la API. Revisa tu internet]")
        except anthropic.APIStatusError as e:
            print(f"\n[Error {e.status_code} de la API: {e.message}]")
    con.close()

# ============================================================
# 6. PILOTO (paso D.2): los 10 clientes con su guion, más la pregunta de cierre
# ============================================================
def piloto(tope_usd: float, trabajadores: int) -> None:
    client = anthropic.Anthropic()
    con0 = bd.conectar()
    clientes = bd.cargar_clientes(con0)
    con0.close()
    gasto, lock, parar = {"usd": 0.0, "n": 0}, threading.Lock(), threading.Event()

    def atender(c):
        con = bd.conectar()
        guion = c["guion"] + [PREGUNTA_CIERRE]
        hechos = len(cargar_historial(con, c["id"])) // 2
        for texto in guion[hechos:]:
            if parar.is_set():
                return f"{c['nombre']}: detenido"
            _, _, costo = atender_turno(client, con, c["id"], texto, mostrar=False)
            with lock:
                gasto["usd"] += costo
                gasto["n"] += 1
                if gasto["usd"] >= tope_usd:
                    parar.set()
        con.close()
        return f"{c['nombre']}: {len(guion)} turnos"

    with ThreadPoolExecutor(max_workers=trabajadores) as ex:
        for r in ex.map(atender, clientes):
            print(r, f"| {gasto['n']} llamadas, {gasto['usd']:.4f} USD", flush=True)
    print(f"\nListo: {gasto['n']} llamadas nuevas, {gasto['usd']:.4f} USD")


def sonda_completa() -> None:
    """La misma pregunta de cierre con el historial COMPLETO del 3.4 (mismas reglas y effort):
    aísla el efecto de la ventana sobre la memoria. No guarda mensajes; sí registra la ejecución."""
    client = anthropic.Anthropic()
    con = bd.conectar()
    total = 0.0
    for c in bd.cargar_clientes(con):
        mensajes = bd.historial(con, c["id"]) + [{"role": "user", "content": PREGUNTA_CIERRE}]
        inicio = time.perf_counter()
        respuesta, final = responder(client, mensajes, mostrar=False)
        total += registrar(con, c["id"], len(c["guion"]) + 1, final, time.perf_counter() - inicio,
                           {"effort": EFFORT, "ventana": "completa", "catalogo": "completo"})
        con.execute("insert or replace into mensajes (cliente_id, config, turno, rol, contenido) values (?, ?, ?, 'asesor', ?)",
                    (c["id"], "sonda-completa", len(c["guion"]) + 1, respuesta))
        con.commit()
        print(f"{c['nombre']}: {'recuerda' if re.search(DATO_CLAVE[c['id']], respuesta, re.I) else 'NO recuerda'} "
              f"el dato clave ({c['dato_a_recordar']})")
    print(f"\nGasto: {total:.5f} USD")
    con.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--piloto", action="store_true")
    ap.add_argument("--sonda-completa", action="store_true")
    ap.add_argument("--tope-usd", type=float, default=0.30)
    ap.add_argument("--trabajadores", type=int, default=3)
    a = ap.parse_args()
    if a.piloto:
        piloto(a.tope_usd, a.trabajadores)
    elif a.sonda_completa:
        sonda_completa()
    else:
        main()
