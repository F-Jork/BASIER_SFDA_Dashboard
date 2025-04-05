import streamlit as st
import pandas as pd

# ---------------------------
# ✅ Page Configuration
# ---------------------------
st.set_page_config(page_title="SFDA Dashboard – RA-KSA-2025-041", layout="wide")

# ---------------------------
# ✅ Session Authentication
# ---------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    with st.sidebar:
        st.markdown("### 🔐 Login Panel")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "basier_admin" and password == "sfda2024":
                st.session_state["authenticated"] = True
                st.success("✅ Login successful.")
            else:
                st.error("❌ Invalid credentials")
    st.stop()

# ---------------------------
# ✅ Load Excel Data
# ---------------------------
file_path = "Superior_SFDA_Tracker.xlsx"
sheet_matrix = "Requirements Matrix"
sheet_submission = "Client Submission Tracker"
sheet_gap = "Gap Analysis"

try:
    matrix = pd.read_excel(file_path, sheet_name=sheet_matrix)
    submission = pd.read_excel(file_path, sheet_name=sheet_submission)
    gap = pd.read_excel(file_path, sheet_name=sheet_gap)
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ---------------------------
# ✅ UI Layout
# ---------------------------
st.image("logo.png", width=120)
st.title("📄 SFDA Device Registration Dashboard – RA-KSA-2025-041")

st.markdown("""
**Client:** Superior Business Co.  
**Project:** Alcohol Swabs Registration at SFDA  
**Classification:** Class I – Rule 1, Annex 5  
**Intended Use:** Topical skin disinfection pre-injection – single use  
**Country of Origin:** KSA – Sudair Industrial City
""")

st.markdown("## 📄 Documentation Matrix by Classification")
st.dataframe(matrix, use_container_width=True)

st.markdown("## 📋 Client Submission Tracker")
st.dataframe(submission, use_container_width=True)

st.markdown("## 💡 Regulatory Gap Analysis")
st.dataframe(gap, use_container_width=True)

st.markdown("---")
st.markdown("🔒 Confidential – Dashboard developed by **BASIER** for regulatory engagement with **SFDA**.")
