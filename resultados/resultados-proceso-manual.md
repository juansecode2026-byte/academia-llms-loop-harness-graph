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

1. **Qué significa «manual» aquí:** el proceso se hace paso a paso con Claude, que escribe el código, lo ejecuta, lo explica y documenta lo que pasa; yo superviso y reviso en este documento. No es programar sin ayuda: es no delegar sin entender, con el aprendizaje escrito para poder revisarlo.
2. Avanzar en orden: no se pasa de nivel sin terminar el proyecto del nivel anterior — el proyecto es la prueba.
3. Cada tema tiene el mismo checklist de 5 pasos y un bloque de **Notas del proceso** que se reemplaza por lo aprendido.
4. Las casillas se guardan en este navegador. Para que el avance quede como prueba en GitHub, al cerrar un tema se marcan sus casillas en el `.md` (`- [x]`), se regenera el HTML y se hace commit.
5. **Todo se sigue aquí, agentes incluidos:** las Partes 3 y 4 (agente, loop, graph, harness y su tablero) son los temas 3.27 a 3.43, con el mismo checklist. El documento [agentizando](resultados-proceso-agentizando.html) queda como un segundo pase opcional, para repetir cada tema con agentes cuando este checklist esté cerrado.
6. **Ejercicio práctico:** el Nivel 1 se construye sobre un caso simulado, un asesor de viajes que atiende por WhatsApp a 10 clientes ficticios. Su explicación y su paso a paso están en [Ejercicio simulado · Chat de consola](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html). Los pasos del ejercicio aparecen como casillas «Ejercicio» dentro de cada tema y se marcan aquí, desde la primera llamada hasta el agente y su tablero.

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

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#f0) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "fase 0: entorno y configuración"`

> **Notas del proceso**
> Punto de control superado (2026-10-12): `import anthropic, dotenv` imprime ok con anthropic 1.13.0 y Python 3.12.10; `.env` existe y Git lo ignora.
> Tropiezos, para no repetirlos: la clave se pegó por error en `.env.example` (la plantilla que sí se sube a Git); se detectó antes de subirla y se restauró la plantilla. El `pip install` falló porque la terminal estaba en la raíz del proyecto y no en `chat-consola`, y porque se escribió «Grpip».
> La clave es exclusiva de este proyecto, creada en la consola de Anthropic con vencimiento.
> Qué hace cada archivo: `requirements.txt` lista las tres bibliotecas; `.env.example` es la plantilla pública sin clave; `.env` guarda la clave y Git lo ignora; `.gitignore` le dice a Git qué no subir; `etapas/` guardará los scripts de las etapas.

