import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="SFDA Dashboard", layout="wide")

# إعداد بيانات المستخدمين
USERS = {
    "basier_admin": "sfda2024",
    "superior_client": "superior2025"
}

# تسجيل الدخول
def login_panel():
    st.sidebar.title("🔐 Login Panel")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        if username in USERS and USERS[username] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("✅ Login successful.")
        else:
            st.error("❌ Invalid username or password.")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_panel()
    st.stop()

# التطبيق الرئيسي
def main():
    logo = Image.open("logo.png")
    st.sidebar.image(logo, use_column_width=True)

    st.markdown("## 📄 SFDA Device Registration Dashboard – RA-KSA-2025-041")
    st.markdown("""
    **Client:** Superior Business Co.  
    **Project:** Alcohol Swabs Registration at SFDA  
    **Classification:** Class I – Rule 1, Annex 5  
    **Intended Use:** Topical skin disinfection pre-injection – single use  
    **Country of Origin:** KSA – Sudair Industrial City  
    """)

    file_path = "Superior_SFDA_Tracker.xlsx"
    sheet_matrix = "Documentation Matrix"
    sheet_submission = "Client Submission"
    sheet_gaps = "Gap Analysis"

    matrix = pd.read_excel(file_path, sheet_name=sheet_matrix)
    submission = pd.read_excel(file_path, sheet_name=sheet_submission)
    gaps = pd.read_excel(file_path, sheet_name=sheet_gaps)

    st.markdown("### 📄 Documentation Matrix by Classification")
    st.dataframe(matrix, use_container_width=True)

    st.markdown("### 📂 Client Submission Tracker")
    st.dataframe(submission, use_container_width=True)

    st.markdown("### 💡 Regulatory Gap Analysis")
    st.dataframe(gaps, use_container_width=True)

    st.markdown("""---  
🔒 Confidential – Dashboard developed by **BASIER** for regulatory engagement with **SFDA**  
    """, unsafe_allow_html=True)

main()
