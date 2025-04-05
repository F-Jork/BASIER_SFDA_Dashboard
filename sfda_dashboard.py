# ✅ SFDA REGISTRATION DASHBOARD – BASIER CUSTOM

import streamlit as st
import pandas as pd
from PIL import Image

# =========================== PAGE CONFIG ===========================
st.set_page_config(page_title="SFDA RegCard – RA-KSA-2025-041", layout="wide")

# =========================== STYLES ================================
st.markdown("""
    <style>
        body {background-color: #1E1E2F; color: #EAEAEA; font-family: 'Segoe UI';}
        .block-container {padding-top: 1rem; padding-bottom: 2rem;}
        .css-1v0mbdj, .css-1c7y2kd {color: #EAEAEA;}
        th {background-color: #2b2b40 !important; color: white !important;}
        td {background-color: #2b2b2f !important; color: #e0e0e0;}
        .header {font-size: 32px; font-weight: bold; margin-bottom: 20px;}
        .subheader {font-size: 20px; font-weight: bold; margin-bottom: 5px;}
    </style>
""", unsafe_allow_html=True)

# =========================== LOGIN ================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.sidebar:
        st.title("🔐 Login Panel")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "basier_admin" and password == "sfda2024":
                st.session_state.authenticated = True
                st.success("✅ Login successful.")
            else:
                st.error("❌ Invalid credentials.")
    st.stop()

# =========================== HEADER ================================
col1, col2 = st.columns([1, 8])
with col1:
    logo = Image.open("logo.png")
    st.image(logo, width=120)

with col2:
    st.markdown("""
    # 🗂️ SFDA Device Registration Dashboard – RA-KSA-2025-041
    **Client:** Superior Business Co.  
    **Project:** Alcohol Swabs Registration at SFDA  
    **Classification:** Class I – Rule 1, Annex 5  
    **Intended Use:** Topical skin disinfection pre-injection – single use  
    **Country of Origin:** KSA – Sudair Industrial City
    """)

st.markdown("---")

# =========================== FILE LOAD ================================
file_path = "Superior_SFDA_Tracker_pro.xlsx"
sheet_matrix = "Requirements Matrix"
sheet_tracker = "Client Submission Tracker"
sheet_gap = "Gap Analysis"
sheet_summary = "Dashboard Summary"

matrix = pd.read_excel(file_path, sheet_name=sheet_matrix)
tracker = pd.read_excel(file_path, sheet_name=sheet_tracker)
gap = pd.read_excel(file_path, sheet_name=sheet_gap)
summary = pd.read_excel(file_path, sheet_name=sheet_summary)

# =========================== TABS ================================
tabs = st.tabs(["📄 Documentation Matrix", "📦 Submission Tracker", "💡 Gap Analysis", "📊 Summary"])

# --- 1. Matrix
with tabs[0]:
    st.subheader("📄 Documentation Matrix by Classification")
    st.dataframe(matrix, use_container_width=True)

# --- 2. Submission Tracker
with tabs[1]:
    st.subheader("📦 Client Submission Tracker")
    st.dataframe(tracker, use_container_width=True)

# --- 3. Gap Analysis
with tabs[2]:
    st.subheader("💡 Regulatory Gap Analysis")
    st.dataframe(gap, use_container_width=True)

# --- 4. Summary View
with tabs[3]:
    st.subheader("📊 Dashboard Summary")
    st.dataframe(summary, use_container_width=True)
    total_docs = summary["Count"].sum()
    received = summary[summary["Status"] == "Received"]["Count"].sum()
    percent = int((received / total_docs) * 100)
    st.progress(percent / 100.0, text=f"Progress: {percent}%")

# ============================ FOOTER ================================
st.markdown("""
---
🔒 Confidential – Dashboard developed by **BASIER** for regulatory engagement with **SFDA**
""")
