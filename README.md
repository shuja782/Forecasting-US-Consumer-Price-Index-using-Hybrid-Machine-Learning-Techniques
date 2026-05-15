# 📈 Forecasting US Consumer Price Index using Hybrid Machine Learning Techniques

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?style=flat-square&logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A hybrid machine learning model for forecasting the US Consumer Price Index (CPI),
benchmarked against the Federal Reserve's Nowcast predictions. The model achieved
an **R² of 0.9887** with a **MAPE of just 0.61%** across 21 months of out-of-sample
predictions 

An interactive Streamlit dashboard visualizes month-by-month comparisons between
actual CPI, Fed Nowcast, and model predictions with full error analysis.

---

## 📊 Results

| Metric | Our Model | 
|--------|-----------|
| **R²** | **0.9887** |
| **MAE** | **0.0184** 
| **MAPE** | **0.61%** 
| **MSE** | **0.0004** 
| **RMSE** | **0.0200** 



---

## 🏗️ How It Works

The pipeline combines multiple ML techniques in a hybrid ensemble approach:

**Data Collection** — Historical CPI data sourced from FRED (Federal Reserve Economic Data)
alongside macroeconomic indicators including unemployment rate, PPI, money supply,
and interest rates.

**Feature Engineering** — Lag features, rolling statistics, and economic indicator
transformations to capture temporal dependencies in inflation dynamics.

**Hybrid Model** — Ensemble of regression models combining the strengths of multiple
algorithms to capture both linear and non-linear patterns in CPI movement.

**Benchmarking** — Model predictions compared head-to-head against the Federal Reserve's
official Nowcast predictions across 21 months of real data.

**Streamlit Dashboard** — Interactive visualization of actual vs predicted CPI,
error analysis, and month-by-month comparison metrics.

---

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/shuja782/Forecasting-US-Consumer-Price-Index-using-Hybrid-Machine-Learning-Techniques.git
cd Forecasting-US-Consumer-Price-Index-using-Hybrid-Machine-Learning-Techniques

# Install dependencies
pip install streamlit pandas numpy matplotlib scikit-learn

# Run the dashboard
streamlit run main.py
```

---

## 📦 Tech Stack

| Category | Tools |
|----------|-------|
| **ML Models** | scikit-learn |
| **Data** | FRED API, pandas, numpy |
| **Visualization** | Streamlit, matplotlib |
| **Evaluation** | R², MAE, MAPE, MSE, RMSE |

---

## 👤 Author

**Muhammad Shuja**
- GitHub: [@shuja782](https://github.com/shuja782)

---

## 📄 License

MIT License — free to use, modify, and distribute with attribution.
