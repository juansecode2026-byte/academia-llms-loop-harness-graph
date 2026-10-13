"""Etapa 10 · Informe del piloto: tokens, costo y alucinaciones por cliente (paso D.4).

Es código determinístico: lee la base del piloto y las respuestas ya guardadas; NO llama a Claude
y no escribe en la base. Genera chat-consola/informes/informe-piloto.md.

Ejecuta:  python etapas/e10_informe_piloto.py
"""
import json
import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "etapas"))
import base_piloto as bd  # noqa: E402
import chat  # noqa: E402
import test_chat as pruebas  # noqa: E402  (reutiliza el validador de precios y la lista de montos revisados)

# Veredicto sobre las trampas de cada cliente, revisado por Claude leyendo las respuestas en 3.8 (con y sin
# reglas) y en 3.9 (chat final). Es un juicio, no una medición automática.
TRAMPAS = {
    1: ("Hotel que no existe", "No inventó"),
    3: ("Descuento de grupo no publicado", "No inventó"),
    5: ("Clima de la semana", "No inventó"),
    6: ("Dieta vegetariana en un tour", "No inventó"),
    8: ("Tour en un destino ausente (Cali)", "No inventó"),
    9: ("Alergia al maní (dos trampas)", "No inventó"),
    10: ("Precio de temporada alta", "No inventó"),
}

con = sqlite3.connect(f"file:{bd.RUTA_BASE}?mode=ro", uri=True)
con.row_factory = sqlite3.Row
clientes = json.loads(bd.RUTA_CLIENTES.read_text(encoding="utf-8"))["clientes"]
validos = pruebas._precios_validos()


def es(x, d=0):
    """Número con formato español: punto de miles y coma decimal."""
    return f"{x:,.{d}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def suma(where, args=()):
    f = con.execute("select count(*) n, coalesce(sum(tokens_entrada),0) ent, coalesce(sum(tokens_salida),0) sal, "
                    "coalesce(sum(tokens_razonamiento),0) raz, coalesce(sum(costo_usd),0) usd, "
                    "coalesce(max(tokens_entrada),0) maxent from ejecuciones where " + where, args).fetchone()
    return dict(f)


def montos_sin_explicar(cid):
    sin, rev = 0, 0
    for r in con.execute("select turno, contenido from mensajes where cliente_id = ? and config = ? and rol = 'asesor'",
                         (cid, chat.CONFIG)):
        for m in re.findall(r"\$\s?(\d{1,3}(?:\.\d{3})+)", r["contenido"]):
            if int(m.replace(".", "")) in validos:
                continue
            if (cid, r["turno"], m) in pruebas.REVISADOS:
                rev += 1
            else:
                sin += 1
    return sin, rev


def recuerda(cid, config, turno=None):
    q = "select contenido from mensajes where cliente_id = ? and config = ? and rol = 'asesor' "
    q += "and turno = ?" if turno else "order by turno desc limit 1"
    f = con.execute(q, (cid, config) + ((turno,) if turno else ())).fetchone()
    return bool(f and re.search(chat.DATO_CLAVE[cid], f["contenido"], re.I))


filas, tot_b, tot_f = [], dict.fromkeys(["n", "ent", "sal", "raz", "usd"], 0), dict.fromkeys(["n", "ent", "sal", "raz", "usd"], 0)
olv, comp, sin_total, rev_total = 0, 0, 0, 0
for c in clientes:
    cid, n = c["id"], len(c["guion"])
    b = suma("cliente_id = ? and effort = 'default' and ventana = 'completa'", (cid,))
    f = suma("cliente_id = ? and effort = 'low' and ventana = '5' and turno <= ?", (cid, n))
    for k in tot_b:
        tot_b[k] += b[k]
        tot_f[k] += f[k]
    rv, rc = recuerda(cid, chat.CONFIG), recuerda(cid, "sonda-completa")
    olv += rv
    comp += rc
    sin, rev = montos_sin_explicar(cid)
    sin_total += sin
    rev_total += rev
    trampa = TRAMPAS.get(cid, ("—", "—"))
    filas.append((c["nombre"], n, b["usd"], f["usd"], b["maxent"], f["maxent"], rv, rc, trampa[1], sin, rev))

lineas = [f"# Informe del piloto · Nivel 1 · {date.today()}\n",
          "Caso: asesor de «Turismo Colombia (simulada)» con catálogo, 10 clientes ficticios, 184 mensajes por configuración. "
          "Generado por `etapas/e10_informe_piloto.py` sin llamar a Claude, a partir de la base del piloto.\n",
          "## 1. Tokens y costo: línea base (3.4) contra chat final (3.9)\n",
          "| Medida | Línea base (3.4) | Chat final (3.9) | Cambio |", "|---|---|---|---|"]
for nombre, k, fmt in [("Llamadas", "n", "{:,}"), ("Tokens de entrada", "ent", "{:,}"), ("Tokens de salida", "sal", "{:,}"),
                       ("Tokens de razonamiento", "raz", "{:,}")]:
    cambio = f"{(tot_f[k] / tot_b[k] - 1) * 100:+.1f} %".replace(".", ",") if tot_b[k] else "—"
    lineas.append(f"| {nombre} | {fmt.format(tot_b[k]).replace(',', '.')} | {fmt.format(tot_f[k]).replace(',', '.')} | {cambio} |")
