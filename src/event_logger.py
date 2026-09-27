import json
from pathlib import Path


class EventLogger:
    """Stores security events as JSON lines."""

    def __init__(self, log_file="events.jsonl"):
        self.log_file = Path(log_file)

    def log(self, event):
        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(json.dumps(event) + "\n")
            