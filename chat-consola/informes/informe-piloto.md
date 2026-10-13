# Informe del piloto · Nivel 1 · 2026-10-13

Caso: asesor de «Turismo Colombia (simulada)» con catálogo, 10 clientes ficticios, 184 mensajes por configuración. Generado por `etapas/e10_informe_piloto.py` sin llamar a Claude, a partir de la base del piloto.

## 1. Tokens y costo: línea base (3.4) contra chat final (3.9)

| Medida | Línea base (3.4) | Chat final (3.9) | Cambio |
|---|---|---|---|
| Llamadas | 184 | 184 | +0,0 % |
| Tokens de entrada | 1.747.598 | 1.393.846 | -20,2 % |
| Tokens de salida | 76.523 | 47.473 | -38,0 % |
| Tokens de razonamiento | 25.101 | 9.795 | -61,0 % |
| Costo (USD) | 0,2130 | 0,1631 | -23,4 % |

## 2. Por cliente

| Cliente | Turnos | Costo base (USD) | Costo final (USD) | Entrada máx. base | Entrada máx. final | Dato clave con ventana | Dato clave con historial completo | Trampa | Montos sin explicar | Montos revisados |
|---|---|---|---|---|---|---|---|---|---|---|
| Laura (pareja) | 14 | 0,0150 | 0,0126 | 10.812 | 8.049 | sí | sí | No inventó | 0 | 0 |
| Familia Ramírez | 18 | 0,0222 | 0,0165 | 12.808 | 8.126 | **NO** | sí | — | 0 | 0 |
| Andrés (grupo) | 16 | 0,0204 | 0,0149 | 11.716 | 8.101 | sí | sí | No inventó | 0 | 0 |
| Doña Marta | 14 | 0,0172 | 0,0134 | 11.719 | 8.130 | sí | sí | — | 0 | 0 |
| Camilo | 10 | 0,0090 | 0,0081 | 8.568 | 7.439 | **NO** | sí | No inventó | 0 | 0 |
| Valentina | 20 | 0,0221 | 0,0175 | 11.840 | 8.147 | **NO** | sí | No inventó | 0 | 0 |
| Pareja Torres | 22 | 0,0261 | 0,0187 | 12.803 | 7.732 | sí | sí | — | 0 | 4 |
| Julián | 24 | 0,0317 | 0,0225 | 14.845 | 8.165 | **NO** | sí | No inventó | 0 | 4 |
| Familia Ortiz | 18 | 0,0192 | 0,0153 | 11.358 | 7.903 | sí | sí | No inventó | 0 | 0 |
| Sofía | 28 | 0,0301 | 0,0236 | 12.129 | 7.906 | sí | sí | No inventó | 0 | 0 |

## 3. Alucinaciones

- **Precios:** 0 montos sin explicar y 8 sumas revisadas a mano y correctas, en 194 respuestas del chat final.
- **Trampas del catálogo** (hotel inexistente, descuento, clima, dieta, destino ausente, alergia, temporada alta): 0 de 8 inventadas, con y sin reglas (juicio de Claude, temas 3.8 y 3.9).
- **Memoria:** el chat final recordó el dato clave de 6 de 10 clientes con la ventana de 5 turnos y de 10 de 10 con el historial completo.
- **Límite:** el recuento de precios es automático; el veredicto de las trampas es un juicio, no una medición.

## 4. Gasto del piloto en la base

388 llamadas registradas en `ejecuciones`, 0.3997 USD en total (las tres configuraciones). Las pruebas sueltas de los temas 3.5 a 3.8 se midieron en sus scripts y no están en esta cuenta.

## 5. Checklist de cierre del nivel (guía, apartado 10.1)

| Punto | Estado | Evidencia |
|---|---|---|
| Explico qué es un LLM y cómo predice tokens | Hecho | Temas 3.2 y 3.3 (notas y análisis) |
| Sé calcular el costo de una conversación y por qué crece con la memoria | Hecho | Tema 3.4: 184 llamadas medidas |
| Sé qué controlan max_tokens, effort y system, y qué no (temperatura) | Hecho | Tema 3.5 |
| Elegí modelo con datos | Hecho | Tema 3.6: Haiku (0,00086 contra 0,01691 y 0,03555 USD) |
| Entiendo que la memoria es una lista que se reenvía | Hecho | Tema 3.7 |
| Completé el análisis de limitaciones | Hecho | Tema 3.8 e `informes/limitaciones-resultados.md` |
| El chat final recuerda entre sesiones, recorta, muestra costos y sobrevive a errores | Hecho, con una brecha | chat.py: memoria en la base y ventana; olvida el dato clave de 4 de 10 clientes (ficha del cliente pendiente) |
| pytest -q pasa | Hecho | 13 passed y 1 xfailed (falla esperada documentada) |
| `.env` nunca llegó a Git | Hecho | Archivo rastreado: no; clave en el historial: no |
| Hay un commit por etapa | Hecho | 11 commits «etapa N» en el historial |
