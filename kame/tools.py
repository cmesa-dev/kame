import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SEVERITY_WEIGHT = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def load_incidents(path: Path) -> list[dict[str, Any]]:
    """Read and validate the local, synthetic incident data source."""
    records = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("Incident source must contain a list.")
    required = {"id", "service", "severity", "status", "summary", "minutes_open"}
    for incident in records:
        if not required.issubset(incident):
            raise ValueError("Incident record is missing required fields.")
        if incident["severity"] not in SEVERITY_WEIGHT:
            raise ValueError("Incident severity is not supported.")
    return records


def analyse_incidents(incidents: list[dict[str, Any]]) -> dict[str, Any]:
    open_items = [item for item in incidents if item["status"] != "resolved"]
    prioritised = sorted(
        open_items,
        key=lambda item: (SEVERITY_WEIGHT[item["severity"]], item["minutes_open"]),
        reverse=True,
    )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(incidents),
        "open": len(open_items),
        "resolved": len(incidents) - len(open_items),
        "open_by_severity": dict(Counter(item["severity"] for item in open_items)),
        "services_affected": sorted({item["service"] for item in open_items}),
        "priority_queue": prioritised,
    }


def write_brief(task: str, analysis: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    severity = analysis["open_by_severity"]
    lines = [
        "# Operations Brief",
        "",
        f"Task: {task}",
        "",
        "## Summary",
        "",
        f"- Open incidents: {analysis['open']} of {analysis['total']}",
        f"- Resolved incidents: {analysis['resolved']}",
        f"- Services affected: {', '.join(analysis['services_affected']) or 'None'}",
        f"- Open severity distribution: critical={severity.get('critical', 0)}, "
        f"high={severity.get('high', 0)}, medium={severity.get('medium', 0)}, low={severity.get('low', 0)}",
        "",
        "## Priority Queue",
        "",
        "| ID | Service | Severity | Minutes open | Summary |",
        "|---|---|---|---:|---|",
    ]
    for incident in analysis["priority_queue"]:
        lines.append(
            f"| {incident['id']} | {incident['service']} | {incident['severity']} | "
            f"{incident['minutes_open']} | {incident['summary']} |"
        )
    lines += [
        "",
        "## Scope",
        "",
        "Generated from synthetic local data by the public KAME workflow demo.",
    ]
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
