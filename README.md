# 💳 Credit Default Prediction App

An interactive, dark-themed AI credit risk assessment and default prediction web application built with **Streamlit** and **Python**.

---

## 🚀 Features

- **🔐 Secure Demo Authentication**: Protected login screen.
- **📊 Interactive Risk Assessment**: Evaluates borrower risk based on:
  - Age & credit history length
  - Monthly income & annual earning potential
  - Requested loan amount & Debt-to-Income (DTI) ratio
  - Credit score (CIBIL/FICO range 300–900)
- **⚡ Dynamic Visual Scoring**: Real-time progress meter with categorized risk indicators (*Low*, *Moderate*, *High*).
- **🔍 Automated Insights & Suggestions**: Tailored explanations and actionable financial advice based on the user's specific profile.
- **🎨 Sleek UI**: Custom dark + crimson styling optimized for clarity and readability.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (Web framework)
- **Pandas & NumPy** (Data processing)
- **Scikit-learn & XGBoost** (Machine Learning utilities)

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd Credit_Default_Project
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   python -m streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

---

## 🔑 Demo Credentials

| Role | Username | Password |
| :--- | :--- | :--- |
| **Admin** | `admin` | `1234` |

---

## 📂 Project Structure

```text
Credit_Default_Project/
├── app.py              # Main Streamlit web application
├── datasets/           # Historical credit datasets & documentation
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored cache & temporary files
└── README.md           # Project documentation
```
