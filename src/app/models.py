from dataclasses import dataclass

@dataclass
class TypingStats:
    wpm: int = 0
    accuracy: int = 100
    time: int = 0
    errors: int = 0
    correct_chars: int = 0
    total_chars: int = 0

@dataclass
class Settings:
    difficulty: str = "intermediate"
    theme: str = "dark"
    sound: bool = True
    predictive_typing: bool = False
    time_limit: int = 30
