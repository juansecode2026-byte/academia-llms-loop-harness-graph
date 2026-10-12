<!-- Fuente de verdad. Editar este .md y correr: python scripts/md_a_html.py (regenera el HTML). -->
---
doc: transferencia-crm
titulo: Transferencia a candyCRM
fecha: 2026-10-12
gemelo: resultados-proceso-manual.html | ← Ir al documento manual
lead: Cómo lo que se construye en la Academia LLMs puede usarse en el CRM de ventas (candyCRM), para que el tiempo de estudio también avance el producto. Basado en la revisión del repositorio del CRM del 2026-10-12, sin modificarlo.
---

# Transferencia a <em>candyCRM</em>

## 1. Resumen

candyCRM ya usa un LLM en un solo lugar: el **Router**, que lee cada mensaje entrante y decide a qué embudo va el lead. Usa Claude Haiku 4.5 con salida estructurada, solo cuando las reglas fijas no alcanzan. Todo lo demás que tiene que ver con IA está pendiente: el panel Copiloto se ve vacío porque el **Agente Analista** no existe, y los siete agentes del plan (Catálogo, SDR, Soporte, Agendador, Enriquecedor, Analista, Recuperación) están aplazados en su `docs/DECISIONES.md`.

El Nivel 1 de la Academia enseña justo lo que esos agentes necesitan: medir costo y calidad, defenderse de las alucinaciones, probar sin gastar tokens y, en las Partes 3 y 4, construir un agente con límites y medir si funciona.

**La recomendación principal:** que el «proceso real» que la Parte 3 automatiza sea un proceso de candyCRM. Así, cada hora de estudio de las Partes 2 a 4 produce, además del aprendizaje, una pieza que el CRM ya tiene planeada.

## 2. Qué se encontró en el CRM

| Pieza | Estado | Qué tiene que ver con la Academia |
|---|---|---|
| Router de clasificación (`supabase/functions/router/`) | Funciona | Llama a Haiku con `fetch`, `max_tokens` 512 y umbral de confianza 0.6 |
| Tabla `router_decisions` | Funciona | Guarda capa, confianza, señales y tipo sugerido de cada decisión; no guarda tokens ni costo |
| Umbral de confianza 0.6 | Fijado sin datos | El propio código dice que se calibrará «con datos reales más adelante» |
| Panel Copiloto (score, sentimiento, resumen, sugerencia) | Vacío | Depende del Agente Analista [7b], aplazado |
| Agentes conversacionales [6a]–[6d] | Aplazados | Necesitan memoria de conversación y defensas contra alucinaciones |
| Agente de Recuperación [7c] | Aplazado | Es el único con loop: necesita condición de salida, manejo de errores y control de gasto |
| Panel de hoy | Funciona | Ya tiene indicadores de «autonomía de la IA» (`deal_events` distingue bot y humano) |
| Pruebas del Router | No hay | Cada cambio se prueba contra la API real |

## 3. Qué se lleva de cada parte de la guía

| Lo que se aprende en la Academia | Dónde sirve en candyCRM | Qué se gana |
|---|---|---|
| 3.4 Tokens y costos · 3.6 Panorama de modelos | Router | Saber cuánto cuesta clasificar cada lead y si conviene cambiar de modelo (hoy usa Haiku 4.5; la guía trabaja con la familia 5.5) |
| 3.8 Limitaciones de los LLM | Agentes [6a]–[6c], antes de que le hablen a un cliente | Una batería de pruebas para que el bot no invente precios, cupos ni políticas |
| 3.7 y 3.9 Memoria y chat final | Agentes [6a]–[6d] | El patrón de historial reenviado, recorte y manejo de errores (límite de uso, sin conexión) |
| 3.10 Pruebas sin gastar tokens | Router y futuros agentes | El patrón de cliente falso: probar la lógica de clasificación sin llamar a la API |
| Parte 2 · Laboratorio (motor, registro, batería, juez) | Router | Medir aciertos del Router con mensajes reales etiquetados, por modelo y umbral |
| 3.26 Tablero de decisiones | Router | Un `decisiones.json` con el umbral y el modelo recomendados, decididos con datos |
| Parte 3 · Loop, graph y harness | Agente de Recuperación [7c] y Analista [7b] | Loop con límites, presupuesto de tokens, aprobación humana y trazas |
| Parte 4 · Tablero agéntico | Panel de hoy | Indicadores para saber si el agente mejora o empeora frente a la línea base |

## 4. Propuesta de orden

1. **Ahora, mientras se hace la Parte 1:** solo aprender. Nada se lleva todavía, pero conviene leer el Router con los ojos de cada etapa (dónde están los tokens, el umbral, el manejo de errores).
2. **Parte 2 · Laboratorio:** usar como batería de preguntas (3.17) mensajes reales del tenant Hellominus, anonimizados, con el embudo correcto anotado a mano. El laboratorio mide al Router de verdad, no un ejemplo inventado.
3. **3.26 Tablero de decisiones:** sale con datos el umbral y el modelo del Router. Es el primer cambio concreto que viaja al CRM.
4. **Parte 3 · Agente:** elegir como proceso real el **Agente Analista [7b]**, que llena el panel Copiloto. No tiene loop ni dependencias externas, y su resultado se ve en pantalla. El Agente de Recuperación [7c] queda como segundo caso, cuando exista `payment_links`.
5. **Parte 4 · Tablero agéntico:** reutilizar los indicadores de autonomía de la IA que ya tiene el Panel de hoy, en vez de inventar otros.

## 5. Cuidados

- **Lenguaje distinto.** La Academia trabaja en Python; las funciones del CRM son TypeScript sobre Deno (Edge Functions de Supabase). Los conceptos se llevan tal cual; el código se reescribe al pasar. El prototipo se hace aquí y se porta allá.
- **Datos de clientes.** candyCRM es multi-tenant. Para la batería del laboratorio solo se usan mensajes del tenant Hellominus, anonimizados, nunca de otros tenants.
- **Reglas del laboratorio.** Nada de esto se construye en el CRM sobre la marcha. Cada idea entra como candidato en `docs/DECISIONES.md` del CRM (allá vive en `docs/`, no en la raíz) y la decisión es tuya y de tu socio.
- **Reglas del CRM.** Cualquier tabla nueva (por ejemplo, para guardar tokens y costo del Router) va como migración nueva, con RLS y FK compuestas, como exige su `CLAUDE.md`.

## 6. Checklist de transferencia

- [ ] Decidir si la Parte 3 de la Academia usa el Agente Analista [7b] de candyCRM como proceso real
- [ ] Registrar en `docs/DECISIONES.md` del CRM el candidato «Medir tokens y costo de cada decisión del Router»
- [ ] Armar la batería del laboratorio con mensajes reales del tenant Hellominus, anonimizados y etiquetados
- [ ] Medir el Router en el laboratorio: aciertos por modelo y por umbral
- [ ] Llevar al CRM el umbral y el modelo que recomiende el tablero de decisiones
- [ ] Llevar al Router el patrón de pruebas con cliente falso
- [ ] Llevar la batería de limitaciones (3.8) como prueba obligatoria antes de activar cualquier agente que hable con clientes

## 7. Bitácora de cambios

| Fecha | Cambio |
|---|---|
| 2026-10-12 | Creación del documento a partir de la revisión del repositorio de candyCRM (rama `juanse-candycrm-ventas`). |
