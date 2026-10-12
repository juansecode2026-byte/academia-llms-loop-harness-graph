<!-- Fuente de verdad. Editar este .md y correr: python scripts/md_a_html.py (regenera el HTML). -->
---
doc: manual
titulo: Resultados · Proceso manual
fecha: 2026-10-12
gemelo: resultados-proceso-agentizando.html | Ir al documento agentizando →
lead: Academia LLMs — módulo LLMs del Pensum AI Engineer. Aquí se documenta, tema por tema y en formato checklist, cómo se construye cada pieza **con Claude como copiloto**, entendiendo qué pasa en cada paso, para dominar el proceso antes de agentizarlo.
---

# Resultados del proceso <em>manual</em>

## 1. Cómo usar este documento

1. **Qué significa «manual» aquí:** el proceso se hace paso a paso con Claude, que escribe el código y lo explica; yo reviso, ejecuto y no avanzo hasta entender qué pasa y por qué. No es programar sin ayuda: es no delegar sin entender.
2. Avanzar en orden: no se pasa de nivel sin terminar el proyecto del nivel anterior — el proyecto es la prueba.
3. Cada tema tiene el mismo checklist de 5 pasos y un bloque de **Notas del proceso** que se reemplaza por lo aprendido.
4. Las casillas se guardan en este navegador. Para que el avance quede como prueba en GitHub, al cerrar un tema se marcan sus casillas en el `.md` (`- [x]`), se regenera el HTML y se hace commit.
5. Todo lo que se aprenda aquí alimenta el documento [agentizando](resultados-proceso-agentizando.html), que reutiliza la misma numeración.

## 2. Objetivo, alcance y base del proyecto

Construir un portafolio que demuestre conocimiento en AI Engineering, construyendo proyectos de forma guiada, con Claude escribiendo el código mientras yo entiendo cada paso, y con cada avance registrado en commits de GitHub.

El conocimiento se transfiere después a **Minus** para implementarlo en sus proyectos.

**Alcance de este repositorio:** la habilidad **LLMs** del pensum, niveles 1 a 4. El entorno de Python y la API key se preparan en la [Preparación (3.1)](#s3-1).

- [x] Objetivo y alcance escritos en el `CLAUDE.md` del proyecto
- [x] Repositorio en GitHub creado (privado, rama `main`)
- [x] Git configurado y primer commit hecho
- [x] `.gitignore` que excluye `.env` y entornos virtuales
- [x] Documentación (pensum y guía v7) separada de los resultados

## 3. Nivel 1 · Fundamentos {nivel=1}

⏱ 2–3 semanas · Herramientas: Anthropic API, OpenAI API, Gemini API

<!-- parte: 1 | Parte 1 · Chat de consola con memoria | Preparación y 10 etapas | p1 -->

### 3.1 Preparación {ref=f0:F0}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#f0)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "fase 0: entorno y configuración"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.2 Primera llamada a la API {ref=e1:E1}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e1)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 1: primera llamada a la API"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.3 Ver cómo el modelo predice tokens {ref=e2:E2}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e2)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 2: streaming y razonamiento"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.4 Tokens, ventana de contexto y costos {ref=e3:E3}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e3)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 3: tokens y costos"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.5 Parámetros de generación {ref=e4:E4}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e4)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 4: parámetros de generación"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.6 Panorama de modelos de Anthropic {ref=e5:E5}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e5)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 5: panorama de modelos"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.7 Primer chat con memoria {ref=e6:E6}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e6)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 6: chat con memoria"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.8 Limitaciones de los LLM {ref=e7:E7}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e7)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 7: pruebas de limitaciones"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.9 Ensamblar el chat final {ref=e8:E8}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e8)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 8: chat final ensamblado"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.10 Pruebas automáticas sin gastar tokens {ref=e9:E9}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e9)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 9: pruebas automáticas"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.11 Cierre del nivel {ref=e10:E10}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e10)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

<!-- parte: 2 | Parte 2 · Laboratorio de parámetros | 15 apartados | p2 -->

### 3.12 Qué vas a construir (laboratorio) {ref=d0:D0}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d0)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.13 Qué controlamos y qué medimos {ref=d1:D1}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d1)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.14 Preparación del laboratorio {ref=d2:D2}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d2)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D2: preparación del laboratorio"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.15 Motor de medición {ref=d3:D3}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d3)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D3: motor de medición"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.16 Registro de experimentos (SQLite) {ref=d4:D4}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d4)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D4: registro en SQLite"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.17 Batería de preguntas y modelo juez {ref=d5:D5}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d5)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D5: batería y juez"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.18 Estructura de la app {ref=d6:D6}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d6)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D6: estructura de la app"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.19 Controles {ref=d7:D7}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d7)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.20 Vista Playground {ref=d8:D8}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d8)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.21 Vista Comparador {ref=d9:D9}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d9)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.22 Vista Batería de alucinaciones {ref=d10:D10}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d10)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.23 Vista Métricas {ref=d11:D11}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d11)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.24 Pruebas del laboratorio {ref=d12:D12}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d12)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D12: pruebas del laboratorio"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.25 Experimentos y cierre {ref=d13:D13}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d13)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 3.26 Tablero de decisiones {ref=d14:D14 etiqueta="En plan en la guía"}

- [ ] Leer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d14)
- [ ] Construirlo con Claude siguiendo «Construcción»: que escriba el código y explique cada parte; no avanzar sin entender qué hace
- [ ] Ejecutarlo y comparar con «Ejecuta y observa» o el punto de control
- [ ] Anotar con tus palabras qué hace el código y qué observaste; responder «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D14: tablero de decisiones"`

