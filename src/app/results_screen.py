import tkinter as tk

class ResultsScreen(tk.Frame):
    def __init__(self, master, stats, on_back):
        super().__init__(master, bg="#020617")

        tk.Label(
            self,
            text="Performance Results",
            font=("Segoe UI", 24),
            fg="white",
            bg="#020617"
        ).pack(pady=20)

        tk.Label(
            self,
            text=f"WPM: {stats.wpm}\nAccuracy: {stats.accuracy}%\nErrors: {stats.errors}",
            font=("Segoe UI", 16),
            fg="#38bdf8",
            bg="#020617"
        ).pack(pady=30)

        tk.Button(
            self,
            text="New Test",
            command=on_back,
            bg="#38bdf8",
            fg="black",
            font=("Segoe UI", 14)
        ).pack()
