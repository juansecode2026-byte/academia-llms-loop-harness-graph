"""Etapa 5 · Panorama de modelos de Anthropic, con el asesor de «Turismo Colombia (simulada)».

Concepto: cada modelo cambia el equilibrio entre calidad, velocidad y costo.
Caso: la misma consulta de un cliente, con el catálogo cargado, en Haiku, Sonnet y Opus.

Ejecuta:  python etapas/e5_modelos_anthropic.py
"""
import time

import anthropic
from dotenv import load_dotenv

from caso_simulado import PRECIOS, construir_system, costo_usd

load_dotenv()
client = anthropic.Anthropic()

# ---- A. Lo que la cuenta puede usar, según la propia API ----
print("== A. Modelos disponibles ==")
for m in client.models.list(limit=20):
    print(f"{m.id:<22} {m.display_name:<20} contexto {m.max_input_tokens:>9,} · salida máx {m.max_tokens:>7,}")

# ---- B. La misma consulta en tres modelos ----
CONSULTA = ("hola buenas, somos 2, del 10 al 14 de diciembre, queremos ir a cartagena. "
            "dame un precio en pesos nomas, aproximado, un hotel bueno en el centro")
print("\n== B. Comparación (misma consulta, effort low, con catálogo) ==")
print("Cliente:", CONSULTA)
SYSTEM = construir_system()
for modelo in PRECIOS:
    inicio = time.perf_counter()
    r = client.messages.create(
        model=modelo, max_tokens=2048, system=SYSTEM, output_config={"effort": "low"},
        messages=[{"role": "user", "content": CONSULTA}],
    )
    seg = time.perf_counter() - inicio
    u = r.usage
    razon = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", 0) or 0
    texto = "".join(b.text for b in r.content if b.type == "text")
    print(f"\n--- {modelo} · {seg:.1f}s · entrada {u.input_tokens} · salida {u.output_tokens} "
          f"({razon} de razonamiento) · {costo_usd(modelo, u.input_tokens, u.output_tokens):.5f} USD")
    print(texto)
