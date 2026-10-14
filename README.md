# Academia LLMs · Loop, Harness, Graph

Portafolio de AI Engineering: construir con la API de Anthropic un asesor de viajes con catálogo y memoria, y **medir cada decisión con datos**. Los clientes, el catálogo y las conversaciones son **simulados** («Turismo Colombia (simulada)», piloto de 10 clientes).

Lo aprendido se lleva después a proyectos reales (candyCRM y los proyectos de Minus). Cada avance es un commit: el commit es la prueba.

## Tres hallazgos

1. **El modelo más barato bastó para consultar precios.** La misma consulta costó 0,00086 USD con Haiku, 0,01691 con Sonnet y 0,03555 con Opus, con la misma cifra correcta del catálogo ($1.920.000 por 4 noches). Cambia el estilo de la respuesta, no el dato (una muestra por modelo).
2. **Ahorrar tiene un precio que solo se ve midiendo.** Recortar la memoria a 5 turnos, con reglas y esfuerzo bajo, bajó el costo de las 184 conversaciones un 23,4 % (de 0,2130 a 0,1631 USD), pero el asesor olvidó el dato clave de 4 de 10 clientes. El promedio lo escondía; el informe por cliente lo mostró. La solución propuesta (una ficha del cliente) está escrita y tiene su prueba esperando.
3. **Con el catálogo cargado, el asesor no inventó en 8 trampas** (un hotel inexistente, un descuento, el clima, una dieta, un destino ausente, una alergia y la temporada alta). Es una muestra pequeña y una respuesta por trampa, y así está dicho en los resultados.

## Dónde ver la evidencia

| Qué | Enlace |
|---|---|
| Resultados del proceso, tema por tema, con cifras y análisis | [Ver como página](https://juansecode2026-byte.github.io/academia-llms-loop-harness-graph/resultados/resultados-proceso-manual.html) · [Fuente en Markdown](resultados/resultados-proceso-manual.md) |
| El ejercicio simulado (el caso, las fases y los pasos) | [Ver como página](https://juansecode2026-byte.github.io/academia-llms-loop-harness-graph/Documentaci%C3%B3n%20para%20la%20construcci%C3%B3n%20del%20proyecto/ejercicio-simulado-chat-consola.html) |
| Informe del piloto: tokens, costo y memoria por cliente | [informe-piloto.md](chat-consola/informes/informe-piloto.md) |
| Las 8 trampas, con y sin reglas | [limitaciones-resultados.md](chat-consola/informes/limitaciones-resultados.md) |
| Código del asesor | [chat-consola/chat.py](chat-consola/chat.py) y [chat-consola/etapas/](chat-consola/etapas/) |
| Pruebas sin gastar tokens | [chat-consola/test_chat.py](chat-consola/test_chat.py) |

## Qué se construyó (Nivel 1, Parte 1)

Un chat de consola con memoria por cliente guardada en SQLite, ventana de turnos, reglas contra inventar, streaming, costo por llamada y un informe del piloto. Cada tema del checklist (3.1 a 3.11) tiene su commit, sus cifras medidas y su análisis. Las cifras se marcan como **medidas**, **calculadas** o **estimadas**, y lo que falta se llama **por medir**.

## Cómo probarlo

```
cd chat-consola
python -m venv .venv
.venv\Scripts\activate        # en macOS o Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q                     # no gasta tokens ni necesita clave
```

Para conversar con el asesor hace falta una clave de la API de Anthropic propia: copia `.env.example` a `.env`, escribe tu clave en `ANTHROPIC_API_KEY` y ejecuta `python chat.py`. El archivo `.env` está ignorado por Git y la clave nunca se sube. Cada llamada cuesta fracciones de centavo.

## Qué no demuestra todavía

Uso de **herramientas** (tool use), **RAG con vectores**, **fine-tuning**, modelos de otros proveedores y **datos reales**. Eso corresponde a los niveles siguientes y a su aplicación en candyCRM. Tampoco se ha construido aún el laboratorio de parámetros (Parte 2), que agregará una app para comparar configuraciones.

## Cómo está organizado

| Carpeta | Contenido |
|---|---|
| `resultados/` | Los documentos de seguimiento (el `.md` es la fuente; el `.html` se regenera con un script) |
| `chat-consola/` | El asesor: código, datos simulados, pruebas e informes |
| `Documentación para la construcción del proyecto/` | El pensum, la guía v7 y el ejercicio simulado |
| `scripts/` | Generadores de HTML y el hook que mantiene el análisis |
