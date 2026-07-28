import tkinter as tk
from tkinter import messagebox

class EducationalKeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Educational Keylogger Simulator")
        self.root.geometry("500x350")

        title = tk.Label(
            root,
            text="Educational Keylogger Simulator",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        info = (
            "This project is intended only for learning\n"
            "cybersecurity concepts in a controlled environment.\n\n"
            "No real keystrokes are recorded by this demo."
        )

        tk.Label(root, text=info, justify="center").pack(pady=10)

        self.status = tk.Label(
            root,
            text="Status: Idle",
            fg="blue",
            font=("Arial", 12)
        )
        self.status.pack(pady=15)

        tk.Button(
            root,
            text="Start Demo",
            width=20,
            command=self.start_demo
        ).pack(pady=5)

        tk.Button(
            root,
            text="Stop Demo",
            width=20,
            command=self.stop_demo
        ).pack(pady=5)

        tk.Button(
            root,
            text="Exit",
            width=20,
            command=root.quit
        ).pack(pady=20)

    def start_demo(self):
        self.status.config(text="Status: Demo Running", fg="green")
        messagebox.showinfo(
            "Demo Started",
            "Simulation started.\nNo keyboard input is being recorded."
        )

    def stop_demo(self):
        self.status.config(text="Status: Stopped", fg="red")
        messagebox.showinfo(
            "Demo Stopped",
            "Simulation stopped."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = EducationalKeyloggerApp(root)
    root.mainloop()
