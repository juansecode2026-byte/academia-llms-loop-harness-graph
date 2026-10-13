<!-- Fuente de verdad. Editar este .md y correr: python scripts/md_a_html.py "Documentación para la construcción del proyecto/ejercicio-simulado-chat-consola.md" -->
---
doc: ejercicio-simulado
titulo: Ejercicio simulado · Chat de consola
fecha: 2026-10-12
gemelo: ../resultados/resultados-proceso-manual.html | Ir al checklist del proceso manual →
lead: El caso práctico sobre el que se construye el chat de consola del Nivel 1: un asesor de viajes que atiende por WhatsApp a clientes simulados, con datos ficticios tratados como reales. Este documento explica el ejercicio y su paso a paso; **el avance se marca en el checklist del proceso manual**, al que enlaza cada paso.
---

# Ejercicio simulado: <em>chat de consola</em>

## 1. En qué consiste el ejercicio

Se construye el chat de consola de la guía v7, pero en lugar de conversar sobre temas sueltos, el chat atiende un **caso de negocio simulado**: una agencia de viajes ficticia, **«Turismo Colombia (simulada)»**, que recibe por WhatsApp mensajes de clientes que quieren viajar.

El objetivo no cambia: **cumplir el checklist de LLMs del Nivel 1**. El caso solo da un escenario realista donde cada concepto (tokens, memoria, parámetros, alucinaciones, costos) se ve con datos que se parecen a los de un negocio de verdad.

| Pregunta | Respuesta |
|---|---|
| ¿Qué se construye? | Un chatbot de consola que actúa como asesor de viajes |
| ¿Con qué datos? | Ficticios, pero tratados como reales: un catálogo de destinos, hospedajes y tours, y 10 clientes con sus conversaciones |
| ¿Por qué un caso simulado? | Para medir diferencias reales (tokens, costo, memoria, alucinaciones) sin depender de clientes ni de la API de WhatsApp |
| ¿Por qué viajes? | La memoria importa (el cliente cuenta de a poco fechas, personas, presupuesto) y el catálogo existe en candyCRM, así que lo aprendido se puede llevar allá |
| ¿Es el piloto? | Sí: 10 clientes. Si funciona, se amplía a 30 |

> **Datos ficticios**
> Ningún cliente, número de teléfono ni empresa es real. Los archivos y carpetas del caso llevan «simulado» en el nombre. Se tratan como reales solo en su forma: mensajes cortos e informales, varios seguidos, clientes que vuelven otro día.

## 2. Cómo funciona

El mismo recorrido que hace un mensaje de WhatsApp en un CRM, pero sin la API de WhatsApp: un **simulador** entrega los mensajes.

1. **El simulador entrega un mensaje** de un cliente ficticio, por ejemplo «hola buenas, cuanto vale ir a cartagena 4 noches?», con su número, nombre y hora.
2. **El chat busca la memoria de ese cliente**: todo lo que habló antes, guardado en la base de datos del piloto. Si el cliente vuelve al día siguiente, su historial sigue ahí.
3. **El chat arma la petición a Claude**: el mensaje de sistema (quién es el asesor, sus reglas y el catálogo) más el historial del cliente (completo o recortado, según la configuración) más el mensaje nuevo.
4. **Claude responde**, y la respuesta vuelve al cliente simulado.
5. **Se guarda todo**: el mensaje, la respuesta y la medición de esa llamada (modelo, tokens de entrada, salida y razonamiento, costo, tiempo y motivo de parada).
6. **El simulador entrega el siguiente mensaje**, del mismo cliente o de otro.

| Pieza | Qué es | Llama a Claude |
|---|---|---|
| Simulador de clientes | Script que entrega los mensajes guion de cada cliente, en orden, como si llegaran por WhatsApp | No |
| Chat de consola (el asesor) | El programa de la guía, adaptado al caso | Sí |
| Catálogo | Archivo JSON con destinos, hospedajes y tours | No |
| Base del piloto | SQLite: clientes, mensajes y ejecuciones | No |

