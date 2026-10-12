"""Etapa 1 · Primera llamada a la API de Anthropic desde Python.

Concepto: un LLM recibe texto y devuelve texto generado token a token.
Ejecuta:  python etapas/e1_primera_llamada.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()                     # 1. carga ANTHROPIC_API_KEY desde .env
client = anthropic.Anthropic()    # 2. crea el cliente (lee la clave solo)

respuesta = client.messages.create(   # 3. la llamada
    model="claude-haiku-5-5",
    max_tokens=2048,
    messages=[
        {"role": "user", "content": "¿Qué es un modelo de lenguaje? Responde en dos frases."}
    ],
)

# 4. La respuesta trae una LISTA de bloques: razonamiento ('thinking') y texto ('text')
print("== Bloques de la respuesta ==")
for bloque in respuesta.content:
    print("-", bloque.type)

texto = "".join(b.text for b in respuesta.content if b.type == "text")
print("\n== Texto ==")
print(texto)

# 5. Metadatos: por qué terminó y cuántos tokens consumió
print("\n== Metadatos ==")
print("modelo:            ", respuesta.model)
print("stop_reason:       ", respuesta.stop_reason)
print("tokens de entrada: ", respuesta.usage.input_tokens)
print("tokens de salida:  ", respuesta.usage.output_tokens)
