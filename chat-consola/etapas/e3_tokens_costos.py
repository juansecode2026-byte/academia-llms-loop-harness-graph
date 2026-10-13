"""Etapa 3 · Tokens, ventana de contexto y costos: la radiografía del contexto.

Concepto: pagas por tokens de entrada y de salida, y en un chat con memoria la entrada
crece en cada turno porque reenvías toda la conversación, además del catálogo.

Lee las conversaciones que dejó el simulador (base del piloto) y responde, con datos:
  1. ¿De qué está hecha cada llamada? instrucciones, catálogo, historial, mensaje nuevo.
  2. ¿Cuánto es texto redundante (ya enviado en la llamada anterior)?
  3. ¿Cuánto del catálogo es innecesario para lo que preguntó cada cliente?
  4. ¿Cómo crece la entrada turno a turno?
  5. ¿Cuánto cuesta una conversación, y cuánto bajaría con cada palanca?

Los tokens de cada mensaje se cuentan con la API (`count_tokens`), que no genera respuesta.
Las palancas se CALCULAN sobre las conversaciones reales; no se generan respuestas nuevas,
así que no se mide si la calidad cambia (eso se prueba en el laboratorio).

Ejecuta:  python etapas/e3_tokens_costos.py        (requiere haber corrido simulador_clientes.py)
Escribe:  informes/radiografia-contexto.md
"""
import json
import statistics as st
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic
from dotenv import load_dotenv

import base_piloto as bd
from caso_simulado import RUTA_CATALOGO, SYSTEM_BASE, construir_system, costo_usd

MODELO = "claude-haiku-5-5"
INFORME = Path(__file__).resolve().parent.parent / "informes" / "radiografia-contexto.md"
CACHE = Path(__file__).resolve().parent.parent / "informes" / "cache-conteo-tokens.json"

load_dotenv()
client = anthropic.Anthropic()
cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}


def contar(texto: str = ".", system: str | None = None) -> int:
    """Tokens de una petición con ese mensaje (y ese mensaje de sistema). No genera respuesta."""
    clave = json.dumps([texto, system], ensure_ascii=False)
    if clave in cache:
        return cache[clave]
    for intento in range(6):
        try:
            kw = {"system": system} if system else {}
            n = client.messages.count_tokens(
                model=MODELO, messages=[{"role": "user", "content": texto}], **kw).input_tokens
            cache[clave] = n
            return n
        except anthropic.RateLimitError:
            time.sleep(2 + 3 * intento)
    raise RuntimeError("count_tokens: demasiados reintentos")


def catalogo_filtrado(destinos: list[str]) -> str:
    """Mensaje de sistema con solo los registros de los destinos de interés del cliente."""
    cat = json.loads(RUTA_CATALOGO.read_text(encoding="utf-8"))
    cat["destinos"] = [d for d in cat["destinos"] if d["slug"] in destinos]
    cat["alojamientos"] = [a for a in cat["alojamientos"] if a["destino"] in destinos]
    cat["tours"] = [t for t in cat["tours"] if t["destino"] in destinos]
    return SYSTEM_BASE + "\n\nCatálogo de la agencia (JSON):\n" + json.dumps(cat, ensure_ascii=False, separators=(",", ":"))


# ------------------------------------------------------------------ datos reales
con = bd.conectar()
clientes = {c["id"]: c for c in bd.cargar_clientes(con)}
filas = con.execute(
    "select cliente_id, turno, tokens_entrada, tokens_salida, tokens_razonamiento, costo_usd, segundos "
    "from ejecuciones where modelo = ? and effort = 'default' and ventana = 'completa' and catalogo = 'completo' "
    "order by cliente_id, turno", (MODELO,)).fetchall()
esperados = sum(len(c["guion"]) for c in clientes.values())
assert len(filas) == esperados, f"faltan turnos: hay {len(filas)} de {esperados}; corre simulador_clientes.py"
msgs = {(m["cliente_id"], m["turno"], m["rol"]): m["contenido"] for m in con.execute("select * from mensajes")}

# ------------------------------------------------------------------ conteos con la API
c0 = contar(".")                                   # petición mínima: formato + "."
sist_base = contar(".", SYSTEM_BASE) - c0          # instrucciones del asesor
sist_full = contar(".", construir_system()) - c0   # instrucciones + catálogo completo
cat_full = sist_full - sist_base

with ThreadPoolExecutor(max_workers=4) as ex:
    pedidos = sorted(msgs)
    cuentas = dict(zip(pedidos, ex.map(lambda k: contar(msgs[k]) - (c0 - 1), pedidos)))  # tokens del texto solo
    filtrados = {cid: contar(".", catalogo_filtrado(c["destinos_interes"])) - c0 - sist_base
                 for cid, c in clientes.items()}
