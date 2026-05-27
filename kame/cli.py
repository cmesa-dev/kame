import argparse
from pathlib import Path

from .agent import WorkflowAgent


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Run the public KAME operations workflow demo.")
    parser.add_argument(
        "task",
        nargs="?",
        default="Prepare a reliability brief for the open service incidents.",
        help="Task recorded in the generated brief.",
    )
    parser.add_argument("--data", type=Path, default=root / "examples" / "incidents.json")
    parser.add_argument("--output", type=Path, default=root / "runs" / "latest")
    arguments = parser.parse_args()

    run = WorkflowAgent(arguments.data, arguments.output).run(arguments.task)
    print("KAME workflow completed")
    for event in run["trace"]:
        step = event["step"]
        print(f"- {step['description']} ({event['duration_ms']} ms)")
    print(f"Report: {run['report']}")
    print(f"Trace: {arguments.output / 'trace.json'}")


if __name__ == "__main__":
    main()
