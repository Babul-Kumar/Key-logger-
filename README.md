# Advanced Educational Keylogger Lab 🛡️

**Warning / Important:** This project is for educational purposes only. Do not use this software to monitor, record, or intrude on other people's systems or input without explicit, informed consent. Misuse may be illegal and unethical. The author is not responsible for misuse.

## Project Overview

This repository contains an educational keylogger implementation written in Python. The program demonstrates event-driven keyboard listening (via `pynput`), in-memory buffering and bulk writes to reduce I/O overhead, simple log rotation when the log exceeds 1 MB, timestamped session headers and entries, and a safe termination flow.

The implementation is intentionally minimal and designed for local experimentation in a controlled lab environment only.

---

## Key Features

- Event-driven keyboard listening using `pynput`.
- Memory buffering: keystrokes are accumulated and flushed to disk in bulk for efficiency.
- Log rotation: when the log file grows past the configured maximum size, it gets renamed to a timestamped backup and a new log file is started.
- Timestamps: session headers and enter-key events include human-readable timestamps for auditing.
- Safe termination: press `ESC` to stop the listener (or use `Ctrl+C` in a terminal) — buffered data is flushed before exit.

---

## How it works (high level)

- The program listens for `on_press` and `on_release` events from `pynput.keyboard.Listener`.
- `on_press` formats the key using `format_key_output()` and appends it to an in-memory `key_buffer` list.
- When the buffer reaches `BUFFER_FLUSH_COUNT` (default: 10) the buffer is written to `system_activity.log` and cleared.
- Before each write, `rotate_log_if_needed()` checks the current log's size; if it exceeds `MAX_FILE_SIZE_BYTES` (default: 1 MB) the current log is renamed to a timestamped backup and a fresh log file is created.
- Special keys are translated into readable tokens (e.g. `[BKSP]`, `[ENTER]`, `[SHIFT]` ignored) and `Enter` inserts a newline plus a timestamp.
- On `ESC` or `KeyboardInterrupt`, remaining buffered keys are flushed and the listener exits cleanly.

---

## File / Log format

- Default log file: `system_activity.log` (configurable in `main.py`).
- Each run appends a session header like:

  --- Session Started at 2026-07-29 12:34:56 ---

- Keystrokes are written literally; special keys are surrounded by brackets for clarity (` [BKSP] `, ` [TAB] `, etc.). `Enter` inserts a newline and a timestamp so subsequent lines are time-stamped.

---

## Prerequisites & Installation

1. Python 3.7+ is recommended.
2. Clone or download this repository.
3. Install dependencies:

```bash
pip install pynput
```

---

## Usage

Run the script from a terminal in the project directory:

```bash
python main.py
```

- The program will print the absolute path to the active log file and start listening.
- Press `ESC` to stop the listener and flush remaining buffered keys.
- You can also stop with `Ctrl+C` — the program traps `KeyboardInterrupt`, flushes the buffer, and exits safely.

---

## Configuration

Open `main.py` and edit the configuration constants at the top to change behavior:

- `LOG_FILE` — path/name of the log file (default: `system_activity.log`).
- `MAX_FILE_SIZE_BYTES` — number of bytes at which the active log will be rotated (default: 1 * 1024 * 1024).
- `BUFFER_FLUSH_COUNT` — number of buffered keystrokes before a bulk write to disk (default: 10).

Adjust these values to tune performance and storage behavior for your local experiments.

---

## Safety, Testing & Development

- Always run this code in a controlled environment (a VM or test machine) where you have explicit permission to record input.
- Review `format_key_output()` if you want to change how special keys are recorded.
- If you modify the code to capture additional events or run as a background service, add appropriate security and privacy safeguards.

---

## Contributing

Contributions are welcome for bug fixes, documentation improvements, and safer / clearer examples. Please keep changes focused on education, safety, and responsible usage.

---

## License

This repository does not include a license file. If you intend to share or reuse this code, add an appropriate license and update the README accordingly.
