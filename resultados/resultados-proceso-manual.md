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
- [x] Ejercicio C.1: crear el catálogo ficticio (JSON); adelantado, ya está creado en `chat-consola/datos-simulados/` ([ver paso C.1](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.2: crear los 10 clientes ficticios y sus guiones tipo WhatsApp; adelantado en el tema 3.4, ya está creado ([ver paso C.2](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.3: crear la base SQLite del piloto (clientes, mensajes, ejecuciones); es la base única, el tema 3.16 la amplía; adelantado en el tema 3.4, ya está creado ([ver paso C.3](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
- [x] Ejercicio C.4: construir el simulador que entrega los mensajes; adelantado en el tema 3.4, ya está creado ([ver paso C.4](../Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html#s8))
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
| Memoria (historial) | La conversación anterior, que se reenvía en cada mensaje | 2.936 tokens por llamada en promedio; la entrada va de 6.565 (turno 1) a 12.480 (turnos 21 a 28) (3.4) | Ventana de 5 turnos (−16 %); resumen de lo viejo | Medido; ahorro calculado; resumen por medir | 3.25 |
| Texto redundante | Lo que se envía igual que en la llamada anterior | 96,7 % de la entrada (3.4) | Caché de prompts | Medido; tarifa por verificar | 3.4 en adelante |
| Longitud de la conversación | Cuántos turnos dura | De 0,0090 USD (10 turnos) a 0,0317 USD (24 turnos) por conversación (3.4) | Ventana, resumen, filtrar catálogo | Medido | 3.25 |
| Razonamiento | Lo que el modelo piensa antes de responder | 39 % de la salida en el primer mensaje largo (3.3); 17 % en las conversaciones (3.4), cerca del 3 % del costo | Esfuerzo (effort) según el tipo de mensaje | Medido | 3.5, 3.32 |
| Longitud de la respuesta | Lo que el asesor escribe al cliente | 416 tokens de salida por respuesta en promedio, 18 % del costo (3.4) | Respuestas de chat; tope de `max_tokens` | Medido | 3.5 |
| Modelo | Haiku, Sonnet u Opus | Sonnet cuesta unas 20 veces más que Haiku por token | Elegir el modelo según la tarea | Calculado con los precios | 3.6 |
| Formato de los datos | Cómo se escribe el catálogo | Compacto: 18 % menos tokens (7.923 a 6.469) | Ya aplicado | Medido | — |
| Idioma | Español frente a inglés | El español usa cerca de 1,5 veces más tokens (21 contra 14 en la misma frase) | Instrucciones internas en inglés, respuestas en español | Medido en frases; por medir en el sistema | 3.4 en adelante |
| Fuente de los datos | Si un precio sale del catálogo o lo inventa el modelo | Con catálogo, 3 de 3 respuestas con la misma cifra verificable: $1.920.000 de `casa-naranja-del-centro` (3.2); 13 de 14 recuerdos correctos con el historial completo (3.4) | Datos del catálogo y cálculos en código | Medido | 3.8, 3.30 |
| Tiempo hasta el primer token | Cuánto tarda el asesor en empezar a responder | Sin medir | «Escribiendo…» y mensajes cortos | Por medir | 3.15 |

#### Lo que vamos logrando

#### 2 · Base del proyecto (2026-10-12)

**Qué se hizo:** se escribió el objetivo del proyecto, se creó el repositorio privado en GitHub, se configuró Git y se separó la documentación de los resultados.

**A qué nos conduce:** ya hay un lugar ordenado donde cada avance queda guardado y fechado. Desde ahora, todo lo que se construya deja rastro, y ese rastro es el portafolio.

**En el ejercicio:** el repositorio es donde viven el catálogo ficticio, los 10 clientes, el simulador y la base de datos del piloto, junto con cada commit del asesor de viajes. Si mañana el caso se lleva a otro proyecto, este historial muestra cómo se construyó.


> **Ejemplo**
> Funciona como la historia clínica de un paciente. Si dentro de seis meses alguien de un cliente de Minus pregunta «¿desde cuándo saben conectar sistemas a Claude?», no hace falta decir «hace un tiempo»: se abre GitHub y se ve el commit «etapa 1: primera llamada a la API», con fecha, código y resultado.

#### 3.1 · Preparación (2026-10-12)

**Qué se hizo:** se creó un entorno de Python aislado para el proyecto (así sus bibliotecas no se mezclan con las de otros), se instaló el SDK de Anthropic, que es el programa que permite hablar con Claude desde código, y se guardó la clave de acceso en un archivo `.env` que Git no sube. La clave es exclusiva de este proyecto y vence sola.

**A qué nos conduce:** es el piso sobre el que se apoya todo lo demás. Sin entorno aislado, los proyectos se estorban entre sí; sin la clave protegida, un descuido la publicaría y alguien podría gastar tu dinero. Con esto listo, el siguiente paso es el primero emocionante: hacer que un programa nuestro le haga una pregunta a Claude y reciba la respuesta.

**En el ejercicio:** es el mismo entorno desde el que corre el asesor de viajes. La clave solo se gasta con clientes simulados, y como es exclusiva de este proyecto, el gasto del ejercicio se ve aparte del resto.


> **Ejemplo**
> El entorno virtual es como tener una caja de herramientas aparte para cada obra. Si el CRM necesita una versión de la biblioteca `anthropic` y esta Academia otra, cada uno usa la suya y ninguno rompe al otro.
> La clave en `.env` es como la llave de la casa guardada en un cajón, no pegada en la puerta: el programa la usa, pero no queda a la vista. Cuando hoy la clave quedó escrita en `.env.example` (la plantilla que sí se sube a GitHub), fue como dejarla pegada en la puerta; por eso se cambió la cerradura: se revocó y se creó otra.

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