## 3. Qué hace el chatbot

#### Lo que sí hace

- Recomienda destinos, hospedajes y tours **solo del catálogo**.
- Recuerda lo que cada cliente fue diciendo: cuántos viajan, fechas, presupuesto, si hay niños, alergias o movilidad reducida.
- Atiende a varios clientes, cada uno con su propia conversación y su propia memoria.
- Calcula un estimado con los precios «desde» del catálogo.
- Responde en el tono de WhatsApp: corto, cordial y claro.

#### Lo que no hace, y debe decir que no sabe

- No inventa precios, cupos, fechas disponibles ni hoteles que no están en el catálogo.
- No confirma reservas ni cobra: dice que un asesor humano lo confirma.
- No responde sobre el clima de «esta semana» ni noticias: avisa que su información tiene fecha de corte.

## 4. Los datos del piloto

#### El catálogo ficticio

Tiene la misma forma que el catálogo de turismo de candyCRM (nombre, región, precio desde, capacidad, duración), para que después se pueda llevar allá.

**Ya está creado** (2026-10-13), antes del tema 3.3: `chat-consola/datos-simulados/catalogo-turismo-simulado.json`, con 10 destinos, 15 alojamientos y 12 tours, con precio «desde» en pesos (COP), capacidad, duración, dificultad y si es apto para movilidad reducida. Los lugares son reales; los alojamientos, tours y precios son inventados.

**A propósito no publica** disponibilidad ni cupos, tarifas de temporada alta, descuentos, información sobre alergias y dietas, clima ni precios de vuelos. Son justo las cosas que piden los clientes con trampa, y el asesor debe decir que no las sabe en vez de inventarlas.

**Pesa unos 7.900 tokens** (6.500 si se guarda en formato compacto). Como va dentro del mensaje de sistema, esos tokens se reenvían en cada llamada: es lo que más pesa en el costo del asesor.

| Tipo | Cantidad | Ejemplo de lo que tendría |
|---|---|---|
| Destinos | 10 | Cartagena, Eje Cafetero, San Andrés, Medellín, Santa Marta, Villa de Leyva |
| Hospedajes | 15 | Hotel, hostal o finca, con precio desde, huéspedes máximos y destino |
| Tours | 12 | Duración, horario, dificultad, mínimo y máximo de personas y precio desde |

#### Los 10 clientes ficticios

Cada uno tiene un perfil y algo que el chat debe recordar más adelante. Algunos incluyen una trampa: piden algo que no está en el catálogo, para medir si el chat inventa.

| # | Cliente (ficticio) | Perfil | Dato que debe recordar | Trampa |
|---|---|---|---|---|
| 1 | Laura (pareja) | Luna de miel, presupuesto alto | Fecha de la boda | Pide un hotel que no existe |
| 2 | Familia Ramírez | 2 adultos y 3 niños | Edades de los niños | — |
| 3 | Andrés (grupo) | 6 amigos, presupuesto ajustado | Número de personas | Pide un descuento que no está |
| 4 | Doña Marta | Adulta mayor, viaja con su hija | Movilidad reducida | — |
| 5 | Camilo | Viaje de trabajo a Medellín | Fechas exactas | Pregunta por el clima de esta semana |
| 6 | Valentina | Viajera sola, aventura | Que no come carne | — |
| 7 | Pareja Torres | Aniversario, vuelve al día siguiente | Lo que eligió el día anterior | — |
| 8 | Julián | Duda entre dos destinos | Los dos destinos y su presupuesto | Pide un tour de un destino que no está |
| 9 | Familia Ortiz | Con alergia al maní | La alergia | — |
| 10 | Sofía | Compara precios, muy breve | Lo que ya se le cotizó | Pide precio de temporada alta no publicado |

Las conversaciones van de 10 a 40 turnos, con mensajes tipo WhatsApp («hola buenas», «cuanto vale», «ah y somos 5», «oiga y lo de ayer?»). Los números de teléfono siguen un patrón claramente falso (`+57 300 000 00XX`).

