# viewer.py

import tkinter as tk
from tkinter import scrolledtext
from storage import Storage


class LogViewer:
    def __init__(self):
        self.storage = Storage()

        self.root = tk.Tk()
        self.root.title("Log Viewer")
        self.root.geometry("700x500")

        self.text = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Consolas", 11)
        )
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame,
            text="Refresh",
            width=12,
            command=self.load_logs
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Clear Logs",
            width=12,
            command=self.clear_logs
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="Close",
            width=12,
            command=self.root.destroy
        ).grid(row=0, column=2, padx=5)

        self.load_logs()
        self.root.mainloop()

    def load_logs(self):
        self.text.delete(1.0, tk.END)

        logs = self.storage.load_events()

        if not logs:
            self.text.insert(tk.END, "No logs found.\n")
            return

        for i, log in enumerate(logs, start=1):
            self.text.insert(
                tk.END,
                f"{i}. [{log['timestamp']}] {log['event']}\n"
            )

    def clear_logs(self):
        self.storage.clear_events()
        self.load_logs()


if __name__ == "__main__":
    LogViewer()
