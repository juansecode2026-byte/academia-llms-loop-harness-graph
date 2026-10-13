"""Piezas comunes del caso simulado: el asesor de «Turismo Colombia (simulada)».

Las etapas importan de aquí para no repetir el mensaje de sistema, el catálogo ni los
mensajes del cliente de prueba.
"""
import json
from pathlib import Path

RUTA_CATALOGO = Path(__file__).resolve().parent.parent / "datos-simulados" / "catalogo-turismo-simulado.json"

# Quién es el asesor. Las reglas contra inventar se construyen en el tema 3.8.
SYSTEM_BASE = (
    "Eres el asesor de ventas de «Turismo Colombia (simulada)», una agencia de viajes. "
    "Atiendes por WhatsApp, en español, con mensajes cortos y cordiales."
)

# Lo que escribe el cliente, tal como llegaría por WhatsApp: primero pregunta, luego insiste.
MENSAJES_CLIENTE = [
    "hola buenas, cuanto vale ir a cartagena 4 noches?",
    "somos 2, del 10 al 14 de diciembre. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro",
]


def construir_system() -> str:
    """Mensaje de sistema del asesor, con el catálogo en formato compacto (mismo contenido, menos tokens)."""
    catalogo = json.loads(RUTA_CATALOGO.read_text(encoding="utf-8"))
    return SYSTEM_BASE + "\n\nCatálogo de la agencia (JSON):\n" + json.dumps(
        catalogo, ensure_ascii=False, separators=(",", ":")
    )


# Precios en USD por millón de tokens, verificados el 2026-10-11 en la página de precios de Anthropic.
PRECIOS = {
    "claude-haiku-5-5": {"in": 0.10, "out": 0.50},
    "claude-sonnet-5-5": {"in": 2.00, "out": 10.00},
    "claude-opus-5-5": {"in": 4.00, "out": 20.00},
}


def costo_usd(modelo: str, tokens_entrada: int, tokens_salida: int) -> float:
    p = PRECIOS[modelo]
    return (tokens_entrada * p["in"] + tokens_salida * p["out"]) / 1_000_000
