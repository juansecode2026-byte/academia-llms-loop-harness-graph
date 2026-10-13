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

1. **Manual (guiado con Claude):** Claude escribe el código, lo ejecuta, lo explica y
   documenta lo que pasa (notas, análisis de resultados, casillas); el usuario supervisa
   y revisa en los documentos. No es programar sin ayuda: es no delegar sin entender, con
   el aprendizaje escrito. El usuario **no escribe notas ni resúmenes con sus palabras**:
   todo lo documental lo hace Claude. Al trabajar en este modo: ir etapa por etapa,
   explicar cada bloque, ejecutar los comandos (salvo los que exigen la clave o una
   decisión del usuario) y dejar el avance marcado en el `.md`.
2. **Agentizado:** el proceso se delega a agentes (loops, scripts con el SDK) que
   ejecutan con autonomía, partiendo del proceso manual ya entendido; el usuario
   define el objetivo, pone los límites y revisa. Se mide qué cambia en tiempo,
   costo y calidad.

Un tema no se agentiza hasta que su versión manual está cerrada y documentada.

## Estructura de carpetas

| Carpeta | Contenido |
|---|---|
| `Documentación para la construcción del proyecto/` | Material de referencia: el pensum y la guía v7 (solo lectura), y `ejercicio-simulado-chat-consola` (escrito aquí: su `.md` es la fuente y `html_a_md.py` lo omite). |
| `resultados/` | Lo que produce el proyecto: los dos documentos de seguimiento. |

Documentos en `resultados/` (cada uno es un par `.md` + `.html`):

- `resultados-proceso-manual.md` / `.html`
- `resultados-proceso-agentizando.md` / `.html` — segundo pase opcional (repetir cada tema con agentes más adelante)

## Documentación para otros proyectos

`Documentación para otros proyectos/` guarda lo que se extrae de este proyecto para
usarlo en otros (hoy: `documentacion-para-aplicar-en-candy-crm-ventas`, cómo se lleva lo aprendido a candyCRM).
Es **solo local: no se sube a git** (está en `.gitignore`; no se hace `git init` ahí ni
se hacen commits de esa carpeta). Sirve para que el usuario sepa que existe y de qué
proyecto salió. Los repos de los otros proyectos (por ejemplo `CRM VENTAS`) nunca se
modifican desde aquí. Sigue la misma regla de `.md` fuente + HTML regenerado
(`python scripts/md_a_html.py "Documentación para otros proyectos/<archivo>.md"`).

## Ejercicio simulado

El Nivel 1 se construye sobre un caso simulado: un asesor de viajes («Turismo Colombia
(simulada)») que atiende por WhatsApp a clientes ficticios, piloto de 10 clientes, con
catálogo JSON y **una sola** base SQLite (clientes, mensajes, ejecuciones) que nace en el
tema 3.7 y que el tema 3.16 amplía con el registro de experimentos, sin crear otra. Explicación y fases en
`Documentación para la construcción del proyecto/ejercicio-simulado-chat-consola.md`.
Sus pasos son casillas «Ejercicio X.N» dentro de los temas del manual: se marcan allí.
La infraestructura de WhatsApp y Supabase quedan para candyCRM.

**Todo en un solo lugar y nada se aplaza (decisión del 2026-10-13):** el checklist se reinició sobre el ejercicio y
cubre todo el Nivel 1, dashboards incluidos: 3.2 a 3.4 se rehacen con el caso, la Fase E
(3.12 a 3.26, pasos E.1 a E.15) cubre el laboratorio y la Fase F (F.1 a F.17) el agente y su
tablero. Más adelante se puede evaluar juntar todos los resultados en un solo archivo.

## Fuente de verdad: los .md

El usuario lee los HTML, pero **el contexto de trabajo sale de los .md**. Reglas:

- **Resultados:** el `.md` manda. Para cualquier cambio (marcar una casilla `- [x]`,
  agregar notas, evidencias, una fila de bitácora) se edita el `.md` y luego se
  regenera el HTML con `python scripts/md_a_html.py`. Nunca se edita el HTML a mano:
  se pisaría en la siguiente regeneración. Siempre se commitean los dos archivos.
- **Documentación** (pensum y guía v7): el HTML manda y es de solo lectura. Su `.md`
  se genera con `python scripts/html_a_md.py`, solo para leerlo con poco contexto.
  Si se agrega un HTML nuevo a esa carpeta, se corre el script para crear su `.md`.
- **Claude lee siempre el `.md`, nunca el HTML**, en cualquier carpeta (guía, pensum,
  ejercicio simulado, resultados). Los HTML son solo para que el usuario los lea; se
  regeneran y se dejan como están.
- Las casillas que el usuario marca en el navegador viven solo en su navegador.
  Cuando el usuario confirma que algo está hecho, se marca en el `.md`.
- **Al marcar un tema como hecho** en el manual, agregar una entrada en su sección final
  «Análisis de resultados» (sin número) → «Lo que vamos logrando»: `#### N.M · Tema (fecha)`, con
  «Qué se hizo», «A qué nos conduce» y un `> **Ejemplo**` concreto (con números reales
  cuando los haya), en palabras simples para alguien que empieza. El título del tema
  enlaza solo a esa entrada: el formato `#### N.M · ` es lo que lo activa.

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

Secciones 1–9; niveles = secciones 3–6, con índice numerado al inicio y checklist por
tema. **El seguimiento de todo el Nivel 1 está en el manual**: Partes 1 y 2 (temas 3.1 a
3.26), Partes 3 y 4 con el agente y su tablero (temas 3.27 a 3.43) y el proyecto (3.44). Los nuevos HTML de resultados van en `resultados/`, nunca
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