CACHE.parent.mkdir(exist_ok=True)
CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

# ------------------------------------------------------------------ modelo de la entrada, calibrado con lo real
# entrada_t = A + sum(tokens de cada mensaje + k), con k = tokens de formato por mensaje.
real = {(f["cliente_id"], f["turno"]): f for f in filas}
ks = []
for (cid, t), f in real.items():
    if t >= 2:
        delta = f["tokens_entrada"] - real[(cid, t - 1)]["tokens_entrada"]
        ks.append((delta - cuentas[(cid, t - 1, "asesor")] - cuentas[(cid, t, "cliente")]) / 2)
k = st.mean(ks)
A = st.mean(real[(cid, 1)]["tokens_entrada"] - cuentas[(cid, 1, "cliente")] - k for cid in clientes)


def entrada_predicha(cid: int, t: int, ventana: int | None, fijo: float) -> float:
    """Tokens de entrada del turno t si solo se reenvían los `ventana-1` turnos anteriores (None = todos)."""
    previos = list(range(max(1, t - (ventana - 1)) if ventana else 1, t))
    total = fijo + cuentas[(cid, t, "cliente")] + k
    for j in previos:
        total += cuentas[(cid, j, "cliente")] + cuentas[(cid, j, "asesor")] + 2 * k
    return total


errores = [abs(entrada_predicha(cid, t, None, A) - f["tokens_entrada"]) / f["tokens_entrada"] for (cid, t), f in real.items()]

# ------------------------------------------------------------------ 1. composición de la entrada
comp = {"instrucciones": [], "catalogo": [], "historial": [], "mensaje_nuevo": []}
for (cid, t), f in real.items():
    nuevo = cuentas[(cid, t, "cliente")] + k
    fijo_instr = sist_base
    fijo_cat = cat_full
    hist = f["tokens_entrada"] - (f["tokens_entrada"] - (A - 0) if False else 0)
    resto = f["tokens_entrada"] - nuevo - fijo_instr - fijo_cat
    comp["instrucciones"].append(fijo_instr)
    comp["catalogo"].append(fijo_cat)
    comp["mensaje_nuevo"].append(nuevo)
    comp["historial"].append(max(resto, 0))
prom = {x: st.mean(v) for x, v in comp.items()}
tot_in = sum(prom.values())

# ------------------------------------------------------------------ 2. redundancia
redun = [real[(cid, t - 1)]["tokens_entrada"] / f["tokens_entrada"] for (cid, t), f in real.items() if t >= 2]

# ------------------------------------------------------------------ 3. catálogo innecesario
necesario = {cid: filtrados[cid] / cat_full for cid in clientes}

# ------------------------------------------------------------------ 4. curva de crecimiento y costo por tramo de turno
tramos = [(1, 1), (2, 5), (6, 10), (11, 20), (21, 28)]
curva = []
for a, b in tramos:
    fs = [f for (cid, t), f in real.items() if a <= t <= b]
    if fs:
        curva.append((a, b, len(fs), st.mean(f["tokens_entrada"] for f in fs), st.mean(f["tokens_salida"] for f in fs),
                      st.mean(f["costo_usd"] for f in fs)))

# ------------------------------------------------------------------ 5. conversaciones y palancas
por_cliente = {cid: [f for (c, t), f in real.items() if c == cid] for cid in clientes}
costo_conv = {cid: sum(f["costo_usd"] for f in v) for cid, v in por_cliente.items()}
total_real = sum(costo_conv.values())
salida_total = sum(f["tokens_salida"] for f in real.values())
entrada_total = sum(f["tokens_entrada"] for f in real.values())


def costo_config(ventana: int | None, filtrar: bool) -> tuple[float, float]:
    ent = 0.0
    for (cid, t) in real:
        fijo = A - cat_full + (filtrados[cid] if filtrar else cat_full)
        ent += entrada_predicha(cid, t, ventana, fijo)
    return ent, (ent * 0.10 + salida_total * 0.50) / 1_000_000


configs = [
    ("Punto de partida: todo el historial y el catálogo completo (real)", entrada_total, total_real),
    ("Ventana de 10 turnos", *costo_config(10, False)),
    ("Ventana de 5 turnos", *costo_config(5, False)),
    ("Solo el catálogo de las ciudades que le interesan al cliente", *costo_config(None, True)),
    ("Catálogo de interés + ventana de 5 turnos", *costo_config(5, True)),
]

razon = st.mean(f["tokens_razonamiento"] / f["tokens_salida"] for f in real.values() if f["tokens_salida"])
n_conv = len(clientes)

