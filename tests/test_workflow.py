import json
import tempfile
import unittest
from pathlib import Path

from kame.agent import WorkflowAgent
from kame.tools import analyse_incidents, load_incidents


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "examples" / "incidents.json"


class ToolTests(unittest.TestCase):
    def test_analysis_prioritises_open_critical_incidents(self) -> None:
        result = analyse_incidents(load_incidents(DATA))
        self.assertEqual(result["open"], 3)
        self.assertEqual(result["resolved"], 1)
        self.assertEqual(result["priority_queue"][0]["id"], "INC-1042")


class WorkflowTests(unittest.TestCase):
    def test_agent_writes_report_and_trace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            run = WorkflowAgent(DATA, output).run("Prepare an incident brief.")
            report = (output / "operations-brief.md").read_text(encoding="utf-8")
            trace = json.loads((output / "trace.json").read_text(encoding="utf-8"))

        self.assertEqual(run["status"], "completed")
        self.assertIn("checkout-api", report)
        self.assertEqual(len(trace["trace"]), 3)


if __name__ == "__main__":
    unittest.main()
