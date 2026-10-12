# Pensum AI Engineer · v1.1 · 2026-10-09

Ruta de estudio para las habilidades más pedidas en ofertas de AI Engineer: 10 habilidades de IA y 6 lenguajes de programación, cada una en 4 niveles con temas, herramientas y un proyecto que demuestra el nivel.

### 01. Python (74.4 % de las vacantes)

El lenguaje base de toda la IA: datos, modelos, APIs y automatización.

#### Nivel 1 · Fundamentos · 4–6 semanas

1. Sintaxis, variables y tipos de datos
2. Control de flujo: if, for, while
3. Funciones, argumentos y alcance
4. Estructuras: listas, diccionarios, tuplas, sets
5. Lectura y escritura de archivos (txt, CSV, JSON)
6. Manejo de errores con try/except
7. Entornos virtuales e instalación de paquetes

Herramientas: VS Code, uv / venv, pip, Jupyter

Proyecto: Script que lee un CSV de ventas y genera un resumen en consola y en JSON.

#### Nivel 2 · Intermedio · 6–8 semanas

1. Programación orientada a objetos (clases, herencia, dataclasses)
2. Módulos y paquetes propios
3. Comprehensions, generadores e iteradores
4. Decoradores y context managers
5. Type hints y mypy
6. pandas y NumPy para análisis de datos
7. Consumo de APIs con requests / httpx
8. Testing con pytest y control de versiones con Git

Herramientas: pandas, NumPy, httpx, pytest, Git

Proyecto: Limpieza y análisis de un dataset real con pandas + reporte con gráficos (matplotlib/plotly).

#### Nivel 3 · Avanzado · 8–10 semanas

1. Programación asíncrona: asyncio, async/await
2. Concurrencia: threading vs multiprocessing
3. APIs con FastAPI y validación con Pydantic
4. Bases de datos con SQLAlchemy y Alembic
5. Logging estructurado y configuración por entorno
6. Empaquetado con pyproject.toml
7. Polars y procesamiento de datos grandes
8. Profiling y optimización (cProfile, line_profiler)

Herramientas: FastAPI, Pydantic, SQLAlchemy, Polars, Docker

Proyecto: API REST con FastAPI + PostgreSQL, tests, Docker y despliegue en la nube.

#### Nivel 4 · Experto · Continuo

1. Internals de CPython: GIL, memoria, bytecode
2. Python free-threaded (3.13+) y su impacto
3. Metaprogramación: metaclases, descriptores
4. Rendimiento extremo: Numba, Cython, Rust con PyO3
5. Arquitectura limpia y patrones de diseño
6. CI/CD, linters y calidad (ruff, pre-commit)
7. Diseño y publicación de librerías open source

Herramientas: ruff, PyO3, Numba, GitHub Actions

Proyecto: Librería propia publicada en PyPI con documentación, tests y CI.

### 02. LLMs (60.0 % de las vacantes)

Entender, usar, adaptar y servir grandes modelos de lenguaje.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. Qué es un LLM y cómo predice tokens
2. Tokens, ventana de contexto y costos
3. Parámetros: temperatura, top-p, max tokens
4. Panorama de proveedores: Anthropic, OpenAI, Google, open-weights
5. Limitaciones: alucinaciones, sesgos, fecha de corte
6. Primera llamada a una API desde Python

Herramientas: Anthropic API, OpenAI API, Gemini API

Proyecto: Chatbot de consola con memoria de conversación usando un SDK oficial.

#### Nivel 2 · Intermedio · 4–6 semanas

1. SDKs a fondo: mensajes, roles, system prompt
2. Streaming de respuestas
3. Salidas estructuradas (JSON / esquemas)
4. Tool use / function calling
5. Embeddings y similitud semántica
6. Modelos multimodales (imagen, PDF, audio)
7. Rate limits, reintentos y control de costos

Herramientas: SDK Python, Pydantic, tiktoken

Proyecto: Extractor que convierte facturas en PDF a JSON validado.

#### Nivel 3 · Avanzado · 6–8 semanas

