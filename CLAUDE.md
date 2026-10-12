# Academia LLMs · Loop, Harness, Graph

Las reglas universales del laboratorio (aislamiento entre proyectos, estructura
de `PLANTILLA/`, scripts vs. agentes, `DECISIONES.md`) se cargan solas desde el
`CLAUDE.md` de la raíz del laboratorio. Aquí solo va lo propio de este proyecto.

## Objetivo

Portafolio que demuestra conocimiento en AI Engineering: construir proyectos
manualmente y apoyándose en IA, con cada avance como commit en GitHub (el commit
es la prueba). Lo aprendido se transfiere después a Minus, la empresa del usuario
y su socio, para implementarlo en sus proyectos.

## Alcance

La habilidad **LLMs** del Pensum AI Engineer v1.1, niveles 1 a 4. El Nivel 1 se
construye con la guía v7: chat de consola (F0, E1–E10), laboratorio de parámetros
(D0–D14), ingeniería agéntica (AG0–AG9) y tablero agéntico (DA0–DA6). Solo SDK
de Anthropic.

Los códigos F0, E1–E10, D0–D14, AG0–AG9 y DA0–DA6 son etiquetas internas de la
guía v7 (Fase 0, Etapa, Laboratorio/Dashboard, Agente, Dashboard del agente). En los
documentos de `resultados/` los temas se identifican por nombre y número de
sección; el código solo aparece como referencia «ver guía».

## Dos modos de trabajo

Cada tema se hace dos veces, en este orden:

1. **Manual (guiado con Claude):** Claude escribe el código y explica cada parte; el
   usuario ejecuta, revisa y no avanza sin entender qué pasa y por qué. No es
   programar sin ayuda, es no delegar sin entender. Al trabajar en este modo:
   explicar cada bloque antes o después de escribirlo, ir etapa por etapa y
   dejar que el usuario ejecute y observe.
2. **Agentizado:** el proceso se delega a agentes (loops, scripts con el SDK) que
   ejecutan con autonomía, partiendo del proceso manual ya entendido; el usuario
   define el objetivo, pone los límites y revisa. Se mide qué cambia en tiempo,
   costo y calidad.

Un tema no se agentiza hasta que su versión manual está cerrada y documentada.

## Estructura de carpetas

| Carpeta | Contenido |
|---|---|
| `Documentación para la construcción del proyecto/` | Material de referencia: el pensum y la guía v7. Es solo lectura; no se edita. |
| `resultados/` | Lo que produce el proyecto: los dos documentos de seguimiento. |

Documentos en `resultados/` (cada uno es un par `.md` + `.html`):

- `resultados-proceso-manual.md` / `.html`
- `resultados-proceso-agentizando.md` / `.html`
- `transferencia-crm-ventas.md` / `.html` — cómo se lleva lo aprendido al CRM de ventas
  (candyCRM). Se revisó ese repo a pedido del usuario; nunca se modifica desde aquí.

## Fuente de verdad: los .md

El usuario lee los HTML, pero **el contexto de trabajo sale de los .md**. Reglas:

- **Resultados:** el `.md` manda. Para cualquier cambio (marcar una casilla `- [x]`,
  agregar notas, evidencias, una fila de bitácora) se edita el `.md` y luego se
  regenera el HTML con `python scripts/md_a_html.py`. Nunca se edita el HTML a mano:
  se pisaría en la siguiente regeneración. Siempre se commitean los dos archivos.
- **Documentación** (pensum y guía v7): el HTML manda y es de solo lectura. Su `.md`
  se genera con `python scripts/html_a_md.py`, solo para leerlo con poco contexto.
  Si se agrega un HTML nuevo a esa carpeta, se corre el script para crear su `.md`.
- Al leer la guía o el pensum, leer el `.md`, no el HTML.
- Las casillas que el usuario marca en el navegador viven solo en su navegador.
  Cuando el usuario confirma que algo está hecho, se marca en el `.md`.
- **Al marcar un tema como hecho** en el manual, agregar una entrada en su sección final
  «Análisis de resultados» (sin número) → «Lo que vamos logrando»: `#### N.M · Tema (fecha)`, con
  «Qué se hizo» y «A qué nos conduce», en palabras simples para alguien que empieza.

### Formato de los .md de resultados

Bloque inicial `---` con `doc`, `titulo`, `fecha`, `gemelo` y `lead`. Luego:
`# título`; `## N. Sección` (con `{nivel=K}` para los niveles); `### N.M Tema`
(con `{ref=idguia:E1 etiqueta="..."}` o `{proyecto}`); `#### subtítulo`; listas
`- [ ]` / `- [x]`; `1.` listas numeradas; tablas con `|`; notas con `> **Título**`
y `> _texto_`; `⏱` línea de duración y herramientas; `🛠` línea del proyecto. Una sección sin número
(`## Título {id=x}`) se muestra destacada: título grande y otra tipografía. La
marca `<!-- parte: n | Título | Subtítulo | pN -->` antes de un tema agrupa el
índice de la guía. Los números de sección y de tema se escriben a mano y deben
seguir la secuencia; los ids de los enlaces salen de ellos (`s3-2`, `s3-proyecto`).

Misma numeración en ambos (secciones 1–9; niveles = secciones 3–6), con índice
numerado al inicio y checklist por tema. Cada tema del agentizando enlaza a su
equivalente del manual. Los nuevos HTML de resultados van en `resultados/`, nunca
en la carpeta de documentación.

## Convenciones

- Idioma: español, en documentos, commits y comentarios.
- Los HTML de resultados son autocontenidos (sin dependencias
  externas) con modo claro y oscuro.
- Las casillas del checklist se marcan en el `.md` (`- [x]`) y se commitea; es lo que
  cuenta como prueba.
- Cada documento tiene una bitácora de cambios (sección 9): toda modificación
  agrega una fila con fecha.
- Si sale una versión nueva del pensum o de la guía, se agrega como archivo nuevo
  en la carpeta de documentación; no se reemplaza la anterior.
- La API key va en `.env`, nunca en el código ni en commits.
- Commits convencionales, uno por etapa cerrada, con el mensaje que indica la guía
  (por ejemplo `etapa 1: primera llamada a la API`).
- "Artefacto" es una página publicada en claude.ai. La vitrina «Chat y Laboratorio
  Terminados» vive solo como artefacto: https://claude.ai/artifact/1gdPaiwxYXdoMyPe43rX1W

## Repositorio

https://github.com/juansecode2026-byte/academia-llms-loop-harness-graph (privado, rama `main`).
El Nivel 1 de ambos documentos de `resultados/` sigue las etapas de la guía v7
(manual: F0, E1–E10, D0–D14; agentizando: AG0–AG9, DA0–DA6). Los niveles 2 a 4
todavía usan los temas genéricos del pensum.

## Pendiente

- Este proyecto aún no tiene la estructura completa de la plantilla del
  laboratorio (`NOTAS.md`, `DECISIONES.md`, `.mcp.json`, `scripts/`,
  `agentes-sdk/`, `.claude/`). Decidir con el usuario cuáles se crean.
