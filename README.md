<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f172a,50:164e63,100:0f172a&height=200&section=header&text=KAME&fontSize=80&fontColor=67e8f9&animation=fadeIn&fontAlignY=42&desc=Tu%20asistente%20de%20código%20que%20siempre%20elige%20el%20modelo%20más%20barato%20capaz%20de%20resolver%20tu%20tarea&descAlignY=63&descSize=13&descFontColor=94a3b8" width="100%"/>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ollama-local_·_gratis-000000?style=flat-square"/>
  <img src="https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/GPT--4o-OpenAI-412991?style=flat-square&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Claude-Anthropic-CC785C?style=flat-square"/>
  <img src="https://img.shields.io/badge/estado-activo-22c55e?style=flat-square"/>
</p>

---

## El problema

Tienes suscripciones a varios modelos de IA pero acabas usando siempre el más caro por comodidad, aunque tu tarea sea trivial. Un "hola" le cuesta lo mismo que un refactor complejo.

**KAME resuelve esto.** Analiza cada petición antes de enviarla y decide automáticamente cuál es el modelo más barato capaz de responderla bien.

---

## Cómo funciona el analizador

Antes de hacer ninguna llamada, KAME descompone tu petición en señales:

```
"implementa JWT con refresh tokens, blacklist Redis y tests para FastAPI"
         │
         ▼
   parse_query()  ──► intent: generate · domain: backend · modifiers: production
         │
   semantic_triage()  ──► nivel 5 / Arquitectura crítica
         │
   detect_domain()  ──► BACKEND
         │
         ▼
   Resultado: GPT-4o  (único nivel capaz de resolverlo bien)
```

```
"qué tiempo hace en Sevilla?"
         │
         ▼
   intent: search · nivel 1 / Charla trivial
         │
         ▼
   Resultado: Gemini Flash  (suficiente, ~100× más barato)
```

```
"hola"  ──►  nivel 1  ──►  Ollama local  (coste: 0 €)
```

Sin configuración manual. Sin `/model gpt-4o` antes de cada mensaje. El nivel correcto de potencia para cada tarea.

---

## Niveles de routing

| Nivel | Tipo de tarea | Modelo elegido |
|:---:|---|---|
| 1 | Saludo, consulta trivial | Ollama local · gratis |
| 2 | Pregunta rápida, explicación corta | Ollama local / Gemini Flash |
| 3 | Edición estándar, refactor puntual | Gemini Flash |
| 4 | Bug complejo, debug profundo | GPT-4o-mini / GPT-4o |
| 5 | Arquitectura, seguridad, multiarchivo | GPT-4o / Claude Sonnet/Opus |

Los modelos locales (Ollama, LM Studio) tienen siempre preferencia si son capaces. La API solo se usa cuando el problema lo requiere.

---

## Más que un router

### 🛠 Herramientas reales
KAME lee tu proyecto, ejecuta comandos y busca en la web durante el razonamiento:

```
read_file · run_command · search_code · grep_codebase
web_search · web_fetch · git_status · list_dir
```

### 🧠 Memoria semántica entre sesiones
Cada conversación queda vectorizada en ChromaDB local. KAME recuerda decisiones anteriores y las recupera automáticamente cuando son relevantes — sin que tengas que repetirte.

### 🐝 Modo Swarm
Para tareas de arquitectura, tres agentes colaboran en pipeline:

```
Arquitecto (GPT-4o)  →  QA & Seguridad (Gemini)  →  Lead Dev (GPT-4o)
```

Cada rol critica al anterior. El resultado es un plan de implementación con bloques `SEARCH/REPLACE` aplicables directamente.

### 💸 Tracking de coste
Cada llamada a la nube registra tokens y coste en USD. Al cerrar la sesión ves exactamente cuánto has gastado.

---

## Comandos principales

```bash
kame chat                    # Sesión interactiva
kame ask "explica este bug"  # Consulta rápida sobre el proyecto
kame route "tu petición"     # Muestra qué modelo usaría y por qué
kame budget                  # Estado de todos los backends disponibles
kame agent "tarea"           # Agente: planifica, lee el repo y propone cambios
kame swarm "tarea compleja"  # Pipeline Arquitecto → QA → Coder
kame work "tarea"            # Bucle autónomo hasta que los tests pasen
kame status                  # Git status del proyecto
```

---

## Stack

| Capa | Tecnología |
|---|---|
| Inferencia local | Ollama · LM Studio |
| Cloud | OpenAI · Gemini · Anthropic |
| Memoria vectorial | ChromaDB |
| CLI / UI | Typer · Rich · prompt_toolkit |
| Búsqueda web | urllib (sin dependencias extra) |

---

## Inicio rápido

```bash
# Inferencia local (recomendado, sin coste)
ollama pull qwen2.5-coder:7b

# Instalar KAME
pip install kameia

# Claves cloud opcionales en .env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...

# Arrancar
kame chat
```

Sin ninguna clave configurada, KAME corre 100% local.

---

> Proyecto privado en desarrollo activo. Este repositorio documenta la interfaz pública y la arquitectura del sistema.

---

<p align="center">
  <a href="https://www.linkedin.com/in/carlos-mesa-viera-747501197">
    <img src="https://img.shields.io/badge/Carlos%20Mesa%20Viera-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/cmesa-dev">
    <img src="https://img.shields.io/badge/cmesa--dev-GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://cmesa-dev.github.io/cv/es.html">
    <img src="https://img.shields.io/badge/CV-Español-6d28d9?style=for-the-badge&logo=read-the-docs&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://cmesa-dev.github.io/cv/index.html">
    <img src="https://img.shields.io/badge/CV-English-6d28d9?style=for-the-badge&logo=read-the-docs&logoColor=white"/>
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:164e63&height=90&section=footer" width="100%"/>
