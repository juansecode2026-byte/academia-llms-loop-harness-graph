"""Hook PreToolUse (determinístico, sin llamadas a Claude).

Cuando una herramienta (Edit, Write, Bash) toca el manual de resultados, inyecta como
contexto el prompt de AI Engineer que hay que responder y agregar al «Análisis de resultados».
"""
import json
import sqlite3
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "chat-consola" / "datos-simulados" / "piloto-simulado.db"


def base_medida() -> str:
    """Totales reales de la tabla ejecuciones: la línea base contra la que se calcula el ahorro."""
    try:
        con = sqlite3.connect(BASE)
        filas = con.execute(
            "select effort, ventana, count(*), sum(tokens_entrada), sum(tokens_salida), sum(costo_usd) "
            "from ejecuciones group by effort, ventana order by min(id)").fetchall()
        con.close()
        miles = lambda x: f"{x:,}".replace(",", ".")
        partes = [f"effort {e}, ventana {v}: {n} llamadas, {miles(ent)} tokens de entrada, {miles(sal)} de salida, "
                  f"{usd:.4f} USD".replace("0.", "0,") for e, v, n, ent, sal, usd in filas]
        return (" Mediciones en la base del piloto, por configuración (la primera, effort default y ventana "
                "completa, es la línea base del tema 3.4): " + "; ".join(partes) + ".")
    except Exception:
        return ""

PROMPT = (
    "DESDE EL PUNTO DE VISTA DE UN AI ENGINEER: enumera los factores que encarecieron el gasto "
    "de tokens, con datos y números si es necesario, para mirar cómo se podría mejorar. "
    "Y DESDE EL PUNTO DE VISTA DE UN AI ENGINEER: enumera cómo podríamos optimizar ese resultado. "
    "Responde ambos puntos y agrega el resultado a la entrada del tema en el «Análisis de resultados» "
    "(«Qué encareció el proceso» y «Cómo se podría optimizar»), marcando cada cifra como medida, calculada o estimada. "
    "Además, muestra el TOTAL DE TOKENS AHORRADOS expresado en dólares: diferencia entre el resultado obtenido "
    "(tokens y USD medidos) y el resultado con la optimización (tokens y USD calculados o estimados), "
    "en una tabla: concepto, tokens antes, tokens después, tokens ahorrados, USD ahorrados, estado del dato. "
    "Después de la tabla «Variables que afectaron el proceso» agrega el bloque «Para qué sirve cada dato»: una viñeta por "
    "variable con Objetivo (para qué se mide), Decisión (qué permite decidir) y Ejemplo concreto del proyecto con números, "
    "en palabras simples para quien empieza; y a continuación la tabla «Resumen: cada dato y su decisión» con las columnas "
    "Dato | Pregunta que responde | Decisión que permite. "
    "ESTRUCTURA OBLIGATORIA de cada entrada, prolija y numerada: cada título va en su propia línea en negrita "
    "(`**N. Título**`, y `**N.M Título**` para subtítulos; el HTML los muestra como títulos) y los números son fijos: "
    "1. Qué se hizo, 2. A qué nos conduce, 3. En el ejercicio, 4. Qué encareció el proceso, "
    "5. Variables que afectaron el proceso (5.1 Para qué sirve cada dato, 5.2 Resumen: cada dato y su decisión), "
    "6. Cómo optimizar cada variable, 7. Tokens ahorrados en dólares, 8. Ejemplo (nota `> **8. Ejemplo**`), "
    "y al final la nota `> **CONCLUSIONES**`. Si el tema no gastó tokens se omiten los apartados que no aplican y se "
    "conservan los números; los temas de planeación llevan la nota `> **PLANEACIÓN**` y su propia numeración. "
    "La primera mención de «asesor» lleva «(asistente de ventas de Turismo Colombia)». "
    "Y cierra la entrada con el apartado CONCLUSIONES (nota `> **CONCLUSIONES**`, que el HTML muestra con otra letra): "
    "DESDE EL PUNTO DE VISTA DE UN AI ENGINEER, 4 consejos enfocados en solución, basados SOLO en los datos de ese "
    "análisis (qué hacer, cómo, cifra esperada con su estado y en qué tema se prueba), ordenados por prioridad."
)

try:
    datos = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if "resultados-proceso-manual" in json.dumps(datos.get("tool_input", {}), ensure_ascii=False):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": PROMPT + base_medida()}}, ensure_ascii=False))
