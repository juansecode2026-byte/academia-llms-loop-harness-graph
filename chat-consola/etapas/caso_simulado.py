"""Piezas comunes del caso simulado: el asesor de «Turismo Colombia (simulada)».

Las etapas importan de aquí para no repetir el mensaje de sistema, el catálogo ni los
mensajes del cliente de prueba.
"""
import json
from pathlib import Path

RUTA_CATALOGO = Path(__file__).resolve().parent.parent / "datos-simulados" / "catalogo-turismo-simulado.json"

# Quién es el asesor. Sin reglas contra inventar: eso se construye en el tema 3.8.
SYSTEM_BASE = (
    "Eres el asesor de ventas de «Turismo Colombia (simulada)», una agencia de viajes. "
    "Atiendes por WhatsApp, en español, con mensajes cortos y cordiales."
)

# Lo que escribe el cliente, tal como llegaría por WhatsApp: primero pregunta, luego insiste.
MENSAJES_CLIENTE = [
    "hola buenas, cuanto vale ir a cartagena 4 noches?",
    "somos 2, del 10 al 14 de diciembre. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro",
]


def construir_system(con_catalogo: bool) -> str:
    """Mensaje de sistema del asesor; con catálogo en formato compacto (mismo contenido, menos tokens)."""
    if not con_catalogo:
        return SYSTEM_BASE
    catalogo = json.loads(RUTA_CATALOGO.read_text(encoding="utf-8"))
    return SYSTEM_BASE + "\n\nCatálogo de la agencia (JSON):\n" + json.dumps(
        catalogo, ensure_ascii=False, separators=(",", ":")
    )
