"""Regenera los HTML de resultados/ a partir de sus .md (la fuente de verdad).

Uso:  python scripts/md_a_html.py            (todos los .md de resultados/)
      python scripts/md_a_html.py archivo.md (uno solo)

Código determinístico: no llama a ningún modelo. Solo biblioteca estándar.
Formato del .md: ver la sección «Formato de los .md» de CLAUDE.md.
"""
import html
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "resultados"
PLANTILLA = (Path(__file__).resolve().parent / "plantilla-resultados.html").read_text(encoding="utf-8")
GUIA = ("../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/"
        "llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html")


# ---------- inline ----------
def inline(t):
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def attrs(s):
    """Lee {clave=valor clave="valor con espacios" bandera}."""
    out = {}
    for m in re.finditer(r'(\w+)(?:=("[^"]*"|[^\s}]+))?', s):
        v = m.group(2)
        out[m.group(1)] = v.strip('"') if v else True
    return out


# ---------- bloques ----------
def render_blocks(lines, prefix):
    """Convierte líneas de md en html. Devuelve (html, cantidad_de_casillas)."""
    out, n, i = [], 0, 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if re.match(r"- \[[ xX]\] ", ln):
            items = []
            while i < len(lines) and re.match(r"- \[[ xX]\] ", lines[i]):
                m = re.match(r"- \[([ xX])\] (.*)", lines[i])
                n += 1
                chk = " checked" if m.group(1) in "xX" else ""
                items.append(f'<li><label><input type="checkbox" data-id="{prefix}-{n}"{chk}>'
                             f"<span>{inline(m.group(2))}</span></label></li>")
                i += 1
            out.append('<ul class="check">' + "".join(items) + "</ul>")
        elif re.match(r"\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i]))}</li>")
                i += 1
            out.append('<ol class="plain">' + "".join(items) + "</ol>")
        elif re.match(r"- ", ln):
            items = []
            while i < len(lines) and re.match(r"- ", lines[i]) and not re.match(r"- \[[ xX]\] ", lines[i]):
                items.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c) for c in r)]
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
        elif ln.startswith(">"):
            parts = []
            while i < len(lines) and lines[i].startswith(">"):
                parts.append(lines[i][1:].strip())
                i += 1
            label = re.fullmatch(r"\*\*(.+)\*\*", parts[0])
            cuerpo = parts[1:] if label else parts
            ps = ""
            for p in cuerpo:
                if not p:
                    continue
                v = re.fullmatch(r"_(.+)_", p)
                ps += f'<p class="vacio">{inline(v.group(1))}</p>' if v else f"<p>{inline(p)}</p>"
            out.append(f'<div class="nota"><b>{label.group(1) if label else "Notas"}</b>{ps}</div>')
        elif ln.startswith("#### "):
            txt = ln[5:]
            m = re.match(r"(\d+)(?:\.(\d+))? · ", txt)
            if m and prefix == "analisis":
                # entrada del análisis de resultados: ancla propia y enlace de vuelta al tema
                tid = f"s{m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")
                out.append(f'<h3 id="an-{tid}">{inline(txt)} <a class="volver" href="#{tid}">↑ ver el tema</a></h3>')
            else:
                out.append(f"<h3>{inline(txt)}</h3>")
            i += 1
        elif ln.startswith("<!--"):
            i += 1
        elif ln.startswith("⏱"):
            txt = ln
            if "Herramientas:" in txt:
                pre, tools = txt.split("Herramientas:", 1)
                tags = " ".join(f'<span class="tag">{t.strip()}</span>' for t in tools.split(","))
                txt = f"{pre}Herramientas: {tags}"
            out.append(f'<p class="meta">{txt}</p>')
            i += 1
        elif ln.startswith("🛠"):
            out.append(f'<p class="proj">{inline(ln)}</p>')
            i += 1
        else:
            buf = [ln]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"(- |\d+\. |\||>|<!--|⏱|🛠)", lines[i]):
                buf.append(lines[i])
                i += 1
            out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "".join(out), n


# ---------- documento ----------
def parse(texto):
    m = re.search(r"^---\n(.*?)\n---\n(.*)", texto, re.S | re.M)
    meta = dict(re.match(r"(\w+):\s*(.*)", l).groups() for l in m.group(1).splitlines() if l.strip())
    return meta, m.group(2).splitlines()


