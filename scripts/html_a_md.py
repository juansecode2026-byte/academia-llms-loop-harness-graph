"""Genera el .md de cada HTML de «Documentación para la construcción del proyecto».

Dirección: HTML -> MD (la documentación es de solo lectura; el HTML manda). El .md es
la versión liviana para leer sin cargar CSS, JS ni miles de etiquetas.

Uso:  python scripts/html_a_md.py            (todos los HTML de la carpeta)
      python scripts/html_a_md.py archivo.html

Código determinístico: no llama a ningún modelo. Solo biblioteca estándar.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "Documentación para la construcción del proyecto"
OMITIR = {"head", "style", "script", "title", "nav"}
VACIOS = {"br", "meta", "link", "img", "hr", "input"}


class Conversor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf = [], []
        self.omitir = 0
        self.pila = []  # etiquetas abiertas (para emparejar cierres)
        self.listas = []  # [tipo, contador]
        self.heading = None
        self.pre = False
        self.pre_buf = []
        self.cita = 0
        self.tabla = None
        self.celda = None
        self.href = []

    # --- salida ---
    def texto(self):
        t = "".join(self.buf)
        self.buf = []
        return re.sub(r"[ \t\r\n]+", " ", t).strip()

    def emitir(self, linea=""):
        self.out.append(("> " + linea).rstrip() if self.cita and linea else linea)

    def vaciar(self):
        t = self.texto()
        if t:
            self.emitir(t)
            self.emitir("")

    def abrir_item(self, tipo):
        self.vaciar()

    # --- eventos ---
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag not in VACIOS:
            self.pila.append((tag, cls))
        if tag in OMITIR:
            self.omitir += 1
            return
        if self.omitir:
            return
        if tag in ("h1", "h2", "h3", "h4"):
            self.vaciar()
            self.heading = int(tag[1])
        elif tag in ("p", "div", "section", "article", "header", "main", "footer", "span") and tag != "span":
            self.vaciar()
            if tag == "div" and ("box" in cls.split() or "concept" in cls.split()):
                self.cita += 1
            if "file" in cls.split():
                self.buf.append("**")
        elif tag in ("ul", "ol"):
            self.vaciar()
            self.listas.append([tag, 0])
        elif tag == "li":
            self.vaciar()
            if self.tabla is None:
                nivel = len(self.listas) - 1
                if self.listas:
                    self.listas[-1][1] += 1
                    marca = f"{self.listas[-1][1]}." if self.listas[-1][0] == "ol" else "-"
                else:
                    marca = "-"
                self.buf.append("  " * max(nivel, 0) + marca + " ")
        elif tag == "pre":
            self.vaciar()
            self.pre = True
            self.pre_buf = []
        elif tag == "table":
            self.vaciar()
            self.tabla = []
        elif tag == "tr" and self.tabla is not None:
            self.tabla.append([])
        elif tag in ("td", "th") and self.tabla is not None:
            self.celda = []
        elif tag == "code" and not self.pre:
            self.buf.append("`")
        elif tag in ("b", "strong"):
            self.buf.append("**")
        elif tag == "a":
            self.href.append(a.get("href", ""))
            self.buf.append("[")
        elif tag == "br":
            self.buf.append(" ")

    def handle_endtag(self, tag):
        cls = ""
        if tag not in VACIOS:
            while self.pila and self.pila[-1][0] != tag:
                self.pila.pop()
            if self.pila:
                cls = self.pila.pop()[1]
        if tag in OMITIR:
            self.omitir -= 1
            return
        if self.omitir:
            return
        if tag in ("h1", "h2", "h3", "h4") and self.heading:
            t = self.texto()
            if t:
                self.emitir("#" * self.heading + " " + t)
                self.emitir("")
            self.heading = None
        elif tag in ("p", "div", "section", "article", "header", "main", "footer"):
            if "file" in cls.split():
                self.buf.append("**")
            self.vaciar()
            if tag == "div" and ("box" in cls.split() or "concept" in cls.split()) and self.cita:
                self.cita -= 1
        elif tag in ("ul", "ol"):
            self.vaciar()
            if self.listas:
                self.listas.pop()
            if not self.listas:
                self.emitir("")
        elif tag == "li" and self.tabla is None:
            t = self.texto()
            if t:
                self.emitir(t)
        elif tag == "pre":
            self.out.append("```")
            self.out.extend("".join(self.pre_buf).strip("\n").split("\n"))
            self.out.append("```")
            self.out.append("")
            self.pre = False
        elif tag in ("td", "th") and self.tabla is not None and self.celda is not None:
            t = self.texto().replace("|", "\\|")
            self.tabla[-1].append(t)
            self.celda = None
        elif tag == "table" and self.tabla is not None:
            filas = [f for f in self.tabla if f]
            if filas:
                ancho = max(len(f) for f in filas)
                filas = [f + [""] * (ancho - len(f)) for f in filas]
                self.emitir("| " + " | ".join(filas[0]) + " |")
                self.emitir("|" + "|".join("---" for _ in range(ancho)) + "|")
                for f in filas[1:]:
                    self.emitir("| " + " | ".join(f) + " |")
                self.emitir("")
            self.tabla = None
        elif tag == "span":
            self.buf.append(" ")
        elif tag == "code" and not self.pre:
            self.buf.append("`")
        elif tag in ("b", "strong"):
            self.buf.append("**")
        elif tag == "a" and self.href:
            self.buf.append(f"]({self.href.pop()})")

    def handle_data(self, data):
        if self.omitir:
            return
        if self.pre:
            self.pre_buf.append(data)
            return
        self.buf.append(data)


def limpiar(md):
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def de_html(texto):
    c = Conversor()
    c.feed(texto)
    c.vaciar()
    return limpiar("\n".join(c.out))


def pensum(texto):
    """El pensum se dibuja con JavaScript: se lee el arreglo `skills` y se escribe como md."""
    m = re.search(r"const skills = (\[.*?\n\]);", texto, re.S)
    crudo = m.group(1)
    crudo = re.sub(r"([{,]\s*)(\w+):", r'\1"\2":', crudo)
    skills = json.loads(crudo)
    niveles = ["Nivel 1 · Fundamentos", "Nivel 2 · Intermedio", "Nivel 3 · Avanzado", "Nivel 4 · Experto"]
    titulo = re.search(r"<title>(.*?)</title>", texto).group(1)
    md = [f"# {titulo}", "",
          "Ruta de estudio para las habilidades más pedidas en ofertas de AI Engineer: 10 habilidades de IA y "
          "6 lenguajes de programación, cada una en 4 niveles con temas, herramientas y un proyecto que demuestra el nivel.", ""]
    for i, s in enumerate(skills, 1):
        if s.get("group"):
            md += [f"## {s['group']}", "", s.get("gsub", ""), ""]
        md += [f"### {i:02d}. {s['name']} ({s['pct']} % de las vacantes)", "", s["desc"], ""]
        for n, lv in enumerate(s["levels"]):
            md += [f"#### {niveles[n]} · {lv['t']}", ""]
            md += [f"{k}. {x}" for k, x in enumerate(lv["items"], 1)]
            md += ["", "Herramientas: " + ", ".join(lv["tools"]), "", "Proyecto: " + lv["proj"], ""]
    return limpiar("\n".join(md))


def convertir(ruta):
    texto = ruta.read_text(encoding="utf-8")
    return pensum(texto) if "const skills = [" in texto else de_html(texto)


def main():
    destinos = [Path(a) for a in sys.argv[1:]] or sorted(CARPETA.glob("*.html"))
    for h in destinos:
        salida = h.with_suffix(".md")
        salida.write_text(convertir(h), encoding="utf-8")
        print("ok", salida.name, f"({salida.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
