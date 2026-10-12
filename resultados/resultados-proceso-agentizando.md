<!-- Fuente de verdad. Editar este .md y correr: python scripts/md_a_html.py (regenera el HTML). -->
---
doc: agentizando
titulo: Resultados · Proceso agentizando
fecha: 2026-10-12
gemelo: resultados-proceso-manual.html | ← Ir al documento manual
lead: Academia LLMs — módulo LLMs del Pensum AI Engineer. Aquí se repite cada tema **con apoyo de agentes**, partiendo del proceso manual ya entendido, y se mide qué cambia en tiempo, costo y calidad.
---

# Resultados del proceso <em>agentizando</em>

## 1. Cómo usar este documento

1. **Diferencia con el manual:** en el manual Claude me acompaña paso a paso y yo valido cada decisión; aquí el proceso se delega a agentes (loops, scripts con el SDK) que ejecutan con autonomía, y yo defino el objetivo, pongo los límites y reviso el resultado.
2. Un tema solo se agentiza cuando su versión manual está cerrada en el [documento manual](resultados-proceso-manual.html) (misma numeración).
3. Cada tema enlaza a su sección manual, tiene un checklist de 6 pasos y un bloque para guardar el **brief usado y el resultado**.
4. Las casillas se guardan en este navegador; para dejarlas como prueba en GitHub se marcan en el `.md` (`- [x]`), se regenera el HTML y se hace commit.
5. Regla del laboratorio: si algo se repite, no se convierte en agente sobre la marcha — se anota como candidato en `DECISIONES.md` (sección 8).

## 2. Prerrequisitos y herramientas

#### Prerrequisito: proceso manual entendido

- [ ] El tema equivalente está cerrado en el documento manual
- [ ] Sus notas del proceso y su commit están registrados
- [ ] Se identificó en la sección 8 del manual qué parte se va a agentizar

#### Herramientas de agentización

- [ ] Claude Code instalado y funcionando dentro de este proyecto
- [ ] `CLAUDE.md` del proyecto con objetivo, alcance y convenciones
- [ ] Permisos revisados en `.claude/settings.json`
- [ ] Claude Agent SDK (Python) instalado para los scripts de `agentes-sdk/`
- [ ] Forma de medir costo: registrar tokens de entrada/salida por ejecución

> **Notas del proceso**
> _Pendiente de documentar._

## 3. Nivel 1 · Fundamentos {nivel=1}

⏱ 2–3 semanas · Herramientas: Anthropic API, OpenAI API, Gemini API

<!-- parte: 3 | Parte 3 · Ingeniería agéntica | 10 apartados | p3 -->

### 3.1 Qué vas a construir (agente) {ref=ag0:AG0 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag0) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.2 Conceptos: harness, loop y graph {ref=ag1:AG1 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag1) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.3 Proceso, línea base y casos de prueba {ref=ag2:AG2 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag2) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.4 Herramientas {ref=ag3:AG3 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag3) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.5 Loop {ref=ag4:AG4 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag4) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.6 Graph {ref=ag5:AG5 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag5) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.7 Harness {ref=ag6:AG6 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag6) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.8 Trazas (agentes.db) {ref=ag7:AG7 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag7) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.9 Evaluación y optimización {ref=ag8:AG8 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag8) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.10 Pruebas y cierre {ref=ag9:AG9 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag9) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

<!-- parte: 4 | Parte 4 · Tablero de operación agéntica | 7 apartados | p4 -->

### 3.11 Qué vas a construir (tablero agéntico) {ref=da0:DA0 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da0) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.12 Encabezado {ref=da1:DA1 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da1) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.13 Indicadores {ref=da2:DA2 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da2) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.14 Vistas {ref=da3:DA3 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da3) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.15 Reglas de decisión · ciclo de mejora {ref=da4:DA4 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da4) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.16 Bibliotecas y construcción {ref=da5:DA5 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da5) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.17 Pruebas y cierre {ref=da6:DA6 etiqueta="En plan en la guía"}