1. Arquitectura Transformer: atención, embeddings posicionales
2. Tokenización BPE
3. Hugging Face Transformers
4. Modelos open-weights: Llama, Qwen, Mistral, Gemma
5. Fine-tuning eficiente: LoRA y QLoRA
6. Cuantización (GGUF, AWQ) e inferencia local
7. Servir modelos con Ollama y vLLM

Herramientas: Hugging Face, PEFT, Ollama, vLLM

Proyecto: Fine-tuning LoRA de un modelo pequeño para un dominio (ej. contratos inmobiliarios) y comparación vs modelo base.

#### Nivel 4 · Experto · Continuo

1. Entrenar un GPT pequeño desde cero (nanoGPT)
2. Alineamiento: RLHF, DPO y variantes
3. Evaluaciones propias y benchmarks
4. Inferencia a escala: KV cache, batching, speculative decoding
5. Seguridad: prompt injection, jailbreaks, fuga de datos
6. Interpretabilidad básica
7. Optimización costo/latencia y routing entre modelos

Herramientas: PyTorch, TRL, lm-eval-harness

Proyecto: Servicio de inferencia propio con métricas de latencia, costo y calidad, con routing entre modelos.

### 03. AI Agents (44.6 % de las vacantes)

Sistemas donde el LLM decide, usa herramientas y actúa en ciclos.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. Qué es un agente: LLM + herramientas + bucle
2. Patrón ReAct (razonar → actuar → observar)
3. Tool calling desde cero sin frameworks
4. Diferencia entre workflow y agente
5. Cuándo NO usar un agente

Herramientas: SDK Python, Function calling

Proyecto: Agente de consola que consulta clima y calcula con 2–3 herramientas propias.

#### Nivel 2 · Intermedio · 4–6 semanas

1. Frameworks: LangGraph, Claude Agent SDK, OpenAI Agents SDK, CrewAI
2. Model Context Protocol (MCP): clientes y servidores
3. Memoria de corto y largo plazo
4. Planificación y descomposición de tareas
5. Estado y grafos de ejecución
6. Manejo de errores y reintentos de herramientas

Herramientas: LangGraph, MCP, Claude Agent SDK

Proyecto: Agente que lee correos, clasifica solicitudes y crea registros en un CRM.

#### Nivel 3 · Avanzado · 6–8 semanas

1. Sistemas multi-agente y orquestación
2. Human-in-the-loop y aprobaciones
3. Ejecución durable y tareas largas
4. Evaluación de trayectorias de agentes
5. Guardrails y validación de acciones
6. Observabilidad: trazas, costos, pasos
7. Construir servidores MCP propios

Herramientas: Langfuse, LangSmith, Temporal

Proyecto: Agente sobre un ERP (vía API) que genera órdenes de compra con aprobación humana.

#### Nivel 4 · Experto · Continuo

1. Arquitectura de agentes en producción a escala
2. Seguridad: permisos mínimos, sandboxing, inyección indirecta
3. Agentes de código y computer use
4. Benchmarks: SWE-bench, τ-bench, GAIA
5. Optimización de costo por tarea
6. Diseño de producto: UX y confianza del usuario

Herramientas: Docker sandbox, OpenTelemetry

Proyecto: Plataforma multi-cliente de agentes con trazabilidad, permisos y métricas de negocio.

### 04. RAG (42.0 % de las vacantes)

Retrieval-Augmented Generation: respuestas basadas en tus propios documentos.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. Por qué RAG: conocimiento privado y actualizado
2. Embeddings y similitud coseno
3. Chunking básico de documentos
4. Pipeline: indexar → buscar → generar
5. Citar fuentes en la respuesta

Herramientas: Embeddings API, NumPy, FAISS

Proyecto: Q&A sobre 10 PDFs con búsqueda en memoria y citas.

#### Nivel 2 · Intermedio · 4–5 semanas

1. Bases vectoriales: pgvector, Qdrant, Chroma, Pinecone
2. Estrategias de chunking (semántico, por estructura)
3. Filtros por metadatos
4. LlamaIndex y LangChain
5. Parsing de documentos complejos (tablas, escaneos)

Herramientas: pgvector, Qdrant, LlamaIndex, Docling

Proyecto: Asistente de documentación interna con Postgres + pgvector y API.

