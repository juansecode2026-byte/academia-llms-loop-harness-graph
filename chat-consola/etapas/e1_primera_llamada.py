"""Etapa 1 · Primera llamada a la API de Anthropic desde Python, con el caso del ejercicio.

Concepto: un LLM recibe texto y devuelve texto generado token a token.
Caso: un cliente (ficticio) le escribe al asesor de «Turismo Colombia (simulada)» y
el asesor todavía NO tiene catálogo: no tiene de dónde sacar precios reales.
Ejecuta:  python etapas/e1_primera_llamada.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()                     # 1. carga ANTHROPIC_API_KEY desde .env
client = anthropic.Anthropic()    # 2. crea el cliente (lee la clave solo)

# Quién es el asesor. Aún sin catálogo ni reglas contra inventar (eso viene después).
SYSTEM = (
    "Eres el asesor de ventas de «Turismo Colombia (simulada)», una agencia de viajes. "
    "Atiendes por WhatsApp, en español, con mensajes cortos y cordiales."
)
# Lo que escribe el cliente, tal como llegaría por WhatsApp.
MENSAJE_CLIENTE = "hola buenas, cuanto vale ir a cartagena 4 noches?"

respuesta = client.messages.create(   # 3. la llamada
    model="claude-haiku-5-5",
    max_tokens=2048,
    system=SYSTEM,
    messages=[{"role": "user", "content": MENSAJE_CLIENTE}],
)

# 4. La respuesta trae una LISTA de bloques: razonamiento ('thinking') y texto ('text')
print("== Bloques de la respuesta ==")
for bloque in respuesta.content:
    print("-", bloque.type)

texto = "".join(b.text for b in respuesta.content if b.type == "text")
print("\n== Mensaje del cliente ==")
print(MENSAJE_CLIENTE)
print("\n== Respuesta del asesor ==")
print(texto)

# 5. Metadatos: por qué terminó y cuántos tokens consumió
print("\n== Metadatos ==")
print("modelo:            ", respuesta.model)
print("stop_reason:       ", respuesta.stop_reason)
print("tokens de entrada: ", respuesta.usage.input_tokens)
print("tokens de salida:  ", respuesta.usage.output_tokens)
