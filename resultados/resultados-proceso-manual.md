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

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e1) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 1: primera llamada a la API"`
- [x] Ejercicio A.2: primera llamada con la conversación de un cliente del caso, con el catálogo cargado ([ver paso A.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> Archivos: `chat-consola/etapas/e1_primera_llamada.py` y el módulo `chat-consola/etapas/caso_simulado.py` (2026-10-13, `claude-haiku-5-5`, API real).
> Qué hace, línea por línea: `load_dotenv()` carga la clave desde `.env`; `anthropic.Anthropic()` crea el cliente; `construir_system()` arma el mensaje de sistema: el papel de asesor de «Turismo Colombia (simulada)» más el catálogo en formato compacto. Luego el script corre una conversación de dos mensajes del cliente («hola buenas, cuanto vale ir a cartagena 4 noches?» y después «somos 2, del 10 al 14 de diciembre. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro»), reenviando como memoria la respuesta real del asesor, y en cada turno muestra los bloques de la respuesta (`thinking` y `text`), el texto y los tokens.
> Lo observado en 3 ejecuciones: **el asesor usó siempre los precios del catálogo**. Respondió que Casa Naranja del Centro cuesta $480.000 por noche y $1.920.000 por las 4 noches, y en las tres ocasiones aclaró que ese es el precio base de temporada baja, que la tarifa de diciembre puede ser más alta y que la disponibilidad la confirma un asesor humano. Tokens: turno 1 con 6.578 de entrada y 612, 647 y 599 de salida; turno 2 con 7.002, 6.984 y 7.020 de entrada y 340, 526 y 447 de salida. Todas las respuestas incluyeron un bloque `thinking` (razonamiento).
> Costo de una conversación de dos mensajes: unos 0,0019 USD (en promedio, 13.580 tokens de entrada y 1.057 de salida), y casi todo es el catálogo reenviado en cada mensaje.
> Para pensar, «¿la respuesta es idéntica?»: no. La redacción cambia entre ejecuciones, pero las cifras no: las tres veces el total fue $1.920.000, tomado del registro `casa-naranja-del-centro` del catálogo.
> Conclusión del tema: con el catálogo en el contexto, el asesor responde con datos verificables, y lo que el catálogo no tiene (tarifa de temporada alta, cupos, vuelos) lo dice en vez de inventarlo.

### 3.3 Ver cómo el modelo predice tokens {ref=e2:E2}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e2) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 2: streaming y razonamiento"`
- [x] Ejercicio A.3: respuesta por pedazos y razonamiento con el primer mensaje del cliente, con el catálogo cargado ([ver paso A.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> Archivos: `chat-consola/etapas/e2_ver_predecir_tokens.py` y el módulo compartido `chat-consola/etapas/caso_simulado.py` (2026-10-13, `claude-haiku-5-5`, API real).
> Qué hace: usa `client.messages.stream(...)` en vez de `create`, así los eventos llegan a medida que el modelo los genera. Imprime cada pedazo de texto seguido de `|` y, antes, el razonamiento resumido (`thinking={"type": "adaptive", "display": "summarized"}`). Al final `get_final_message()` entrega los tokens.
> Lo observado en la primera ejecución: la respuesta llegó en 67 pedazos y varios cortan palabras («Con| g|usto», «dent|ro», «cu|entas»), porque el modelo trabaja con tokens, no con palabras. El resumen del razonamiento llegó en inglés aunque la respuesta salió en español: «I should present the three accommodation options with their per-night rates, noting these are base low-season prices without flights…».

**Resultado de las 3 ejecuciones con catálogo:**

| | Ejecución 1 | Ejecución 2 | Ejecución 3 | Promedio |
|---|---|---|---|---|
| Tokens de entrada | 6.578 | 6.578 | 6.578 | 6.578 |
| Pedazos de texto | 67 | 92 | 76 | 78 |
| Tokens de salida | 613 | 679 | 567 | 620 |
| de razonamiento | 268 | 266 | 184 | 239 |
| de respuesta | 345 | 413 | 383 | 380 |
| Costo de la respuesta (Haiku) | 0,00096 USD | 0,00100 USD | 0,00094 USD | 0,00097 USD |

> **Qué dice la tabla**
> La entrada es idéntica en las tres ejecuciones porque es el mismo mensaje de sistema con el catálogo: 6.578 tokens, el 68 % del costo de cada respuesta. La salida varía de una a otra (de 567 a 679 tokens), y el razonamiento fue el 39 % de la salida en promedio. Todo el tema costó unos 0,003 USD.
> Para pensar, «¿por qué el razonamiento cuesta aunque solo veas un resumen?»: porque se cobran los tokens que el modelo genera, no los que se te muestran; aquí fueron 239 de 620 tokens de salida. «¿Qué pasa con `max_tokens` si razona mucho?»: razonamiento y respuesta salen del mismo tope; si el razonamiento lo consume, la respuesta se corta. Aquí 2048 sobraron.

### 3.4 Tokens, ventana de contexto y costos {ref=e3:E3}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e3) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 3: tokens y costos"`
- [x] Ejercicio A.4: radiografía del contexto sobre las conversaciones de los 10 clientes: de qué está hecha cada llamada, cuánto es redundante, cuánto catálogo sobra y cuánto bajaría el costo con cada palanca ([ver paso A.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s6))

> **Notas del proceso**
> Archivos (2026-10-13, `claude-haiku-5-5`, API real): `chat-consola/etapas/e3_tokens_costos.py` (la radiografía), `simulador_clientes.py` (entrega los mensajes de los 10 clientes al asesor), `base_piloto.py` (la base SQLite del piloto, `datos-simulados/piloto-simulado.db`, ignorada por git), `caso_simulado.py` y `datos-simulados/clientes-simulados.json` (los 10 clientes con sus guiones). El informe completo queda en `chat-consola/informes/radiografia-contexto.md`.
> Qué hace: el simulador corre las 10 conversaciones (184 mensajes, de 10 a 28 por cliente) contra el asesor, con el catálogo completo y todo el historial, y guarda cada llamada en la tabla `ejecuciones` (tokens de entrada, salida y razonamiento, costo, tiempo y motivo de parada). Después `e3_tokens_costos.py` cuenta con la API (`count_tokens`, que no genera respuesta ni cobra generación) los tokens de cada mensaje y reparte cada llamada en instrucciones, catálogo, historial y mensaje nuevo. La entrada de cualquier llamada se reconstruye exactamente sumando los tokens de cada mensaje más 2 de formato por mensaje: error de 0,00 % en las 184 llamadas. Eso permite calcular con precisión qué pasaría con otra configuración, sin volver a llamar al modelo.
> Tropiezo: con 5 clientes en paralelo el simulador chocó con el límite de la cuenta (500.000 tokens de entrada por minuto) y se detuvo con 159 de 184 llamadas guardadas. Se le agregó una espera con reintento y se retomó con 3 en paralelo; el script continúa donde quedó, así que no se repitió ninguna llamada.
> Costo del tema: 0,213 USD por las 184 llamadas reales. Los conteos de tokens no cobran.
> Memoria con el historial completo (revisado a mano en 14 preguntas de «¿qué te dije?»): 13 respuestas correctas y 1 parcial. Por ejemplo, Familia Ramírez: «los niños tienen 4, 7 y 11 años»; Pareja Torres, un día después: «la Casona Piedra Azul, desde $340.000 por noche»; Sofía: «Casa Naranja del Centro, $480.000 por noche, $1.920.000 por 4 noches». La parcial: Laura preguntó cuántas noches habían dicho en Cartagena y el asesor dudó si las 5 noches eran solo de Cartagena. Esta es la referencia para cuando se recorte la memoria.

**De qué está hecha cada llamada (promedio de 184 llamadas):**

| Parte | Tokens | % de la entrada | % del costo total |
|---|---|---|---|
| Instrucciones del asesor | 67 | 0,7 % | 0,6 % |
| Catálogo completo | 6.478 | 68,2 % | 55,9 % |
| Historial de la conversación | 2.936 | 30,9 % | 25,4 % |
| Mensaje nuevo del cliente | 17 | 0,2 % | 0,1 % |
| Salida (respuesta y razonamiento) | 416 | – | 18,0 % |
| **Total** | **9.914** | | **0,00116 USD por llamada** |

**Cómo crece la entrada turno a turno:**

| Turno | Llamadas | Entrada (tokens) | Salida (tokens) | Costo por llamada (USD) |
|---|---|---|---|---|
| 1 | 10 | 6.565 | 302 | 0,00081 |
| 2 a 5 | 40 | 7.419 | 749 | 0,00112 |
| 6 a 10 | 50 | 8.956 | 385 | 0,00109 |
| 11 a 20 | 70 | 10.895 | 303 | 0,00124 |
| 21 a 28 | 14 | 12.480 | 222 | 0,00136 |

**Las palancas, calculadas sobre las 184 llamadas reales** (se mantiene la salida observada; no se mide si la calidad de las respuestas cambia):

| Configuración | Costo de las 184 llamadas (USD) | Ahorro | 1.000 conversaciones al mes (USD) |
|---|---|---|---|
| Punto de partida: todo el historial y el catálogo completo (real) | 0,2130 | 0 % | 21 |
| Ventana de 10 turnos | 0,1968 | 8 % | 20 |
| Ventana de 5 turnos | 0,1787 | 16 % | 18 |
| Solo el catálogo de las ciudades que le interesan al cliente | 0,1296 | 39 % | 13 |
| Catálogo de interés + ventana de 5 turnos | 0,0953 | 55 % | 10 |

> **Qué dice el resultado**
> 1. **Lo que más pesa es el catálogo, no la memoria.** El catálogo es el 68 % de la entrada y el 56 % del costo; el historial, el 31 % de la entrada y el 25 % del costo. Por eso recortar la memoria a 5 turnos ahorra solo un 16 %, mientras que enviar solo el catálogo de las ciudades que le interesan al cliente ahorra un 39 %.
> 2. **El 97 % de lo que se envía en cada turno ya se había enviado en el turno anterior** (entre 91 % y 99 %). Es texto redundante: la conversación solo agrega la respuesta anterior y el mensaje nuevo. Es el potencial de la caché de prompts, cuya tarifa todavía no está verificada.
> 3. **El 70 % del catálogo sobra** para lo que pregunta cada cliente: con solo sus ciudades pesa en promedio 1.953 tokens (entre 1.069 de Camilo, que solo pregunta por Medellín, y 2.615 de Valentina, que pregunta por tres ciudades).
> 4. **Cada turno cuesta más que el anterior:** la entrada pasa de 6.565 tokens en el turno 1 a 12.480 en los turnos 21 a 28, y una conversación de 10 turnos (Camilo) costó 0,0090 USD contra 0,0317 USD una de 24 (Julián).
> 5. **El razonamiento es poco en conversación:** el 17 % de la salida, que equivale a cerca del 3 % del costo total. Las respuestas son cortas y, en turnos de puro dato («cuanto era la noche?»), casi no razona.
> Para pensar, «¿qué estrategias hay para recordar sin reenviar todo?»: ventana de los últimos N turnos (−16 % con 5), mandar solo el catálogo de interés (−39 %), las dos juntas (−55 %), y por probar: resumir lo viejo en pocas líneas y la caché de prompts. La más rentable no era recortar la memoria sino el catálogo.

### 3.5 Parámetros de generación {ref=e4:E4}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e4) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 4: parámetros de generación"`
- [x] Ejercicio B.1: probar los parámetros con una pregunta del caso de viajes y confirmar qué se puede variar ([ver paso B.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s7))

> **Notas del proceso**
> Script: `chat-consola/etapas/e4_parametros.py`, con el catálogo cargado y el primer mensaje de un cliente («cuanto vale ir a cartagena 4 noches?»). Cada prueba mide tokens, razonamiento, segundos y costo. Gasto total de la etapa: 0,00737 USD.
> 1. **`max_tokens` (el tope de salida):** con 40 y con 150 el asesor **no alcanzó a escribir nada** (`stop_reason = max_tokens`): todo el tope se fue en razonamiento (40 de 40 y 150 de 150). Con 2.048 respondió completo (634 tokens, 228 de razonamiento). El razonamiento cuenta dentro del tope, así que un tope bajo no abarata: se paga igual y no se obtiene respuesta (0,00068 y 0,00073 USD tirados).
> 2. **`effort`:** low 630 tokens de salida (233 de razonamiento, 0,00097 USD), medium 709 (330, 0,00101), high 530 (222, 0,00092). **No subió en orden**: con una sola muestra por nivel, la variación (±5 % en costo) es ruido, no efecto. En una pregunta de precios el esfuerzo casi no cambia nada; el efecto real se mide con muchas muestras en el laboratorio (3.32).
> 3. **`system` (comportamiento):** agregar «máximo 2 frases, usa solo precios del catálogo y di de qué registro salen» produjo una respuesta mucho más corta (un párrafo con los 3 precios) pero **el razonamiento se disparó a 697 tokens** (contra 238) y la llamada costó más: 0,00110 USD contra 0,00098. Una instrucción de brevedad ahorra texto, no necesariamente tokens.
> 4. **Temperatura:** la API devolvió 400: `temperature is deprecated for this model`. En Claude 5.5 no se puede variar; se controlan `max_tokens`, `effort` y `system`.
> **Para pensar** (¿qué effort para un chat de ventas?): para preguntas frecuentes con datos en el catálogo, `low` o el valor por defecto, porque el catálogo ya trae la respuesta y razonar más no cambió las cifras (todas salieron de `casa-naranja-del-centro`, `hotel-brisas-de-bocagrande` y `hostal-la-muralla-viva`). Para analizar un contrato, `high`, porque ahí razonar sí cambia la calidad.

### 3.6 Panorama de modelos de Anthropic {ref=e5:E5}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e5) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 5: panorama de modelos"`
- [x] Ejercicio B.2: comparar Haiku, Sonnet y Opus con una pregunta de un cliente del caso ([ver paso B.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s7))

> **Notas del proceso**
> Script: `chat-consola/etapas/e5_modelos_anthropic.py`. Parte A: la API lista 14 modelos disponibles para la cuenta; los tres de la familia 5.5 (Haiku, Sonnet y Opus) tienen contexto de 1.000.000 de tokens y salida máxima de 128.000; también aparecen Fable 5.1, Opus 5, Sonnet 5, Fable 5 y versiones anteriores (algunas de 200.000 de contexto). Parte B: la misma consulta de un cliente, con el catálogo cargado y `effort` bajo: «somos 2, del 10 al 14 de diciembre, queremos ir a cartagena. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro». Una sola muestra por modelo.
>
> | Modelo | Segundos | Tokens de salida (razonamiento) | Costo (USD) | Calidad (1–5, juicio de Claude) |
> |---|---|---|---|---|
> | Haiku 5.5 | 2,6 | 391 (182) | 0,00086 | 4 |
> | Sonnet 5.5 | 4,1 | 367 (0) | 0,01691 | 5 |
> | Opus 5.5 | 4,7 | 454 (110) | 0,03555 | 5 |
>
> 1. **Los tres usaron el mismo dato del catálogo:** `casa-naranja-del-centro`, 480.000 por noche, 4 noches = $1.920.000. Ninguno inventó un precio; los tres avisaron que diciembre es temporada alta y que un asesor confirma la tarifa. La exactitud de la cifra es igual en los tres.
> 2. **La diferencia está en el estilo, no en los datos:** Haiku dio una respuesta corta con una sola opción y ofreció buscar algo más económico. Sonnet y Opus agregaron alternativas del catálogo (`hotel-brisas-de-bocagrande` desde $360.000; Opus también `hostal-la-muralla-viva` desde $120.000) y cerraron proponiendo pasar con un asesor. Por eso les doy 5 y a Haiku 4: es un juicio mío con una muestra, no una medición.
> 3. **El costo sí cambia mucho:** Sonnet costó 19,7 veces lo de Haiku y Opus 41 veces, con los mismos 6.618 tokens de entrada. El tiempo cambió poco (de 2,6 a 4,7 s). El razonamiento fue distinto sin seguir el orden de precio (Sonnet 0, Opus 110, Haiku 182).
> **Para pensar** (¿la diferencia de calidad justifica la de costo? ¿cuál usar en el chat final?): para esta consulta no. La cifra que le importa al cliente es idéntica y la diferencia es de estilo, a un costo 20 a 41 veces mayor. El chat del piloto debería correr en Haiku, y Sonnet o Opus quedarían para casos que lo exijan (consultas complejas o reclamos), lo que se confirma con la calidad medida en el laboratorio (3.25, 3.26 y 3.32).

### 3.7 Primer chat con memoria {ref=e6:E6}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e6) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 6: chat con memoria"`
- [x] Ejercicio C.1: crear el catálogo ficticio (JSON); adelantado, ya está creado en `chat-consola/datos-simulados/` ([ver paso C.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.2: crear los 10 clientes ficticios y sus guiones tipo WhatsApp; adelantado en el tema 3.4, ya está creado ([ver paso C.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.3: crear la base SQLite del piloto (clientes, mensajes, ejecuciones); es la base única, el tema 3.16 la amplía; adelantado en el tema 3.4, ya está creado ([ver paso C.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.4: construir el simulador que entrega los mensajes; adelantado en el tema 3.4, ya está creado ([ver paso C.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.5: chat con memoria por cliente ([ver paso C.5](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))

> **Notas del proceso**
> Script: `chat-consola/etapas/e6_chat_memoria.py`. Es un chat de consola donde **cada cliente tiene su propia lista de mensajes** (`/cliente NOMBRE` cambia de cliente) y donde, en cada turno, se hacen cuatro pasos: agregar el mensaje del cliente, enviar **toda** su lista, recordar la respuesta del asesor y mostrar cuánto creció la entrada. No escribe en la base del piloto, para no tocar las 184 llamadas medidas en 3.4. Con `--demo` corre una prueba guionada (5 llamadas, 0,00483 USD).
> 1. **La memoria funciona:** Laura dijo «nos casamos el 14 de febrero» y recibió los precios del catálogo; en el turno siguiente preguntó qué fecha había dicho y qué precio le dieron, y el asesor respondió «14 de febrero» y repitió los precios exactos ($120.000, $360.000 y $480.000 por noche, y los dos tours). La entrada pasó de 6.599 a 6.988 tokens: la memoria sumó 389 tokens (5,9 %).
> 2. **Cada cliente tiene la suya:** Camilo, con su lista vacía, preguntó «¿en qué fecha nos casamos?» y el asesor contestó que no tiene acceso a conversaciones anteriores y ofreció ayuda; no mezcló los datos de Laura ni inventó una fecha.
> 3. **Experimento de ruptura:** se repitió el caso de Laura sin guardar las respuestas del asesor. En el segundo turno el asesor solo vio los dos mensajes de la cliente (`user`, `user`) y dijo «no veo un precio anterior en esta conversación», después volvió a listar los precios base. Es una buena respuesta (no inventó), pero perdió el hilo: la conversación ya no continúa lo que se había dicho. Además **no se ahorró casi nada**: la entrada fue 6.613 contra 6.988 tokens.
> **Para pensar** (¿qué pasa con esta memoria al cerrar el programa? ¿y después de 500 turnos?): al cerrar el programa la lista vive solo en la memoria del proceso y se pierde; por eso en el piloto el historial se guarda en la tabla `mensajes` de la base única. Después de 500 turnos, cada llamada reenvía todo: con el crecimiento medido en 3.4 (unos 250 tokens por turno) la entrada llegaría a unos 131.000 tokens en el turno 500 y la conversación entera costaría cerca de 3,5 USD solo en entrada con Haiku, contra unos 0,4 USD con una ventana de 5 turnos (cifras estimadas). Ambos problemas se resuelven al ensamblar el chat final (3.9).

### 3.8 Limitaciones de los LLM {ref=e7:E7}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e7) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 7: pruebas de limitaciones"`
- [x] Ejercicio D.1: correr las trampas del catálogo y medir si el chat inventa ([ver paso D.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> Script: `chat-consola/etapas/e7_limitaciones.py`. Toma 8 mensajes-trampa de los clientes del piloto (cosas que el catálogo no publica) con su conversación previa, y compara dos respuestas: **sin reglas** (la que el asesor ya dio en 3.4, guardada en la base, sin gasto nuevo) y **con reglas** (respuesta nueva con las cinco reglas del prompt: usar solo el catálogo y citar el registro, decir «no lo tengo» si no está, preguntar lo que falte antes de cotizar, recomendar una opción principal y responder corto). Solo lee la base; guarda el resultado en `chat-consola/informes/limitaciones-resultados.md`. Gasto: 8 llamadas, 0,00850 USD.
>
> | Trampa (cliente, turno) | Sin reglas | Con reglas |
> |---|---|---|
> | Hotel que no existe: «casa dorada imperial» (Laura, 7) | No inventó: dijo que no está en el catálogo | Igual; ofreció ver con un asesor |
> | Descuento de grupo del 20 % (Andrés, 9) | No inventó; listó dos alojamientos | No inventó; respuesta más corta y sin lista |
> | Clima de Medellín (Camilo, 6) | No inventó | Dijo que no tiene el dato, pero agregó «suele ser templada, la ciudad de la eterna primavera» (afirmación fuera del catálogo) |
> | Opción vegetariana en el almuerzo (Valentina, 8) | No inventó; pasó al asesor | Igual |
> | Tour en Cali (Julián, 13) | No inventó; sugirió Medellín y dijo que sus alojamientos «quedan bien ubicados para salir de noche» (no está en el catálogo) | No inventó; ofreció el tour `comuna-13-y-metrocable` con su precio |
> | Comida sin maní (Familia Ortiz, 9) | No inventó; pasó al asesor | Igual, más breve |
> | Garantía de que no hay maní (Familia Ortiz, 12) | No inventó; sugirió adrenalina autoinyectable (consejo médico fuera del catálogo) | No inventó; remitió al médico de la hermana |
> | Precio de temporada alta (Sofía, 16) | No inventó; repitió precios base | No inventó; respuesta mucho más corta |
>
> 1. **Resultado principal:** en las 8 trampas, **ninguna de las dos versiones inventó** un hotel, un descuento, un clima, una dieta, una garantía ni un precio. Con el catálogo cargado, Haiku ya reconoce cuando algo no está publicado. Es un hallazgo honesto: la hipótesis de que sin reglas inventaría no se confirmó en estos 8 casos (una muestra por caso; el juicio es de Claude, no una medición automática).
> 2. **Lo que sí cambian las reglas:** el formato y la brevedad (las respuestas pasaron de 2.340 a 1.806 tokens de salida en conjunto, −23 %) y algunas afirmaciones sueltas fuera del catálogo: sin reglas hubo dos (la vida nocturna de Medellín y la adrenalina); con reglas hubo una (el clima «templado» de Medellín). Las reglas no eliminan esos deslices; los reducen.
> 3. **Las reglas pesan 213 tokens por llamada** (9.012 contra 8.799 en el caso de Laura), constantes y reenviados cada vez.
> **Para pensar** (¿qué alucinación sería más peligrosa en un CRM de ventas y cómo evitarla?): la más peligrosa es la que afecta a una persona: asegurar que un tour o alojamiento es libre de maní o apto para movilidad reducida. Le sigue prometer un precio, un descuento o una disponibilidad que no existe, porque obliga a la agencia con el cliente. Para evitarlas: (1) que el dato salga del catálogo y se cite el registro; (2) la regla de decir «no lo tengo» y pasar a un asesor humano, que ya se vio en los casos de los Ortiz; (3) que los precios y totales los calcule el código y no el modelo (tema 3.30); y (4) medir con pruebas, no suponer.

### 3.9 Ensamblar el chat final {ref=e8:E8}

- [x] Claude lee el [apartado de la guía](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/llms-chatbot-consola-nivel-1-fundamentos_v7_2026-10-12.html#e8) y explica qué se va a hacer y por qué
- [x] Claude lo construye siguiendo «Construcción»: escribe el código y explica cada parte
- [x] Claude lo ejecuta y compara con «Ejecuta y observa» o el punto de control
- [x] Claude documenta en las notas qué hace el código y qué se observó, y responde «Para pensar» si el apartado lo trae
- [x] Commit: `git commit -m "etapa 8: chat final ensamblado"`
- [x] Ejercicio D.2: atender a los 10 clientes con recorte de memoria y guardar cada llamada ([ver paso D.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s9))

> **Notas del proceso**
> Programa: `chat-consola/chat.py`, armado por bloques como pide la guía (configuración, memoria, llamada, comandos, bucle) y adaptado al caso. Cada decisión viene de un tema anterior: Haiku (3.6), `max_tokens` 2.048 y `effort` bajo (3.5), catálogo con las reglas contra inventar (3.8), streaming (3.3), costo por llamada (3.4) y una memoria por cliente (3.7). Resuelve los dos problemas del 3.7: **la memoria se guarda en la base del piloto** (tabla `mensajes`, con una columna nueva `config` para no pisar la conversación medida en 3.4) y **se envía con ventana de 5 turnos**. Comandos: `/cliente N`, `/tokens` (cuenta gratis lo que se enviará), `/historial`, `/reset`, `/ayuda`, `/salir`. Errores por tipo (clave inválida, límite de uso, sin conexión, error HTTP) con aviso claro y sin guardar el mensaje fallido.
> **Ejecuta y observa:** (1) en consola, Camilo preguntó por el Hotel Poblado Verde y el asesor respondió en streaming «desde $330.000 COP por noche» (registro `hotel-poblado-verde`) y preguntó fechas y personas antes de cotizar; `/tokens` dijo 6.926 tokens para la próxima llamada y `/historial` mostró la ventana; (2) con una clave falsa salió «[API key inválida. Revisa tu .env]», sin traza de error y sin guardar nada; (3) al abrir el chat dice cuántos turnos tiene guardados cada cliente, porque la memoria vive en la base.
> **Paso D.2 (los 10 clientes):** `python chat.py --piloto` atendió los mismos 184 mensajes del 3.4 con la configuración final, más una pregunta de cierre por cliente («¿me confirmas los datos de mi viaje que te he dado?»): 194 llamadas, 0,1725 USD, todas terminadas sin cortes (`end_turn`). Después, `--sonda-completa` hizo la misma pregunta de cierre con el historial completo (10 llamadas, 0,01415 USD), para aislar el efecto de la ventana.
>
> | Medida (184 mensajes) | Línea base (3.4) | Chat final (3.9) | Cambio |
> |---|---|---|---|
> | Tokens de entrada | 1.747.598 | 1.393.846 | −20,2 % |
> | Tokens de salida | 76.523 | 47.473 | −38,0 % |
> | Razonamiento | 25.101 | 9.795 | −61,0 % |
> | Costo | 0,2130 USD | 0,1631 USD | −23,4 % |
> | Entrada máxima de una llamada | 14.845 (Julián) | 8.165 (Julián) | Ya no crece con la conversación |
>
> 1. **Más barato:** −23,4 % en las mismas 184 llamadas, por encima del −16 % calculado solo para la ventana, porque también bajó la salida (reglas de brevedad y `effort` bajo).
> 2. **Pero olvida:** con la ventana de 5 turnos, el asesor recordó el dato clave en **6 de 10 clientes**; con el historial completo, en **10 de 10**. Olvidó las edades de los niños Ramírez (4, 7 y 11), las fechas de Camilo (3 al 6 de noviembre), que Valentina no come carne y el presupuesto de 3 millones de Julián. No inventó: dijo «no me has dado fechas» o «no me has dicho cuál es», y en el caso de Valentina incluso corrigió una suposición suya. Es justo el riesgo que se había anticipado en 3.4.
> 3. **Las trampas siguen bien:** en el chat final, 0 de 8 trampas inventadas. En la de Andrés hizo bien la cuenta: 6 personas en cabañas de 3 (`ecohostal-selva-tayrona`, `huespedes_max` 3) son 2 cabañas, «$380.000 por noche».
> **Para pensar** (de la guía: ¿qué pasa al cerrar y después de 500 turnos?): al cerrar ya no se pierde nada (vive en la base), y la entrada ya no crece: con la ventana, la llamada más grande pesó 8.165 tokens en vez de 14.845. El costo que queda es el catálogo, y el precio de la ventana es la memoria: hace falta una ficha del cliente que conserve los datos clave fuera de la ventana.

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
| 2026-10-12 | Los títulos de los temas enlazan a su entrada del análisis de resultados; cada entrada lleva un ejemplo. |
| 2026-10-12 | Se vincula el ejercicio simulado (asesor de viajes, piloto de 10 clientes): enlace en la sección 1 y casillas «Ejercicio» en los temas 3.5–3.11, 3.17, 3.25 y 3.26. |
| 2026-10-13 | Decisión del ejercicio: la base SQLite nace en 3.7 y el 3.16 la amplía; nueva casilla «Ejercicio E.0» en 3.16. |
| 2026-10-13 | Se reinicia el checklist sobre el ejercicio: 3.2 a 3.4 se rehacen con el caso (casillas desmarcadas, notas previas conservadas); nuevas casillas «Ejercicio» en 3.12 a 3.15 y 3.24; renumerados los pasos E.5, E.6, E.8 y E.9; temas 3.18 a 3.23 (dashboard) aplazados. |
| 2026-10-13 | Se revierte el aplazamiento: los temas 3.18 a 3.23 (dashboard) vuelven al checklist, con sus casillas «Ejercicio E.7 a E.12»; las pruebas, los experimentos y las decisiones pasan a E.13, E.14 y E.15. |
| 2026-10-13 | Las Partes 3 y 4 (agente y tablero) pasan a este documento como los temas 3.27 a 3.43, con las casillas «Ejercicio F.1 a F.17»; el proyecto del nivel pasa a ser el 3.44. El agentizando queda como segundo pase opcional. |
| 2026-10-13 | Se reescribe el texto general del «Análisis de resultados» con el ejercicio del asesor de viajes y se agrega «En el ejercicio» a cada entrada. Las filas de esta bitácora que habían quedado al final del archivo vuelven a esta tabla. |
| 2026-10-13 | Tema 3.2 rehecho con el caso del asesor de viajes: casillas marcadas, notas nuevas y entrada del análisis reescrita. |
| 2026-10-13 | Se adelanta la creación del catálogo ficticio (paso C.1, marcado): ya existe antes del tema 3.3; las casillas A.3 y A.4 pasan a usarlo. |
| 2026-10-13 | Tema 3.2 repetido con el catálogo cargado. Tema 3.3 rehecho con el caso: 6 ejecuciones, casillas marcadas, notas y entrada del análisis reescritas. |
| 2026-10-13 | Los ejemplos de las entradas 3.2 y 3.3 del análisis muestran las respuestas con catálogo y el registro del que sale cada cifra. |
| 2026-10-13 | Las entradas del análisis suman «Qué encareció el proceso» y «Cómo se podría optimizar» (mirada de AI Engineer); aplicado a 3.2 y 3.3. |
| 2026-10-13 | El análisis suma «Variables que afectaron el proceso» y «Cómo optimizar cada variable» (tablas con cifras) en 3.2 y 3.3, y un «resumen acumulado de variables» para decidir con datos. |
| 2026-10-13 | Los temas 3.2 y 3.3 quedan enfocados solo en el asesor con el catálogo cargado (notas, tablas, análisis y resumen de variables). |
| 2026-10-13 | Tema 3.4 completo con 10 conversaciones reales (184 llamadas, 0,213 USD): radiografía del contexto, palancas calculadas y entrada del análisis. Se adelantan los pasos C.2, C.3 y C.4 (clientes, base SQLite y simulador). Las estimaciones de 3.2 y 3.3 pasan a cifras calculadas. |
| 2026-10-13 | La entrada 3.4 suma la tabla «Tokens ahorrados en dólares» (medido contra optimizado) y se agrega un hook que pide esa tabla en cada entrada del análisis. |
| 2026-10-13 | Tema 3.5 completo con el asesor y el catálogo (8 llamadas, 0,00737 USD): max_tokens, effort, system y temperatura; entrada del análisis con la tabla de ahorro. |
| 2026-10-13 | Tema 3.6 completo con el asesor y el catálogo (3 llamadas, una por modelo, 0,0533 USD): lista de modelos de la API, comparación Haiku, Sonnet y Opus y entrada del análisis con la tabla de ahorro. |
| 2026-10-13 | Tema 3.7 completo con una memoria por cliente (5 llamadas, 0,00483 USD): memoria, aislamiento entre clientes y experimento de ruptura; entrada del análisis con la tabla de ahorro. Se marca el paso C.5. |
| 2026-10-13 | Tema 3.8 completo con 8 trampas del catálogo (0,00850 USD): sin reglas contra con reglas del prompt; ninguna de las dos inventó. Se agregan las reglas a `caso_simulado.py` (opcionales) y se marca el paso D.1. |
| 2026-10-13 | Cada entrada del análisis cierra con «CONCLUSIONES» (cuatro consejos de AI Engineer enfocados en solución, con otra letra en el HTML); el hook automático lo pide en cada entrada nueva. |
| 2026-10-13 | Tema 3.9 completo: `chat.py` con memoria en la base (columna `config` en `mensajes`) y ventana de 5 turnos; paso D.2 con los 10 clientes (194 llamadas, 0,1725 USD) y sonda con historial completo (0,01415 USD): −23,4 % de costo, pero recuerda el dato clave en 6 de 10 clientes contra 10 de 10. |

## Análisis de resultados {id=analisis}

Esta sección explica, en palabras simples, para qué sirve todo lo que se construye aquí y qué va dejando cada tema. Está pensada para alguien que empieza en el campo de la inteligencia artificial.

#### El objetivo, en una frase

Aprender a usar un modelo de lenguaje (un LLM, como Claude) desde un programa propio, medir cuánto cuesta y qué tan bien responde, y usar esas mediciones para construir un agente que haga trabajo real por sí solo, con reglas y bajo control. Todo se hace sobre un caso simulado que se trata como real.

#### El caso sobre el que se hace todo

En lugar de practicar con preguntas sueltas, todo el checklist se vive sobre un mismo caso: un **asesor de viajes** de una agencia ficticia, «Turismo Colombia (simulada)», que atiende por WhatsApp a 10 clientes ficticios. Los datos son inventados (catálogo de destinos, hospedajes y tours, y las conversaciones de los clientes), pero se tratan como reales: mensajes cortos e informales, clientes que vuelven otro día, preguntas trampa sobre cosas que no están en el catálogo.

¿Por qué un caso y no ejemplos sueltos? Porque así cada concepto se ve con consecuencias de negocio. Un precio inventado deja de ser una curiosidad técnica: es una cotización falsa a un cliente. Un chat que olvida que alguien es alérgico al maní deja de ser un detalle de memoria: es un problema de verdad. Y como el proceso es el mismo para cualquier negocio, lo que se aprende aquí se puede llevar a otros proyectos cambiando solo el catálogo y los clientes. El ejercicio completo está explicado en el documento «Ejercicio simulado · Chat de consola».

#### Qué se construye y qué se obtiene

1. **El chat del asesor de viajes, con memoria** (Parte 1, temas 3.1 a 3.11). Es un programa que conversa con Claude desde la terminal, atiende a varios clientes y recuerda lo que cada uno dijo. Construirlo enseña lo básico: cómo se le habla al modelo, qué es un token, cuánto cuesta cada mensaje y por qué el modelo a veces inventa. **Resultado:** saber conectar cualquier programa a un LLM y saber qué puede salir mal.
2. **El laboratorio de parámetros, con su dashboard** (Parte 2, temas 3.12 a 3.26). Es una aplicación para probar el mismo pedido de un cliente con distintos modelos y ajustes, y medir tiempo, costo y calidad. **Resultado:** decidir con datos, no a ojo, qué modelo y qué configuración usar.
3. **El agente asesor** (Parte 3, temas 3.27 a 3.36). Es un programa en el que el LLM no solo responde: decide pasos, consulta el catálogo con herramientas y repite hasta resolver, con límites de gasto y aprobación humana cuando hace falta. **Resultado:** automatizar de punta a punta la atención de un cliente, bajo control.
4. **El tablero del agente** (Parte 4, temas 3.37 a 3.43). Muestra qué tan bien trabaja el agente comparado con hacerlo a mano, y sugiere ajustes. **Resultado:** mejorar el agente con evidencia y saber si vale la pena.
5. **El proyecto del nivel** (tema 3.44). El resumen de todo lo anterior como una pieza que se puede mostrar.

#### Para qué sirve todo esto

- **Para el portafolio:** cada etapa queda como un commit en GitHub, que es la prueba de que se sabe hacer.
- **Para Minus:** es la base para ofrecer a clientes asistentes y agentes que funcionan, cuestan lo que se calculó y se pueden medir. El asesor de viajes es el modelo; lo mismo vale para una inmobiliaria, una constructora o un call center.
- **Para otros proyectos:** el proceso queda estandarizado (checklist, forma de medir y de documentar), así que se puede llevar a otro repositorio, como el CRM de ventas, cambiando solo los datos.
- **Para el criterio propio:** se aprende a detectar cuándo un LLM sirve y cuándo no, cuánto va a costar antes de construir y cómo evitar que invente datos.

#### Cómo leer cada entrada

Cada vez que se marca un tema como hecho, aquí se agrega una entrada con estas partes: **qué se hizo**, **a qué nos conduce**, **en el ejercicio** (qué significa ese resultado para el asesor de viajes), **qué encareció el proceso** (en qué se fueron los tokens, explicado en palabras simples), **las variables que afectaron el proceso** con su dato y su efecto, y **cómo optimizar cada variable** (mirada de AI Engineer: qué cambiar, resultado esperado, si el dato es medido, calculado o estimado, y dónde se prueba) y un **ejemplo** concreto con números cuando los hay. Desde que existe el catálogo, los ejemplos muestran las respuestas del asesor **ancladas en los registros del catálogo** (con el nombre del registro de donde sale cada cifra), para poder verificarlas. El número y el título de cada tema, más arriba, llevan directo a su entrada.

#### Variables del proceso: resumen acumulado

La mirada de un AI Engineer: qué variables mueven el costo y la exactitud del asesor, cuánto se midieron y cómo se optimizan. Se actualiza con cada tema; las decisiones se toman con estos datos.

| Variable | Qué es, en simple | Dato más reciente | Cómo optimizarla | Estado del dato | Tema |
|---|---|---|---|---|---|
| Catálogo completo | Los datos de la agencia que se mandan en cada mensaje | 6.478 tokens por llamada: 68,2 % de la entrada y 56 % del costo (3.4, 184 llamadas) | Mandar solo el catálogo de interés | Medido | 3.4, 3.25, 3.30 |
| Catálogo innecesario | La parte del catálogo que no sirve para lo que preguntó el cliente | 70 %: con solo sus ciudades, 1.953 tokens en promedio (3.4) | Filtrar por ciudades de interés: −39 % del costo | Medido; ahorro calculado | 3.25, 3.30 |
| Memoria (historial) | La conversación anterior, que se reenvía en cada mensaje | 2.936 tokens por llamada en promedio; la entrada va de 6.565 (turno 1) a 12.480 (turnos 21 a 28) (3.4) |  Ventana de 5 turnos (−16 %); resumen de lo viejo | Medido; ahorro calculado; resumen por medir | 3.25 |
| Texto redundante | Lo que se envía igual que en la llamada anterior | 96,7 % de la entrada (3.4) | Caché de prompts | Medido; tarifa por verificar | 3.4 en adelante |
| Longitud de la conversación | Cuántos turnos dura | De 0,0090 USD (10 turnos) a 0,0317 USD (24 turnos) por conversación (3.4) | Ventana, resumen, filtrar catálogo | Medido | 3.25 |
| Razonamiento | Lo que el modelo piensa antes de responder | 39 % de la salida en el primer mensaje largo (3.3); 17 % en las conversaciones (3.4), cerca del 3 % del costo | Esfuerzo (effort) según el tipo de mensaje; sin efecto claro con 1 muestra por nivel (3.5) | Medido; efecto por medir | 3.32 |
| Longitud de la respuesta | Lo que el asesor escribe al cliente | 416 tokens de salida por respuesta en promedio, 18 % del costo (3.4) | Respuestas de chat; un tope bajo corta sin abaratar (3.5) | Medido | 3.5, 3.32 |
| Modelo | Haiku, Sonnet u Opus | La misma consulta costó 0,00086 (Haiku), 0,01691 (Sonnet, 19,7 veces) y 0,03555 USD (Opus, 41 veces) con el mismo precio correcto del catálogo (3.6) | Haiku por defecto; Sonnet u Opus solo si la tarea lo exige | Medido (1 muestra); calidad por medir | 3.6, 3.26 |
| Formato de los datos | Cómo se escribe el catálogo | Compacto: 18 % menos tokens (7.923 a 6.469) | Ya aplicado | Medido | — |
| Idioma | Español frente a inglés | El español usa cerca de 1,5 veces más tokens (21 contra 14 en la misma frase) | Instrucciones internas en inglés, respuestas en español | Medido en frases; por medir en el sistema | 3.4 en adelante |
| Fuente de los datos | Si un precio sale del catálogo o lo inventa el modelo | Con catálogo, 3 de 3 respuestas con la misma cifra verificable: $1.920.000 de `casa-naranja-del-centro` (3.2); 13 de 14 recuerdos correctos con el historial completo (3.4); 0 de 8 trampas del catálogo inventadas, con y sin reglas (3.8) | Datos del catálogo y cálculos en código | Medido | 3.8, 3.30 |
| Tiempo hasta el primer token | Cuánto tarda el asesor en empezar a responder | Sin medir | «Escribiendo…» y mensajes cortos | Por medir | 3.15 |

#### Lo que vamos logrando

#### 2 · Base del proyecto (2026-10-12)

**Qué se hizo:** se escribió el objetivo del proyecto, se creó el repositorio privado en GitHub, se configuró Git y se separó la documentación de los resultados.

**A qué nos conduce:** ya hay un lugar ordenado donde cada avance queda guardado y fechado. Desde ahora, todo lo que se construya deja rastro, y ese rastro es el portafolio.

**En el ejercicio:** el repositorio es donde viven el catálogo ficticio, los 10 clientes, el simulador y la base de datos del piloto, junto con cada commit del asesor de viajes. Si mañana el caso se lleva a otro proyecto, este historial muestra cómo se construyó.


> **Ejemplo**
> Funciona como la historia clínica de un paciente. Si dentro de seis meses alguien de un cliente de Minus pregunta «¿desde cuándo saben conectar sistemas a Claude?», no hace falta decir «hace un tiempo»: se abre GitHub y se ve el commit «etapa 1: primera llamada a la API», con fecha, código y resultado.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Un commit por etapa con su cifra.** Que el mensaje lleve el dato clave (por ejemplo «184 llamadas, 0,213 USD»): el historial de GitHub se vuelve evidencia medible, no solo fechas.
> 2. **Las mediciones viven en archivos, no en el chat.** Base del piloto, informes en `chat-consola/informes/` y este análisis: todo lo que se mide queda versionado y se puede volver a calcular.
> 3. **Separar lo que gasta tokens de lo que no.** Código sin IA en `scripts/` y agentes aparte, como pide el laboratorio: así se sabe exactamente qué parte del sistema cuesta dinero.
> 4. **Llevar el gasto por tema en la bitácora.** Cada tema anota cuántas llamadas y cuántos USD gastó; sumado, es el costo real de aprender y el presupuesto de referencia para candyCRM.

#### 3.1 · Preparación (2026-10-12)

**Qué se hizo:** se creó un entorno de Python aislado para el proyecto (así sus bibliotecas no se mezclan con las de otros), se instaló el SDK de Anthropic, que es el programa que permite hablar con Claude desde código, y se guardó la clave de acceso en un archivo `.env` que Git no sube. La clave es exclusiva de este proyecto y vence sola.

**A qué nos conduce:** es el piso sobre el que se apoya todo lo demás. Sin entorno aislado, los proyectos se estorban entre sí; sin la clave protegida, un descuido la publicaría y alguien podría gastar tu dinero. Con esto listo, el siguiente paso es el primero emocionante: hacer que un programa nuestro le haga una pregunta a Claude y reciba la respuesta.

**En el ejercicio:** es el mismo entorno desde el que corre el asesor de viajes. La clave solo se gasta con clientes simulados, y como es exclusiva de este proyecto, el gasto del ejercicio se ve aparte del resto.


> **Ejemplo**
> El entorno virtual es como tener una caja de herramientas aparte para cada obra. Si el CRM necesita una versión de la biblioteca `anthropic` y esta Academia otra, cada uno usa la suya y ninguno rompe al otro.
> La clave en `.env` es como la llave de la casa guardada en un cajón, no pegada en la puerta: el programa la usa, pero no queda a la vista. Cuando hoy la clave quedó escrita en `.env.example` (la plantilla que sí se sube a GitHub), fue como dejarla pegada en la puerta; por eso se cambió la cerradura: se revocó y se creó otra.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Bloquear claves antes de que se suban.** Lo que pasó con `.env.example` se evita con una revisión automática en cada commit que rechace textos con forma de clave (`sk-ant-`), sin depender de la memoria de nadie.
> 2. **Una clave por proyecto con límite de gasto.** Si la clave se filtra, el daño queda acotado al tope del espacio de trabajo y el gasto del ejercicio se ve aparte.
> 3. **Tope de gasto en todo script que haga muchas llamadas.** Como el `--tope-usd` del simulador (3.4): una corrida con un error no puede vaciar el saldo.
> 4. **Fijar versiones en `requirements.txt`.** El mismo código debe dar el mismo resultado en otra máquina; sin versiones fijas, una actualización del SDK cambia las mediciones.

#### 3.2 · Primera llamada a la API (2026-10-13)

**Qué se hizo:** se escribió un programa de unas 35 líneas que le manda a Claude la conversación de un cliente ficticio (dos mensajes, el segundo insistiendo en un precio aproximado) con el papel de asesor de viajes y el catálogo de la agencia cargado, y muestra todo lo que devuelve. Se ejecutó tres veces.

**A qué nos conduce:** a comprobar que, con los datos delante, el asesor responde con cifras verificables. Las tres veces usó el precio del catálogo (480.000 por noche, 1.920.000 por las 4 noches) y aclaró lo que el catálogo no tiene: tarifa de temporada alta, disponibilidad y vuelos. Y a ver lo que cuesta darle esos datos: el catálogo viaja en cada mensaje.

**En el ejercicio:** es la base del asesor. Todo lo que sigue (memoria, parámetros, modelos y trampas) se construye sobre un asesor que consulta el catálogo, y cada cifra de sus respuestas se puede rastrear a un registro.

**Qué encareció el proceso:** dos cosas, y las dos son contexto, es decir, texto que se le manda al modelo antes de que responda.

- **El catálogo viajando en cada mensaje.** Cada mensaje del cliente carga unos 6.500 tokens del catálogo completo, aunque el cliente pregunte solo por Cartagena. En la conversación de dos mensajes eso fue casi todo de los 13.580 tokens de entrada, y cerca del 72 % de todo el costo.
- **La memoria.** En el segundo mensaje se reenvía todo lo anterior: la entrada sube de 6.578 a unos 7.000 tokens. Con dos mensajes casi no se nota, pero en una conversación de 20 crece sin parar (se mide en el tema 3.4).
- **Un costo menos visible: el razonamiento.** Todas las respuestas incluyeron un bloque de razonamiento, que se cobra como salida aunque el cliente no lo vea (39 % de la salida, medido en el tema 3.3).

| Conversación de dos mensajes (Haiku, promedio de 3) | Tokens | Costo |
|---|---|---|
| Entrada | 13.580 | 0,00136 USD |
| Salida | 1.057 | 0,00053 USD |
| **Total** | | **0,0019 USD** |

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Catálogo en el contexto | 6.578 tokens de entrada por mensaje (6.469 son el catálogo compacto) | Cerca del 72 % del costo de la conversación |
| Memoria (historial reenviado) | La entrada sube de 6.578 a unos 7.000 tokens en el segundo mensaje | Crece en cada turno; con dos mensajes es poco, en 20 se dispara |
| Razonamiento | 39 % de la salida (tema 3.3) | Se cobra como salida aunque el cliente no lo vea |
| Longitud de la respuesta | El primer mensaje listó 3 hoteles y 2 tours: entre 599 y 647 tokens de salida con razonamiento | Más salida, que es la parte más cara por token, y más historial para el turno siguiente |
| Fuente de los datos | Las 3 ejecuciones dieron la misma cifra: $1.920.000, del registro `casa-naranja-del-centro` | Exactitud: 3 de 3 respuestas verificables |

**Cómo optimizar cada variable (mirada de AI Engineer):** primero la que más pesa, una a la vez, midiendo costo **y** exactitud.

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Catálogo en el contexto | Mandar solo los registros de las ciudades que le interesan al cliente | De 6.478 a unos 1.953 tokens por mensaje en promedio (entre 1.069 y 2.615); el costo total baja un 39 % | **Calculado** sobre 184 llamadas reales (tema 3.4); la calidad se prueba en 3.25 y 3.26 | 3.25 y 3.26, herramienta en 3.30 |
| Catálogo repetido en cada turno | Caché de prompts: la parte que se repite se cobra más barata | Menor costo de entrada desde el segundo mensaje | **Por verificar** (tarifa sin confirmar en los modelos 5.5) | 3.4 |
| Cálculos de precios | Que el código calcule el total (4 × 480.000) y el modelo solo lo redacte | Total siempre exacto y menos razonamiento | **Por medir** | 3.30 |
| Longitud de la respuesta | Respuestas del tamaño de un chat: preguntar personas y fechas antes de listar todo; tope de `max_tokens` | Menos salida y menos historial para reenviar | **Por medir** | 3.5 |
| Razonamiento | Esfuerzo (effort) según el tipo de mensaje: bajo en un saludo, alto en una cotización | Menos tokens de razonamiento en mensajes simples | **Por medir** | 3.5 y 3.32 |
| Sensación de rapidez | Mostrar «escribiendo…» desde el primer token y enviar mensajes cortos | No baja el costo; el cliente siente que el asesor responde rápido | **Por medir** (tiempo hasta el primer token) | 3.15 |

> **Ejemplo**
> El cliente escribe: «somos 2, del 10 al 14 de diciembre, dame un precio aproximado, un hotel bueno en el centro».
> El asesor, las tres veces: «Casa Naranja del Centro: $480.000 por noche, **$1.920.000** en total. Es el precio base de temporada baja; diciembre suele ser temporada alta, así que el precio final será más alto. Un asesor humano te confirma disponibilidad y precio exacto».
> ¿De dónde sale cada dato? Del registro del catálogo `casa-naranja-del-centro`: `precio_desde` 480000 y ubicación «Dentro del centro amurallado» (por eso es «el hotel del centro»). El total son 4 noches × 480.000 = 1.920.000. Lo que el catálogo no tiene, como la tarifa de diciembre y los cupos, el asesor lo dijo en vez de inventarlo. Cualquiera puede verificar la respuesta abriendo el archivo del catálogo.
> El costo: una conversación de dos mensajes costó unos 0,0019 USD. Si cada conversación tuviera esos dos mensajes, 10.000 conversaciones al mes costarían unos 19 USD con Haiku.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Mandar solo el catálogo que sirve.** De 6.578 a unos 1.953 tokens por mensaje filtrando por las ciudades del cliente: −39 % del costo del piloto (**calculado**, 3.4). Se prueba en 3.25 y 3.26.
> 2. **Que el código haga las cuentas.** 4 × 480.000 = 1.920.000 lo calcula Python y el modelo solo lo redacta: el total siempre exacto y menos razonamiento (**por medir**, 3.30).
> 3. **Preguntar antes de listar.** La primera respuesta listó 3 hoteles y 2 tours (599 a 647 tokens de salida); con las reglas de «una opción» y «pregunta lo que falte», la salida bajó 23 % en 3.8 (**medido**).
> 4. **Ordenar el prompt para la caché.** Rol, reglas y catálogo primero (lo fijo), conversación al final (lo que cambia): deja listo el ahorro de la caché cuando se verifique su tarifa.

#### 3.3 · Ver cómo el modelo predice tokens (2026-10-13)

**Qué se hizo:** se recibió en vivo, pedazo por pedazo, la respuesta del asesor al primer mensaje del cliente, con el catálogo cargado y el razonamiento resumido a la vista. Se repitió tres veces.

**A qué nos conduce:** a ver en qué se va el costo de una respuesta del asesor: con el catálogo, lo que se envía son 6.578 tokens y el costo de cada respuesta ronda los 0,00097 USD, y dos tercios de ese costo son el catálogo reenviado, no lo que el asesor escribe. También se ve el streaming: la respuesta llega en 67 a 92 pedazos que cortan palabras, y por eso en un chat de WhatsApp el cliente puede empezar a leer a los pocos segundos en vez de esperar la respuesta completa.

**En el ejercicio:** la decisión de cuánto catálogo cargar (todo, o solo lo que el cliente pregunta) es la primera palanca de costo del asesor. Se mide en el tema 3.4, junto con cuántos turnos recuerda.

**Qué encareció el proceso:** en una respuesta con catálogo, el costo se reparte así:

| Parte de la respuesta | Tokens | Costo (Haiku) | % del costo |
|---|---|---|---|
| Lo que se envía: instrucciones y catálogo | 6.578 | 0,00066 USD | 68 % |
| Lo que el asesor escribe al cliente | 380 | 0,00019 USD | 20 % |
| Lo que el asesor piensa antes de escribir | 239 | 0,00012 USD | 12 % |
| **Total** | | **0,00097 USD** | 100 % |

En palabras simples: dos de cada tres pesos se van en volver a mandarle al asesor el catálogo completo en cada mensaje, no en lo que contesta. Y una parte se paga por un razonamiento que el cliente nunca ve.

**Variables que afectaron el proceso (mirada de AI Engineer):** promedio de 3 ejecuciones.

| Variable | Dato | Efecto |
|---|---|---|
| Entrada (instrucciones y catálogo) | 6.578 tokens | 68 % del costo de la respuesta (0,00066 de 0,00097 USD) |
| Respuesta visible | 380 tokens (entre 345 y 413) | 20 % del costo |
| Razonamiento | 239 tokens (39 % de la salida; entre 184 y 268) | 12 % del costo |
| Pedazos del streaming | 78 pedazos (entre 67 y 92); varios cortan palabras | No cambia el costo; permite mostrar la respuesta antes |
| Idioma del razonamiento | El resumen llegó en inglés aunque la respuesta salió en español | No afecta al cliente; sí a quien audita las conversaciones |

**Cómo optimizar cada variable (mirada de AI Engineer):** el origen es la ficha que la API devuelve en cada llamada; se ataca primero lo que más pesa.

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Entrada (68 %) | Solo los registros del catálogo que sirven, o caché de la parte que se repite | El costo de las conversaciones baja un 39 % solo con el catálogo de interés (tema 3.4) | **Calculado** | 3.25 y 3.26 |
| Respuesta visible (20 %) | Mensajes cortos de chat, con instrucción clara y tope de `max_tokens` | Menos salida por respuesta | **Por medir** | 3.5 |
| Razonamiento (12 %) | Esfuerzo (effort) bajo en saludos, alto en cotizaciones | Menos razonamiento en mensajes simples | **Por medir** | 3.5 y 3.32 |
| Streaming | «Escribiendo…» desde el primer token y envío por párrafos | Mejor tiempo percibido, mismo costo | **Por medir** (tiempo hasta el primer token) | 3.15 |
| Razonamiento para auditar | Guardar el resumen del razonamiento en las trazas | Saber por qué el asesor recomendó algo | **Por construir** | 3.34 |

> **Ejemplo**
> Es como un vendedor que, antes de contestar cada mensaje, relee todo el catálogo de la agencia: contesta bien, pero cuesta más.
> La respuesta real de la primera ejecución, a «hola buenas, cuanto vale ir a cartagena 4 noches?», listó tres alojamientos con su total de 4 noches: Casa Naranja del Centro, $480.000 por noche, **$1.920.000**; Hotel Brisas de Bocagrande, $360.000 por noche, **$1.440.000**; Hostal La Muralla Viva, $120.000 por noche, **$480.000**. Cada cifra sale de un registro de alojamientos del catálogo en Cartagena (`casa-naranja-del-centro`, `hotel-brisas-de-bocagrande`, `hostal-la-muralla-viva`).
> El costo: con 10.000 mensajes al mes con Haiku serían unos 9,7 USD. Si en lugar del catálogo completo (unos 6.500 tokens) se cargaran solo los alojamientos y tours de la ciudad por la que pregunta el cliente, en el tema 3.4 se calculó que pesaría en promedio unos 1.950 tokens (entre 1.069 y 2.615 según las ciudades) y que las conversaciones costarían un 39 % menos.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Atacar la entrada antes que la salida.** La entrada es el 68 % del costo de cada respuesta; el catálogo de interés rinde más que cualquier ajuste de la respuesta (−39 %, **calculado**).
> 2. **No recortar con `max_tokens`.** En 3.5 un tope de 40 o 150 dejó al asesor sin responder; la salida se acorta con instrucciones y `effort`, no con el tope.
> 3. **Usar el streaming para la sensación de rapidez.** Medir el tiempo hasta el primer token y mostrar «escribiendo…»: no baja el costo, pero el cliente lee a los pocos segundos (3.15).
> 4. **Guardar el resumen del razonamiento en las trazas.** Es el 12 % del costo y explica por qué el asesor recomendó algo; guardarlo permite auditar sin repetir la llamada (3.34).

#### 3.4 · Tokens, ventana de contexto y costos (2026-10-13)

**Qué se hizo:** se corrieron las conversaciones completas de 10 clientes ficticios (184 mensajes, de 10 a 28 por cliente) contra el asesor con el catálogo cargado, y se midió en qué se va cada token de cada llamada: instrucciones, catálogo, historial, mensaje nuevo y respuesta. Con esos datos reales se calculó cuánto bajaría el costo con cada palanca.

**A qué nos conduce:** a una sorpresa que cambia qué optimizar primero: **lo que más pesa no es la memoria, es el catálogo**. Se esperaba que el historial, que crece, fuera el problema; pero el catálogo completo es el 68 % de lo que se envía, y el 70 % de él no le sirve al cliente que está preguntando. Además, el 97 % de lo que se envía en cada turno ya se había enviado en el turno anterior. Con esto ya no se optimiza a ojo: se sabe qué atacar primero y cuánto se espera ganar.

**En el ejercicio:** las 10 conversaciones quedaron guardadas en la base única del piloto, con cada llamada medida. Esa es la línea base con la que se compara cada mejora en los temas 3.25 y 3.26, y los 14 «¿qué te dije?» revisados (13 correctos, 1 parcial) son la referencia para comprobar que recortar la memoria no hace que el asesor olvide los datos del cliente.

**Qué encareció el proceso:** el costo de una llamada promedio (0,00116 USD) se reparte así:

| Parte | Costo (USD) | % del costo |
|---|---|---|
| Catálogo completo, reenviado en cada mensaje | 0,00065 | 56 % |
| Historial de la conversación | 0,00029 | 25 % |
| Respuesta del asesor (incluye el razonamiento) | 0,00021 | 18 % |
| Instrucciones y mensaje nuevo | 0,00001 | 1 % |

En palabras simples: más de la mitad del dinero se va en volver a mandarle al asesor un catálogo del que casi siempre usa una cuarta parte; otra cuarta parte, en repetirle la conversación; y menos de una quinta parte, en lo que el asesor escribe. Y como cada turno reenvía todo lo anterior, una conversación larga cuesta mucho más que una corta: 0,0317 USD la de 24 turnos contra 0,0090 USD la de 10.

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Catálogo completo | 6.478 tokens por llamada; 68,2 % de la entrada | 56 % del costo |
| Historial (la memoria) | 2.936 tokens por llamada en promedio; la entrada crece de 6.565 (turno 1) a 12.480 (turnos 21 a 28) | 25 % del costo; sube con cada turno |
| Texto redundante | 96,7 % de lo que se envía ya se había enviado en la llamada anterior (entre 90,7 % y 99,3 %) | Casi toda la entrada se paga más de una vez |
| Catálogo innecesario | Con solo las ciudades de cada cliente pesaría 1.953 tokens en promedio, 30 % del completo | 70 % del catálogo no le sirve al cliente |
| Longitud de la conversación | De 10 a 28 turnos: 0,0090 a 0,0317 USD por conversación | El costo crece más rápido que el número de turnos |
| Salida y razonamiento | 416 tokens por respuesta; el razonamiento es el 17 % | 18 % del costo; el razonamiento, cerca del 3 % |

**Cómo optimizar cada variable (mirada de AI Engineer):** se cambia una cosa a la vez y se mide costo **y** exactitud. Los ahorros son calculados sobre las 184 llamadas reales; la calidad de las respuestas se prueba en el laboratorio.

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Catálogo innecesario | Mandar solo los registros de las ciudades que le interesan al cliente | Costo total −39 % (de 0,2130 a 0,1296 USD en las 184 llamadas) | **Calculado** | 3.25 y 3.26; herramienta en 3.30 |
| Historial | Ventana de los últimos 5 turnos | −16 % (−8 % con 10 turnos); riesgo: que olvide datos del cliente | **Calculado**; la memoria se prueba con los 14 «¿qué te dije?» | 3.25 y 3.26 |
| Las dos anteriores juntas | Catálogo de interés más ventana de 5 turnos | −55 %: de unos 21 a unos 10 USD por 1.000 conversaciones | **Calculado** | 3.25 y 3.26 |
| Texto redundante | Caché de prompts: se guarda la parte que se repite y se cobra más barata | Potencial: el 97 % de la entrada se repite | **Por verificar** (la tarifa de los modelos 5.5 no está confirmada) | 3.4 en adelante |
| Historial | Resumir lo viejo en pocas líneas en lugar de recortarlo | Conserva los datos del cliente con menos tokens | **Por medir** | 3.25 y 3.26 |
| Salida y razonamiento | Respuestas del tamaño de un chat y esfuerzo (effort) según el tipo de mensaje | Reducir ese 18 % del costo | **Por medir** | 3.5 y 3.32 |

**Tokens ahorrados en dólares (mirada de AI Engineer):** diferencia entre lo medido (184 llamadas: 1.747.598 tokens de entrada, 76.523 de salida, 0,2130 USD) y lo que habría costado con cada optimización. Como las palancas solo recortan la entrada (a 0,10 USD por millón en Haiku 5,5), los tokens ahorrados salen de dividir los dólares ahorrados por esa tarifa.

| Concepto | Tokens de entrada antes | Tokens de entrada después | Tokens ahorrados | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| Catálogo de interés | 1.747.598 | ~913.600 | ~834.000 | 0,0834 (0,2130 → 0,1296) | **Calculado** |
| Ventana de 5 turnos | 1.747.598 | ~1.406.600 | ~341.000 | 0,0341 (16 %) | **Calculado** |
| Las dos juntas | 1.747.598 | ~570.600 | ~1.177.000 | 0,1177 (0,2130 → 0,0953) | **Calculado** |
| Las dos juntas, a 1.000 conversaciones | ~175 millones | ~57 millones | ~118 millones | ~11,8 (de 21,3 a 9,5) | **Estimado** (se asume que las 10 conversaciones son representativas) |

En palabras simples: de los 1,75 millones de tokens que se enviaron, casi 1,2 millones (el 67 %) se podían no enviar, y eso es 0,12 USD de los 0,21 USD gastados.

> **Ejemplo**
> Julián, el cliente que dudaba entre Santa Marta y San Andrés, tuvo la conversación más larga de las que comparaban destinos: 24 turnos. En su último mensaje se enviaron 14.845 tokens, de los cuales 6.478 eran el catálogo completo, aunque Julián solo preguntó por Santa Marta y San Andrés, cuyos registros (por ejemplo `posada-playa-dorada`, `hotel-coral-sereno`, `tayrona-senderismo`) pesan 1.941 tokens: el 30 % del catálogo. Su conversación costó 0,0317 USD.
> Lo mismo con Camilo, que solo pregunta por Medellín: su catálogo útil son 1.069 tokens y la conversación de 10 turnos costó 0,0090 USD.
> Si se mandara a cada cliente solo el catálogo de sus ciudades y se recordaran los últimos 5 turnos, las 10 conversaciones habrían costado 0,0953 USD en lugar de 0,2130 USD, un 55 % menos. A 1.000 conversaciones al mes con Haiku, de unos 21 USD a unos 10 USD.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Primero el catálogo de interés.** Es la palanca más grande y ya está calculada: de 0,2130 a 0,1296 USD en las 184 llamadas (−39 %). Se prueba en 3.25 y 3.26.
> 2. **Ventana de 5 turnos con ficha del cliente.** La ventana corta el historial y una ficha de 3 a 5 líneas (personas, fechas, restricciones) protege los 13 de 14 recuerdos; junto con el catálogo de interés, −55 % (0,0953 USD, **calculado**).
> 3. **Verificar la caché antes de prometerla.** El 96,7 % de lo enviado se repite; confirmar la tarifa de caché de los modelos 5.5 y medirla con 2 o 3 conversaciones reales antes de dar una cifra.
> 4. **Usar las 184 llamadas como línea base fija.** Cada cambio se mide con los mismos 10 clientes y se compara costo **y** exactitud; nunca se acepta un ahorro sin revisar que el asesor siga recordando y citando el catálogo.

#### 3.5 · Parámetros de generación (2026-10-13)

**Qué se hizo:** se probaron los cuatro mandos de la generación sobre el asesor con el catálogo cargado y el mismo mensaje de un cliente: el tope de salida (`max_tokens`), el esfuerzo de razonamiento (`effort`), el mensaje de sistema y la temperatura. Se midieron 8 llamadas por 0,00737 USD.

**A qué nos conduce:** a dos hallazgos que van contra la intuición. Primero, **un tope de salida bajo no ahorra: deja al asesor sin respuesta**, porque el razonamiento se come el tope antes de escribir. Segundo, **pedir respuestas cortas no baja necesariamente el costo**: el asesor escribió menos pero razonó casi tres veces más. Y un tercero confirmado: la temperatura ya no se controla en Claude 5.5 (error 400), así que el comportamiento se gobierna con el catálogo, el mensaje de sistema y el `effort`.

**En el ejercicio:** el asesor responde siempre con los precios del catálogo ($480.000, $1.440.000 y $1.920.000 por 4 noches), sin importar `effort` ni tope. Para el piloto, el tope debe dejarse holgado (2.048 como hoy) y el ahorro buscarse en el contexto, no en estos mandos.

**Qué encareció el proceso:** cada llamada costó cerca de 0,00097 USD, y 0,00066 USD de eso (68 %) fue el catálogo de 6.578 tokens, igual que en 3.4. Lo propio de este tema fueron dos gastos inútiles: las dos llamadas con tope bajo (40 y 150) costaron 0,00141 USD en conjunto y no entregaron ninguna respuesta; y la instrucción de brevedad subió el razonamiento a 697 tokens y el costo en un 12 % (0,00110 contra 0,00098 USD).

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Tope de salida (`max_tokens`) | 40 y 150 → sin respuesta; 2.048 → 634 tokens y respuesta completa | Un tope menor que el razonamiento más la respuesta deja 100 % del gasto sin uso |
| Razonamiento | 222 a 330 tokens de 530 a 709 de salida (35 % a 47 %) en las respuestas completas; 697 de 869 (80 %) con la instrucción de brevedad | Es la parte de la salida que más varía y no se ve en el chat |
| Esfuerzo (`effort`) | low 0,00097; medium 0,00101; high 0,00092 USD (1 muestra por nivel) | Variación de ±5 % en costo sin orden: ruido, no efecto |
| Mensaje de sistema | Con reglas de brevedad: 869 tokens de salida (697 razonando) contra 647 (238) | Texto más corto, costo +12 % |
| Catálogo | 6.578 tokens por llamada, 68 % del costo | Sigue siendo lo que más pesa, por encima de todos estos mandos |
| Temperatura | Error 400 (`temperature is deprecated for this model`) | No es una palanca disponible |

**Cómo optimizar cada variable (mirada de AI Engineer):**

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Tope de salida | Dejarlo holgado (2.048) y no usarlo para ahorrar; si se baja, comprobar que `stop_reason` sea `end_turn` | Evitar la pérdida total de las llamadas cortadas | **Medido** | 3.5 (hecho) y 3.26 |
| Razonamiento + mensaje de sistema | Pedir brevedad **y** `effort` bajo juntos, para que el asesor no razone de más | Salida de unos 350 tokens en vez de 634: −0,00014 USD por llamada (−15 %) | **Estimado** (supone ~230 de razonamiento y ~120 de texto) | 3.25 y 3.32 |
| Esfuerzo | Medir con 10 o más muestras por nivel antes de decidir | Decidir con datos y no con una sola muestra | **Por medir** | 3.32 |
| Catálogo | Mandar solo el de interés (palanca ya calculada en 3.4) | −39 % del costo | **Calculado** | 3.25 y 3.26 |
| Temperatura | Ninguna: no existe; fijar el comportamiento con catálogo y mensaje de sistema | — | **Medido** (error 400) | — |

**Tokens ahorrados en dólares (mirada de AI Engineer):** diferencia entre lo medido y lo que habría costado con la optimización. Referencia medida en esta etapa: una llamada completa de 6.578 tokens de entrada y 634 de salida, 0,00097 USD. El piloto completo gastó 0,2130 USD en 184 llamadas (1.747.598 tokens de entrada y 76.523 de salida).

| Concepto | Tokens antes | Tokens después | Tokens ahorrados | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| Llamadas con tope bajo (40 y 150) | 13.156 de entrada y 190 de salida, sin respuesta | 0 (no se hacen) | 13.346 | 0,00141 (100 % del gasto de esas llamadas) | **Medido** |
| Brevedad con `effort` bajo, por llamada | 634 de salida | ~350 de salida | ~284 de salida | ~0,00014 (−15 %) | **Estimado** |
| Lo anterior en las 184 llamadas del piloto | 76.523 de salida | ~42.500 | ~34.000 | ~0,017 de 0,2130 (−8 %) | **Estimado** (supone la misma proporción en todas) |
| Catálogo de interés (de 3.4) | 1.747.598 de entrada | ~913.600 | ~834.000 | 0,0834 (−39 %) | **Calculado** |

En palabras simples: los mandos de este tema ahorran poco (cerca del 8 % si todo sale como se estima); el ahorro grande sigue estando en no reenviar el catálogo entero, y lo único seguro de esta etapa es no poner topes bajos.

> **Ejemplo**
> Al cliente que pregunta «cuanto vale ir a cartagena 4 noches?» el asesor respondió, con los mismos datos del catálogo en todas las pruebas: `hostal-la-muralla-viva` $480.000, `hotel-brisas-de-bocagrande` $1.440.000 y `casa-naranja-del-centro` $1.920.000 (120.000, 360.000 y 480.000 por noche). Con `max_tokens=150` esa respuesta nunca salió: el asesor gastó los 150 tokens pensando y el cliente se quedó sin respuesta, por 0,00073 USD. Con la regla «máximo 2 frases», la respuesta fue un solo párrafo con los tres precios, pero costó más (0,00110 USD) porque el asesor razonó 697 tokens para resumir.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Tope holgado y alarma en código.** `max_tokens` en 2.048 y una alerta si `stop_reason` es `max_tokens`: las 2 llamadas cortadas tiraron 0,00141 USD sin dar respuesta (**medido**).
> 2. **Brevedad y `effort` bajo juntos.** Pedir respuestas cortas sola subió el razonamiento y el costo 12 %; combinadas podrían bajar la salida a ~350 tokens (−15 %, **estimado**). Se prueba en 3.25 y 3.32.
> 3. **Decidir `effort` con muchas muestras.** Con una muestra por nivel la variación fue ±5 % sin orden (ruido); se necesitan 10 o más por nivel (3.32).
> 4. **Poner el esfuerzo donde está el dinero.** Estos mandos ahorran cerca del 8 % (**estimado**); el contexto (68 % del costo) ahorra el 39 % o más. El orden de trabajo es contexto primero, parámetros después.

#### 3.6 · Panorama de modelos de Anthropic (2026-10-13)

**Qué se hizo:** se consultó a la API qué modelos puede usar la cuenta (14 en total) y se puso a los tres de la familia 5.5, Haiku, Sonnet y Opus, a responder la misma consulta de un cliente con el catálogo cargado. Se midieron tiempo, tokens y costo. Fueron 3 llamadas por 0,0533 USD.

**A qué nos conduce:** a que **elegir modelo es la decisión de costo más grande que hay**, mucho más que `effort` o la longitud de la respuesta. Con los mismos datos del catálogo, los tres dieron el mismo precio correcto, y la diferencia fue de estilo: Sonnet y Opus ofrecieron alternativas y cerraron mejor. Esa mejora de estilo cuesta de 20 a 41 veces más. Con una sola muestra no se concluye la calidad, pero sí que no se justifica pagar más por el precio de una cotización simple.

**En el ejercicio:** el piloto del asesor debería correr en Haiku. Si más adelante un tipo de consulta exige más (un reclamo, una cotización con muchas condiciones), se le puede enviar a un modelo más grande, y eso se decide con la calidad medida en el laboratorio.

**Qué encareció el proceso:** la entrada fue la misma en los tres (6.618 tokens, casi todo catálogo), así que **el precio por token fue lo único que movió el costo**. Haiku cobra 0,10 USD por millón de tokens de entrada, Sonnet 2,00 y Opus 4,00. En los tres, la entrada con el catálogo fue la mayor parte: 77 % del costo en Haiku, 78 % en Sonnet y 74 % en Opus.

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Modelo | 0,00086 USD (Haiku), 0,01691 (Sonnet), 0,03555 (Opus) | Sonnet cuesta 19,7 veces y Opus 41,3 veces lo de Haiku por la misma consulta |
| Tokens de entrada | 6.618 en los tres | Igual para todos; es el catálogo reenviado |
| Tiempo de respuesta | 2,6 s, 4,1 s y 4,7 s | Sonnet y Opus tardan 1,6 y 1,8 veces más, una diferencia pequeña frente al costo |
| Razonamiento | 182, 0 y 110 tokens | No sigue el orden de precio; es parte de la salida y se paga a la tarifa de salida |
| Calidad de la cifra | Los tres: $1.920.000, de `casa-naranja-del-centro` | Idéntica; el modelo más caro no mejora el dato |
| Estilo de la respuesta | Haiku una opción; Sonnet y Opus agregan alternativas | Es lo único que se compra al pagar más |

**Cómo optimizar cada variable (mirada de AI Engineer):**

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Modelo | Haiku por defecto y modelo grande solo para casos que lo exijan (enrutar por tipo de consulta) | Costo del piloto 20 veces menor que con Sonnet | **Calculado** con los precios y los tokens medidos; la calidad, **por medir** | 3.26 y 3.32 |
| Calidad por modelo | Medir con las 10 conversaciones y una rúbrica, no con una sola muestra | Decidir si el estilo de Sonnet u Opus justifica su precio | **Por medir** | 3.26 y 3.32 |
| Tokens de entrada | Filtrar el catálogo por ciudad de interés | Con Haiku −39 %; con un modelo grande el ahorro en dólares sería 20 a 40 veces mayor | **Calculado** | 3.25 y 3.30 |
| Tiempo de respuesta | Medir primer token y tiempos con más muestras | Saber si la diferencia de 2,1 s pesa en WhatsApp | **Por medir** | 3.15 |

**Tokens ahorrados en dólares (mirada de AI Engineer):** el ahorro de elegir modelo no está en tokens, que son los mismos, sino en el precio de cada uno. Comparación entre la consulta medida en cada modelo y el piloto completo (184 llamadas, 1.747.598 tokens de entrada, 76.523 de salida, 0,2130 USD en Haiku).

| Concepto | Tokens | Costo en Sonnet (USD) | Costo en Haiku (USD) | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| Una consulta (6.618 de entrada y ~400 de salida) | Igual en ambos | 0,01691 | 0,00086 | 0,01605 (−95 %) | **Medido** (1 muestra) |
| Una consulta en Opus frente a Haiku | Igual | 0,03555 | 0,00086 | 0,03469 (−98 %) | **Medido** (1 muestra) |
| Las 184 llamadas del piloto, en Sonnet frente a Haiku | 1.747.598 de entrada y 76.523 de salida | ~4,26 | 0,2130 | ~4,05 | **Calculado** (tokens y tarifa medidos; supone el mismo comportamiento) |
| Las 184 llamadas del piloto, en Opus frente a Haiku | Igual | ~8,52 | 0,2130 | ~8,31 | **Calculado** (mismo supuesto) |
| Haiku con catálogo filtrado, frente a Sonnet con catálogo completo | 1.747.598 de entrada a ~570.600 | ~4,26 | ~0,0953 | ~4,16 | **Calculado** |

En palabras simples: en este piloto, quedarse en Haiku ahorra unos 4 USD frente a Sonnet y unos 8 frente a Opus por cada 10 conversaciones, y la cifra que ve el cliente es la misma. Falta confirmar con las 10 conversaciones que Haiku no pierda calidad en los casos difíciles.

> **Ejemplo**
> El cliente dijo: «somos 2, del 10 al 14 de diciembre, queremos ir a cartagena. dame un precio en pesos nomas, aproximado, un hotel bueno en el centro». Los tres modelos recomendaron `casa-naranja-del-centro` (480.000 por noche, 4 noches, $1.920.000) y avisaron que diciembre es temporada alta. Haiku lo hizo por 0,00086 USD. Sonnet agregó `hotel-brisas-de-bocagrande` (desde $360.000) por 0,01691 USD, y Opus sumó también `hostal-la-muralla-viva` (desde $120.000) por 0,03555 USD. A 1.000 conversaciones con unos 18 mensajes cada una, la diferencia entre Haiku y Sonnet sería de cientos de dólares al mes por un cierre de respuesta mejor redactado.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Haiku por defecto.** La misma consulta costó 0,00086 USD en Haiku, 0,01691 en Sonnet y 0,03555 en Opus, con la misma cifra correcta del catálogo (**medido**, 1 muestra).
> 2. **Enrutar por tipo de mensaje.** Un clasificador barato (reglas en código o Haiku) que envíe a Sonnet solo reclamos y cotizaciones con muchas condiciones; medir qué porcentaje de mensajes lo necesita.
> 3. **Calidad con rúbrica antes de fijar el modelo.** Correr las 10 conversaciones en los tres modelos y calificar con criterios fijos (exactitud, cita del registro, tono); la nota de 4 contra 5 fue un juicio con una muestra (3.26 y 3.32).
> 4. **Si se usa un modelo grande, optimizar el contexto primero.** El catálogo de interés ahorra 20 a 40 veces más dólares en Sonnet u Opus que en Haiku (**calculado** con las tarifas).

#### 3.7 · Primer chat con memoria (2026-10-13)

**Qué se hizo:** se construyó el chat con memoria: una lista de mensajes por cliente que se reenvía completa en cada turno, y se probó con tres casos reales del piloto: que el asesor recuerde lo que dijo la cliente (Laura), que no mezcle datos entre clientes (Camilo) y qué pasa si no se recuerda lo que el asesor contestó (experimento de ruptura). Fueron 5 llamadas por 0,00483 USD.

**A qué nos conduce:** a entender que **el asesor no recuerda nada por sí mismo: recuerda lo que nosotros le volvemos a enviar**. Eso explica dos cosas del tema 3.4: por qué cada turno cuesta más que el anterior (se reenvía todo) y por qué cada cliente necesita su propio historial (si no, se mezclan). También mostró que quitar la memoria no ahorra casi nada, porque el peso es el catálogo.

**En el ejercicio:** el paso C.5 queda hecho: cada cliente del piloto tiene su historial separado. En el piloto completo ese historial vive en la tabla `mensajes` de la base única, para que sobreviva si el programa se cierra.

**Qué encareció el proceso:** cada llamada costó entre 0,00082 y 0,00107 USD, y 6.580 a 6.613 tokens de entrada eran el catálogo y el mensaje de sistema. La memoria de Laura sumó solo 389 tokens (5,9 %) en el segundo turno. Lo que más pesó en la salida fue la longitud de la respuesta: la primera respuesta de Laura fue de 789 tokens y otras llegaron a 817, porque el asesor listó todo el catálogo de Cartagena aunque la cliente no lo había pedido.

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Memoria del cliente | 389 tokens en el turno 2 (5,9 % de la entrada) | Pequeña al comienzo; crece con cada turno hasta 12.480 tokens en los turnos 21 a 28 (3.4) |
| Catálogo | 6.580 tokens por llamada, constante | Es el 94 % de la entrada en el turno 2 |
| Longitud de la respuesta | 256 a 817 tokens de salida; las respuestas largas listan todo el catálogo de la ciudad | Hasta 0,00107 USD por llamada contra 0,00083 la corta |
| Guardar o no la respuesta del asesor | Sin guardarla, la entrada del turno 2 fue 6.613 contra 6.988 tokens | Ahorra 375 tokens (5 %), pero el asesor pierde el hilo |
| Separación por cliente | Camilo no recibió datos de Laura | Sin separación se mezclarían los datos de los clientes |
| Duración de la conversación | Estimado: con ~250 tokens de crecimiento por turno, 500 turnos costarían ~3,5 USD solo en entrada | El costo total crece con el cuadrado del número de turnos |

**Cómo optimizar cada variable (mirada de AI Engineer):**

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Memoria del cliente | Ventana de los últimos 5 turnos y resumen de lo viejo, guardando el historial completo en la base | −16 % en el piloto (3.4); conversaciones largas mucho menos costosas | **Calculado** (ventana); resumen **por medir** | 3.9, 3.25 y 3.26 |
| Longitud de la respuesta | Reglas de prompt que pidan una sola opción y preguntar antes de listar (3.8) | Salidas más cortas, aunque en 3.5 la brevedad sola subió el razonamiento | **Por medir** | 3.8 y 3.32 |
| Guardar la respuesta | Siempre guardarla; es 5 % de ahorro a cambio de perder el hilo | No es una optimización válida | **Medido** | — |
| Separación por cliente | Una lista (y una fila de la tabla `mensajes`) por cliente | Evitar mezclar datos | **Medido** | 3.10 (pruebas) |
| Duración de la conversación | Ventana más resumen para que el costo crezca de forma lineal, no cuadrática | ~0,4 USD en vez de ~3,5 USD por 500 turnos | **Estimado** | 3.25 y 3.26 |

**Tokens ahorrados en dólares (mirada de AI Engineer):** diferencia entre lo medido y lo que habría costado con la optimización. La demo mide el turno 2 de Laura (6.988 tokens de entrada); el resto usa la línea base del piloto (184 llamadas, 1.747.598 tokens de entrada, 0,2130 USD).

| Concepto | Tokens antes | Tokens después | Tokens ahorrados | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| No guardar la respuesta (turno 2) | 6.988 de entrada | 6.613 | 375 | 0,00004 (y el asesor pierde el hilo) | **Medido**; no es una optimización válida |
| Ventana de 5 turnos en el piloto | 1.747.598 de entrada | ~1.406.600 | ~341.000 | 0,0341 (−16 %) | **Calculado** (de 3.4) |
| Ventana más catálogo de interés | 1.747.598 de entrada | ~570.600 | ~1.177.000 | 0,1177 (−55 %) | **Calculado** (de 3.4) |
| Conversación de 500 turnos: ventana de 5 turnos frente a historial completo | ~34,5 millones de entrada | ~3,9 millones | ~30,6 millones | ~3,06 de ~3,45 | **Estimado** (supone crecimiento lineal de 250 tokens por turno) |

En palabras simples: en conversaciones cortas la memoria casi no se nota, pero en las largas se vuelve lo más caro después del catálogo. La ventana la mantiene a raya sin tocar lo que el asesor sabe del cliente, si el historial completo queda guardado aparte.

> **Ejemplo**
> Laura escribió «nos casamos el 14 de febrero y queremos viajar esa semana a cartagena. cuanto vale?». El asesor respondió con los precios del catálogo: `hostal-la-muralla-viva` desde $120.000, `hotel-brisas-de-bocagrande` desde $360.000 y `casa-naranja-del-centro` desde $480.000 por noche. Al preguntar en el turno siguiente qué fecha y qué precio le había dado, el asesor repitió «14 de febrero» y los mismos tres precios, por 0,00083 USD. Camilo, con su propia lista vacía, preguntó por la misma boda y el asesor respondió que no tenía esa información. Sin guardar sus respuestas, Laura recibió «no veo un precio anterior en esta conversación».

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Historial completo en la base, ventana en la llamada.** Guardar todo en la tabla `mensajes` y enviar solo los últimos 5 turnos: el costo de una conversación larga pasa de crecer con el cuadrado a crecer de forma lineal (~0,4 contra ~3,5 USD en 500 turnos, **estimado**). Se construye en 3.9.
> 2. **Nunca quitar la respuesta del asesor para ahorrar.** Ahorra solo 375 tokens (5 %) y el asesor pierde el hilo (**medido**).
> 3. **Memoria separada por cliente, con prueba automática.** Una lista por teléfono o id y una prueba que confirme que Camilo nunca ve los datos de Laura (3.10).
> 4. **Resumir lo viejo cuando la conversación crece.** Pasar los turnos antiguos a una ficha corta y medir con los 14 «¿qué te dije?» que no se pierda ningún dato (3.25 y 3.26).

#### 3.8 · Limitaciones de los LLM (2026-10-13)

**Qué se hizo:** se tomaron 8 mensajes-trampa de los clientes del piloto (un hotel que no existe, un descuento no publicado, el clima, una dieta, un destino ausente, una alergia grave, una garantía y la temporada alta) y se compararon dos respuestas del asesor con la misma conversación previa: la que ya había dado sin reglas y la nueva con cinco reglas escritas en el prompt. Fueron 8 llamadas nuevas por 0,00850 USD.

**A qué nos conduce:** a un hallazgo que corrige una suposición. Con el catálogo cargado, **el asesor no inventó en ninguna de las 8 trampas, ni con reglas ni sin ellas**: reconoce que algo no está publicado y lo pasa a un asesor humano. Las reglas no hicieron falta para evitar el invento grueso; sirvieron para pulir (respuestas más cortas y enfocadas, menos consejos sueltos). Eso cambia dónde poner el esfuerzo: el riesgo que queda son las afirmaciones pequeñas fuera del catálogo (como «Medellín suele ser templada»), y esas se cazan con pruebas, no con más reglas.

**En el ejercicio:** el paso D.1 queda hecho y el piloto ya tiene su primera medición de seguridad: 0 de 8 trampas inventadas. La versión de las reglas queda en `caso_simulado.py` (`construir_system(con_reglas=True)`) para usarla en el chat final (3.9) y volver a medir en las pruebas (3.10) y el informe (3.11).

**Qué encareció el proceso:** cada llamada de prueba llevó en promedio 9.497 tokens de entrada: unos 6.500 del catálogo, unos 2.700 del historial de ese cliente y 213 de las reglas. La salida fue pequeña (226 tokens por respuesta con reglas, 293 sin ellas). Es decir, probar una trampa en el turno 13 o 16 cuesta más que en el turno 3, porque se reenvía toda la conversación anterior.

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Reglas del prompt | 213 tokens por llamada, constantes | +0,00002 USD por llamada de entrada |
| Longitud de la respuesta | 1.806 tokens de salida con reglas contra 2.340 sin ellas en las 8 trampas (−23 %) | Ahorra 534 tokens de salida (−0,00027 USD) |
| Costo total de las 8 llamadas | 0,00850 con reglas contra 0,00860 sin ellas | −1,2 %: la ganancia en salida casi se compensa con el costo de las reglas |
| Historial de cada cliente | 7.977 a 11.186 tokens de entrada, según el turno de la trampa | Mientras más tarde la trampa, más cara la prueba |
| Catálogo | Cerca de 6.500 tokens por llamada | Sigue siendo la mayor parte de la entrada |
| Invento de datos | 0 de 8 trampas, con y sin reglas | El riesgo grueso no apareció; quedan deslices menores (2 sin reglas, 1 con reglas) |

**Cómo optimizar cada variable (mirada de AI Engineer):**

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Reglas del prompt | Mantenerlas cortas; probar cada una por separado para quedarse con las que cambian algo | Menos de 213 tokens sin perder las ventajas | **Por medir** | 3.26 y 3.32 |
| Costo de las reglas | Caché de prompts: las reglas y el catálogo son la parte fija que se repite en cada llamada | Potencial sobre ~6.700 tokens fijos | **Por verificar** (tarifa de caché no confirmada) | Después de 3.9 |
| Longitud de la respuesta | Mantener «una opción principal» y «responde corto» | −23 % de salida en estas 8 trampas | **Medido** (8 casos, 1 muestra) | 3.26 y 3.32 |
| Deslices menores | Prueba automática que busque afirmaciones fuera del catálogo (clima, vida nocturna, consejos médicos) | Detectarlos sin leer las 184 respuestas a mano | **Por medir** | 3.10 y 3.11 |
| Precios y totales | Que los calcule el código y no el modelo | Elimina el error aritmético y el precio inventado | **Por medir** | 3.30 |

**Tokens ahorrados en dólares (mirada de AI Engineer):** diferencia entre las 8 respuestas sin reglas (medidas en 3.4: 74.272 tokens de entrada y 2.340 de salida, 0,00860 USD) y las mismas con reglas (75.976 de entrada y 1.806 de salida, 0,00850 USD).

| Concepto | Tokens antes | Tokens después | Tokens ahorrados | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| Salida con reglas, 8 trampas | 2.340 | 1.806 | 534 | 0,00027 | **Medido** |
| Entrada por las reglas, 8 trampas | 74.272 | 75.976 | −1.704 (más tokens) | −0,00017 | **Medido** |
| Neto de las 8 trampas | 76.612 | 77.782 | −1.170 en total, pero los de salida valen 5 veces más | 0,00010 (−1,2 %) | **Medido** |
| Neto extendido a las 184 llamadas del piloto | 1.747.598 de entrada y 76.523 de salida | ~1.786.800 y ~59.060 | −39.192 de entrada y +17.460 de salida | ~0,0048 de 0,2130 (−2,3 %) | **Estimado** (supone la misma proporción en todas las llamadas) |
| Catálogo de interés (de 3.4) | 1.747.598 de entrada | ~913.600 | ~834.000 | 0,0834 (−39 %) | **Calculado** |

En palabras simples: las reglas pagan su propio costo y dejan una ganancia mínima de dinero, así que **no se justifican por ahorro sino por control**: respuestas más cortas, enfocadas y con menos deslices. El ahorro grande sigue en el catálogo filtrado.

> **Ejemplo**
> Valentina, que no come carne, preguntó si el almuerzo de los tours tiene opción vegetariana. El catálogo no publica nada de comidas (`tayrona-senderismo` y `minca-y-cascadas` no traen ese dato). Sin reglas, el asesor dijo «no tengo información publicada sobre el almuerzo» y envió a un asesor humano; con reglas, dijo lo mismo y sugirió llevar un snack. Con la Familia Ortiz, cuya hermana es alérgica al maní, ninguna versión prometió nada y las dos pasaron el caso a un asesor humano; la versión sin reglas, además, recomendó llevar adrenalina autoinyectable, un consejo médico que el catálogo no respalda, y la versión con reglas lo reemplazó por «consulte al médico de su hermana». Y en el caso de Sofía, sobre temporada alta, la respuesta con reglas bajó de 269 a 169 tokens de salida diciendo lo mismo.

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Reestructurar el prompt y cerrar el hueco de los deslices.** Bloques fijos `<rol>`, `<reglas>`, `<ejemplos>` y `<catalogo>`; una regla nueva: «no agregues conocimiento general (clima, salud, vida nocturna) aunque sea cierto»; y una frase fija para lo que no está («eso no lo tengo publicado; te lo confirma un asesor»). Meta: 0 deslices en las 8 trampas (hoy 1 con reglas y 2 sin ellas). Se prueba en 3.26 y 3.32.
> 2. **Validar cada respuesta en código.** Revisar que cada precio y cada nombre de hotel o tour existan en el catálogo y marcar palabras de riesgo (clima, adrenalina, garantía, descuento, %): 0 tokens y detección automática de deslices sin leer a mano (3.10 y 3.11).
> 3. **Empaquetar el contexto en vez de enviar todo.** Catálogo de interés, ventana de 5 turnos y ficha del cliente: −55 % del costo (**calculado**, 3.4). Para 37 registros no hace falta un RAG con vectores: un filtro por ciudad es más barato y exacto; el RAG con vectores conviene cuando el catálogo crezca o se busque por descripción.
> 4. **Caché para la parte fija.** Reglas y catálogo (~6.700 tokens) se repiten en cada llamada; con el prompt ordenado (lo fijo primero) la caché los cobra más barato. Ahorro **por verificar** hasta confirmar la tarifa de los modelos 5.5.

#### 3.9 · Ensamblar el chat final (2026-10-13)

**Qué se hizo:** se juntó todo lo aprendido en un solo programa, `chat.py`: el asesor con el catálogo y las reglas, en Haiku, con streaming, memoria por cliente guardada en la base y ventana de 5 turnos. Con él se atendió a los 10 clientes del piloto (los mismos 184 mensajes del 3.4) y se les hizo una pregunta de cierre para ver si el asesor seguía recordando su dato clave. Fueron 205 llamadas en total por 0,1875 USD (incluye la prueba en consola y la comparación con el historial completo).

**A qué nos conduce:** a la primera decisión real de AI Engineer con datos propios: **la ventana ahorra, pero hace olvidar**. El costo bajó 23,4 % y la entrada dejó de crecer (la llamada más grande pasó de 14.845 a 8.165 tokens), pero el asesor solo recordó el dato clave de 6 de los 10 clientes, contra 10 de 10 con la memoria completa. Ningún ahorro se acepta sin medir lo que se pierde, y aquí se perdió algo importante: que Valentina no come carne o que los niños Ramírez tienen 4, 7 y 11 años.

**En el ejercicio:** el paso D.2 queda hecho y el asesor ya funciona como programa completo: cualquier cliente se puede retomar donde quedó. Antes de usarlo con clientes de verdad hay que resolver la memoria con una ficha del cliente; las pruebas automáticas del 3.10 deben vigilar justamente que no se pierdan esos datos.

**Qué encareció el proceso:** con el historial recortado, **el catálogo pasó a ser casi todo el gasto**. De los 7.575 tokens de entrada promedio por llamada, 6.478 son el catálogo (85,5 %). Repartido sobre el costo de los 184 mensajes (0,1631 USD):

| Parte | Tokens (184 llamadas) | Costo (USD) | % del costo |
|---|---|---|---|
| Catálogo completo, reenviado en cada mensaje | ~1.192.000 | ~0,1192 | ~73 % |
| Respuestas del asesor (incluye 9.795 de razonamiento) | 47.473 | 0,0237 | ~15 % |
| Ventana de la conversación, mensaje nuevo e instrucciones | ~163.000 | ~0,0163 | ~10 % |
| Reglas contra inventar | ~39.000 | ~0,0039 | ~2 % |

Además, medir la memoria tuvo su costo: la pregunta de cierre con historial completo pesó 12.275 tokens por llamada, contra 7.567 con la ventana (cifras **calculadas** con los tokens medidos de las 184 llamadas; el reparto entre catálogo y ventana es aproximado).

**Variables que afectaron el proceso (mirada de AI Engineer):**

| Variable | Dato | Efecto |
|---|---|---|
| Ventana de 5 turnos | Entrada máxima de 14.845 a 8.165 tokens; entrada total −20,2 % | Ahorra y deja el costo por llamada estable |
| Memoria con la ventana | Dato clave recordado: 6 de 10 clientes, contra 10 de 10 con el historial completo | Pierde edades, fechas, dieta y presupuesto dichos al principio |
| Catálogo completo | 6.478 de 7.575 tokens de entrada por llamada (85,5 %) | ~73 % del costo: ahora es casi todo el gasto |
| Reglas y `effort` bajo | Salida −38 %; razonamiento de 25.101 a 9.795 tokens (−61 %) | Respuestas más cortas y menos razonamiento sin perder exactitud en las trampas |
| Reglas contra inventar | 213 tokens por llamada (~39.000 en el piloto) | ~2 % del costo; 0 de 8 trampas inventadas |
| Longitud de la conversación | Costo por cliente de 0,0081 (Camilo, 10 turnos) a 0,0236 USD (Sofía, 28 turnos) | Con la ventana crece casi en línea recta con los turnos |

**Cómo optimizar cada variable (mirada de AI Engineer):**

| Variable | Cómo optimizarla | Resultado esperado | Estado del dato | Dónde se prueba |
|---|---|---|---|---|
| Memoria con la ventana | Ficha del cliente: 3 a 5 líneas con personas, fechas, presupuesto y restricciones, que viaja siempre fuera de la ventana | Volver a 10 de 10 recuerdos por unos 80 tokens más por llamada | **Estimado** | 3.25 y 3.26 |
| Catálogo completo | Mandar solo los registros de las ciudades del cliente | ~−4.500 tokens por llamada; costo del chat final de 0,1631 a ~0,080 USD | **Estimado** (con el promedio de 1.953 tokens medido en 3.4) | 3.25, 3.26 y 3.30 |
| Parte fija repetida (catálogo y reglas) | Caché de prompts | Potencial sobre el ~75 % de la entrada | **Por verificar** (tarifa de los modelos 5.5) | Después de 3.10 |
| Tamaño de la ventana | Probar 5, 8 y 10 turnos con la misma pregunta de cierre | Encontrar el punto donde no se olvida sin pagar el historial completo | **Por medir** | 3.25 y 3.26 |
| Medición de la memoria | Convertir la pregunta de cierre en prueba automática (patrón del dato clave por cliente) | Detectar olvidos sin leer respuestas a mano | **Medido** (ya funciona en este tema) | 3.10 |

**Tokens ahorrados en dólares (mirada de AI Engineer):** diferencia entre la línea base medida (184 llamadas: 1.747.598 tokens de entrada, 76.523 de salida, 0,2130 USD) y el chat final, más lo que se ahorraría con la siguiente optimización.

| Concepto | Tokens antes | Tokens después | Tokens ahorrados | USD ahorrados | Estado del dato |
|---|---|---|---|---|---|
| Entrada, chat final contra línea base | 1.747.598 | 1.393.846 | 353.752 | 0,0354 | **Medido** |
| Salida, chat final contra línea base | 76.523 | 47.473 | 29.050 | 0,0145 | **Medido** |
| Total del chat final | 1.824.121 | 1.441.319 | 382.802 | 0,0499 (−23,4 %: de 0,2130 a 0,1631) | **Medido** |
| Más catálogo de interés sobre el chat final | 1.393.846 de entrada | ~561.000 | ~833.000 | ~0,083 (de 0,1631 a ~0,080; −62 % frente a la línea base) | **Estimado** |
| Más ficha del cliente (costo, no ahorro) | — | +~14.700 de entrada | −14.700 | −0,0015 | **Estimado** |
| A 1.000 conversaciones al mes | ~182 millones | ~144 millones con el chat final; ~61 millones con catálogo de interés | ~38 a ~121 millones | ~5 a ~13 USD (de ~21,3 a ~16,3 o ~8,0) | **Estimado** (supone que las 10 conversaciones son representativas) |

En palabras simples: el chat final ya ahorra una cuarta parte, y filtrando el catálogo ahorraría casi dos tercios. Pero el ahorro de la ventana tiene un precio en memoria, y recuperarlo con una ficha del cliente cuesta casi nada (unos 0,0015 USD en todo el piloto).

> **Ejemplo**
> Valentina dijo al comienzo «no como carne, soy vegetariana». Veinte turnos después, al preguntarle qué datos tenía de su viaje, el asesor con la ventana de 5 turnos respondió: «Restricción de comida o alergia: no me has dicho cuál es» y corrigió una suposición suya («yo dije que ibas sola, pero tú no lo mencionaste»). No inventó, pero olvidó lo más importante para recomendarle un tour. Con el historial completo, el mismo asesor sí lo recordó. En cambio, a Andrés, que pidió un descuento para 6 personas, el chat final le respondió bien: no hay descuentos publicados, y por el `ecohostal-selva-tayrona` (máximo 3 huéspedes, desde $190.000) serían 2 cabañas, «$380.000 por noche».

> **CONCLUSIONES**
> _Desde el punto de vista de un AI Engineer: cuatro consejos enfocados en solución, basados en los datos de este análisis y ordenados por prioridad._
> 1. **Agregar la ficha del cliente antes de cualquier otro ahorro.** La ventana olvidó el dato clave en 4 de 10 clientes (Ramírez, Camilo, Valentina y Julián). Una ficha de 3 a 5 líneas (personas, fechas, presupuesto y restricciones como dieta, alergia o movilidad) que viaje siempre fuera de la ventana debería volver a 10 de 10 por unos 80 tokens por llamada (~0,0015 USD en el piloto, **estimado**). Se mide con la misma pregunta de cierre en 3.25 y 3.26.
> 2. **Filtrar el catálogo: ahora es el 73 % del costo.** Con la ventana, el catálogo completo quedó como casi todo el gasto (6.478 de 7.575 tokens por llamada). Mandar solo las ciudades del cliente bajaría el chat final de 0,1631 a ~0,080 USD (**estimado**), −62 % frente a la línea base. Se prueba en 3.25, 3.26 y como herramienta en 3.30.
> 3. **Convertir la pregunta de cierre en prueba automática.** El patrón del dato clave por cliente ya detecta olvidos sin leer a mano (6 de 10 contra 10 de 10). Llevarlo a las pruebas del 3.10, junto con las 8 trampas, para que ningún cambio de ventana, catálogo o prompt se acepte si baja la memoria o aparece un invento.
> 4. **Elegir el tamaño de la ventana con datos.** Probar 5, 8 y 10 turnos, con y sin ficha, midiendo costo y recuerdos en las mismas 10 conversaciones; quedarse con la combinación más barata que mantenga 10 de 10. La caché de la parte fija (catálogo y reglas, ~75 % de la entrada) se suma después, cuando se verifique su tarifa.