#### Nivel 3 · Avanzado · 6–8 semanas

1. Búsqueda híbrida (BM25 + vectores)
2. Reranking con cross-encoders
3. Reescritura de consultas y HyDE
4. Contextual retrieval
5. Evaluación: precisión de recuperación y fidelidad
6. Datasets de prueba propios

Herramientas: Cohere Rerank, RAGAS, Elasticsearch

Proyecto: RAG con métricas antes/después de reranking y búsqueda híbrida.

#### Nivel 4 · Experto · Continuo

1. Agentic RAG y multi-hop
2. GraphRAG y grafos de conocimiento
3. RAG multimodal (imágenes, planos, tablas)
4. Fine-tuning de modelos de embeddings
5. Escala: índices HNSW/IVF, millones de documentos
6. Permisos por documento y multi-tenancy
7. Caché semántica

Herramientas: Neo4j, HNSW, Sentence Transformers

Proyecto: RAG empresarial multi-cliente con control de acceso por documento.

### 05. Prompt Engineering (24.1 % de las vacantes)

Diseñar instrucciones y contexto para obtener resultados fiables.

#### Nivel 1 · Fundamentos · 1–2 semanas

1. Instrucciones claras y específicas
2. Dar rol y contexto
3. Few-shot: ejemplos positivos y negativos
4. Definir formato de salida
5. Iterar y comparar respuestas

Herramientas: Consola de Anthropic, Playground

Proyecto: Biblioteca de 10 prompts para tareas de tu negocio con antes/después.

#### Nivel 2 · Intermedio · 2–3 semanas

1. Chain-of-thought y razonamiento paso a paso
2. Etiquetas XML para estructurar
3. System prompts robustos
4. Encadenamiento de prompts
5. Plantillas con variables

Herramientas: Jinja2, SDK Python

Proyecto: Pipeline de 3 prompts encadenados que resume, clasifica y redacta respuesta.

#### Nivel 3 · Avanzado · 3–4 semanas

1. Evaluación sistemática con datasets de prueba
2. Versionado de prompts
3. Context engineering para agentes
4. Descripción efectiva de herramientas
5. Prompt caching para reducir costos
6. LLM-as-judge

Herramientas: promptfoo, Langfuse

Proyecto: Suite de evaluación automática que puntúa versiones de un prompt.

#### Nivel 4 · Experto · Continuo

1. Optimización automática con DSPy
2. Defensas contra prompt injection
3. Prompts portables entre modelos
4. Gestión de prompts en producción
5. Investigación de técnicas nuevas

Herramientas: DSPy

Proyecto: Prompt optimizado automáticamente con mejora medible sobre baseline.

### 06. APIs (23.1 % de las vacantes)

Consumir y construir las interfaces que conectan sistemas e IA.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. HTTP: métodos, headers, status codes
2. JSON y REST
3. Probar APIs con curl, Postman o Bruno
4. Autenticación con API keys
5. Leer documentación de APIs

Herramientas: curl, Postman, httpx

Proyecto: Script que integra dos APIs públicas y combina sus datos.

#### Nivel 2 · Intermedio · 4–5 semanas

1. Diseñar APIs REST con FastAPI
2. OpenAPI / Swagger
3. OAuth2 y JWT
4. Paginación, filtros y versionado
5. Webhooks
6. Manejo de errores consistente

Herramientas: FastAPI, OAuth2, Swagger

Proyecto: API con autenticación JWT y webhooks hacia otro servicio.

#### Nivel 3 · Avanzado · 5–7 semanas

1. GraphQL y gRPC
2. WebSockets y Server-Sent Events (streaming de LLMs)
3. Rate limiting, caché e idempotencia
4. Colas y tareas en segundo plano
5. Integración con ERPs (OData, SOAP, APIs propietarias)

Herramientas: Redis, Celery, RabbitMQ, GraphQL

Proyecto: Middleware que sincroniza un ERP con un CRM usando colas y reintentos.

#### Nivel 4 · Experto · Continuo

1. API gateways y microservicios
2. Arquitectura orientada a eventos (Kafka)
3. Seguridad: OWASP API Top 10
4. Observabilidad con OpenTelemetry
5. Diseño API-first y contratos
6. SLAs y gestión de versiones

