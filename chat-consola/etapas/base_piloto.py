"""Base de datos del piloto (SQLite): una sola base, con tres tablas.

- clientes:    los 10 clientes ficticios.
- mensajes:    el historial de cada cliente; es la memoria del asesor.
- ejecuciones: cada llamada a Claude, con su configuración y su medición.

Se crea en el tema 3.4 (antes de lo previsto, porque la medición necesita guardar cada
llamada). El tema 3.16 la amplía con el registro de experimentos de la guía.
"""
import json
import sqlite3
from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "datos-simulados"
RUTA_BASE = CARPETA / "piloto-simulado.db"
RUTA_CLIENTES = CARPETA / "clientes-simulados.json"

ESQUEMA = """
create table if not exists clientes (
    id integer primary key,
    nombre text not null,
    telefono text not null,
    perfil text,
    dato_a_recordar text,
    trampa text,
    destinos_interes text
);
create table if not exists mensajes (
    id integer primary key autoincrement,
    cliente_id integer not null references clientes(id),
    turno integer not null,
    rol text not null check (rol in ('cliente', 'asesor')),
    contenido text not null,
    creado text default (datetime('now')),
    unique (cliente_id, turno, rol)
);
create table if not exists ejecuciones (
    id integer primary key autoincrement,
    cliente_id integer not null references clientes(id),
    turno integer not null,
    modelo text not null,
    effort text,
    ventana text,
    catalogo text,
    tokens_entrada integer,
    tokens_salida integer,
    tokens_razonamiento integer,
    costo_usd real,
    segundos real,
    stop_reason text,
    creado text default (datetime('now')),
    unique (cliente_id, turno, modelo, effort, ventana, catalogo)
);
"""


def conectar() -> sqlite3.Connection:
    con = sqlite3.connect(RUTA_BASE, timeout=60)
    con.row_factory = sqlite3.Row
    con.executescript(ESQUEMA)
    return con


def cargar_clientes(con: sqlite3.Connection) -> list[dict]:
    """Lee los clientes del JSON, los registra en la base (si faltan) y los devuelve."""
    clientes = json.loads(RUTA_CLIENTES.read_text(encoding="utf-8"))["clientes"]
    for c in clientes:
        con.execute(
            "insert or ignore into clientes (id, nombre, telefono, perfil, dato_a_recordar, trampa, destinos_interes) "
            "values (?, ?, ?, ?, ?, ?, ?)",
            (c["id"], c["nombre"], c["telefono"], c["perfil"], c["dato_a_recordar"], c["trampa"],
             ",".join(c["destinos_interes"])),
        )
    con.commit()
    return clientes


def historial(con: sqlite3.Connection, cliente_id: int, hasta_turno: int | None = None) -> list[dict]:
    """Mensajes del cliente en el formato de la API (user/assistant), en orden."""
    filas = con.execute(
        "select turno, rol, contenido from mensajes where cliente_id = ? "
        + ("and turno <= ? " if hasta_turno else "")
        + "order by turno, case rol when 'cliente' then 0 else 1 end",
        (cliente_id, hasta_turno) if hasta_turno else (cliente_id,),
    ).fetchall()
    return [{"role": "user" if f["rol"] == "cliente" else "assistant", "content": f["contenido"]} for f in filas]
