"""Etapa 3 · Tokens, ventana de contexto y costos.

Concepto: pagas por tokens de entrada y de salida, y en un chat con memoria
la entrada crece en cada turno porque reenvías toda la conversación.
Ejecuta:  python etapas/e3_tokens_costos.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODELO = "claude-haiku-5-5"

# Precios USD por millón de tokens (MTok). Verificados el 2026-10-11 en
# https://platform.claude.com/docs/en/about-claude/pricing  -> revísalos antes de usar.
PRECIOS = {
    "claude-haiku-5-5":  {"in": 0.10, "out": 0.50},   # prompts de hasta 100k tokens
    "claude-sonnet-5-5": {"in": 2.00, "out": 10.00},
    "claude-opus-5-5":   {"in": 4.00, "out": 20.00},
}


def costo_usd(modelo, tokens_in, tokens_out):
    p = PRECIOS[modelo]
    return (tokens_in * p["in"] + tokens_out * p["out"]) / 1_000_000


def contar(texto):
    """Cuenta tokens sin generar respuesta (no cobra generación)."""
    return client.messages.count_tokens(
        model=MODELO, messages=[{"role": "user", "content": texto}]
    ).input_tokens


# ---- Parte A: cuántos tokens ocupa cada tipo de texto ----
print("== A. Mismo contenido, distinto número de tokens ==")
base = contar(".")  # el formato del mensaje también ocupa algunos tokens
textos = {
    "español": "El modelo predice el siguiente token a partir de los anteriores.",
    "inglés":  "The model predicts the next token from the previous ones.",
    "código":  "def suma(a, b):\n    return a + b",
    "números": "3.14159 2718281828 1234567890",
    "emoji":   "🚀🔥😂👍",
}
for nombre, texto in textos.items():
    n = contar(texto) - base
    print(f"{nombre:<8} {len(texto):>3} caracteres -> ~{n:>3} tokens")

# ---- Parte B: por qué la memoria cuesta ----
print("\n== B. Simulación: chat de 20 turnos reenviando todo el historial ==")
TOK_SYSTEM, TOK_USUARIO, TOK_RESPUESTA = 60, 40, 200
contexto = TOK_SYSTEM
total_in = total_out = 0
print("turno | entrada de ESA llamada | entrada acumulada")
for turno in range(1, 21):
    contexto += TOK_USUARIO          # tu mensaje se suma al historial
    total_in += contexto             # se envía TODO el historial
    total_out += TOK_RESPUESTA
    contexto += TOK_RESPUESTA        # la respuesta también queda en el historial
    if turno in (1, 5, 10, 20):
        print(f"{turno:>5} | {contexto - TOK_RESPUESTA:>22} | {total_in:>17}")

print(f"\nSin memoria la entrada total sería ~{(TOK_SYSTEM + TOK_USUARIO) * 20} tokens; con memoria es {total_in}.")

# ---- Parte C: cuánto costaría esa conversación en cada modelo ----
print("\n== C. Costo de esa misma conversación ==")
for modelo in PRECIOS:
    print(f"{modelo:<18} ${costo_usd(modelo, total_in, total_out):.4f} USD")
print("\nVentana de contexto de los modelos 5.5: 1.000.000 tokens. Cabe mucho, pero todo se cobra.")