Herramientas: Kafka, Kong, OpenTelemetry

Proyecto: Plataforma de integración con gateway, eventos y monitoreo.

### 07. AWS (21.5 % de las vacantes)

Desplegar y escalar soluciones de IA en la nube más usada.

#### Nivel 1 · Fundamentos · 3–4 semanas

1. Cuenta, regiones y zonas de disponibilidad
2. IAM: usuarios, roles, políticas
3. EC2 y S3
4. Alertas de facturación
5. AWS CLI
6. Certificación: Cloud Practitioner

Herramientas: AWS CLI, IAM, S3, EC2

Proyecto: Sitio estático en S3 + una API simple en EC2.

#### Nivel 2 · Intermedio · 5–6 semanas

1. Lambda y API Gateway (serverless)
2. RDS y DynamoDB
3. VPC y redes básicas
4. CloudWatch: logs y métricas
5. Secrets Manager
6. Certificación: AI Practitioner / Solutions Architect Associate

Herramientas: Lambda, DynamoDB, RDS, CloudWatch

Proyecto: API serverless de un chatbot con Lambda + DynamoDB.

#### Nivel 3 · Avanzado · 6–8 semanas

1. Amazon Bedrock (modelos, agentes, knowledge bases)
2. SageMaker
3. ECS / Fargate para contenedores
4. Step Functions, SQS y SNS
5. Infraestructura como código: CDK o Terraform
6. CI/CD con GitHub Actions

Herramientas: Bedrock, SageMaker, CDK, Terraform

Proyecto: RAG en Bedrock desplegado 100% con infraestructura como código.

#### Nivel 4 · Experto · Continuo

1. Arquitectura multi-cuenta y Well-Architected
2. Seguridad: KMS, GuardDuty, Security Hub
3. FinOps: optimización de costos
4. MLOps en SageMaker
5. Alta disponibilidad y recuperación ante desastres
6. Certificación: ML Engineer Associate / Solutions Architect Professional

Herramientas: Organizations, KMS, Cost Explorer

Proyecto: Arquitectura de referencia de IA para un cliente enterprise documentada.

### 08. Machine Learning (21.0 % de las vacantes)

Los fundamentos matemáticos y técnicos detrás de todos los modelos.

#### Nivel 1 · Fundamentos · 6–8 semanas

1. Álgebra lineal, cálculo y probabilidad aplicados
2. Estadística descriptiva e inferencial
3. Tipos de aprendizaje: supervisado, no supervisado, refuerzo
4. Regresión lineal y logística
5. scikit-learn: train/test split
6. Métricas: accuracy, precision, recall, F1, RMSE

Herramientas: scikit-learn, pandas, matplotlib

Proyecto: Modelo que predice el precio de inmuebles con regresión.

#### Nivel 2 · Intermedio · 6–8 semanas

1. Árboles, Random Forest
2. Gradient boosting: XGBoost, LightGBM
3. Feature engineering
4. Validación cruzada y tuning de hiperparámetros
5. Clustering y PCA
6. Overfitting y regularización

Herramientas: XGBoost, LightGBM, Optuna

Proyecto: Modelo de predicción de abandono de clientes con explicación de variables (SHAP).

#### Nivel 3 · Avanzado · 8–10 semanas

1. Redes neuronales y backpropagation
2. PyTorch a fondo
3. CNN para visión
4. RNN y Transformers
5. Optimizadores y entrenamiento en GPU
6. Series de tiempo y forecasting

Herramientas: PyTorch, Colab / GPU, Lightning

Proyecto: Clasificador de imágenes o forecasting de demanda con red neuronal.

#### Nivel 4 · Experto · Continuo

1. MLOps: MLflow, DVC, Weights & Biases
2. Despliegue y monitoreo de drift
3. Feature stores
4. Entrenamiento distribuido
5. JAX
6. Leer e implementar papers

Herramientas: MLflow, W&B, JAX

Proyecto: Pipeline MLOps completo: entrenamiento, registro, despliegue y monitoreo.

### 09. Azure (18.5 % de las vacantes)

