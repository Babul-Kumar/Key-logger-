# Advanced Educational Keylogger Lab 🛡️

An advanced educational cybersecurity project designed to demonstrate keystroke monitoring mechanics, event-driven architecture, memory buffering, and log management in a controlled local environment.

## 📌 Project Overview
This project is developed as part of a cybersecurity lab assignment to explore how input tracking and system activity monitoring function at the application level. Understanding these concepts helps security researchers design robust detection mechanisms, endpoint protection systems, and behavioral monitoring controls.

---

## 🚀 Key Features
- **Event-Driven Listening:** Uses the `pynput` library to asynchronously capture keyboard events in real-time.
- **Memory Buffering:** Implements bulk-writing buffers to optimize disk I/O performance and minimize overhead.
- **Log Rotation:** Automatically checks and rotates log file sizes once they exceed the 1 MB threshold to manage storage efficiently.
- **Timestamp Integration:** Appends exact timestamps to entries for detailed activity auditing.
- **Safe Termination:** Gracefully handles session exits via the `ESC` key or standard keyboard interrupts (`Ctrl+C`).

---

## 🛠️ Prerequisites & Installation

Ensure you have Python installed on your system.

1. Clone or download the project files into your workspace.
2. Install the required dependency (`pynput`):
   ```bash
   pip install pynput
   
