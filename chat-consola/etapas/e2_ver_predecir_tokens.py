"""Etapa 2 · Ver cómo el modelo genera la respuesta pedazo a pedazo (streaming), con el caso.

Concepto: el LLM predice un token, lo agrega al texto y vuelve a predecir.
Con streaming recibes esos tokens en pedazos a medida que se generan.
Caso: el primer mensaje del cliente de «Turismo Colombia (simulada)», con el catálogo cargado.

Ejecuta:  python etapas/e2_ver_predecir_tokens.py
"""
import anthropic
from dotenv import load_dotenv

from caso_simulado import MENSAJES_CLIENTE, construir_system

load_dotenv()
client = anthropic.Anthropic()

PREGUNTA = MENSAJES_CLIENTE[0]
print("Cliente:", PREGUNTA, "\n")
pedazos = 0
pensando = False

with client.messages.stream(
    model="claude-haiku-5-5",
    max_tokens=2048,
    system=construir_system(),
    messages=[{"role": "user", "content": PREGUNTA}],
    thinking={"type": "adaptive", "display": "summarized"},  # muestra un resumen del razonamiento
) as stream:
    for evento in stream:
        if evento.type == "thinking":
            if not pensando:
                print("[razonamiento resumido] ", end="")
                pensando = True
            print(evento.thinking, end="", flush=True)
        elif evento.type == "text":
            if pensando:
                print("\n\n[respuesta, cada | separa un pedazo recibido]")
                pensando = False
            pedazos += 1
            print(evento.text + "|", end="", flush=True)
    final = stream.get_final_message()

u = final.usage
razon = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", 0) or 0
print("\n\n== Lo que pasó por dentro ==")
print(f"Tokens de entrada:          {u.input_tokens}")
print(f"Pedazos de texto recibidos: {pedazos}")
print(f"Tokens de salida totales:   {u.output_tokens}")
print(f"  de razonamiento:          {razon}")
print(f"  de respuesta (aprox.):    {u.output_tokens - razon}")
print("Cada pedazo puede traer varios tokens: el servidor los agrupa al enviarlos.")
