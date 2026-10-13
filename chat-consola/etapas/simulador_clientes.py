"""Simulador de clientes: entrega los mensajes de cada cliente ficticio al asesor, como si
llegaran por WhatsApp, y guarda cada respuesta y la medición de cada llamada.

Cada cliente tiene su propia conversación y su propia memoria (la tabla `mensajes`).
Los clientes corren en paralelo; los turnos de un mismo cliente, en orden. Si se
interrumpe, al volver a correr retoma donde quedó. Tiene un tope de gasto de seguridad.

Ejecuta:  python etapas/simulador_clientes.py
          python etapas/simulador_clientes.py --reiniciar        (borra la base y empieza de cero)
          python etapas/simulador_clientes.py --tope-usd 0.8     (cambia el tope de gasto)
"""
import argparse
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import anthropic
from dotenv import load_dotenv

import base_piloto as bd
from caso_simulado import construir_system, costo_usd

MODELO = "claude-haiku-5-5"
CONFIG = {"effort": "default", "ventana": "completa", "catalogo": "completo"}

parser = argparse.ArgumentParser()
parser.add_argument("--reiniciar", action="store_true", help="borra la base del piloto y empieza de cero")
parser.add_argument("--tope-usd", type=float, default=0.60, help="tope de gasto de seguridad")
parser.add_argument("--trabajadores", type=int, default=3, help="clientes en paralelo")
args = parser.parse_args()

load_dotenv()
client = anthropic.Anthropic()
SYSTEM = construir_system()

if args.reiniciar and bd.RUTA_BASE.exists():
    bd.RUTA_BASE.unlink()
con0 = bd.conectar()
clientes = bd.cargar_clientes(con0)
con0.close()

gasto = {"usd": 0.0, "turnos": 0}
lock = threading.Lock()
parar = threading.Event()


def atender(c: dict) -> str:
    con = bd.conectar()
    hechos = {r["turno"] for r in con.execute(
        "select turno from ejecuciones where cliente_id = ? and modelo = ? and effort = ? and ventana = ? and catalogo = ?",
        (c["id"], MODELO, CONFIG["effort"], CONFIG["ventana"], CONFIG["catalogo"]))}
    for turno, mensaje in enumerate(c["guion"], 1):
        if turno in hechos:
            continue
        if parar.is_set():
            return f"{c['nombre']}: detenido en el turno {turno}"
        # memoria de este cliente = todo lo guardado antes + el mensaje nuevo
        mensajes = bd.historial(con, c["id"], turno - 1) + [{"role": "user", "content": mensaje}]
        inicio = time.perf_counter()
        for intento in range(8):
            try:
                r = client.messages.create(model=MODELO, max_tokens=2048, system=SYSTEM, messages=mensajes)
                break
            except anthropic.RateLimitError:
                # límite de tokens por minuto de la cuenta: se espera y se reintenta
                time.sleep(15 + 10 * intento)
        else:
            raise RuntimeError(f"{c['nombre']}: demasiados reintentos por límite de velocidad")
        seg = time.perf_counter() - inicio
        texto = "".join(b.text for b in r.content if b.type == "text")
        u = r.usage
        razon = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", 0) or 0
        costo = costo_usd(MODELO, u.input_tokens, u.output_tokens)
        con.execute("insert or replace into mensajes (cliente_id, turno, rol, contenido) values (?, ?, 'cliente', ?)",
                    (c["id"], turno, mensaje))
        con.execute("insert or replace into mensajes (cliente_id, turno, rol, contenido) values (?, ?, 'asesor', ?)",
                    (c["id"], turno, texto))
        con.execute(
            "insert or replace into ejecuciones (cliente_id, turno, modelo, effort, ventana, catalogo, tokens_entrada, "
            "tokens_salida, tokens_razonamiento, costo_usd, segundos, stop_reason) values (?,?,?,?,?,?,?,?,?,?,?,?)",
            (c["id"], turno, MODELO, CONFIG["effort"], CONFIG["ventana"], CONFIG["catalogo"],
             u.input_tokens, u.output_tokens, razon, costo, seg, r.stop_reason))
        con.commit()
        with lock:
            gasto["usd"] += costo
            gasto["turnos"] += 1
            if gasto["usd"] >= args.tope_usd:
                parar.set()
    con.close()
    return f"{c['nombre']}: {len(c['guion'])} turnos completos"


with ThreadPoolExecutor(max_workers=args.trabajadores) as ex:
    for resultado in ex.map(atender, clientes):
        print(resultado, f"| acumulado: {gasto['turnos']} turnos, {gasto['usd']:.4f} USD", flush=True)

print(f"\nListo. {gasto['turnos']} llamadas nuevas, gasto de esta corrida: {gasto['usd']:.4f} USD")
if parar.is_set():
    print("Se alcanzó el tope de gasto de seguridad: faltan turnos. Vuelve a correr para retomar.")
