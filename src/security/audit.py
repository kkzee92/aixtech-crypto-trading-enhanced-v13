"""Audit logger: append-only JSONL with optional hash chaining for integrity."""

import json
import hashlib
from datetime import datetime
from pathlib import Path

class AuditLogger:
    def __init__(self, log_path: str = "logs/audit.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.prev_hash = "0" * 64

    def log(self, event_type: str, data: dict):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": event_type,
            "data": data,
            "prev_hash": self.prev_hash,
        }
        # Simple chain
        entry_str = json.dumps(entry, sort_keys=True)
        entry["hash"] = hashlib.sha256(entry_str.encode()).hexdigest()
        self.prev_hash = entry["hash"]

        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
