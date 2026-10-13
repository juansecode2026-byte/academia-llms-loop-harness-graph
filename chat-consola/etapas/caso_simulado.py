"""Piezas comunes del caso simulado: el asesor de «Turismo Colombia (simulada)».

Las etapas importan de aquí para no repetir el mensaje de sistema, el catálogo ni los
mensajes del cliente de prueba.
"""
import json
from pathlib import Path

RUTA_CATALOGO = Path(__file__).resolve().parent.parent / "datos-simulados" / "catalogo-turismo-simulado.json"

# Quién es el asesor.
SYSTEM_BASE = (
    "Eres el asesor de ventas de «Turismo Colombia (simulada)», una agencia de viajes. "
    "Atiendes por WhatsApp, en español, con mensajes cortos y cordiales."
)

# Reglas del prompt contra inventar y contra responder en abanico (tema 3.8). Se agregan solo si se pide.
REGLAS = (
    "Reglas:\n"
    "1. Usa solo datos del catálogo y nombra el alojamiento o tour del que sale cada precio.\n"
    "2. Si lo que piden no está en el catálogo (un alojamiento o destino que no existe, disponibilidad, "
    "temporada alta, descuentos, alergias o dietas, clima, vuelos), dilo con claridad, no inventes ni estimes, "
    "y di que un asesor humano lo confirma.\n"
    "3. Si faltan fechas o número de personas, pregúntalos antes de cotizar.\n"
    "4. Recomienda una opción principal, no una lista completa.\n"
    "5. Responde corto, como en WhatsApp."
)

# Lo que escribe el cliente, tal como llegaría por WhatsApp: primero pregunta, luego insiste.
MENSAJES_CLIENTE = [
    "hola buenas, cuanto vale ir a cartagena 4 noches?",
    "somos 2, del 10 al 14 de diciembre. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro",
]


def construir_system(con_reglas: bool = False) -> str:
    """Mensaje de sistema del asesor, con el catálogo en formato compacto (mismo contenido, menos tokens)."""
    catalogo = json.loads(RUTA_CATALOGO.read_text(encoding="utf-8"))
    base = SYSTEM_BASE + ("\n\n" + REGLAS if con_reglas else "")
    return base + "\n\nCatálogo de la agencia (JSON):\n" + json.dumps(
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
