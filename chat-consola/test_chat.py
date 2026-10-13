"""Pruebas sin gastar tokens del chat final y de la memoria por cliente.  Ejecuta: pytest -q

Un cliente falso reemplaza a la API: devuelve respuestas fijas y anota lo que se le envió.
Las pruebas usan una base temporal; nunca tocan la base del piloto ni llaman a la API real.
Las dos últimas secciones leen las respuestas YA guardadas del piloto (tema 3.9) para vigilar
la memoria y los precios sin volver a gastar.
"""
import json
import re
import sqlite3
import sys
from pathlib import Path
from types import SimpleNamespace as NS

import httpx2 as httpx
import anthropic
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent / "etapas"))
import base_piloto as bd  # noqa: E402
import chat  # noqa: E402
from caso_simulado import RUTA_CATALOGO, costo_usd  # noqa: E402

RAIZ = Path(__file__).resolve().parent
BASE_PILOTO = bd.RUTA_BASE   # se guarda antes de que las pruebas la reemplacen


# ---------- cliente falso ----------
def usage(i=100, o=50, razon=10):
    return NS(input_tokens=i, output_tokens=o, output_tokens_details=NS(thinking_tokens=razon))


class FakeStream:
    def __init__(self, texto, stop="end_turn"):
        self.eventos = [NS(type="thinking", thinking="...")] + [NS(type="text", text=t) for t in texto]
        self.final = NS(usage=usage(), stop_reason=stop)

    def __enter__(self): return self
    def __exit__(self, *a): return False
    def __iter__(self): return iter(self.eventos)
    def get_final_message(self): return self.final


class FakeMessages:
    def __init__(self, respuestas, error=None):
        self.respuestas, self.error, self.llamadas = list(respuestas), error, []

    def stream(self, **kw):
        self.llamadas.append({**kw, "messages": [dict(m) for m in kw["messages"]]})  # foto del envío
        if self.error:
            err, self.error = self.error, None
            raise err
        return FakeStream(self.respuestas.pop(0))

    def count_tokens(self, **kw):
        return NS(input_tokens=42)


def fake_client(respuestas, error=None):
    return NS(messages=FakeMessages(respuestas, error))


@pytest.fixture()
def con(tmp_path, monkeypatch):
    """Base temporal con el mismo esquema y los 10 clientes del piloto."""
    monkeypatch.setattr(bd, "RUTA_BASE", tmp_path / "prueba.db")
    c = bd.conectar()
    bd.cargar_clientes(c)
    yield c
    c.close()


