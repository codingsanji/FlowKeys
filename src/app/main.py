import tkinter as tk
from app.typing_screen import TypingScreen
from app.results_screen import ResultsScreen
from app.models import TypingStats, Settings


class FlowKeysApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FlowKeys")
        self.geometry("1000x800")
        self.configure(bg="#0f172a")

        self.stats = TypingStats()
        self.settings = Settings()
        self.current_screen = None

        self.show_typing_screen()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_typing_screen(self):
        self.clear_screen()
        self.current_screen = TypingScreen(
            self,
            self.stats,
            self.settings,
            on_complete=self.show_results_screen
        )
        self.current_screen.pack(fill="both", expand=True)

    def show_results_screen(self):
        self.clear_screen()
        self.current_screen = ResultsScreen(
            self,
            self.stats,
            on_back=self.show_typing_screen
        )
        self.current_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = FlowKeysApp()
    app.mainloop()