La nube preferida por empresas con ecosistema Microsoft.

#### Nivel 1 · Fundamentos · 3–4 semanas

1. Portal, suscripciones y resource groups
2. Microsoft Entra ID (identidad)
3. Storage Accounts y VMs
4. Azure CLI
5. Certificación: AZ-900

Herramientas: Azure CLI, Entra ID, Storage

Proyecto: Despliegue de una app simple en una VM con almacenamiento.

#### Nivel 2 · Intermedio · 5–6 semanas

1. App Service y Azure Functions
2. Azure SQL y Cosmos DB
3. Key Vault
4. Azure Monitor
5. Certificación: AZ-204

Herramientas: Functions, Cosmos DB, Key Vault

Proyecto: API serverless con Functions + Cosmos DB.

#### Nivel 3 · Avanzado · 6–8 semanas

1. Azure OpenAI y Azure AI Foundry
2. Azure AI Search para RAG
3. Document Intelligence
4. AKS (Kubernetes)
5. Bicep o Terraform
6. Certificación: AI-102

Herramientas: Azure OpenAI, AI Search, Bicep

Proyecto: RAG empresarial con AI Search + Azure OpenAI.

#### Nivel 4 · Experto · Continuo

1. Landing Zones y arquitectura enterprise
2. Gobernanza con Azure Policy
3. Seguridad: Defender, redes privadas
4. Integración con Microsoft 365 y Copilot Studio
5. Certificación: AZ-305

Herramientas: Azure Policy, Defender, Copilot Studio

Proyecto: Agente integrado en Teams conectado a datos corporativos.

### 10. GenAI (18.0 % de las vacantes)

IA generativa más allá del texto: imagen, audio, video y producto.

#### Nivel 1 · Fundamentos · 1–2 semanas

1. Panorama: texto, imagen, audio, video, código
2. Casos de uso por industria
3. Ética, derechos de autor y uso responsable
4. Herramientas no-code para prototipar

Herramientas: Claude, Midjourney, ElevenLabs

Proyecto: Mapa de 10 casos de uso de GenAI para un sector (ej. construcción).

#### Nivel 2 · Intermedio · 3–4 semanas

1. Modelos de difusión a alto nivel
2. APIs de generación de imagen
3. Voz: speech-to-text y text-to-speech
4. Aplicaciones multimodales
5. Moderación de contenido

Herramientas: Whisper, FLUX, Diffusers

Proyecto: Asistente de voz: audio → transcripción → LLM → respuesta hablada.

#### Nivel 3 · Avanzado · 5–6 semanas

1. Difusión a fondo: ruido, scheduler, guidance
2. Fine-tuning LoRA de imágenes
3. ComfyUI y pipelines
4. Evaluación de calidad generativa
5. UX de productos GenAI: latencia y expectativas

Herramientas: ComfyUI, Diffusers, LoRA

Proyecto: Generador de renders de inmuebles con estilo de marca propio.

#### Nivel 4 · Experto · Continuo

1. Arquitecturas: VAE, GAN, difusión, flow matching
2. Modelos de video
3. Entrenamiento de modelos propios
4. Regulación: EU AI Act y normativa local
5. Estrategia de producto y ROI de GenAI

Herramientas: PyTorch, Hugging Face

Proyecto: Producto GenAI con métricas de uso, costo y retorno para un cliente.

## Lenguajes de programación

Ranking de lenguajes en las mismas vacantes. Python ya está cubierto en el bloque anterior (74.4%).

### 11. TypeScript (13.1 % de las vacantes)

JavaScript con tipos: el estándar para frontends y backends de productos de IA. Aprende JavaScript (14) primero.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. Tipos básicos, interfaces y type aliases
2. Uniones, literales y narrowing
3. Funciones tipadas y genéricos simples
4. tsconfig y compilación
5. Node.js con TypeScript

Herramientas: TypeScript, Node.js, tsx

Proyecto: CLI en TypeScript que llama a la API de un LLM.

#### Nivel 2 · Intermedio · 4–5 semanas

1. Genéricos avanzados y utility types
2. Validación en runtime con Zod
3. React + TypeScript
4. Next.js (App Router, server actions)
5. Testing con Vitest