def piloto_con(sql, args=()):
    """Lee la base REAL del piloto (solo lectura)."""
    c = sqlite3.connect(f"file:{BASE_PILOTO}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    try:
        return c.execute(sql, args).fetchall()
    finally:
        c.close()


# ---------- memoria: ventana ----------
def test_recortar_conserva_ultimos_turnos_y_empieza_en_user():
    msgs = []
    for i in range(30):
        msgs += [{"role": "user", "content": f"u{i}"}, {"role": "assistant", "content": f"a{i}"}]
    msgs.append({"role": "user", "content": "nuevo"})
    r = chat.recortar(msgs)
    assert r[0]["role"] == "user"
    assert r[-1]["content"] == "nuevo"
    assert len(r) <= chat.MAX_TURNS * 2


def test_ventana_de_5_turnos():
    assert chat.MAX_TURNS == 5


# ---------- memoria por cliente (base SQLite) ----------
def test_guardar_y_cargar_ida_y_vuelta_con_tildes(con):
    chat.guardar_turno(con, 1, 1, "Hola, ñandú", "¡Hola, Laura!")
    assert chat.cargar_historial(con, 1) == [
        {"role": "user", "content": "Hola, ñandú"}, {"role": "assistant", "content": "¡Hola, Laura!"}]


def test_cada_cliente_tiene_su_memoria(con):
    chat.guardar_turno(con, 1, 1, "nos casamos el 14 de febrero", "Felicidades")
    assert chat.cargar_historial(con, 5) == []        # Camilo no ve lo de Laura
    assert len(chat.cargar_historial(con, 1)) == 2


def test_las_configuraciones_no_se_mezclan(con):
    """Lo medido en el tema 3.4 ('completa') no se pisa con el chat final."""
    chat.guardar_turno(con, 1, 1, "hola", "respuesta vieja", config="completa")
    chat.guardar_turno(con, 1, 1, "hola", "respuesta nueva")
    assert bd.historial(con, 1, config="completa")[1]["content"] == "respuesta vieja"
    assert chat.cargar_historial(con, 1)[1]["content"] == "respuesta nueva"


# ---------- costos ----------
def test_costo_haiku():
    assert costo_usd("claude-haiku-5-5", 1_000_000, 1_000_000) == pytest.approx(0.60)


def test_costo_sonnet_y_opus():
    assert costo_usd("claude-sonnet-5-5", 1_000_000, 1_000_000) == pytest.approx(12.0)
    assert costo_usd("claude-opus-5-5", 1_000_000, 1_000_000) == pytest.approx(24.0)


# ---------- turno completo con cliente falso ----------
def test_el_modelo_recibe_solo_la_ventana_y_la_configuracion_correcta(con):
    client = fake_client([["respuesta"]] * 8)
    for i in range(8):                                # 8 turnos de Laura
        chat.atender_turno(client, con, 1, f"mensaje {i + 1}", mostrar=False)

    ultima = client.messages.llamadas[-1]
    assert len(ultima["messages"]) == 9               # 4 turnos anteriores + el nuevo (ventana de 5)
    assert ultima["messages"][0]["role"] == "user"
    assert ultima["messages"][-1]["content"] == "mensaje 8"
    assert "temperature" not in ultima                # los modelos 5.5 la rechazan
    assert ultima["output_config"] == {"effort": "low"}
    assert ultima["model"] == "claude-haiku-5-5"
    assert "Reglas:" in ultima["system"]              # reglas contra inventar (3.8)
    assert "casa-naranja-del-centro" in ultima["system"]   # el catálogo viaja en cada llamada
    assert len(chat.cargar_historial(con, 1)) == 16   # pero la memoria completa queda guardada


def test_cada_llamada_queda_registrada_en_ejecuciones(con):
    client = fake_client([["hola"]])
    chat.atender_turno(client, con, 3, "hola", mostrar=False)
    fila = con.execute("select * from ejecuciones where cliente_id = 3").fetchone()
    assert (fila["modelo"], fila["effort"], fila["ventana"], fila["tokens_entrada"],
            fila["tokens_salida"]) == ("claude-haiku-5-5", "low", "5", 100, 50)
    assert fila["costo_usd"] == pytest.approx(costo_usd("claude-haiku-5-5", 100, 50))


def test_un_error_de_la_api_no_guarda_nada(con):
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    err = anthropic.AuthenticationError("clave", response=httpx.Response(401, request=req), body=None)
    client = fake_client([["ok"]], error=err)
    with pytest.raises(anthropic.AuthenticationError):
        chat.atender_turno(client, con, 1, "hola", mostrar=True)
    assert chat.cargar_historial(con, 1) == []
    chat.atender_turno(client, con, 1, "hola otra vez", mostrar=False)   # y el siguiente turno funciona
    assert [m["role"] for m in chat.cargar_historial(con, 1)] == ["user", "assistant"]


def test_comandos_de_consola(con, monkeypatch, capsys):
    monkeypatch.setattr(bd, "conectar", lambda: con)
    client = fake_client([["respuesta"]])
    entradas = iter(["hola", "/tokens", "/historial", "/cliente 5", "/historial", "/reset", "/salir"])
    monkeypatch.setattr("builtins.input", lambda _="": next(entradas))
    chat.main(client)
    salida = capsys.readouterr().out
    assert "42 tokens" in salida                       # /tokens cuenta lo que se enviará
    assert "(memoria vacía)" in salida                 # Camilo (cliente 5) no hereda la memoria de Laura
    assert "Camilo" in salida


# ---------- el piloto real: vigilar memoria y precios sin gastar ----------
def test_la_memoria_con_historial_completo_recuerda_los_10_datos_clave():
    filas = piloto_con("select cliente_id, contenido from mensajes where config = 'sonda-completa'")
    assert len(filas) == 10
    for f in filas:
        assert re.search(chat.DATO_CLAVE[f["cliente_id"]], f["contenido"], re.I), f"cliente {f['cliente_id']}"


@pytest.mark.xfail(strict=True, reason="Problema conocido del tema 3.9: la ventana de 5 turnos olvida el dato "
                                       "clave de 4 de 10 clientes. Pasará a verde cuando exista la ficha del cliente.")
def test_la_ventana_de_5_turnos_recuerda_los_10_datos_clave():
    olvidos = []
    for f in piloto_con("select cliente_id, contenido from mensajes where config = ? and rol = 'asesor' "
                        "and turno = (select max(turno) from mensajes m2 where m2.cliente_id = mensajes.cliente_id "
                        "and m2.config = mensajes.config)", (chat.CONFIG,)):
        if not re.search(chat.DATO_CLAVE[f["cliente_id"]], f["contenido"], re.I):
            olvidos.append(f["cliente_id"])
    assert olvidos == []


def _precios_validos():
    """Todo precio que el asesor puede decir: los del catálogo y sus múltiplos (noches, personas)."""
    cat = json.loads(RUTA_CATALOGO.read_text(encoding="utf-8"))
    base = [x["precio_desde"] for x in cat["alojamientos"] + cat["tours"]]
    return {p * n for p in base for n in range(1, 61)}


# Montos que no son múltiplo de un solo precio del catálogo, pero que se revisaron a mano (3.10) y son
# sumas o divisiones correctas hechas por el asesor: (cliente, turno, monto).
REVISADOS = {
    (8, 2, "2.060.000"),    # 1.440.000 + 440.000 + 180.000
    (8, 10, "65.000"),      # 260.000 / 4 personas
    (8, 10, "63.000"),      # 190.000 / 3 personas (redondeado)
    (7, 17, "1.280.000"), (7, 18, "1.280.000"), (7, 21, "1.280.000"), (7, 23, "1.280.000"),  # 1.020.000 + 260.000
    (8, 19, "1.480.000"),   # 1.140.000 + 340.000
}


def test_las_respuestas_del_chat_final_solo_dicen_precios_del_catalogo():
    """Cada monto en pesos debe ser un precio del catálogo, un múltiplo (noches, personas) o una suma ya
    revisada. Un monto nuevo hace fallar la prueba: hay que mirarlo antes de aceptarlo."""
    validos = _precios_validos()
    sin_explicar = set()
    for f in piloto_con("select cliente_id, turno, contenido from mensajes where config = ? and rol = 'asesor'",
                        (chat.CONFIG,)):
        for monto in re.findall(r"\$\s?(\d{1,3}(?:\.\d{3})+)", f["contenido"]):
            if int(monto.replace(".", "")) not in validos:
                sin_explicar.add((f["cliente_id"], f["turno"], monto))
    assert sin_explicar <= REVISADOS, sorted(sin_explicar - REVISADOS)
