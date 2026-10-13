# Radiografía del contexto (tema 3.4)

Modelo `claude-haiku-5-5`. 10 conversaciones simuladas, 184 llamadas reales a la API, con el catálogo completo y todo el historial.

Costo real de las 184 llamadas: **0.2130 USD**; 0.0213 USD por conversación; 0.00116 USD por llamada.

## 1. De qué está hecha cada llamada (promedio)

| Parte | Tokens | % de la entrada |
|---|---|---|
| Instrucciones del asesor | 67 | 0.7 % |
| Catálogo completo | 6,478 | 68.2 % |
| Historial de la conversación | 2,936 | 30.9 % |
| Mensaje nuevo del cliente | 17 | 0.2 % |
| **Entrada total** | **9,498** | 100 % |

Salida promedio: 416 tokens por respuesta, de los cuales 17 % es razonamiento.

## 2. Texto redundante

En promedio, el **96.7 %** de lo que se envía en un turno ya se había enviado en la llamada anterior (mínimo 90.7 %, máximo 99.3 %). La conversación solo agrega la respuesta anterior y el mensaje nuevo.

## 3. Catálogo innecesario

El catálogo completo pesa 6,478 tokens. Con solo los registros de las ciudades por las que pregunta cada cliente pesaría, en promedio, **1,953 tokens** (30 % del completo; entre 1,069 y 2,615). Es decir, en promedio **70 % del catálogo es innecesario** para lo que el cliente preguntó.

| Cliente | Ciudades de interés | Catálogo que sirve (tokens) | % del completo |
|---|---|---|---|
| Laura (pareja) | cartagena, san-andres | 2,115 | 33 % |
| Familia Ramírez | eje-cafetero, guatape, medellin | 2,415 | 37 % |
| Andrés (grupo) | santa-marta, san-andres | 1,941 | 30 % |
| Doña Marta | cartagena, medellin, bogota | 2,563 | 40 % |
| Camilo | medellin | 1,069 | 17 % |
| Valentina | santa-marta, eje-cafetero, barichara | 2,615 | 40 % |
| Pareja Torres | villa-de-leyva, barichara | 1,393 | 22 % |
| Julián | santa-marta, san-andres | 1,941 | 30 % |
| Familia Ortiz | guatape, medellin, bogota | 2,016 | 31 % |
| Sofía | cartagena | 1,465 | 23 % |

## 4. Cómo crece la entrada turno a turno

| Turnos | Llamadas | Entrada (tokens) | Salida (tokens) | Costo por llamada (USD) |
|---|---|---|---|---|
| 1 | 10 | 6,565 | 302 | 0.00081 |
| 2 a 5 | 40 | 7,419 | 749 | 0.00112 |
| 6 a 10 | 50 | 8,956 | 385 | 0.00109 |
| 11 a 20 | 70 | 10,895 | 303 | 0.00124 |
| 21 a 28 | 14 | 12,480 | 222 | 0.00136 |

## 5. Costo por conversación

| Cliente | Turnos | Entrada del último turno | Costo (USD) |
|---|---|---|---|
| Laura (pareja) | 14 | 10,812 | 0.0150 |
| Familia Ramírez | 18 | 12,808 | 0.0222 |
| Andrés (grupo) | 16 | 11,716 | 0.0204 |
| Doña Marta | 14 | 11,719 | 0.0172 |
| Camilo | 10 | 8,568 | 0.0090 |
| Valentina | 20 | 11,840 | 0.0221 |
| Pareja Torres | 22 | 12,803 | 0.0261 |
| Julián | 24 | 14,845 | 0.0317 |
| Familia Ortiz | 18 | 11,358 | 0.0192 |
| Sofía | 28 | 12,129 | 0.0301 |

## 6. Palancas (calculadas sobre las conversaciones reales)

Se mantiene la salida observada. **No se mide si la calidad de las respuestas cambia**: eso se prueba en el laboratorio.

| Configuración | Entrada total (tokens) | Costo de las 184 llamadas (USD) | Ahorro | Por conversación (USD) | 1.000 conversaciones al mes (USD) |
|---|---|---|---|---|---|
| Punto de partida: todo el historial y el catálogo completo (real) | 1,747,598 | 0.2130 | 0 % | 0.0213 | 21 |
| Ventana de 10 turnos | 1,585,472 | 0.1968 | 8 % | 0.0197 | 20 |
| Ventana de 5 turnos | 1,404,836 | 0.1787 | 16 % | 0.0179 | 18 |
| Solo el catálogo de las ciudades que le interesan al cliente | 913,192 | 0.1296 | 39 % | 0.0130 | 13 |
| Catálogo de interés + ventana de 5 turnos | 570,430 | 0.0953 | 55 % | 0.0095 | 10 |

## 7. Calidad del modelo de cálculo

Para calcular las palancas se reconstruye la entrada de cada llamada sumando los tokens de cada mensaje, más 2.0 tokens de formato por mensaje. Comparado con la entrada real de las 184 llamadas, el error promedio es de **0.00 %** (máximo 0.00 %).
