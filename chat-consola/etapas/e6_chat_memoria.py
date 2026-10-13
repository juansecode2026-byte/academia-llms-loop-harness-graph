"""Etapa 6 · Primer chat con memoria, un historial por cliente, con el asesor de «Turismo Colombia (simulada)».

Concepto: el modelo NO recuerda nada entre llamadas. La memoria es la lista `messages`,
que se reenvía completa en cada turno. Aquí cada cliente tiene la suya (un diccionario).
Con el catálogo cargado, como en todo el ejercicio.

Ejecuta:  python etapas/e6_chat_memoria.py            (chat en consola; /cliente N cambia de cliente, /salir termina)
          python etapas/e6_chat_memoria.py --demo     (prueba guionada: memoria, aislamiento y experimento de ruptura)

No escribe en la base del piloto: así las 184 llamadas medidas en el tema 3.4 quedan intactas.
"""
import sys

import anthropic
from dotenv import load_dotenv

from caso_simulado import construir_system, costo_usd

load_dotenv()
client = anthropic.Anthropic()
MODELO = "claude-haiku-5-5"
SYSTEM = construir_system()
total = 0.0


def atender(memoria: list, texto: str, recordar_respuesta: bool = True) -> str:
    """Un turno: agrega el mensaje del cliente, envía TODA la memoria y (si se quiere) recuerda la respuesta."""
    global total
    memoria.append({"role": "user", "content": texto})                    # 1. agregar el mensaje
    r = client.messages.create(model=MODELO, max_tokens=2048, system=SYSTEM, messages=memoria)  # 2. enviar todo
    respuesta = "".join(b.text for b in r.content if b.type == "text")
    if recordar_respuesta:
        memoria.append({"role": "assistant", "content": respuesta})        # 3. recordar la respuesta
    costo = costo_usd(MODELO, r.usage.input_tokens, r.usage.output_tokens)
    total += costo
    print(f"   [mensajes en memoria: {len(memoria)} · entrada: {r.usage.input_tokens} tokens · "
          f"salida: {r.usage.output_tokens} · {costo:.5f} USD]")                       # 4. observar cómo crece
    return respuesta


def demo():
    # A. La memoria funciona: Laura da un dato y luego lo pregunta
    print("== A. Memoria de un cliente (Laura) ==")
    laura = []
    for texto in ("hola, soy Laura, nos casamos el 14 de febrero y queremos viajar esa semana a cartagena. cuanto vale?",
                  "me recuerdas que fecha te dije que nos casabamos y que precio me diste?"):
        print("Laura:", texto)
        print("Asesor:", atender(laura, texto), "\n")

    # B. Aislamiento: otro cliente tiene su propia memoria vacía
    print("== B. Otro cliente (Camilo) con su propia memoria ==")
    camilo = []
    texto = "hola, soy Camilo. me recuerdas en que fecha nos casamos?"
    print("Camilo:", texto)
    print("Asesor:", atender(camilo, texto), "\n")

    # C. Experimento de ruptura: no se recuerda lo que el asesor contestó
    print("== C. Experimento de ruptura (no se guarda la respuesta del asesor) ==")
    rota = []
    for texto in ("hola, soy Laura, nos casamos el 14 de febrero y queremos viajar esa semana a cartagena. cuanto vale?",
                  "me recuerdas que precio me diste?"):
        print("Laura:", texto)
        print("Asesor:", atender(rota, texto, recordar_respuesta=False), "\n")
    print("Mensajes que vio el asesor en el último turno:", [m["role"] for m in rota])


def chat():
    memorias = {}   # nombre del cliente -> su lista de mensajes
    cliente = "Cliente 1"
    print("Chat con memoria. Escribe /cliente NOMBRE para cambiar de cliente, /salir para terminar.")
    while True:
        texto = input(f"\n{cliente}: ").strip()
        if texto == "/salir":
            break
        if texto.startswith("/cliente "):
            cliente = texto[9:].strip() or cliente
            memorias.setdefault(cliente, [])
            print(f"(ahora atiendes a {cliente}; mensajes en su memoria: {len(memorias[cliente])})")
            continue
        if not texto:
            continue
        print("Asesor:", atender(memorias.setdefault(cliente, []), texto))
    print(f"\nGasto de la sesión: {total:.5f} USD")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
        print(f"\nGasto total de la etapa: {total:.5f} USD")
    else:
        chat()