### 3.2 Primera llamada a la API {ref=e1:E1}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e1) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 1: primera llamada a la API"`
- [ ] Ejercicio A.2: primera llamada con un mensaje de cliente del caso, sin catálogo, para ver cómo inventa precios ([ver paso A.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> _Versión previa (2026-10-12), hecha con ejemplos sueltos de la guía. Se rehace con el caso del ejercicio._
> Archivo: `chat-consola/etapas/e1_primera_llamada.py`. Se ejecutó 3 veces con `claude-haiku-5-5` y la API real (2026-10-12). Las tres terminaron con `end_turn`.
> Qué hace, línea por línea: `load_dotenv()` carga la clave desde `.env`; `anthropic.Anthropic()` crea el cliente que habla con la API; `client.messages.create(...)` envía el mensaje con tres datos obligatorios (modelo, tope de salida `max_tokens` y la lista de mensajes); luego el script recorre `respuesta.content`, que es una lista de bloques, y une los de tipo `text`.
> Lo observado: la respuesta trae una lista de bloques, no un texto suelto. En estas ejecuciones vino solo el bloque `text`: el modelo decidió no razonar para una pregunta tan simple. Tokens: 34 de entrada y 116, 108 y 113 de salida. Costo de las tres llamadas juntas: unos 0,0002 USD.
> Para pensar, «¿la respuesta es idéntica?»: no. Las tres versiones dicen lo mismo con palabras distintas («patrones estadísticos y semánticos», «patrones, estructuras y relaciones»). El modelo elige cada token con algo de azar; lo controlaremos en la etapa de parámetros.

### 3.3 Ver cómo el modelo predice tokens {ref=e2:E2}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e2) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 2: streaming y razonamiento"`
- [ ] Ejercicio A.3: respuesta por pedazos y razonamiento con ese mismo mensaje ([ver paso A.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> _Versión previa (2026-10-12), hecha con ejemplos sueltos de la guía. Se rehace con el caso del ejercicio._
> Archivo: `chat-consola/etapas/e2_ver_predecir_tokens.py` (2026-10-12, `claude-haiku-5-5`, API real).
> Qué hace: usa `client.messages.stream(...)` en vez de `create`, así los eventos llegan a medida que el modelo los genera. Imprime cada pedazo de texto seguido de `|` para ver dónde corta el servidor, y al final `get_final_message()` entrega el mensaje completo con el conteo de tokens. El parámetro `thinking={"type": "adaptive", "display": "summarized"}` pide un resumen del razonamiento, que por defecto viene oculto.
> Lo observado con la frase del café: 40 pedazos de texto para 172 tokens de salida; los pedazos cortan en medio de palabras («Reconoc|ido m|undialmente»), porque el modelo trabaja con tokens, no con palabras. Razonamiento: 0 tokens, el modelo decidió no pensar en una pregunta tan simple.
> Prueba extra, no guardada como archivo, con el acertijo de las tres cajas con etiquetas equivocadas: sí razonó. 385 tokens de salida, de los cuales 287 fueron de razonamiento (75 %); el texto visible fue de unos 100 tokens. El resumen del razonamiento llegó en inglés aunque la respuesta salió en español.
> Para pensar, «¿por qué el razonamiento cuesta aunque solo veas un resumen?»: porque se cobran los tokens que el modelo genera, no los que se te muestran. El resumen es una versión corta de un razonamiento mucho más largo. «¿Qué pasa con `max_tokens` si razona mucho?»: razonamiento y respuesta salen del mismo tope; si el razonamiento lo consume, la respuesta puede cortarse o no llegar. Por eso los scripts de la guía usan 2048 o más.

### 3.4 Tokens, ventana de contexto y costos {ref=e3:E3}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e3) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 3: tokens y costos"`
- [ ] Ejercicio A.4: contar tokens de mensajes tipo WhatsApp y simular la memoria con una conversación de ejemplo del caso ([ver paso A.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> _Versión previa (2026-10-12), hecha con ejemplos sueltos de la guía. Se rehace con el caso del ejercicio._
> Archivo: `chat-consola/etapas/e3_tokens_costos.py` (2026-10-12, `claude-haiku-5-5`, API real para la parte A; las partes B y C son aritmética).
> Qué hace: la parte A usa `client.messages.count_tokens(...)`, que cuenta tokens sin generar respuesta (no cobra generación), y resta el conteo de un «.» para quitar el formato del mensaje. La parte B simula 20 turnos de un chat con memoria: en cada turno se suma el mensaje del usuario, se reenvía todo el historial y se suma la respuesta. La parte C pasa esos totales a dólares con los precios de cada modelo.
> Parte A, lo observado: español 64 caracteres → 21 tokens; inglés 57 caracteres → 14 tokens; código 32 caracteres → 13; números 29 caracteres → 13; emoji 4 caracteres → 9. El mismo contenido en español ocupa cerca de 1,5 veces más tokens que en inglés, y cuatro emojis ocupan más tokens que una frase corta de código.
> Parte B: sin memoria la entrada total de 20 turnos sería de unos 2.000 tokens; con memoria es 47.600 (casi 24 veces). La entrada de una sola llamada pasa de 100 tokens en el turno 1 a 4.660 en el turno 20.
> Parte C, costo de esa conversación de 20 turnos: Haiku 0,0068 USD, Sonnet 0,1352 USD, Opus 0,2704 USD.
> Experimento sugerido, `TOK_RESPUESTA = 500` (calculado, no es una llamada): entrada acumulada 104.600 tokens; Haiku 0,0155 USD, Sonnet 0,3092 USD, Opus 0,6184 USD. Respuestas 2,5 veces más largas encarecen el chat unas 2,3 veces, porque cada respuesta se vuelve a pagar como entrada en los turnos siguientes.
> Para pensar, «¿qué estrategias hay para recordar sin reenviar todo?»: (1) ventana deslizante, conservar solo los últimos N turnos; con la misma simulación, 10 turnos → 34.400 tokens de entrada y 5 turnos → 18.800, frente a 47.600 sin recorte (es el recorte de la etapa 8); (2) resumir lo viejo en pocas líneas y reenviar solo el resumen; (3) caché de prompts, que abarata la parte repetida del historial; (4) guardar los hechos importantes aparte y buscarlos cuando hagan falta (idea que reaparece en RAG).

### 3.5 Parámetros de generación {ref=e4:E4}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e4) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 4: parámetros de generación"`
- [ ] Ejercicio B.1: probar los parámetros con una pregunta del caso de viajes y confirmar qué se puede variar ([ver paso B.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s7))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.6 Panorama de modelos de Anthropic {ref=e5:E5}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e5) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 5: panorama de modelos"`
- [ ] Ejercicio B.2: comparar Haiku, Sonnet y Opus con una pregunta de un cliente del caso ([ver paso B.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s7))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.7 Primer chat con memoria {ref=e6:E6}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e6) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 6: chat con memoria"`
- [ ] Ejercicio C.1: crear el catálogo ficticio (JSON) ([ver paso C.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [ ] Ejercicio C.2: crear los 10 clientes ficticios y sus guiones tipo WhatsApp ([ver paso C.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [ ] Ejercicio C.3: crear la base SQLite del piloto (clientes, mensajes, ejecuciones); es la base única, el tema 3.16 la amplía ([ver paso C.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [ ] Ejercicio C.4: construir el simulador que entrega los mensajes ([ver paso C.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [ ] Ejercicio C.5: chat con memoria por cliente ([ver paso C.5](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.8 Limitaciones de los LLM {ref=e7:E7}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e7) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 7: pruebas de limitaciones"`
- [ ] Ejercicio D.1: correr las trampas del catálogo y medir si el chat inventa ([ver paso D.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.9 Ensamblar el chat final {ref=e8:E8}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e8) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 8: chat final ensamblado"`
- [ ] Ejercicio D.2: atender a los 10 clientes con recorte de memoria y guardar cada llamada ([ver paso D.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.10 Pruebas automáticas sin gastar tokens {ref=e9:E9}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e9) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "etapa 9: pruebas automáticas"`
- [ ] Ejercicio D.3: pruebas sin gastar tokens del simulador y de la memoria por cliente ([ver paso D.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.11 Cierre del nivel {ref=e10:E10}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e10) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio D.4: informe del piloto: tokens, costo y alucinaciones por cliente ([ver paso D.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> _Pendiente de documentar._

<!-- parte: 2 | Parte 2 · Laboratorio de parámetros | 15 apartados | p2 -->

### 3.12 Qué vas a construir (laboratorio) {ref=d0:D0}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d0) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.1: definir qué se va a medir del asesor de viajes y con qué objetivo ([ver paso E.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.13 Qué controlamos y qué medimos {ref=d1:D1}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d1) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.2: fijar los controles (modelo, effort, ventana, mensaje de sistema) y las mediciones sobre el caso ([ver paso E.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.14 Preparación del laboratorio {ref=d2:D2}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d2) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D2: preparación del laboratorio"`
- [ ] Ejercicio E.3: preparar la estructura del laboratorio (carpetas y dependencias, incluido Streamlit) ([ver paso E.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.15 Motor de medición {ref=d3:D3}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d3) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D3: motor de medición"`
- [ ] Ejercicio E.4: construir el motor de medición con la configuración del caso ([ver paso E.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.16 Registro de experimentos (SQLite) {ref=d4:D4}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d4) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D4: registro en SQLite"`
- [ ] Ejercicio E.5: ampliar la base del piloto, creada en el tema 3.7, con el registro de experimentos, sin crear otra base ([ver paso E.5](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.17 Batería de preguntas y modelo juez {ref=d5:D5}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d5) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D5: batería y juez"`
- [ ] Ejercicio E.6: armar la batería y el modelo juez desde el caso de viajes ([ver paso E.6](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.18 Estructura de la app {ref=d6:D6}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d6) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D6: estructura de la app"`
- [ ] Ejercicio E.7: construir la estructura del dashboard del laboratorio ([ver paso E.7](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.19 Controles {ref=d7:D7}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d7) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.8: los controles del laboratorio: modelo, effort, memoria y mensaje de sistema del caso ([ver paso E.8](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.20 Vista Playground {ref=d8:D8}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d8) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.9: vista Playground: probar una conversación del caso con cualquier configuración ([ver paso E.9](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.21 Vista Comparador {ref=d9:D9}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d9) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.10: vista Comparador: la misma pregunta de un cliente con varias configuraciones lado a lado ([ver paso E.10](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.22 Vista Batería de alucinaciones {ref=d10:D10}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d10) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.11: vista Batería: correr las trampas del catálogo y calificar si inventó ([ver paso E.11](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.23 Vista Métricas {ref=d11:D11}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d11) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.12: vista Métricas: tokens, costo y alucinaciones por configuración ([ver paso E.12](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.24 Pruebas del laboratorio {ref=d12:D12}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d12) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D12: pruebas del laboratorio"`
- [ ] Ejercicio E.13: pruebas sin gastar tokens del motor, el registro y la batería ([ver paso E.13](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.25 Experimentos y cierre {ref=d13:D13}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d13) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio E.14: correr la grilla del piloto: 10 clientes × 12 configuraciones ([ver paso E.14](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.26 Tablero de decisiones {ref=d14:D14 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#d14) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit: `git commit -m "D14: tablero de decisiones"`
- [ ] Ejercicio E.15: decidir modelo, effort y ventana con los datos del piloto, en un informe ([ver paso E.15](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s10))

> **Notas del proceso**
> _Pendiente de documentar._

<!-- parte: 3 | Parte 3 · Ingeniería agéntica | 10 apartados | p3 -->

### 3.27 Qué vas a construir (agente) {ref=ag0:AG0 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag0) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.1: definir qué hará el agente asesor y qué queda siempre en manos de un humano ([ver paso F.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.28 Conceptos: harness, loop y graph {ref=ag1:AG1 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag1) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.2: aplicar al caso los conceptos de harness, loop y graph ([ver paso F.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.29 Proceso, línea base y casos de prueba {ref=ag2:AG2 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag2) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.3: medir la línea base y fijar los casos de prueba con los 10 clientes ([ver paso F.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.30 Herramientas {ref=ag3:AG3 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag3) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.4: herramientas: buscar en el catálogo, estimar un precio, escalar a un humano ([ver paso F.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.31 Loop {ref=ag4:AG4 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag4) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.5: loop que consulta el catálogo con límite de vueltas ([ver paso F.5](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.32 Graph {ref=ag5:AG5 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag5) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.6: graph que clasifica, consulta, responde y verifica, enrutando por modelo según el costo ([ver paso F.6](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.33 Harness {ref=ag6:AG6 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag6) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.7: harness con tope de gasto por conversación y aprobación humana antes del precio final ([ver paso F.7](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.34 Trazas (agentes.db) {ref=ag7:AG7 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag7) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.8: trazas de cada paso del agente en la base única ([ver paso F.8](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.35 Evaluación y optimización {ref=ag8:AG8 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag8) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.9: evaluar las variantes (sin loop, con loop, con graph, con harness) y compararlas ([ver paso F.9](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.36 Pruebas y cierre {ref=ag9:AG9 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#ag9) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.10: pruebas sin gastar tokens y cierre ([ver paso F.10](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

<!-- parte: 4 | Parte 4 · Tablero de operación agéntica | 7 apartados | p4 -->

### 3.37 Qué vas a construir (tablero agéntico) {ref=da0:DA0 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da0) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.11: definir qué indicadores del agente se ven y qué decisión habilita cada uno ([ver paso F.11](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.38 Encabezado {ref=da1:DA1 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da1) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.12: encabezado del tablero: qué agente, qué variante y qué periodo se mira ([ver paso F.12](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.39 Indicadores {ref=da2:DA2 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da2) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.13: calcular los indicadores del agente asesor de viajes: éxito, costo por tarea, inventó, escalado ([ver paso F.13](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.40 Vistas {ref=da3:DA3 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da3) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.14: vistas del tablero: resumen, variantes, grafo, ejecuciones y decisiones ([ver paso F.14](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.41 Reglas de decisión · ciclo de mejora {ref=da4:DA4 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da4) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.15: reglas «si… entonces…» para ajustar el agente y volver a evaluarlo ([ver paso F.15](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.42 Bibliotecas y construcción {ref=da5:DA5 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da5) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.16: construir el tablero con las bibliotecas de la guía ([ver paso F.16](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.43 Pruebas y cierre {ref=da6:DA6 etiqueta="En plan en la guía"}

- [ ] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#da6) y explica qué se va a hacer y por qué
- [ ] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [ ] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [ ] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [ ] Commit con mensaje descriptivo y registrar el hash en la sección 7
- [ ] Ejercicio F.17: pruebas sin gastar tokens del tablero y cierre ([ver paso F.17](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s11))

> **Notas del proceso**
> _Pendiente de documentar._

### 3.44 Proyecto del nivel {proyecto}

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

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.2 Streaming de respuestas

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.3 Salidas estructuradas (JSON / esquemas)

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.4 Tool use / function calling

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.5 Embeddings y similitud semántica

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.6 Modelos multimodales (imagen, PDF, audio)

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 4.7 Rate limits, reintentos y control de costos

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
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

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.2 Tokenización BPE

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.3 Hugging Face Transformers

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.4 Modelos open-weights: Llama, Qwen, Mistral, Gemma

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.5 Fine-tuning eficiente: LoRA y QLoRA

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.6 Cuantización (GGUF, AWQ) e inferencia local

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 5.7 Servir modelos con Ollama y vLLM

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
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

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.2 Alineamiento: RLHF, DPO y variantes

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.3 Evaluaciones propias y benchmarks

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.4 Inferencia a escala: KV cache, batching, speculative decoding

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.5 Seguridad: prompt injection, jailbreaks, fuga de datos

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.6 Interpretabilidad básica

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
- [ ] Commit en GitHub con mensaje convencional y registrar el hash en la sección 7

> **Notas del proceso**
> _Pendiente de documentar._

### 6.7 Optimización costo/latencia y routing entre modelos

- [ ] Claude estudia el concepto en la fuente oficial y escribe un resumen de 3–5 líneas
- [ ] Claude lo construye paso a paso: escribe el código y explica cada parte
- [ ] Ubicar el código según el CLAUDE.md del laboratorio: `scripts/` si no llama a un LLM, `agentes-sdk/` si sí
- [ ] Claude documenta aquí: pasos seguidos, comandos, errores encontrados y cómo se resolvieron
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

Cada vez que se marca un tema como hecho, aquí se agrega una entrada corta: qué se hizo, en palabras simples, a qué nos conduce y un ejemplo concreto. El número y el título de cada tema, más arriba, llevan directo a su entrada.

#### 2 · Base del proyecto (2026-10-12)

**Qué se hizo:** se escribió el objetivo del proyecto, se creó el repositorio privado en GitHub, se configuró Git y se separó la documentación de los resultados.

**A qué nos conduce:** ya hay un lugar ordenado donde cada avance queda guardado y fechado. Desde ahora, todo lo que se construya deja rastro, y ese rastro es el portafolio.

> **Ejemplo**
> Funciona como la historia clínica de un paciente. Si dentro de seis meses alguien de un cliente de Minus pregunta «¿desde cuándo saben conectar sistemas a Claude?», no hace falta decir «hace un tiempo»: se abre GitHub y se ve el commit «etapa 1: primera llamada a la API», con fecha, código y resultado.

#### 3.1 · Preparación (2026-10-12)

**Qué se hizo:** se creó un entorno de Python aislado para el proyecto (así sus bibliotecas no se mezclan con las de otros), se instaló el SDK de Anthropic, que es el programa que permite hablar con Claude desde código, y se guardó la clave de acceso en un archivo `.env` que Git no sube. La clave es exclusiva de este proyecto y vence sola.

**A qué nos conduce:** es el piso sobre el que se apoya todo lo demás. Sin entorno aislado, los proyectos se estorban entre sí; sin la clave protegida, un descuido la publicaría y alguien podría gastar tu dinero. Con esto listo, el siguiente paso es el primero emocionante: hacer que un programa nuestro le haga una pregunta a Claude y reciba la respuesta.

> **Ejemplo**
> El entorno virtual es como tener una caja de herramientas aparte para cada obra. Si el CRM necesita una versión de la biblioteca `anthropic` y esta Academia otra, cada uno usa la suya y ninguno rompe al otro.
> La clave en `.env` es como la llave de la casa guardada en un cajón, no pegada en la puerta: el programa la usa, pero no queda a la vista. Cuando hoy la clave quedó escrita en `.env.example` (la plantilla que sí se sube a GitHub), fue como dejarla pegada en la puerta; por eso se cambió la cerradura: se revocó y se creó otra.

#### 3.2 · Primera llamada a la API (2026-10-12)

**Versión previa:** hecha con ejemplos sueltos de la guía; se actualizará al rehacerlo con el caso del ejercicio.

**Qué se hizo:** se escribió un programa de 25 líneas que le hace una pregunta a Claude y muestra todo lo que devuelve: la respuesta, por qué terminó y cuántos tokens usó. Se ejecutó tres veces con la API real.

**A qué nos conduce:** es la prueba de que la conexión funciona y de que ya podemos usar un modelo de lenguaje desde nuestro propio código. Dos cosas que se aprenden de verlo en vivo: la respuesta cambia un poco cada vez, así que un LLM no es una base de datos con respuestas fijas; y cada respuesta tiene un costo medible en tokens, que aquí fue de centésimas de centavo. Esas dos ideas, variación y costo, son las que más adelante se miden en el laboratorio y deciden si un agente es viable.

> **Ejemplo**
> La pregunta «¿Qué es un modelo de lenguaje?» usó 34 tokens de entrada y unos 112 de salida. Con los precios de Haiku 5.5 (0,10 USD por millón de tokens de entrada y 0,50 por millón de salida), cada respuesta cuesta unos 0,00006 USD. Un asistente que contestara 10.000 preguntas parecidas al mes gastaría unos 0,60 USD.
> Y la variación: es como preguntarle lo mismo a una persona tres veces. Las tres respuestas dicen que un modelo de lenguaje «predice y genera palabras de forma coherente», pero cambian el final: «responder preguntas, traducir, resumir» en una, «redactar textos» en otra.

#### 3.3 · Ver cómo el modelo predice tokens (2026-10-12)

**Versión previa:** hecha con ejemplos sueltos de la guía; se actualizará al rehacerlo con el caso del ejercicio.

**Qué se hizo:** se recibió la respuesta de Claude «en vivo», pedazo por pedazo, como cuando ChatGPT va escribiendo en pantalla. Cada pedazo se separó con una barra para ver cómo llegan. También se pidió ver el razonamiento resumido del modelo.

**A qué nos conduce:** se ve con los ojos lo que significa que un modelo «predice el siguiente token»: va armando el texto por trozos pequeños, sin saber de antemano cómo terminará, y los trozos cortan en mitad de palabras. Esto sirve para dos decisiones prácticas: el streaming permite que un chat se sienta rápido (el usuario lee mientras se genera), y el razonamiento es una parte invisible del costo: en la prueba del acertijo, tres de cada cuatro tokens de salida se fueron en pensar. Esa cuenta decide cuándo conviene activar el razonamiento y cuándo apagarlo para ahorrar.

> **Ejemplo**
> Recibir la respuesta en streaming es como ver a alguien escribir en un tablero en vez de esperar a que te entregue la hoja terminada: la frase del café llegó en 40 pedazos y se podía leer desde el primero.
> El costo del razonamiento, con números de hoy: el acertijo de las cajas gastó 385 tokens de salida, 287 de ellos pensando. Si un bot de posventa respondiera 1.000 preguntas así, pagaría unos 0,19 USD; sin razonar (unos 100 tokens por respuesta) serían unos 0,05 USD. Casi cuatro veces menos, a cambio de respuestas que pueden equivocarse más en preguntas difíciles.

#### 3.4 · Tokens, ventana de contexto y costos (2026-10-12)

**Versión previa:** hecha con ejemplos sueltos de la guía; se actualizará al rehacerlo con el caso del ejercicio.

**Qué se hizo:** se contaron los tokens de distintos tipos de texto y se simuló una conversación de 20 turnos para ver cuánto crece lo que se envía en cada mensaje, y cuánto costaría esa conversación con cada modelo.

**A qué nos conduce:** a entender de dónde sale la factura. Un modelo no recuerda nada entre llamadas: para que «recuerde», hay que reenviarle toda la conversación cada vez, y todo lo que se reenvía se cobra de nuevo. Por eso una conversación de 20 turnos cuesta casi 24 veces más que 20 mensajes sueltos. También se ve que el idioma importa (el español usa más tokens que el inglés) y que la elección del modelo mueve el costo muchísimo: el mismo chat cuesta 0,0068 USD con Haiku y 0,2704 USD con Opus. Esas cuentas son las que permiten cotizar un proyecto antes de construirlo.

> **Ejemplo**
> Un asistente de ventas atiende 1.000 conversaciones al mes, de 20 turnos cada una. Con Haiku cuesta unos 6,8 USD al mes; con Sonnet, unos 135; con Opus, unos 270. Es el mismo servicio: cambiar de modelo lo multiplica por 40.
> Y cuánto pesa la memoria: si el asistente solo recordara los últimos 5 turnos en vez de los 20, la entrada baja de 47.600 a 18.800 tokens por conversación (un 60 % menos) y las conversaciones largas dejan de encarecerse sin freno. Es como un vendedor que, antes de cada respuesta, no relee la libreta completa del cliente sino solo las últimas cinco notas.
| 2026-10-12 | Los títulos de los temas enlazan a su entrada del análisis de resultados; cada entrada lleva un ejemplo. |
| 2026-10-12 | Se vincula el ejercicio simulado (asesor de viajes, piloto de 10 clientes): enlace en la sección 1 y casillas «Ejercicio» en los temas 3.5–3.11, 3.17, 3.25 y 3.26. |
| 2026-10-13 | Decisión del ejercicio: la base SQLite nace en 3.7 y el 3.16 la amplía; nueva casilla «Ejercicio E.0» en 3.16. |
| 2026-10-13 | Se reinicia el checklist sobre el ejercicio: 3.2 a 3.4 se rehacen con el caso (casillas desmarcadas, notas previas conservadas); nuevas casillas «Ejercicio» en 3.12 a 3.15 y 3.24; renumerados los pasos E.5, E.6, E.8 y E.9; temas 3.18 a 3.23 (dashboard) aplazados. |
| 2026-10-13 | Se revierte el aplazamiento: los temas 3.18 a 3.23 (dashboard) vuelven al checklist, con sus casillas «Ejercicio E.7 a E.12»; las pruebas, los experimentos y las decisiones pasan a E.13, E.14 y E.15. |
| 2026-10-13 | Las Partes 3 y 4 (agente y tablero) pasan a este documento como los temas 3.27 a 3.43, con las casillas «Ejercicio F.1 a F.17»; el proyecto del nivel pasa a ser el 3.44. El agentizando queda como segundo pase opcional. |
