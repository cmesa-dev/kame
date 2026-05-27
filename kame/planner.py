from dataclasses import dataclass


@dataclass(frozen=True)
class Step:
    key: str
    description: str


class Planner:
    """Builds the bounded plan supported by this public demo."""

    def create_plan(self, task: str) -> list[Step]:
        if not task.strip():
            raise ValueError("Task must not be empty.")
        return [
            Step("load_incidents", "Load the synthetic incident dataset"),
            Step("analyse_incidents", "Prioritise open incidents and compute service metrics"),
            Step("write_brief", "Write a Markdown operations brief"),
        ]
