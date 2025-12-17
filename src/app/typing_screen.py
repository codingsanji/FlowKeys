import tkinter as tk
import time

SAMPLE_TEXTS = {
    "beginner": "The quick brown fox jumps over the lazy dog.",
    "intermediate": "Technology has revolutionized the way we communicate.",
    "advanced": "Artificial intelligence is transforming industries worldwide.",
    "expert": "Quantum computing leverages superposition and entanglement."
}

class TypingScreen(tk.Frame):
    def __init__(self, master, stats, settings, on_complete):
        super().__init__(master, bg="#020617")

        self.stats = stats
        self.settings = settings
        self.on_complete = on_complete

        self.text = SAMPLE_TEXTS[settings.difficulty]
        self.user_input = ""
        self.start_time = None
        self.time_remaining = settings.time_limit
        self.timer_id = None

        self.build_ui()

    def build_ui(self):
        self.text_label = tk.Label(
            self,
            text=self.text,
            wraplength=900,
            font=("Consolas", 20),
            fg="#94a3b8",
            bg="#020617"
        )
        self.text_label.pack(pady=40)

        self.entry = tk.Entry(
            self,
            font=("Consolas", 18),
            bg="#020617",
            fg="white",
            insertbackground="cyan"
        )
        self.entry.pack(fill="x", padx=200)
        self.entry.bind("<KeyRelease>", self.on_type)
        self.entry.focus()

        self.stats_label = tk.Label(
            self,
            text="WPM: 0 | Accuracy: 100%",
            fg="#38bdf8",
            bg="#020617",
            font=("Segoe UI", 12)
        )
        self.stats_label.pack(pady=20)

    def on_type(self, event):
        if not self.start_time:
            self.start_time = time.time()
            self.start_timer()

        value = self.entry.get()
        correct = sum(
            1 for i, c in enumerate(value)
            if i < len(self.text) and c == self.text[i]
        )

        elapsed = max(time.time() - self.start_time, 1)
        wpm = int((correct / 5) / (elapsed / 60))
        accuracy = int((correct / max(len(value), 1)) * 100)

        self.stats.wpm = wpm
        self.stats.accuracy = accuracy
        self.stats.correct_chars = correct
        self.stats.total_chars = len(value)
        self.stats.time = int(elapsed)

        self.stats_label.config(
            text=f"WPM: {wpm} | Accuracy: {accuracy}%"
        )

        if value == self.text:
            self.finish()

    def start_timer(self):
        if self.time_remaining <= 0:
            self.finish()
            return

        self.time_remaining -= 1
        self.timer_id = self.after(1000, self.start_timer)

    def finish(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.on_complete()