> **Notas del proceso**
> _Pendiente de documentar._

### 3.27 Proyecto del nivel {proyecto}

🛠 Chatbot de consola con memoria de conversación usando un SDK oficial.

- [ ] Definir alcance, entradas, salidas y criterio de “terminado”
- [ ] Construir con Claude la versión mínima funcional, entendiendo cada decisión de diseño
- [ ] Escribir README del proyecto: qué hace, cómo se ejecuta, decisiones tomadas
- [ ] Dejar evidencia: capturas, ejemplos de entrada/salida o video corto
- [ ] Commit + tag de versión del nivel (ej. `llm-n1-v1`)
- [ ] Anotar en la sección 8 qué partes del proceso son candidatas a agentizar

> **Resultado y evidencia**
> _Pendiente de documentar._

## 4. Nivel 2 · Intermedio {nivel=2}

⏱ 4–6 semanas · Herramientas: SDK Python, Pydantic, tiktoken

### 4.1 SDKs a fondo: mensajes, roles, system prompt

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.2 Streaming de respuestas

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.3 Salidas estructuradas (JSON / esquemas)

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.4 Tool use / function calling

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.5 Embeddings y similitud semántica

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.6 Modelos multimodales (imagen, PDF, audio)

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.7 Rate limits, reintentos y control de costos

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.8 Proyecto del nivel {proyecto}

🛠 Extractor que convierte facturas en PDF a JSON validado.

- [ ] Definir alcance, entradas, salidas y criterio de “terminado”
- [ ] Construir con Claude la versión mínima funcional, entendiendo cada decisión de diseño
- [ ] Escribir README del proyecto: qué hace, cómo se ejecuta, decisiones tomadas
- [ ] Dejar evidencia: capturas, ejemplos de entrada/salida o video corto
- [ ] Commit + tag de versión del nivel (ej. `llm-n2-v1`)
- [ ] Anotar en la sección 8 qué partes del proceso son candidatas a agentizar

> **Resultado y evidencia**
> _Pendiente de documentar._

## 5. Nivel 3 · Avanzado {nivel=3}

⏱ 6–8 semanas · Herramientas: Hugging Face, PEFT, Ollama, vLLM

### 5.1 Arquitectura Transformer: atención, embeddings posicionales

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.2 Tokenización BPE

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.3 Hugging Face Transformers

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.4 Modelos open-weights: Llama, Qwen, Mistral, Gemma

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.5 Fine-tuning eficiente: LoRA y QLoRA

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.6 Cuantización (GGUF, AWQ) e inferencia local

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.7 Servir modelos con Ollama y vLLM

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.8 Proyecto del nivel {proyecto}

🛠 Fine-tuning LoRA de un modelo pequeño para un dominio (ej. contratos inmobiliarios) y comparación vs modelo base.

- [ ] Definir alcance, entradas, salidas y criterio de “terminado”
- [ ] Construir con Claude la versión mínima funcional, entendiendo cada decisión de diseño
- [ ] Escribir README del proyecto: qué hace, cómo se ejecuta, decisiones tomadas
- [ ] Dejar evidencia: capturas, ejemplos de entrada/salida o video corto
- [ ] Commit + tag de versión del nivel (ej. `llm-n3-v1`)
- [ ] Anotar en la sección 8 qué partes del proceso son candidatas a agentizar

> **Resultado y evidencia**
> _Pendiente de documentar._

## 6. Nivel 4 · Experto {nivel=4}

⏱ Continuo · Herramientas: PyTorch, TRL, lm-eval-harness

### 6.1 Entrenar un GPT pequeño desde cero (nanoGPT)

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.2 Alineamiento: RLHF, DPO y variantes

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.3 Evaluaciones propias y benchmarks

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.4 Inferencia a escala: KV cache, batching, speculative decoding

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.5 Seguridad: prompt injection, jailbreaks, fuga de datos

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.6 Interpretabilidad básica

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.7 Optimización costo/latencia y routing entre modelos

- [ ] Estudiar el concepto en la fuente oficial y escribir un resumen propio de 3–5 líneas
- [ ] Construirlo con Claude paso a paso: que escriba el código y explique cada parte; no avanzar hasta poder explicar con tus palabras qué hace
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Documentar aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.8 Proyecto del nivel {proyecto}

