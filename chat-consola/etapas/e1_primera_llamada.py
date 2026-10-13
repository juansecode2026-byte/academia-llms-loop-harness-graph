"""Etapa 1 · Primera llamada a la API de Anthropic desde Python, con el caso del ejercicio.

Concepto: un LLM recibe texto y devuelve texto generado token a token.
Caso: un cliente (ficticio) le escribe al asesor de «Turismo Colombia (simulada)», que
tiene el catálogo de la agencia en su mensaje de sistema, y después insiste en un precio.

Ejecuta:  python etapas/e1_primera_llamada.py
"""
import anthropic
from dotenv import load_dotenv

from caso_simulado import MENSAJES_CLIENTE, construir_system

load_dotenv()                     # 1. carga ANTHROPIC_API_KEY desde .env
client = anthropic.Anthropic()    # 2. crea el cliente (lee la clave solo)

SYSTEM = construir_system()   # papel del asesor + catálogo

historial = []   # la memoria: la lista de mensajes que se reenvía completa en cada turno
for turno, mensaje in enumerate(MENSAJES_CLIENTE, 1):
    historial.append({"role": "user", "content": mensaje})

    respuesta = client.messages.create(   # 3. la llamada
        model="claude-haiku-5-5",
        max_tokens=2048,
        system=SYSTEM,
        messages=historial,
    )

    # 4. La respuesta trae una LISTA de bloques: razonamiento ('thinking') y texto ('text')
    bloques = [b.type for b in respuesta.content]
    texto = "".join(b.text for b in respuesta.content if b.type == "text")
    historial.append({"role": "assistant", "content": texto})

    print(f"\n===== Turno {turno} =====")
    print("Cliente:", mensaje)
    print("Bloques:", bloques)
    print("Asesor:\n" + texto)

    # 5. Metadatos: por qué terminó y cuántos tokens consumió
    print(f"[{respuesta.model} · stop_reason={respuesta.stop_reason} · "
          f"entrada={respuesta.usage.input_tokens} tokens · salida={respuesta.usage.output_tokens} tokens]")