Herramientas: React, Next.js, Zod, Vitest

Proyecto: Interfaz de chat con streaming en Next.js.

#### Nivel 3 · Avanzado · 5–6 semanas

1. Vercel AI SDK y SDKs de LLM en TS
2. Backends con Hono / NestJS
3. ORMs: Prisma o Drizzle
4. Monorepos (Turborepo)
5. Servidores MCP en TypeScript

Herramientas: AI SDK, Prisma, Hono, MCP SDK

Proyecto: SaaS de agente con auth, base de datos y streaming.

#### Nivel 4 · Experto · Continuo

1. Tipos condicionales, mapped y template literal types
2. Diseño de librerías y tipos públicos
3. Rendimiento en el edge
4. Arquitectura full-stack a escala
5. Contribuir a open source

Herramientas: tsup, Bun, Deno

Proyecto: Librería npm tipada para integrar un ERP con agentes.

### 12. SQL (11.8 % de las vacantes)

El idioma de los datos: indispensable para RAG, analítica y sistemas empresariales.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. SELECT, WHERE, ORDER BY, LIMIT
2. Funciones de agregación y GROUP BY
3. JOINs (inner, left, right, full)
4. INSERT, UPDATE, DELETE
5. Tipos de datos y llaves primarias/foráneas

Herramientas: PostgreSQL, DBeaver, SQLite

Proyecto: Base de datos de un inventario con 20 consultas de negocio.

#### Nivel 2 · Intermedio · 3–4 semanas

1. Subconsultas y CTEs
2. Funciones de ventana (ROW_NUMBER, LAG, SUM OVER)
3. Diseño y normalización
4. Índices y su impacto
5. Vistas y transacciones

Herramientas: PostgreSQL, Supabase

Proyecto: Modelo de datos de un CRM con reportes de ventas mensuales.

#### Nivel 3 · Avanzado · 4–5 semanas

1. EXPLAIN y optimización de consultas
2. pgvector y búsqueda semántica en SQL
3. JSONB y datos semiestructurados
4. Row Level Security
5. Migraciones y versionado de esquemas
6. Text-to-SQL con LLMs

Herramientas: pgvector, Alembic, EXPLAIN

Proyecto: Agente text-to-SQL seguro sobre una base real con permisos de solo lectura.

#### Nivel 4 · Experto · Continuo

1. Data warehousing: modelado dimensional
2. dbt y transformación de datos
3. Particionamiento y replicación
4. Motores analíticos: BigQuery, Snowflake, DuckDB
5. Gobernanza y calidad de datos

Herramientas: dbt, DuckDB, Snowflake

Proyecto: Data warehouse con dbt alimentando dashboards y un agente analista.

### 13. Java (8.7 % de las vacantes)

Clave en grandes empresas, bancos y sistemas legados que deben integrarse con IA.

#### Nivel 1 · Fundamentos · 3–4 semanas

1. Sintaxis, tipos y control de flujo
2. Clases, objetos e interfaces
3. Colecciones (List, Map, Set)
4. Excepciones
5. Maven o Gradle

Herramientas: JDK 21, IntelliJ, Maven

Proyecto: Aplicación de consola de gestión de inventario.

#### Nivel 2 · Intermedio · 4–6 semanas

1. Streams y lambdas
2. Genéricos
3. Records y pattern matching
4. Testing con JUnit
5. Spring Boot básico

Herramientas: Spring Boot, JUnit

Proyecto: API REST con Spring Boot y base de datos.

#### Nivel 3 · Avanzado · 5–6 semanas

1. Spring Data, Security y JPA
2. Virtual threads (concurrencia moderna)
3. Spring AI y LangChain4j
4. Integración con mensajería (Kafka)
5. Docker y despliegue

Herramientas: Spring AI, LangChain4j, Kafka

Proyecto: Servicio Java que agrega un asistente LLM a un sistema empresarial existente.

#### Nivel 4 · Experto · Continuo

1. JVM internals y garbage collectors
2. Rendimiento y profiling
3. Microservicios a escala
4. GraalVM y compilación nativa
5. Modernización de sistemas legados

Herramientas: GraalVM, JFR, Kubernetes

