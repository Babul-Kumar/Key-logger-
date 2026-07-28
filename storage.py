# storage.py

import json
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "events.json")


class Storage:
    def __init__(self):
        os.makedirs(LOG_DIR, exist_ok=True)

        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def save_event(self, event):
        """Save a simulated event to the JSON log."""

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_record = {
            "timestamp": timestamp,
            "event": event
        }

        data = self.load_events()
        data.append(new_record)

        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_events(self):
        """Load all stored events."""

        try:
            with open(LOG_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def clear_events(self):
        """Delete all stored events."""

        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

    def event_count(self):
        """Return the number of stored events."""

        return len(self.load_events())
