"""Etapa 4 · Parámetros de generación sobre el asesor de «Turismo Colombia (simulada)».

Concepto: se puede controlar cuánto genera el modelo (max_tokens), cuánto razona (effort)
y cómo se comporta (system). La temperatura en Claude 5.5 no se puede variar.
Cada prueba mide tokens, razonamiento, segundos y costo, siempre con el catálogo cargado.

Ejecuta:  python etapas/e4_parametros.py
"""
import time

import anthropic
from dotenv import load_dotenv

from caso_simulado import MENSAJES_CLIENTE, construir_system, costo_usd

load_dotenv()
client = anthropic.Anthropic()
MODELO = "claude-haiku-5-5"
PREGUNTA = MENSAJES_CLIENTE[0]
total = 0.0


def llamar(titulo, **kw):
    """Hace la llamada, mide y muestra la respuesta del asesor."""
    global total
    kw.setdefault("system", construir_system())
    kw.setdefault("messages", [{"role": "user", "content": PREGUNTA}])
    inicio = time.perf_counter()
    r = client.messages.create(model=MODELO, **kw)
    seg = time.perf_counter() - inicio
    texto = "".join(b.text for b in r.content if b.type == "text")
    razon = getattr(getattr(r.usage, "output_tokens_details", None), "thinking_tokens", 0) or 0
    costo = costo_usd(MODELO, r.usage.input_tokens, r.usage.output_tokens)
    total += costo
    print(f"[{titulo}] {seg:4.1f}s · entrada {r.usage.input_tokens} · salida {r.usage.output_tokens} "
          f"({razon} de razonamiento) · {costo:.5f} USD · stop_reason={r.stop_reason}")
    print("   ->", texto.replace("\n", " ") or "(sin texto: el tope se gastó antes de terminar)", "\n")


print("Cliente:", PREGUNTA, "\n")

print("== A. max_tokens: el tope duro de salida ==")
for tope in (40, 150, 2048):
    llamar(f"max_tokens={tope}", max_tokens=tope)

print("== B. effort: cuánto razona antes de responder ==")
for esfuerzo in ("low", "medium", "high"):
    llamar(f"effort={esfuerzo}", max_tokens=4000, output_config={"effort": esfuerzo})

print("== C. system: el comportamiento ==")
llamar("system base", max_tokens=2048)
llamar("system con reglas", max_tokens=2048,
       system=construir_system() + "\n\nResponde en máximo 2 frases. Usa solo precios del catálogo y di de qué registro salen.")

print("== D. temperatura = 0.2 ==")
try:
    client.messages.create(model=MODELO, max_tokens=200, system=construir_system(),
                           messages=[{"role": "user", "content": "Hola"}],
                           extra_body={"temperature": 0.2})
    print("La API lo aceptó con este modelo.")
except anthropic.BadRequestError as e:
    print("La API lo rechazó (400):", e.message)

print(f"\nGasto total de la etapa: {total:.5f} USD")
