"""Hook PreToolUse (determinístico, sin llamadas a Claude).

Cuando una herramienta (Edit, Write, Bash) toca el manual de resultados, inyecta como
contexto el prompt de AI Engineer que hay que responder y agregar al «Análisis de resultados».
"""
import json
import sys

PROMPT = (
    "DESDE EL PUNTO DE VISTA DE UN AI ENGINEER: enumera los factores que encarecieron el gasto "
    "de tokens, con datos y números si es necesario, para mirar cómo se podría mejorar. "
    "Y DESDE EL PUNTO DE VISTA DE UN AI ENGINEER: enumera cómo podríamos optimizar ese resultado. "
    "Responde ambos puntos y agrega el resultado a la entrada del tema en el «Análisis de resultados» "
    "(«Qué encareció el proceso» y «Cómo se podría optimizar»), marcando cada cifra como medida, calculada o estimada."
)

try:
    datos = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if "resultados-proceso-manual" in json.dumps(datos.get("tool_input", {}), ensure_ascii=False):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": PROMPT}}, ensure_ascii=False))
