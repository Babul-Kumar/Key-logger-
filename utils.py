# uti

import os
from datetime import datetime

LOG_DIR = "logs"


def ensure_log_directory():
    """Create the log directory if it doesn't exist."""
    os.makedirs(LOG_DIR, exist_ok=True)


def get_timestamp():
    """Return the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_duration(start_time, end_time):
    """Return session duration in HH:MM:SS format."""
    duration = end_time - start_time
    total_seconds = int(duration.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def print_banner():
    """Print a simple application banner."""
    print("=" * 45)
    print(" Educational Keylogger Simulator ")
    print("=" * 45)


def separator():
    """Return a separator line."""
    return "-" * 45
