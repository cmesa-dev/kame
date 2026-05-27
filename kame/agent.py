import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from typing import Any

from .planner import Planner
from .tools import analyse_incidents, load_incidents, write_brief


class WorkflowAgent:
    """Runs a bounded, inspectable operations reporting workflow."""

    def __init__(self, data_path: Path, output_dir: Path):
        self.data_path = data_path
        self.output_dir = output_dir
        self.planner = Planner()

    def run(self, task: str) -> dict[str, Any]:
        plan = self.planner.create_plan(task)
        trace: list[dict[str, Any]] = []
        state: dict[str, Any] = {}
        started = perf_counter()

        for step in plan:
            step_started = perf_counter()
            if step.key == "load_incidents":
                state["incidents"] = load_incidents(self.data_path)
                result = {"records": len(state["incidents"]), "source": str(self.data_path)}
            elif step.key == "analyse_incidents":
                state["analysis"] = analyse_incidents(state["incidents"])
                result = {"open": state["analysis"]["open"], "services": state["analysis"]["services_affected"]}
            elif step.key == "write_brief":
                report_path = self.output_dir / "operations-brief.md"
                write_brief(task, state["analysis"], report_path)
                result = {"report": str(report_path)}
            else:
                raise RuntimeError(f"Unsupported plan step: {step.key}")
            trace.append(
                {
                    "step": asdict(step),
                    "duration_ms": round((perf_counter() - step_started) * 1000, 3),
                    "result": result,
                }
            )

        run = {
            "task": task,
            "status": "completed",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "duration_ms": round((perf_counter() - started) * 1000, 3),
            "plan": [asdict(step) for step in plan],
            "trace": trace,
            "report": str(self.output_dir / "operations-brief.md"),
        }
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "trace.json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
        return run