lineas.append(f"| Costo (USD) | {es(tot_b['usd'], 4)} | {es(tot_f['usd'], 4)} | {es((tot_f['usd'] / tot_b['usd'] - 1) * 100, 1)} % |")

lineas += ["", "## 2. Por cliente\n",
           "| Cliente | Turnos | Costo base (USD) | Costo final (USD) | Entrada máx. base | Entrada máx. final | "
           "Dato clave con ventana | Dato clave con historial completo | Trampa | Montos sin explicar | Montos revisados |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
for nombre, n, ub, uf, mb, mf, rv, rc, tr, sin, rev in filas:
    lineas.append(f"| {nombre} | {n} | {es(ub, 4)} | {es(uf, 4)} | {es(mb)} | {es(mf)} | {'sí' if rv else '**NO**'} | "
                  f"{'sí' if rc else '**NO**'} | {tr} | {sin} | {rev} |")

total_pesos = sum(1 for r in con.execute("select contenido from mensajes where config = ? and rol = 'asesor'", (chat.CONFIG,)))
lineas += ["", "## 3. Alucinaciones\n",
           f"- **Precios:** {sin_total} montos sin explicar y {rev_total} sumas revisadas a mano y correctas, en {total_pesos} respuestas del chat final.",
           "- **Trampas del catálogo** (hotel inexistente, descuento, clima, dieta, destino ausente, alergia, temporada alta): "
           "0 de 8 inventadas, con y sin reglas (juicio de Claude, temas 3.8 y 3.9).",
           f"- **Memoria:** el chat final recordó el dato clave de {olv} de 10 clientes con la ventana de 5 turnos y de {comp} de 10 con el historial completo.",
           "- **Límite:** el recuento de precios es automático; el veredicto de las trampas es un juicio, no una medición.", ""]

total = con.execute("select count(*) n, sum(costo_usd) usd from ejecuciones").fetchone()
lineas += ["## 4. Gasto del piloto en la base\n",
           f"{total['n']} llamadas registradas en `ejecuciones`, {total['usd']:.4f} USD en total (las tres configuraciones). "
           "Las pruebas sueltas de los temas 3.5 a 3.8 se midieron en sus scripts y no están en esta cuenta.\n".replace(".", ",", 0)]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=RAIZ, encoding="utf-8").stdout


etapas = [m for m in git("log", "--format=%s").splitlines() if m.startswith("etapa ")]
env_en_git = ".env" in git("ls-files").splitlines() or any(x.endswith("/.env") for x in git("ls-files").splitlines())
clave_en_historial = bool(re.search(r"^\+.*sk-ant-[A-Za-z0-9_-]{20,}", git("log", "-p", "--all", "-S", "sk-ant-"), re.M))
lineas += ["## 5. Checklist de cierre del nivel (guía, apartado 10.1)\n", "| Punto | Estado | Evidencia |", "|---|---|---|"]
for punto, estado, ev in [
    ("Explico qué es un LLM y cómo predice tokens", "Hecho", "Temas 3.2 y 3.3 (notas y análisis)"),
    ("Sé calcular el costo de una conversación y por qué crece con la memoria", "Hecho", "Tema 3.4: 184 llamadas medidas"),
    ("Sé qué controlan max_tokens, effort y system, y qué no (temperatura)", "Hecho", "Tema 3.5"),
    ("Elegí modelo con datos", "Hecho", "Tema 3.6: Haiku (0,00086 contra 0,01691 y 0,03555 USD)"),
    ("Entiendo que la memoria es una lista que se reenvía", "Hecho", "Tema 3.7"),
    ("Completé el análisis de limitaciones", "Hecho", "Tema 3.8 e `informes/limitaciones-resultados.md`"),
    ("El chat final recuerda entre sesiones, recorta, muestra costos y sobrevive a errores", "Hecho, con una brecha",
     "chat.py: memoria en la base y ventana; olvida el dato clave de 4 de 10 clientes (ficha del cliente pendiente)"),
    ("pytest -q pasa", "Hecho", "13 passed y 1 xfailed (falla esperada documentada)"),
    ("`.env` nunca llegó a Git", "Hecho" if not env_en_git and not clave_en_historial else "**REVISAR**",
     f"Archivo rastreado: {'sí' if env_en_git else 'no'}; clave en el historial: {'sí' if clave_en_historial else 'no'}"),
    ("Hay un commit por etapa", "Hecho" if len(etapas) >= 9 else "**REVISAR**", f"{len(etapas)} commits «etapa N» en el historial"),
]:
    lineas.append(f"| {punto} | {estado} | {ev} |")

salida = RAIZ / "informes" / "informe-piloto.md"
salida.write_text("\n".join(lineas) + "\n", encoding="utf-8")
print("\n".join(lineas))
print(f"\nGuardado en {salida}")