Proyecto: Modernización de un módulo legado con capa de IA.

### 14. JavaScript (7.7 % de las vacantes)

La base de la web. Apréndelo antes de TypeScript.

#### Nivel 1 · Fundamentos · 3–4 semanas

1. Variables, tipos y operadores
2. Funciones, arrays y objetos
3. DOM y eventos
4. Fetch y JSON
5. ES Modules

Herramientas: Navegador, Node.js

Proyecto: Página que consume una API pública y muestra resultados.

#### Nivel 2 · Intermedio · 3–4 semanas

1. Promesas y async/await
2. Closures, this y prototipos
3. Destructuring, spread, métodos de arrays
4. Node.js y npm
5. Express básico

Herramientas: Node.js, npm, Express

Proyecto: Backend en Express que hace de proxy a una API de LLM.

#### Nivel 3 · Avanzado · 4–5 semanas

1. Event loop a fondo
2. Streams y Server-Sent Events
3. Web APIs: WebSockets, Web Workers
4. Bundlers (Vite)
5. Seguridad web: XSS, CORS, CSP

Herramientas: Vite, WebSockets

Proyecto: Widget de chat embebible en cualquier sitio web.

#### Nivel 4 · Experto · Continuo

1. Rendimiento web y Core Web Vitals
2. Motores JS (V8) y memoria
3. Patrones de arquitectura frontend
4. Migración a TypeScript

Herramientas: Chrome DevTools, Lighthouse

Proyecto: Optimizar una app real con métricas antes/después.

### 15. Go (6.2 % de las vacantes)

Servicios rápidos y concurrentes: infraestructura, gateways y backends de alto tráfico.

#### Nivel 1 · Fundamentos · 2–3 semanas

1. Sintaxis, tipos y structs
2. Slices y maps
3. Funciones e interfaces
4. Manejo de errores idiomático
5. Módulos de Go

Herramientas: Go, go mod

Proyecto: CLI que procesa archivos en lote.

#### Nivel 2 · Intermedio · 3–4 semanas

1. Goroutines y channels
2. Paquete net/http
3. JSON y APIs REST
4. Testing y benchmarks
5. Context y cancelación

Herramientas: net/http, testing

Proyecto: API REST concurrente que consulta varios servicios en paralelo.

#### Nivel 3 · Avanzado · 4–5 semanas

1. Patrones de concurrencia (worker pools, fan-out)
2. gRPC y Protocol Buffers
3. Bases de datos (pgx, sqlc)
4. Observabilidad
5. Docker multi-stage

Herramientas: gRPC, sqlc, pgx

Proyecto: Gateway de LLMs con rate limiting, caché y fallback entre proveedores.

#### Nivel 4 · Experto · Continuo

1. Runtime y scheduler de Go
2. Profiling con pprof
3. Operadores de Kubernetes
4. Sistemas distribuidos

Herramientas: pprof, Kubernetes

Proyecto: Servicio de alto rendimiento para servir embeddings.

### 16. R (0.8 % de las vacantes)

Baja demanda en AI Engineering; útil solo si trabajas en estadística o investigación. Prioridad mínima.

#### Nivel 1 · Fundamentos · 2 semanas

1. Vectores, data frames y funciones
2. RStudio
3. Importar datos

Herramientas: R, RStudio

Proyecto: Análisis exploratorio de un dataset.

#### Nivel 2 · Intermedio · 2–3 semanas

1. tidyverse: dplyr, tidyr
2. Gráficos con ggplot2
3. R Markdown / Quarto

Herramientas: tidyverse, ggplot2, Quarto

Proyecto: Reporte estadístico reproducible.

#### Nivel 3 · Avanzado · 3–4 semanas

1. Modelos estadísticos y pruebas de hipótesis
2. tidymodels
3. Shiny para apps

Herramientas: tidymodels, Shiny

Proyecto: Dashboard Shiny con un modelo predictivo.

#### Nivel 4 · Experto · Continuo

1. Estadística bayesiana
2. Creación de paquetes
3. Integración R + Python (reticulate)

Herramientas: Stan, reticulate

Proyecto: Paquete R publicado o análisis de investigación.
