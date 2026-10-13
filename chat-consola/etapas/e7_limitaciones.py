"""Etapa 7 · Limitaciones: el asesor frente a las trampas del catálogo, sin reglas y con reglas.

Concepto: el modelo genera texto probable, no texto verificado. Si el cliente pide algo que el
catálogo no publica (un hotel que no existe, un descuento, el clima, una dieta...), puede inventarlo.
Aquí se toman 8 mensajes-trampa de los clientes del piloto, con su conversación previa:
- «sin reglas»: la respuesta que el asesor YA dio en el tema 3.4 (guardada en la base, sin gasto nuevo);
- «con reglas»: la respuesta nueva, con las reglas del prompt (REGLAS en caso_simulado.py).
Solo lee la base del piloto; no escribe en ella. El resultado se guarda en informes/limitaciones-resultados.md.

Ejecuta:  python etapas/e7_limitaciones.py
"""
import json
from pathlib import Path

import anthropic
from dotenv import load_dotenv

import base_piloto as bd
from caso_simulado import construir_system, costo_usd

load_dotenv()
client = anthropic.Anthropic()
MODELO = "claude-haiku-5-5"
SYSTEM = construir_system(con_reglas=True)

# (cliente_id, turno, qué se le pide al asesor que el catálogo no publica)
TRAMPAS = [
    (1, 7, "Alojamiento que no existe"),
    (3, 9, "Descuento de grupo no publicado"),
    (5, 6, "Clima de la semana"),
    (6, 8, "Opción vegetariana en un tour"),
    (8, 13, "Tour en un destino que no está (Cali)"),
    (9, 9, "Comida sin maní (alergia)"),
    (9, 12, "Garantía de que no hay maní"),
    (10, 16, "Precio de temporada alta"),
]

con = bd.conectar()
clientes = {c["id"]: c for c in bd.cargar_clientes(con)}
salida = [f"# Pruebas de limitaciones · {MODELO}\n\nEl asesor frente a 8 trampas del catálogo, con la conversación previa de cada cliente.\n"]
total = 0.0
for cid, turno, tipo in TRAMPAS:
    mensaje = clientes[cid]["guion"][turno - 1]
    previa = bd.historial(con, cid, turno - 1)
    sin_reglas = con.execute(
        "select contenido from mensajes where cliente_id = ? and turno = ? and rol = 'asesor'", (cid, turno)
    ).fetchone()["contenido"]
    r = client.messages.create(model=MODELO, max_tokens=2048, system=SYSTEM,
                               messages=previa + [{"role": "user", "content": mensaje}])
    con_reglas = "".join(b.text for b in r.content if b.type == "text").strip()
    costo = costo_usd(MODELO, r.usage.input_tokens, r.usage.output_tokens)
    total += costo
    print(f"\n== {tipo} · {clientes[cid]['nombre']}, turno {turno} · {r.usage.input_tokens} entrada, "
          f"{r.usage.output_tokens} salida, {costo:.5f} USD ==")
    print("Cliente:", mensaje)
    print("\n[sin reglas]", sin_reglas)
    print("\n[con reglas]", con_reglas)
    salida.append(f"\n## {tipo} · {clientes[cid]['nombre']}, turno {turno}\n**Cliente:** {mensaje}\n"
                  f"\n**Sin reglas:**\n\n{sin_reglas}\n\n**Con reglas** ({r.usage.input_tokens} entrada, "
                  f"{r.usage.output_tokens} salida, {costo:.5f} USD):\n\n{con_reglas}\n")
con.close()

archivo = Path(__file__).resolve().parent.parent / "informes" / "limitaciones-resultados.md"
archivo.write_text("".join(salida), encoding="utf-8")
print(f"\nGasto de la etapa: {total:.5f} USD. Resultados guardados en {archivo}")