- [ ] Releer el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da6) y confirmar que el Nivel 1 manual está cerrado ([ver manual](resultados-proceso-manual.html#s3))
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir; nunca aceptar sin leer
- [ ] Medir contra la línea base: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado)

> **Brief usado y resultado**
> _Pendiente de documentar._

### 3.18 Proyecto del nivel {proyecto}

🛠 Chatbot de consola con memoria de conversación usando un SDK oficial.

- [ ] Partir del README y alcance del proyecto manual del nivel
- [ ] Diseñar el flujo agentizado: qué hace el agente, qué revisa el humano
- [ ] Construir el proyecto apoyado en el agente y registrar cada intervención humana
- [ ] Comparar resultado agentizado vs manual (sección 7)
- [ ] Commit + tag (ej. `llm-n1-agente-v1`)
- [ ] Si el proceso se repite, anotarlo como candidato en `DECISIONES.md` (sección 8) — no construirlo sobre la marcha

> **Resultado y evidencia**
> _Pendiente de documentar._

## 4. Nivel 2 · Intermedio {nivel=2}

⏱ 4–6 semanas · Herramientas: SDK Python, Pydantic, tiktoken

### 4.1 SDKs a fondo: mensajes, roles, system prompt

- [ ] Releer el proceso manual de este tema ([manual 4.1](resultados-proceso-manual.html#s4-1)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.2 Streaming de respuestas

- [ ] Releer el proceso manual de este tema ([manual 4.2](resultados-proceso-manual.html#s4-2)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.3 Salidas estructuradas (JSON / esquemas)

- [ ] Releer el proceso manual de este tema ([manual 4.3](resultados-proceso-manual.html#s4-3)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.4 Tool use / function calling

- [ ] Releer el proceso manual de este tema ([manual 4.4](resultados-proceso-manual.html#s4-4)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.5 Embeddings y similitud semántica

- [ ] Releer el proceso manual de este tema ([manual 4.5](resultados-proceso-manual.html#s4-5)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.6 Modelos multimodales (imagen, PDF, audio)

- [ ] Releer el proceso manual de este tema ([manual 4.6](resultados-proceso-manual.html#s4-6)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.7 Rate limits, reintentos y control de costos

- [ ] Releer el proceso manual de este tema ([manual 4.7](resultados-proceso-manual.html#s4-7)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 4.8 Proyecto del nivel {proyecto}

🛠 Extractor que convierte facturas en PDF a JSON validado.

- [ ] Partir del README y alcance del proyecto manual del nivel
- [ ] Diseñar el flujo agentizado: qué hace el agente, qué revisa el humano
- [ ] Construir el proyecto apoyado en el agente y registrar cada intervención humana
- [ ] Comparar resultado agentizado vs manual (sección 7)
- [ ] Commit + tag (ej. `llm-n2-agente-v1`)
- [ ] Si el proceso se repite, anotarlo como candidato en `DECISIONES.md` (sección 8) — no construirlo sobre la marcha

> **Resultado y evidencia**
> _Pendiente de documentar._

## 5. Nivel 3 · Avanzado {nivel=3}

⏱ 6–8 semanas · Herramientas: Hugging Face, PEFT, Ollama, vLLM

### 5.1 Arquitectura Transformer: atención, embeddings posicionales

- [ ] Releer el proceso manual de este tema ([manual 5.1](resultados-proceso-manual.html#s5-1)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.2 Tokenización BPE

- [ ] Releer el proceso manual de este tema ([manual 5.2](resultados-proceso-manual.html#s5-2)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.3 Hugging Face Transformers

- [ ] Releer el proceso manual de este tema ([manual 5.3](resultados-proceso-manual.html#s5-3)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.4 Modelos open-weights: Llama, Qwen, Mistral, Gemma

- [ ] Releer el proceso manual de este tema ([manual 5.4](resultados-proceso-manual.html#s5-4)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.5 Fine-tuning eficiente: LoRA y QLoRA

- [ ] Releer el proceso manual de este tema ([manual 5.5](resultados-proceso-manual.html#s5-5)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.6 Cuantización (GGUF, AWQ) e inferencia local

- [ ] Releer el proceso manual de este tema ([manual 5.6](resultados-proceso-manual.html#s5-6)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.7 Servir modelos con Ollama y vLLM

- [ ] Releer el proceso manual de este tema ([manual 5.7](resultados-proceso-manual.html#s5-7)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 5.8 Proyecto del nivel {proyecto}

🛠 Fine-tuning LoRA de un modelo pequeño para un dominio (ej. contratos inmobiliarios) y comparación vs modelo base.

- [ ] Partir del README y alcance del proyecto manual del nivel
- [ ] Diseñar el flujo agentizado: qué hace el agente, qué revisa el humano
- [ ] Construir el proyecto apoyado en el agente y registrar cada intervención humana
- [ ] Comparar resultado agentizado vs manual (sección 7)
- [ ] Commit + tag (ej. `llm-n3-agente-v1`)
- [ ] Si el proceso se repite, anotarlo como candidato en `DECISIONES.md` (sección 8) — no construirlo sobre la marcha

> **Resultado y evidencia**
> _Pendiente de documentar._

## 6. Nivel 4 · Experto {nivel=4}

⏱ Continuo · Herramientas: PyTorch, TRL, lm-eval-harness

### 6.1 Entrenar un GPT pequeño desde cero (nanoGPT)

- [ ] Releer el proceso manual de este tema ([manual 6.1](resultados-proceso-manual.html#s6-1)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.2 Alineamiento: RLHF, DPO y variantes

- [ ] Releer el proceso manual de este tema ([manual 6.2](resultados-proceso-manual.html#s6-2)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.3 Evaluaciones propias y benchmarks

- [ ] Releer el proceso manual de este tema ([manual 6.3](resultados-proceso-manual.html#s6-3)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.4 Inferencia a escala: KV cache, batching, speculative decoding

- [ ] Releer el proceso manual de este tema ([manual 6.4](resultados-proceso-manual.html#s6-4)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.5 Seguridad: prompt injection, jailbreaks, fuga de datos

- [ ] Releer el proceso manual de este tema ([manual 6.5](resultados-proceso-manual.html#s6-5)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.6 Interpretabilidad básica

- [ ] Releer el proceso manual de este tema ([manual 6.6](resultados-proceso-manual.html#s6-6)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.7 Optimización costo/latencia y routing entre modelos

- [ ] Releer el proceso manual de este tema ([manual 6.7](resultados-proceso-manual.html#s6-7)) y confirmar que se entendió
- [ ] Redactar el brief para el agente: objetivo, contexto, restricciones y formato de salida
- [ ] Elegir la forma: Claude Code interactivo, subagente, skill o script con Agent SDK
- [ ] Ejecutar, revisar la salida y corregir — nunca aceptar sin leer
- [ ] Medir contra el manual: tiempo, costo en tokens y calidad (sección 7)
- [ ] Commit con la evidencia (prompt usado + resultado) en GitHub

> **Brief usado y resultado**
> _Pendiente de documentar._

### 6.8 Proyecto del nivel {proyecto}

🛠 Servicio de inferencia propio con métricas de latencia, costo y calidad, con routing entre modelos.

- [ ] Partir del README y alcance del proyecto manual del nivel
- [ ] Diseñar el flujo agentizado: qué hace el agente, qué revisa el humano
- [ ] Construir el proyecto apoyado en el agente y registrar cada intervención humana
- [ ] Comparar resultado agentizado vs manual (sección 7)
- [ ] Commit + tag (ej. `llm-n4-agente-v1`)
- [ ] Si el proceso se repite, anotarlo como candidato en `DECISIONES.md` (sección 8) — no construirlo sobre la marcha

> **Resultado y evidencia**
> _Pendiente de documentar._

## 7. Comparativa manual vs agentizado

Una fila por tema o proyecto agentizado.

| Sección | Tiempo manual | Tiempo agentizado | Costo (tokens / USD) | Calidad y observaciones |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 8. Candidatos a automatizar

Procesos que se repitieron. Se trasladan a `DECISIONES.md` como candidatos aplazados, con su condición de activación; el agente `seleccionar-forma` los evalúa y la decisión final es del usuario.

| Proceso | De dónde salió | Condición de activación | Estado en DECISIONES.md |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 9. Bitácora de cambios

| Fecha | Cambio |
|---|---|
| 2026-10-12 | Creación del documento con índice y checklist de los 4 niveles. Pensum v1.1 copiado a docs/ y enlazado. Documentos movidos a resultados/; Nivel 1 rehecho con las etapas de la guía v7; agregado el índice de la guía; índices con casilla de avance por tema; códigos de la guía (F0, E1…) reemplazados por nombres; secciones reordenadas (niveles = 3 a 6); «manual» redefinido como guiado con Claude; carpeta docs/ renombrada a «Documentación para la construcción del proyecto». |
| 2026-10-12 | Los .md pasan a ser la fuente de verdad: se edita el .md y el HTML se regenera con scripts/md_a_html.py. |
