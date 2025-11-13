# KeyAI — An AI-Powered Typing Practice Desktop App 

**KeyAI** is a Python-based typing practice application inspired by MonkeyType but with my own touch (it runs fully offline using **Tkinter**, and integrates lightweight **AI features** to help you analyze, improve, and personalize your typing experience — all locally on your computer).
---

## Features
### Typing Practice
- Real-time typing speed, accuracy, and word-per-minute (WPM) tracking.  
- Multiple difficulty modes (Beginner → Expert).  
- Custom text modes (quotes, code, random words, etc.).

### AI-Powered Enhancements
| Feature | Description | Dataset Used |
|----------|--------------|---------------|
| **AI Typing Pattern Analyzer** | Detects your error patterns (e.g., missed keys, frequent typos) and gives personalized tips. | Custom-trained from your own typing logs + optional public typing datasets. |
| **Adaptive Difficulty** | Adjusts word complexity based on your typing performance. | [`English Word Frequency Dataset`](https://www.kaggle.com/rtatman/english-word-frequency) |
| **Smart Word Predictor (Offline)** | Suggests the next word based on your typing context. | [`Text8 Dataset`](http://mattmahoney.net/dc/text8.zip) or [`Wikipedia Corpus`](https://www.kaggle.com/datasets/alik604/20-million-english-words) |
| **Typing Fatigue Estimator** | Uses a simple ML model to estimate your “mental fatigue” based on speed fluctuations. | Generated locally from your session data. |
| **Offline Feedback Generator** | Uses rule-based mini AI logic (no internet or GPT) to give motivational and constructive feedback. | No dataset needed — pure logic-based AI. |

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend (GUI)** | Tkinter (Python built-in GUI library) |
| **Backend / Logic** | Python |
| **AI Models** | Scikit-learn, TensorFlow Lite, or joblib-trained ML models |
| **Data Storage** | Local `.csv` or `.json` logs |
| **Visualization** | Matplotlib or Tkinter Canvas |
| **Packaging** | PyInstaller (to make an executable `.exe` version) |

---

### Datasets
- [English Word Frequency Dataset (Kaggle)](https://www.kaggle.com/rtatman/english-word-frequency)
- [Wikipedia Text Corpus (Kaggle)](https://www.kaggle.com/datasets/alik604/20-million-english-words)
- [Typing Patterns Dataset (Kaggle)](https://www.kaggle.com/datasets/competitions/keystroke-dynamics-benchmark)