🛠 Servicio de inferencia propio con métricas de latencia, costo y calidad, con routing entre modelos.

- [ ] Definir alcance, entradas, salidas y criterio de “terminado”
- [ ] Construir con Claude la versión mínima funcional, entendiendo cada decisión de diseño
- [ ] Escribir README del proyecto: qué hace, cómo se ejecuta, decisiones tomadas
- [ ] Dejar evidencia: capturas, ejemplos de entrada/salida o video corto
- [ ] Commit + tag de versión del nivel (ej. `llm-n4-v1`)
- [ ] Anotar en la sección 8 qué partes del proceso son candidatas a agentizar

> **Resultado y evidencia**
> _Pendiente de documentar._

## 7. Registro de evidencias

Cada tema y proyecto cerrado deja una fila aquí. Es el índice de pruebas del portafolio.

| Fecha | Sección | Qué se hizo | Commit / tag | Enlace |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 8. Lecciones aprendidas para agentizar

Qué partes del proceso fueron repetitivas, cuáles exigieron criterio humano y qué instrucciones necesitaría un agente para hacerlas.

| Sección | Paso repetitivo | Requiere criterio humano | Instrucción clave para el agente |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 9. Bitácora de cambios

| Fecha | Cambio |
|---|---|
| 2026-10-12 | Creación del documento con índice y checklist de los 4 niveles. Pensum v1.1 copiado a docs/ y enlazado. Documentos movidos a resultados/; Nivel 1 rehecho con las etapas de la guía v7; agregado el índice de la guía; índices con casilla de avance por tema; códigos de la guía (F0, E1…) reemplazados por nombres; secciones reordenadas (niveles = 3 a 6); «manual» redefinido como guiado con Claude; carpeta docs/ renombrada a «Documentación para la construcción del proyecto». |
| 2026-10-12 | Los .md pasan a ser la fuente de verdad: se edita el .md y el HTML se regenera con scripts/md_a_html.py. |
| 2026-10-12 | Nueva sección «Análisis de resultados» (al final, sin número, con título destacado): explicación para principiantes y registro de lo que se va logrando. |

## Análisis de resultados {id=analisis}

Esta sección explica, en palabras simples, para qué sirve todo lo que se construye aquí. Está pensada para alguien que empieza en el campo de la inteligencia artificial.

#### El objetivo, en una frase

Aprender a usar un modelo de lenguaje (un LLM, como Claude) desde un programa propio, medir cuánto cuesta y qué tan bien responde, y usar esas mediciones para construir un agente que haga trabajo real por sí solo, con reglas y bajo control.

#### Qué se construye y qué se obtiene

1. **Un chat de consola con memoria** (Parte 1). Es un programa que conversa con Claude desde la terminal y recuerda lo que se habló. Construirlo enseña lo básico: cómo se le habla al modelo, qué es un token, cuánto cuesta cada mensaje y por qué el modelo a veces inventa. **Resultado:** saber conectar cualquier programa a un LLM.
2. **Un laboratorio de parámetros** (Parte 2). Es una pequeña aplicación web para probar el mismo pedido con distintos modelos y ajustes, y medir tiempo, costo y calidad. **Resultado:** decidir con datos, no a ojo, qué modelo y qué configuración usar para cada tarea.
3. **Un agente** (Parte 3). Es un programa en el que el LLM no solo responde: decide pasos, usa herramientas y repite hasta terminar una tarea, con límites de gasto y con aprobación humana cuando hace falta. **Resultado:** automatizar un proceso real de principio a fin.
4. **Un tablero del agente** (Parte 4). Muestra qué tan bien trabaja el agente comparado con hacerlo a mano, y sugiere ajustes. **Resultado:** mejorar el agente con evidencia y saber si vale la pena.

#### Para qué sirve todo esto

- **Para el portafolio:** cada etapa queda como un commit en GitHub, que es la prueba de que se sabe hacer.
- **Para Minus:** es la base para ofrecer a clientes asistentes y agentes que funcionan, cuestan lo que se calculó y se pueden medir. Por ejemplo, un agente que clasifica y responde las solicitudes de posventa de una constructora.
- **Para el criterio propio:** se aprende a detectar cuándo un LLM sirve y cuándo no, cuánto va a costar antes de construir y cómo evitar que invente datos.

#### Lo que vamos logrando

Cada vez que se marca un tema como hecho, aquí se agrega una entrada corta: qué se hizo, en palabras simples, y a qué nos conduce.

#### 2 · Base del proyecto (2026-10-12)

**Qué se hizo:** se escribió el objetivo del proyecto, se creó el repositorio privado en GitHub, se configuró Git y se separó la documentación de los resultados.

**A qué nos conduce:** ya hay un lugar ordenado donde cada avance queda guardado y fechado. Desde ahora, todo lo que se construya deja rastro, y ese rastro es el portafolio.
