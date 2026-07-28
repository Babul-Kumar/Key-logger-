
# logger.py

from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "session_log.txt")


class Logger:
    def __init__(self):
        os.makedirs(LOG_DIR, exist_ok=True)
        self.is_running = False

    def start(self):
        self.is_running = True
        self._write("=== Session Started ===")

    def stop(self):
        self._write("=== Session Ended ===")
        self.is_running = False

    def log(self, message):
        """Log a simulated event."""
        if not self.is_running:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {message}\n")

    def _write(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"\n[{timestamp}] {message}\n")
