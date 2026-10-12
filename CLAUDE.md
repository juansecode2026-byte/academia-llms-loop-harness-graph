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

## Dos modos de trabajo

Cada tema se hace dos veces, en este orden:

1. **Manual:** el usuario escribe el código para aprender el proceso. La IA solo
   resuelve dudas puntuales; no entrega el código ya hecho.
2. **Agentizado:** se repite con apoyo de agentes, partiendo del proceso manual ya
   entendido, y se mide qué cambia en tiempo, costo y calidad.

Un tema no se agentiza hasta que su versión manual está cerrada y documentada.

## Estructura de carpetas

| Carpeta | Contenido |
|---|---|
| `Documentación para la construcción del proyecto/` | Material de referencia: el pensum y la guía v7. Es solo lectura; no se edita. |
| `resultados/` | Lo que produce el proyecto: los dos documentos de seguimiento. |

Documentos en `resultados/`:

- `resultados-proceso-manual.html`
- `resultados-proceso-agentizando.html`

Misma numeración en ambos (secciones 1–10; niveles = secciones 4–7), con índice
numerado al inicio y checklist por tema. Cada tema del agentizando enlaza a su
equivalente del manual. Los nuevos HTML de resultados van en `resultados/`, nunca
en la carpeta de documentación.

## Convenciones

- Idioma: español, en documentos, commits y comentarios.
- Los documentos de resultados son HTML autocontenidos (sin dependencias
  externas) con modo claro y oscuro.
- Las casillas del checklist se guardan en el navegador; para que cuenten como
  prueba se agrega `checked` en el HTML y se hace commit.
- Cada documento tiene una bitácora de cambios (sección 10): toda modificación
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