def construir(md_path):
    meta, lines = parse(md_path.read_text(encoding="utf-8"))
    con_analisis = {f"s{a}" + (f"-{b}" if b else "")
                    for a, b in (re.match(r"#### (\d+)(?:\.(\d+))? · ", l).groups()
                                 for l in lines if re.match(r"#### \d+(?:\.\d+)? · ", l))}

    def titular(tid, cuerpo):
        """Envuelve número + título en un enlace a su análisis, si existe."""
        if tid in con_analisis:
            return (f'<a class="al-analisis" href="#an-{tid}" title="Ir al análisis de resultados">{cuerpo}'
                    f'<span class="ir-analisis">análisis ↓</span></a>')
        return cuerpo
    h1 = ""
    secciones = []  # {num, titulo, attrs, lineas, temas:[{num,titulo,attrs,lineas}], parte_marks}
    cur = tema = None
    for ln in lines:
        if ln.startswith("# "):
            h1 = inline(ln[2:])
        elif ln.startswith("## "):
            m = re.match(r"## (?:(\d+)\. )?(.*?)\s*(\{.*\})?$", ln)
            cur = {"num": m.group(1), "titulo": m.group(2), "attrs": attrs(m.group(3) or ""), "lineas": [], "temas": []}
            secciones.append(cur)
            tema = None
        elif ln.startswith("### "):
            m = re.match(r"### (\d+)\.(\d+) (.*?)\s*(\{.*\})?$", ln)
            tema = {"sec": m.group(1), "n": m.group(2), "titulo": m.group(3),
                    "attrs": attrs(m.group(4) or ""), "lineas": [], "parte": None}
            cur["temas"].append(tema)
        else:
            pm = re.match(r"<!-- parte: (.*?) \| (.*?) \| (.*?) \| (\w+) -->", ln)
            if pm and cur is not None:
                cur.setdefault("partes", []).append((len(cur["temas"]), pm.groups()))
            (tema if tema else cur)["lineas"].append(ln) if cur is not None else None

    cuerpo, toc_items, nivel1 = [], [], None
    for s in secciones:
        if not s["num"]:
            # sección destacada, sin número: título grande, otra tipografía, al final
            sid = s["attrs"].get("id", "destacada")
            inner, _ = render_blocks(s["lineas"], sid)
            cuerpo.append(f'<section id="{sid}" class="destacada"><h2 class="destacada-t">{s["titulo"]}</h2>{inner}</section>')
            toc_items.append((sid, "✦", s["titulo"], []))
            continue
        sid = f"s{s['num']}"
        nivel = s["attrs"].get("nivel")
        if not nivel:
            inner, _ = render_blocks(s["lineas"], sid)
            cab = titular(sid, f'<span class="num">{s["num"]}</span>{s["titulo"]}')
            cuerpo.append(f'<section id="{sid}"><h2>{cab}</h2>{inner}</section>')
            toc_items.append((sid, s["num"], s["titulo"], []))
            continue
        nivel1 = nivel1 or (s if nivel == "1" else None)
        partes = [render_blocks(s["lineas"], sid)[0]]
        subs = []
        for t in s["temas"]:
            es_proy = "proyecto" in t["attrs"]
            tid = f"{sid}-proyecto" if es_proy else f"{sid}-{t['n']}"
            num = f"{t['sec']}.{t['n']}"
            subs.append((tid, num, t["titulo"]))
            chip = ""
            if t["attrs"].get("etiqueta"):
                chip += f' <span class="tag">{t["attrs"]["etiqueta"]}</span>'
            if t["attrs"].get("ref"):
                gid, cod = t["attrs"]["ref"].split(":")
                chip += f'<span class="refwrap"><a class="ref" href="{GUIA}#{gid}">ver guía: {cod}</a></span>'
            inner, _ = render_blocks(t["lineas"], tid)
            cab = titular(tid, f'<span class="num">{num}</span>{html.escape(t["titulo"])}')
            partes.append(f'<article class="topic{" proyecto" if es_proy else ""}" id="{tid}"><h3>'
                          f'{cab}{chip}</h3>{inner}</article>')
        cuerpo.append(f'<section id="{sid}" class="level" style="--c:var(--l{nivel})"><h2><span class="num">{s["num"]}</span>'
                      f'{s["titulo"]}</h2>{"".join(partes)}</section>')
        toc_items.append((sid, s["num"], s["titulo"], subs))
        s["subs"] = subs

    def toc_li(sid, num, name, subs):
        sub = ""
        if subs:
            sub = "<ol>" + "".join(
                f'<li><a href="#{a}"><i class="ck" data-for="{a}"></i><b>{b}</b>{html.escape(c)}'
                f'<span class="pg" data-for="{a}"></span></a></li>' for a, b, c in subs) + "</ol>"
        return (f'<li><a href="#{sid}"><i class="ck" data-for="{sid}"></i><b>{num}</b>{name}'
                f'<span class="pg" data-for="{sid}"></span></a>{sub}</li>')

    toc = '<nav id="indice" class="toc"><h2>Índice</h2><ol>' + "".join(toc_li(*t) for t in toc_items) + "</ol></nav>"

    # índice de la guía (Nivel 1): tarjetas por parte, según las marcas «parte» del .md
    if nivel1:
        tarjetas = []
        fuera = [(sid, num, nom) for sid, num, nom, _ in toc_items if not any(sid == f"s{x['num']}" and x["attrs"].get("nivel") for x in secciones)]
        li_doc = "".join(f'<li class="nc"><a href="#{a}"><i class="ck" data-for="{a}"></i><span class="gi-num">{b}</span>'
                         f'<span class="gi-t">{c}</span></a></li>' for a, b, c in fuera)
        nums = [b for _, b, _ in fuera if b.isdigit()]
        rango = f"Secciones {nums[0]}–{nums[1]} y {nums[2]}–{nums[-1]}" if len(nums) > 3 else "Secciones"
        if len(nums) < len(fuera):
            rango += " · Análisis"
        tarjetas.append('<section class="gi-card" style="--c:var(--text)"><header><span class="gi-n">§</span>'
                        f"<div><b>Documento</b><span>{rango}</span></div></header><ol>{li_doc}</ol></section>")
        marcas = nivel1.get("partes", [])
        subs = nivel1["subs"]
        corte = [m[0] for m in marcas] + [len(subs) - 1]
        for k, (ini, (n, titulo, subt, color)) in enumerate(marcas):
            fin = corte[k + 1]
            lis = "".join(f'<li><a href="#{a}"><i class="ck" data-for="{a}"></i><span class="gi-num">{b}</span>'
                          f'<span class="gi-t">{html.escape(c)}</span></a></li>' for a, b, c in subs[ini:fin])
            tarjetas.append(f'<section class="gi-card" style="--c:var(--{color})"><header><span class="gi-n">{n}</span>'
                            f"<div><b>{titulo}</b><span>{subt}</span></div></header><ol>{lis}</ol></section>")
        a, b, c = subs[-1]
        tarjetas.append('<section class="gi-card" style="--c:var(--l1)"><header><span class="gi-n">★</span>'
                        '<div><b>Cierre del nivel</b><span>Proyecto del nivel 1</span></div></header><ol>'
                        f'<li class="nc"><a href="#{a}"><i class="ck" data-for="{a}"></i><span class="gi-num">{b}</span>'
                        f'<span class="gi-t">{c}</span></a></li></ol></section>')
        toc += ('<nav id="indice-guia" class="gi" aria-label="Índice de la guía"><h2>Índice de la guía · Nivel 1</h2>'
                '<p class="gi-sub">Las mismas etapas de la guía v7, en su orden, cada una enlazada a su checklist. '
                'El índice de arriba sigue el orden del documento.</p><div class="gi-grid">' + "".join(tarjetas) + "</div></nav>")

    gem_url, gem_txt = meta["gemelo"].split("|")
    twin = f'<a href="{gem_url.strip()}">{gem_txt.strip()}</a>'
    reemplazos = {"title": meta["titulo"], "h1": h1, "lead": inline(meta["lead"]), "twin": twin,
                  "fecha": meta["fecha"], "toc": toc, "body": "".join(cuerpo), "key": meta["doc"]}
    out = PLANTILLA
    for k, v in reemplazos.items():
        out = out.replace(f"%%{k}%%", v)
    return out


def main():
    destinos = [Path(a) for a in sys.argv[1:]] or sorted(CARPETA.glob("*.md"))
    for md in destinos:
        salida = md.with_suffix(".html")
        salida.write_text(construir(md), encoding="utf-8")
        print("ok", salida.name)


if __name__ == "__main__":
    main()