# ------------------------------------------------------------------ informe
L = []
p = L.append
p("# Radiografía del contexto (tema 3.4)\n")
p(f"Modelo `{MODELO}`. {n_conv} conversaciones simuladas, {len(real)} llamadas reales a la API, con el catálogo completo y todo el historial.\n")
p(f"Costo real de las {len(real)} llamadas: **{total_real:.4f} USD**; {total_real / n_conv:.4f} USD por conversación; {total_real / len(real):.5f} USD por llamada.\n")
p("## 1. De qué está hecha cada llamada (promedio)\n")
p("| Parte | Tokens | % de la entrada |\n|---|---|---|")
nombres = {"instrucciones": "Instrucciones del asesor", "catalogo": "Catálogo completo", "historial": "Historial de la conversación", "mensaje_nuevo": "Mensaje nuevo del cliente"}
for x in ("instrucciones", "catalogo", "historial", "mensaje_nuevo"):
    p(f"| {nombres[x]} | {prom[x]:,.0f} | {100 * prom[x] / tot_in:.1f} % |")
p(f"| **Entrada total** | **{tot_in:,.0f}** | 100 % |\n")
p(f"Salida promedio: {salida_total / len(real):,.0f} tokens por respuesta, de los cuales {100 * razon:.0f} % es razonamiento.\n")
p("## 2. Texto redundante\n")
p(f"En promedio, el **{100 * st.mean(redun):.1f} %** de lo que se envía en un turno ya se había enviado en la llamada anterior (mínimo {100 * min(redun):.1f} %, máximo {100 * max(redun):.1f} %). La conversación solo agrega la respuesta anterior y el mensaje nuevo.\n")
p("## 3. Catálogo innecesario\n")
p(f"El catálogo completo pesa {cat_full:,} tokens. Con solo los registros de las ciudades por las que pregunta cada cliente pesaría, en promedio, **{st.mean(filtrados.values()):,.0f} tokens** ({100 * st.mean(necesario.values()):.0f} % del completo; entre {min(filtrados.values()):,} y {max(filtrados.values()):,}). Es decir, en promedio **{100 * (1 - st.mean(necesario.values())):.0f} % del catálogo es innecesario** para lo que el cliente preguntó.\n")
p("| Cliente | Ciudades de interés | Catálogo que sirve (tokens) | % del completo |\n|---|---|---|---|")
for cid, c in clientes.items():
    p(f"| {c['nombre']} | {', '.join(c['destinos_interes'])} | {filtrados[cid]:,} | {100 * necesario[cid]:.0f} % |")
p("")
p("## 4. Cómo crece la entrada turno a turno\n")
p("| Turnos | Llamadas | Entrada (tokens) | Salida (tokens) | Costo por llamada (USD) |\n|---|---|---|---|---|")
for a, b, n, e, s, c in curva:
    etiqueta = f"{a}" if a == b else f"{a} a {b}"
    p(f"| {etiqueta} | {n} | {e:,.0f} | {s:,.0f} | {c:.5f} |")
p("")
p("## 5. Costo por conversación\n")
p("| Cliente | Turnos | Entrada del último turno | Costo (USD) |\n|---|---|---|---|")
for cid, c in clientes.items():
    v = por_cliente[cid]
    p(f"| {c['nombre']} | {len(v)} | {v[-1]['tokens_entrada']:,} | {costo_conv[cid]:.4f} |")
p("")
p("## 6. Palancas (calculadas sobre las conversaciones reales)\n")
p("Se mantiene la salida observada. **No se mide si la calidad de las respuestas cambia**: eso se prueba en el laboratorio.\n")
p("| Configuración | Entrada total (tokens) | Costo de las 184 llamadas (USD) | Ahorro | Por conversación (USD) | 1.000 conversaciones al mes (USD) |\n|---|---|---|---|---|---|")
base_costo = configs[0][2]
for nombre, ent, costo in configs:
    p(f"| {nombre} | {ent:,.0f} | {costo:.4f} | {100 * (1 - costo / base_costo):.0f} % | {costo / n_conv:.4f} | {1000 * costo / n_conv:,.0f} |")
p("")
p("## 7. Calidad del modelo de cálculo\n")
p(f"Para calcular las palancas se reconstruye la entrada de cada llamada sumando los tokens de cada mensaje, más {k:.1f} tokens de formato por mensaje. Comparado con la entrada real de las {len(real)} llamadas, el error promedio es de **{100 * st.mean(errores):.2f} %** (máximo {100 * max(errores):.2f} %).\n")
INFORME.parent.mkdir(exist_ok=True)
INFORME.write_text("\n".join(L), encoding="utf-8")
print("\n".join(L))
print("\nInforme guardado en", INFORME)
