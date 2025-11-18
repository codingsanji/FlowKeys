# FlowKeys -- An Offline AI-Powered Typing Practice & Machine Learning Project 

**FlowKeys** is a Python-based typing practice desktop application inspired by MonkeyType but **enhanced with machine learning and fully offline AI**.  The aim is to help users analyze their typing behavior, improve accuracy, and personalize their learning curve.  

---
## Features

| Feature | Description | Dataset Used | ML/AI Type |
|--------|-------------|--------------|------------|
| **Randomized Typing Tests** | Generates word combos or quotes using multiple datasets. Ensures variety and progressive challenge. | [English Word Frequency Dataset](https://www.kaggle.com/rtatman/english-word-frequency) + [Quotes 500K](https://www.kaggle.com/datasets/manann/quotes-500k)  | None (preprocessing / data-driven logic) |
| **Keystroke Error Classification** | Classifies typing errors (missed letters, wrong case, slow/fast presses, fatigue slips) using supervised classification models. Provides insight into typing weaknesses. | User-generated typing logs (CSV/JSON) + Augmented public keystroke datasets to increase training data size. | Classification (Logistic Regression, Random Forest, SVM, Gradient Boosting) |
| **Typing Speed Prediction** | Predicts future WPM and error rate based on recent session patterns. Helps anticipate performance trends. | User-generated typing logs (CSV/JSON) + Augmented public keystroke datasets to improve model robustness. | Regression (Linear Regression, Random Forest Regressor, XGBoost Regressor) |
| **Typing Fatigue Estimator** | Estimates a fatigue score (0–100) based on timing irregularities, error spikes, and speed drop. Guides adaptive difficulty and practice breaks. | Local session logs + Augmented keystroke data to enhance model accuracy. | Regression (Linear Regression, Random Forest Regressor, XGBoost Regressor) |
| **Progress Charts & Graphs** | Visualizes WPM, accuracy, errors, and fatigue trends. Supports analysis of improvement over time. | Local session logs | None (Matplotlib/Tkinter visualization) |

---

## Machine Learning Components
These ML tasks fulfill the classification/regression requirement of the assignment.
<details>
<summary>Number 1:</summary>

### **1. Keystroke Error Classification (Supervised Learning - Classification)**
**Goal:** Predict *what type of typing error* occurred during the session.

#### **Error Classes:**
- **Missed Letters**  
  The user intended to press a key but messed it up (eg., typing “hte” instead of “the”).
- **Incorrect Case**  
  The user typed the correct letter but in the wrong case (uppercase instead of lowercase or vice-versa).
- **Slow or Hesitant Keypress**  
  The key was pressed much slower than the user's usual speed often indicating confusion or the user was stuck searching for the key.
- **Fast or Rushed Keypress**  
  The key was pressed significantly faster than normal usually due to the rush or careless typing.
- **Fatigue-Related Slip**  
  A general typing anomaly caused by tiredness, inconsistent timings, uneven pressure, or unusually long pauses.  
  *(Not directly in standard datasets; usually derived using timing thresholds.)*

#### **Dataset:**  
This project uses a **self-generated dataset** collected from typing sessions stored as a CSV or JSON but also uses augmentated datasets to assist like:
- [Public Keystroke Dynamics Integration Dataset](https://figshare.com/articles/dataset/Public_Keystroke_Dynamics_Integration_Dataset/14066456) 
- [KeyRecs Dataset](https://zenodo.org/records/7886743) 
- [KEasyLogger Dataset](https://zenodo.org/records/6535004) 

Example CSV:
```
user_id, key, press_time, release_time, hold_time, latency, is_error, error_type
01, a, 0.458, 0.612, 0.154, 0.102, 1, missed_letter
01, Shift, 0.900, 1.020, 0.120, 0.200, 1, incorrect_case
```

#### **Models Used:**
- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine (SVM)  
- Gradient Boosting Classifier

#### **Outputs:**
- Confusion Matrix  
- Classification Report (accuracy, precision, recall, F1-score)  
- ROC Curves  
- Model Comparison Chart (Accuracy & F1 Score)

---
</details>

<details>
<summary>Number 2:</summary>

### 2. Typing Speed Prediction (Supervised Learning - Regression)
**Goal:**  
Predict your future typing performance based on your recent session data.  
The model forecasts:  
- **Words Per Minute (WPM)**  
- **Error Rate**  
- **Performance Trend**  

#### **Dataset:**  
- **User-generated typing logs** (CSV/JSON) and augmentated datasets used in the first component.

Example CSV:
```
user_id, session_id, avg_hold_time, avg_latency, total_errors, wpm, fatigue_score
01, 001, 0.152, 0.108, 5, 42, 10
01, 002, 0.145, 0.095, 3, 48, 8
```
Features explained:  
- `avg_hold_time` → average key hold duration  
- `avg_latency` → average delay between key presses  
- `total_errors` → errors per session  
- `wpm` → target variable  
- `fatigue_score` → optional, derived from timing variance  

#### **Models Used:**  
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor

#### **Outputs:**  
- MSE (Mean Squared Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  
- Prediction vs. Actual Graph  

---
</details>

<details>
<summary>Number 3:</summary>

### 3. Typing Fatigue Estimation (Supervised Learning - Regression)
**Goal:**  
Estimate a **“fatigue score” (0-100)** for a user during a typing session.  
Performance-based metric, useful for guiding adaptive difficulty and practice breaks.

#### **Dataset:**  
- Locally generated user typing logs (CSV/JSON)  

Example CSV:
```
user_id, session_id, avg_hold_time, avg_latency, total_errors, wpm, fatigue_score
01, 001, 0.152, 0.108, 5, 42, 10
01, 002, 0.145, 0.095, 6, 40, 15
01, 003, 0.160, 0.120, 8, 35, 25
```
Features explained:  
- `avg_hold_time` → average key hold time  
- `avg_latency` → average delay between key presses  
- `total_errors` → total errors in the session  
- `wpm` → typing speed  
- `fatigue_score` → target variable  

#### **Models Used:**  
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  

#### **Outputs Explained:**  
- Fatigue Trend Line  
- Regression Metrics (MSE, RMSE, R²)  
- Practical Insights for adaptive difficulty and practice guidance

</details>

---

## Tech Stack
| Component | Technology |
|----------|-------------|
| GUI | Tkinter + ttk for modern widgets |
| Machine Learning | Scikit-Learn, XGBoost |
| Backend |Python 3.10+ |
| Data Storage | Local CSV / JSON logs |
| Visualization | Matplotlib, Seaborn, Tkinter Canvas |
| App Packaging | PyInstaller (cross-platform .exe) |
| Pre-processing | Pandas & NumPy |
| Model Serialization | joblib |

---

## Datasets
* [English Word Frequency Dataset](https://www.kaggle.com/rtatman/english-word-frequency)  

These can come in handy but not at the moment...
* [Quotes 500K](https://www.kaggle.com/datasets/manann/quotes-500k)  
* [Public Keystroke Dynamics Integration Dataset](https://figshare.com/articles/dataset/Public_Keystroke_Dynamics_Integration_Dataset/14066456?)  
* [KeyRecs Dataset](https://zenodo.org/records/7886743?)  
* [KEasyLogger Dataset](https://zenodo.org/records/6535004?)  

---

## Installation

```bash
pip install -r requirements.txt
python src/main.py
```