#### La base de datos del piloto

SQLite, un archivo dentro del proyecto.

> **Decisión: una sola base, y nace antes que el laboratorio**
> La base se crea en el tema 3.7 (paso C.3), porque el chat con memoria ya la necesita: guarda el historial de cada cliente y cada llamada a Claude. La guía construye su «registro de experimentos» recién en el tema 3.16, pero ahí **no se crea otra base**: se amplía la misma con las columnas y tablas que pide la guía (configuración del experimento y calificación de cada respuesta). Así no hay dos bases distintas ni datos duplicados, y las llamadas del chat desde el primer día quedan medidas con el mismo formato que usará el laboratorio.

| Tabla | Qué guarda |
|---|---|
| clientes | Los 10 perfiles ficticios |
| mensajes | El historial de cada cliente: es la memoria del chat |
| ejecuciones | Cada llamada a Claude: configuración, tokens de entrada, salida y razonamiento, costo, tiempo y motivo de parada |

## 5. Qué se mide

#### Lo que se puede variar

| Variable | Valores del piloto | Qué cambia |
|---|---|---|
| Modelo | Haiku 5.5 y Sonnet 5.5 | Calidad, velocidad y costo |
| Effort | low y high | Cuánto razona antes de responder |
| Ventana de memoria | Todo el historial, 10 turnos, 5 turnos | Cuántos tokens se reenvían en cada mensaje |
| `max_tokens` | Fijo en el piloto | El tope de la respuesta |
| Mensaje de sistema | Con defensas contra alucinaciones | Si inventa o admite que no sabe |

> **La temperatura no se mide**
> Los modelos Claude 5.5 rechazan el parámetro de temperatura (la guía lo muestra en la etapa de parámetros, con un error 400). Por eso no está entre las variables. Se confirma en el tema 3.5.

#### Lo que se mide en cada llamada

Tokens de entrada, salida y razonamiento; costo en dólares; tiempo de respuesta; motivo de parada; y, en la batería, si la respuesta fue correcta, admitió no saber o inventó.

#### El tamaño del piloto (estimado)

2 modelos × 2 niveles de effort × 3 ventanas = **12 configuraciones**. 10 clientes × 12 configuraciones = **120 corridas**, unas 2.400 llamadas. Con Haiku, el costo estimado es menor de 1 USD; Sonnet se corre solo en una muestra. El saldo de la cuenta hoy es de 1,04 USD, así que conviene recargar antes de la Parte 2.

## 6. Fase A · La base (se rehace con el caso)

Los temas 3.2 a 3.4 ya se hicieron con ejemplos sueltos de la guía. Se **vuelven a hacer** usando el caso de viajes. El tema 3.1 (entorno, bibliotecas y clave) no depende del caso y queda como está.

**El catálogo (paso C.1) se adelantó:** ya existe antes del tema 3.3, porque los temas 3.4 a 3.6 dependen de él (pesa tokens, se usa para probar parámetros y para comparar modelos). El tema 3.2 se hizo sin catálogo a propósito: es la línea base del asesor sin defensas.

