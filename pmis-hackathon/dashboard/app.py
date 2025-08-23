import streamlit as st
import pandas as pd
from pathlib import Path

import plotly.express as px

st.set_page_config(page_title="PMIS – MVP Demo", layout="centered")
st.title("🦠 PMIS – Predictive Mpox Intervention System")

# --- Paths ---
base   = Path(r"D:\Project-Files\Health-care-hackathon\pmis-hackathon\pmis-hackathon\data\interim")
fcst   = pd.read_csv(base / "burundi_forecast.csv")
alloc  = pd.read_csv(base / "vax_allocation.csv")

# --- Tabs ---
tab1, tab2 = st.tabs(["📈 Forecast", "💉 Allocation"])

with tab1:
    st.subheader("Burundi – 4-Week Forecast")
    fig = px.line(fcst, x="ds", y="yhat", labels={"ds":"Week","yhat":"Predicted Cases"})
    st.plotly_chart(fig)

with tab2:
    st.subheader("Optimal Vaccine Allocation")
    st.dataframe(alloc)
    st.bar_chart(alloc.set_index("Country")["doses"])

st.caption("Powered by Prophet + PuLP – MVP build for Zion Tech Hub Hackathon 2025")