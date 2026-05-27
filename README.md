<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,100:16213e&height=200&section=header&text=KAME&fontSize=80&fontColor=00d4ff&animation=fadeIn&fontAlignY=38&desc=Autonomous%20AI%20Agent%20Framework&descAlignY=56&descAlign=50" width="100%"/>
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2500&pause=800&color=00D4FF&center=true&vCenter=true&width=600&lines=Reasoning+%E2%86%92+Planning+%E2%86%92+Acting;Multi-step+task+execution;Tool+calling+%26+memory+management;Built+with+Python+%26+LLMs" alt="Typing SVG"/>
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Estado-En_Desarrollo-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/LLM_Powered-✓-00d4ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Licencia-Privada-red?style=for-the-badge"/>
</div>

---

## ¿Qué es KAME?

**KAME** es un framework de agentes IA autónomos desarrollado desde cero en Python. Su nombre hace referencia al concepto de perseverancia y método — avanza despacio pero no se detiene.

A diferencia de otros agentes, KAME no depende de un único proveedor de LLM: está diseñado para ser **agnóstico al modelo**, pudiendo operar con OpenAI, Anthropic, modelos locales u otros proveedores.

---

## ✨ Capacidades

| Capacidad | Descripción |
|---|---|
| 🧠 **Razonamiento** | Descompone tareas complejas en pasos ejecutables |
| 🔧 **Tool Calling** | Ejecuta herramientas externas: búsqueda, código, APIs |
| 💾 **Memoria** | Mantiene contexto a corto y largo plazo entre sesiones |
| 🔁 **Auto-corrección** | Detecta errores en sus respuestas y se auto-corrige |
| 🌐 **Multi-LLM** | Compatible con OpenAI, Anthropic, Ollama y otros |
| 📋 **Planificación** | Genera y ejecuta planes de acción paso a paso |

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                      KAME CORE                          │
│                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐  │
│  │  INPUT   │───▶│ PLANNER  │───▶│   TASK QUEUE     │  │
│  │ Handler  │    │  Module  │    │                  │  │
│  └──────────┘    └──────────┘    └────────┬─────────┘  │
│                                           │             │
│  ┌──────────────────────────────────────  ▼  ────────┐  │
│  │                  EXECUTOR                         │  │
│  │                                                   │  │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────────┐   │  │
│  │   │   TOOL   │  │  CODE    │  │   MEMORY     │   │  │
│  │   │ Calling  │  │ Runner   │  │   Manager    │   │  │
│  │   └──────────┘  └──────────┘  └──────────────┘   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐  │
│  │   LLM    │    │  OUTPUT  │    │    EVALUATOR     │  │
│  │ Provider │    │ Formatter│    │  (self-critique) │  │
│  └──────────┘    └──────────┘    └──────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Demo — Interacción de ejemplo

> ⚠️ Este repositorio contiene una **demo simplificada**. El código de producción es privado.

```python
from kame import Agent

# Inicializar agente
agent = Agent(
    name="KAME",
    model="gpt-4o",   # o "claude-3-5-sonnet", "ollama/llama3"
    tools=["web_search", "code_runner", "file_manager"]
)

# Ejecutar tarea compleja
result = agent.run(
    "Analiza las últimas noticias sobre IA, "
    "resume los 3 puntos más importantes "
    "y guárdalos en un archivo markdown."
)

print(result.output)
# ✅ Tarea completada en 4 pasos
# 📄 Archivo guardado: resumen_ia_2025.md
```

**Flujo de ejecución real:**
```
[KAME] 🧠 Planificando tarea...
  → Paso 1: Buscar noticias recientes sobre IA
  → Paso 2: Filtrar y analizar resultados
  → Paso 3: Sintetizar los 3 puntos clave
  → Paso 4: Escribir y guardar archivo markdown

[KAME] 🔧 Ejecutando: web_search("noticias IA 2025")
[KAME] 🔧 Ejecutando: code_runner(summarize_articles)
[KAME] 🔧 Ejecutando: file_manager.write("resumen_ia_2025.md")
[KAME] ✅ Completado en 12.3s
```

---

## 🛠️ Stack Tecnológico

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-CC785C?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## 📌 Estado del proyecto

- [x] Core del agente (razonamiento + planificación)
- [x] Sistema de tool calling
- [x] Memoria a corto plazo
- [ ] Memoria persistente entre sesiones (en desarrollo)
- [ ] Interfaz web de administración
- [ ] SDK público (próximamente)

---

## 📬 Contacto

¿Interesado en KAME para tu empresa o proyecto?

[![Email](https://img.shields.io/badge/kmevi32@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:kmevi32@gmail.com)
[![LinkedIn](https://img.shields.io/badge/Carlos_Mesa_Viera-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/carlosmesaviera)

> 💡 El código fuente completo es **privado**. Este repositorio es una demostración pública de las capacidades del proyecto.

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,100:1a1a2e&height=100&section=footer" width="100%"/>
</div>