| Paso | Qué se hace | Checklist |
|---|---|---|
| A.1 | Entorno, bibliotecas y clave (ya hecho, no cambia) | [3.1 Preparación](../resultados/resultados-proceso-manual.html#s3-1) |
| A.2 | Primera llamada con un mensaje de cliente del caso («hola buenas, cuanto vale ir a cartagena 4 noches?») **sin catálogo**, para ver cómo el modelo inventa precios | [3.2 Primera llamada a la API](../resultados/resultados-proceso-manual.html#s3-2) |
| A.3 | Respuesta por pedazos y razonamiento con ese mismo mensaje, ahora **con el catálogo cargado**; comparar con la línea base del tema 3.2 | [3.3 Ver cómo el modelo predice tokens](../resultados/resultados-proceso-manual.html#s3-3) |
| A.4 | Medir cuánto pesa el catálogo en tokens y cuánto cuesta cargarlo en cada llamada; contar tokens de mensajes tipo WhatsApp y simular la memoria con una conversación del caso, catálogo incluido | [3.4 Tokens, ventana de contexto y costos](../resultados/resultados-proceso-manual.html#s3-4) |
## 7. Fase B · Parámetros y modelos con el caso

Se siguen los temas de la guía y, donde encaja, se prueban con una pregunta del caso de viajes.

| Paso | Qué se hace | Checklist |
|---|---|---|
| B.1 | Probar `max_tokens`, effort, mensaje de sistema y temperatura; confirmar qué se puede variar | [3.5 Parámetros de generación](../resultados/resultados-proceso-manual.html#s3-5) |
| B.2 | Comparar Haiku, Sonnet y Opus con una pregunta de un cliente del caso | [3.6 Panorama de modelos de Anthropic](../resultados/resultados-proceso-manual.html#s3-6) |

## 8. Fase C · Datos simulados y memoria por cliente

Se crea el escenario y el chat empieza a atender a los clientes con memoria propia.

| Paso | Qué se hace | Checklist |
|---|---|---|
| C.1 | Crear el catálogo ficticio (JSON). **Adelantado: ya está creado**, antes del tema 3.3 | [3.7 Primer chat con memoria](../resultados/resultados-proceso-manual.html#s3-7) |
| C.2 | Crear los 10 clientes y sus guiones tipo WhatsApp | [3.7](../resultados/resultados-proceso-manual.html#s3-7) |
| C.3 | Crear la base SQLite del piloto: es la base única, que el tema 3.16 más adelante amplía | [3.7](../resultados/resultados-proceso-manual.html#s3-7) |
| C.4 | Construir el simulador que entrega los mensajes | [3.7](../resultados/resultados-proceso-manual.html#s3-7) |
| C.5 | Chat con memoria por cliente: cada cliente con su historial | [3.7](../resultados/resultados-proceso-manual.html#s3-7) |

## 9. Fase D · Limitaciones, chat final y pruebas

| Paso | Qué se hace | Checklist |
|---|---|---|
| D.1 | Correr las trampas del catálogo y medir si el chat inventa | [3.8 Limitaciones de los LLM](../resultados/resultados-proceso-manual.html#s3-8) |
| D.2 | Chat final: los 10 clientes atendidos, con recorte de memoria y cada llamada guardada en ejecuciones | [3.9 Ensamblar el chat final](../resultados/resultados-proceso-manual.html#s3-9) |
| D.3 | Pruebas sin gastar tokens del simulador y de la memoria por cliente | [3.10 Pruebas automáticas](../resultados/resultados-proceso-manual.html#s3-10) |
| D.4 | Informe del piloto: tokens, costo y alucinaciones por cliente | [3.11 Cierre del nivel](../resultados/resultados-proceso-manual.html#s3-11) |

## 10. Fase E · El laboratorio sobre el caso (Parte 2)

Se construye el laboratorio de la guía completo, con su dashboard (Streamlit), y se corre sobre el caso. Nada de esta fase se aplaza.

| Paso | Qué se hace | Checklist |
|---|---|---|
| E.1 | Definir qué se va a medir del asesor de viajes y con qué objetivo | [3.12 Qué vas a construir (laboratorio)](../resultados/resultados-proceso-manual.html#s3-12) |
| E.2 | Fijar los controles (modelo, effort, ventana de memoria, mensaje de sistema) y las mediciones sobre el caso | [3.13 Qué controlamos y qué medimos](../resultados/resultados-proceso-manual.html#s3-13) |
| E.3 | Preparar la estructura del laboratorio: carpetas y dependencias, incluido Streamlit | [3.14 Preparación del laboratorio](../resultados/resultados-proceso-manual.html#s3-14) |
| E.4 | Construir el motor de medición: una llamada medida con la configuración del caso | [3.15 Motor de medición](../resultados/resultados-proceso-manual.html#s3-15) |
| E.5 | Ampliar la base única del piloto (creada en C.3) con el registro de experimentos de la guía, sin crear otra | [3.16 Registro de experimentos (SQLite)](../resultados/resultados-proceso-manual.html#s3-16) |
| E.6 | Armar la batería de preguntas con trampas y el modelo juez desde el caso | [3.17 Batería de preguntas y modelo juez](../resultados/resultados-proceso-manual.html#s3-17) |
| E.7 | Estructura del dashboard del laboratorio | [3.18 Estructura de la app](../resultados/resultados-proceso-manual.html#s3-18) |
| E.8 | Controles: modelo, effort, memoria y mensaje de sistema del caso | [3.19 Controles](../resultados/resultados-proceso-manual.html#s3-19) |
| E.9 | Vista Playground: probar una conversación del caso con cualquier configuración | [3.20 Vista Playground](../resultados/resultados-proceso-manual.html#s3-20) |
| E.10 | Vista Comparador: la misma pregunta de un cliente con varias configuraciones lado a lado | [3.21 Vista Comparador](../resultados/resultados-proceso-manual.html#s3-21) |
| E.11 | Vista Batería de alucinaciones: correr las trampas y calificar si inventó | [3.22 Vista Batería de alucinaciones](../resultados/resultados-proceso-manual.html#s3-22) |
| E.12 | Vista Métricas: tokens, costo y alucinaciones por configuración | [3.23 Vista Métricas](../resultados/resultados-proceso-manual.html#s3-23) |
| E.13 | Pruebas sin gastar tokens del motor, el registro, la batería y el dashboard | [3.24 Pruebas del laboratorio](../resultados/resultados-proceso-manual.html#s3-24) |
| E.14 | Correr la grilla del piloto: 10 clientes × 12 configuraciones | [3.25 Experimentos y cierre](../resultados/resultados-proceso-manual.html#s3-25) |
| E.15 | Decidir modelo, effort y ventana con los datos, en el tablero de decisiones | [3.26 Tablero de decisiones](../resultados/resultados-proceso-manual.html#s3-26) |
## 11. Fase F · El agente sobre el caso (Partes 3 y 4)

Con las decisiones de la Fase E, el asesor de viajes se convierte en un agente con herramientas, un ciclo (loop), un grafo y un harness con límites. Es donde se prueban y comparan las diferencias entre estas piezas. La Parte 4 construye el tablero que mide al agente.

| Paso | Qué se hace | Checklist |
|---|---|---|
| F.1 | Definir qué hará el agente asesor y qué quedará siempre en manos de un humano | [3.27 Qué vas a construir (agente)](../resultados/resultados-proceso-manual.html#s3-27) |
| F.2 | Aplicar al caso los conceptos de harness, loop y graph | [3.28 Conceptos: harness, loop y graph](../resultados/resultados-proceso-manual.html#s3-28) |
| F.3 | Medir la línea base (lo que hace un asesor humano) y fijar los casos de prueba con los 10 clientes | [3.29 Proceso, línea base y casos de prueba](../resultados/resultados-proceso-manual.html#s3-29) |
| F.4 | Herramientas: buscar en el catálogo, estimar un precio, escalar a un humano | [3.30 Herramientas](../resultados/resultados-proceso-manual.html#s3-30) |
| F.5 | Loop: el agente consulta el catálogo cuantas veces haga falta, con límite de vueltas | [3.31 Loop](../resultados/resultados-proceso-manual.html#s3-31) |
| F.6 | Graph: clasificar, consultar, responder y verificar, enrutando por modelo según el costo | [3.32 Graph](../resultados/resultados-proceso-manual.html#s3-32) |
| F.7 | Harness: tope de gasto por conversación y aprobación humana antes de dar un precio final | [3.33 Harness](../resultados/resultados-proceso-manual.html#s3-33) |
| F.8 | Trazas: cada paso del agente guardado en la base única | [3.34 Trazas](../resultados/resultados-proceso-manual.html#s3-34) |
| F.9 | Evaluar las variantes (sin loop, con loop, con graph, con harness) sobre los casos y comparar | [3.35 Evaluación y optimización](../resultados/resultados-proceso-manual.html#s3-35) |
| F.10 | Pruebas sin gastar tokens y cierre | [3.36 Pruebas y cierre](../resultados/resultados-proceso-manual.html#s3-36) |
| F.11 | Definir qué indicadores del agente se ven y qué decisión habilita cada uno | [3.37 Qué vas a construir (tablero agéntico)](../resultados/resultados-proceso-manual.html#s3-37) |
| F.12 | Encabezado del tablero: qué agente, qué variante y qué periodo | [3.38 Encabezado](../resultados/resultados-proceso-manual.html#s3-38) |
| F.13 | Calcular los indicadores: éxito, costo por tarea, información inventada, escalado | [3.39 Indicadores](../resultados/resultados-proceso-manual.html#s3-39) |
| F.14 | Vistas: resumen, variantes, grafo, ejecuciones y decisiones | [3.40 Vistas](../resultados/resultados-proceso-manual.html#s3-40) |
| F.15 | Reglas de decisión y ciclo de mejora del agente | [3.41 Reglas de decisión · ciclo de mejora](../resultados/resultados-proceso-manual.html#s3-41) |
| F.16 | Construir el tablero con las bibliotecas de la guía | [3.42 Bibliotecas y construcción](../resultados/resultados-proceso-manual.html#s3-42) |
| F.17 | Pruebas sin gastar tokens del tablero y cierre | [3.43 Pruebas y cierre](../resultados/resultados-proceso-manual.html#s3-43) |
## 12. Lo que queda para después

| Qué | Por qué no va ahora | Cuándo |
|---|---|---|
| La infraestructura de WhatsApp (webhook de Meta, ventana de 24 h, plantillas) | Es infraestructura, no concepto de LLMs | Al llevarlo a candyCRM |
| Supabase y multi-tenant | SQLite alcanza para el piloto local | Al llevarlo a candyCRM |
| Cliente simulado por Claude (un segundo modelo que hace de cliente) | Llama a Claude, así que cuenta como agente | Partes 2 o 3 |
| Ampliar a 30 clientes | Primero validar el proceso con 10 | Después del piloto |

## 13. Cómo se estandariza

Lo que queda como estándar para otros proyectos no es el caso de viajes, sino el **proceso**: el simulador de clientes, la forma de la base (clientes, mensajes, ejecuciones), el formato de la batería de casos con trampas, las métricas y el checklist. Para otro proyecto se cambia el catálogo y los clientes: una inmobiliaria, una constructora o un call center.

## 14. Bitácora de cambios

| Fecha | Cambio |
|---|---|
| 2026-10-12 | Creación del documento: caso, funcionamiento, datos del piloto (10 clientes), variables, fases y enlaces al checklist. |
| 2026-10-13 | Decisión: la base SQLite nace en 3.7 (C.3) y es la única; el tema 3.16 la amplía con el registro de experimentos (paso E.5) en vez de crear otra. |
| 2026-10-13 | Se reinicia el checklist sobre el ejercicio: la Fase A se rehace con el caso, la Fase E cubre todo el laboratorio sin dashboard (pasos E.1 a E.9, antes E.0 a E.3), nueva Fase F para las Partes 3 y 4, y se aplazan los dashboards. |
| 2026-10-13 | Se revierte el aplazamiento de los dashboards: la Fase E vuelve a cubrir toda la Parte 2 (pasos E.1 a E.15) y la Fase F toda la Parte 3 y 4 (F.1 a F.17). |
| 2026-10-13 | Las Partes 3 y 4 se siguen dentro del checklist del manual (temas 3.27 a 3.43); los pasos F.1 a F.17 enlazan allí. |
| 2026-10-13 | Se adelanta la creación del catálogo ficticio (paso C.1): ya existe en `chat-consola/datos-simulados/`; los pasos A.3 y A.4 pasan a usarlo. |
