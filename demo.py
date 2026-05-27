"""
KAME Agent — Demo público
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Este archivo es una DEMO simplificada con respuestas
simuladas. El código real de KAME es privado.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import time
import random

# ── Colores para terminal ──────────────────────────────
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


class KameAgentDemo:
    """
    Demo pública del agente KAME.
    Simula el flujo real de ejecución con respuestas mockeadas.
    """

    TOOLS = ["web_search", "code_runner", "file_manager", "api_caller"]

    def __init__(self, name: str = "KAME", model: str = "demo-mode"):
        self.name = name
        self.model = model
        self.memory = []
        print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════╗")
        print(f"║        KAME AI Agent — Demo          ║")
        print(f"║  Modelo: {model:<28}║")
        print(f"╚══════════════════════════════════════╝{RESET}\n")

    def _think(self, task: str) -> list[str]:
        """Simula la fase de planificación del agente."""
        steps_map = {
            "busca":   ["Buscar información relevante", "Filtrar resultados", "Sintetizar respuesta"],
            "analiza": ["Recopilar datos", "Procesar y analizar", "Generar informe"],
            "crea":    ["Definir estructura", "Generar contenido", "Revisar y formatear"],
            "resume":  ["Leer fuentes", "Extraer puntos clave", "Redactar resumen"],
        }
        for keyword, steps in steps_map.items():
            if keyword in task.lower():
                return steps
        return ["Interpretar solicitud", "Ejecutar tarea", "Formatear resultado"]

    def _execute_step(self, step: str, index: int) -> str:
        """Simula la ejecución de un paso del plan."""
        tool = random.choice(self.TOOLS)
        time.sleep(0.8)
        print(f"  {CYAN}[Paso {index}]{RESET} {step}")
        print(f"  {YELLOW}  → Usando herramienta: {tool}{RESET}")
        time.sleep(0.5)
        return f"Resultado del paso {index} completado."

    def run(self, task: str) -> dict:
        """Ejecuta una tarea completa con el agente."""
        print(f"{BOLD}📋 Tarea recibida:{RESET}")
        print(f"   \"{task}\"\n")

        print(f"{CYAN}🧠 Planificando...{RESET}")
        time.sleep(1)
        steps = self._think(task)

        print(f"\n{GREEN}✅ Plan generado ({len(steps)} pasos):{RESET}")
        for i, step in enumerate(steps, 1):
            print(f"   {i}. {step}")

        print(f"\n{CYAN}⚙️  Ejecutando...{RESET}\n")
        results = []
        for i, step in enumerate(steps, 1):
            result = self._execute_step(step, i)
            results.append(result)
            self.memory.append({"step": step, "result": result})

        duration = round(random.uniform(3.5, 15.0), 1)

        print(f"\n{GREEN}{BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"✅ Tarea completada en {duration}s")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

        output = (
            f"He completado la tarea '{task[:40]}...' en {len(steps)} pasos. "
            f"Todos los pasos se ejecutaron correctamente."
        )
        print(f"\n💬 {output}\n")

        return {
            "task": task,
            "steps_executed": len(steps),
            "duration_seconds": duration,
            "output": output,
            "status": "completed"
        }


# ── Punto de entrada ───────────────────────────────────
if __name__ == "__main__":
    agent = KameAgentDemo(name="KAME", model="demo-mode")

    demos = [
        "Busca las últimas tendencias en IA generativa y resume las 3 más importantes",
        "Analiza el mercado de integraciones empresariales en España",
        "Crea un informe sobre el estado del desarrollo con Python en 2025",
    ]

    print(f"{BOLD}Selecciona una tarea de demo:{RESET}")
    for i, d in enumerate(demos, 1):
        print(f"  {i}. {d[:60]}...")

    print(f"\n{YELLOW}→ Ejecutando demo automática...{RESET}\n")
    time.sleep(1)

    result = agent.run(demos[0])
