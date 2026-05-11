import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1) Page config and landing
# -----------------------------
st.set_page_config(page_title="CPI Forecast Dashboard", layout="wide")

st.title("CPI Forecast Dashboard")
st.markdown("""
Welcome to the CPI Forecast Dashboard!  
This project compares **actual CPI**, **Fed Nowcast**, and **our AI model predictions**.  
You can explore monthly comparisons, evaluation metrics, and visualizations of model performance.
""")

# -----------------------------
# 2) Load CSV & last month comparison
# -----------------------------
df_compare = pd.read_csv("cpi_comparison_last21.csv", index_col=0, parse_dates=True)

st.subheader("Last 3 Months CPI Comparison")

last3_months = df_compare.iloc[-3:]

for idx, row in last3_months.iterrows():
    st.markdown(f"### {idx.strftime('%B %Y')}")  
    col1, col2, col3 = st.columns(3)
    col1.metric("Actual CPI", f"{row['Actual']:.2f}")
    col2.metric("Fed Nowcast CPI", f"{row['Fed']:.2f}", f"{row['Fed_Error_%']:+.2f}%")
    col3.metric("Model Prediction CPI", f"{row['Model']:.2f}", f"{row['Model_Error_%']:+.2f}%")


# -----------------------------
# 3) Evaluation metrics table
# -----------------------------
st.subheader("Model Evaluation Metrics")
metrics = {
    "Metric": ["R-squared", "MAE", "MAPE", "MSE", "RMSE"],
    "Value": [0.9887, 0.0184, 0.0061, 0.0004, 0.0200]
}
df_metrics = pd.DataFrame(metrics)
st.table(df_metrics)

# -----------------------------
# 4) Plot Actual vs Fed vs Model CPI
# -----------------------------
st.subheader("CPI Comparison Plot")
fig1, ax1 = plt.subplots(figsize=(14,5))
ax1.plot(df_compare.index, df_compare["Actual"], label="Actual CPI", linewidth=2)
ax1.plot(df_compare.index, df_compare["Fed"], label="Fed Nowcast", linestyle="--")
ax1.plot(df_compare.index, df_compare["Model"], label="Model Prediction", linestyle="--")
ax1.set_ylabel("CPI")
ax1.set_title("Actual CPI vs Fed Nowcast vs Model Prediction")
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# -----------------------------
# 5) Bar chart of Error %
# -----------------------------
st.subheader("Error % Comparison")
labels = [d.strftime("%Y-%m") for d in df_compare.index]
x = np.arange(len(labels))
width = 0.4

fig2, ax2 = plt.subplots(figsize=(14,5))
ax2.bar(x - width/2, df_compare["Fed_Error_%"], width=width, label="Fed Error %")
ax2.bar(x + width/2, df_compare["Model_Error_%"], width=width, label="Model Error %")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, rotation=45, ha="right")
ax2.set_ylabel("Error %")
ax2.set_title("Fed vs Model Error % (Last 21 Months)")
ax2.legend()
ax2.grid(axis="y", linestyle="--", alpha=0.4)
st.pyplot(fig2)
