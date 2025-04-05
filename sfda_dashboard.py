
import pandas as pd
import streamlit as st
from login import login

# تفعيل CSS المخصص
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# إعدادات الصفحة
st.set_page_config(page_title="SFDA Registration Dashboard – MLAS201", layout="wide")

# تسجيل الدخول
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()

# عرض الشعار
st.image("logo.png", width=120)

# عنوان وبطاقة الجهاز
st.title("📁 Device Registration Card (RegCard) – RA-KSA-2025-041")
st.markdown("""
**Client:** Superior Business Co.  
**Project:** Alcohol Swabs registration with SFDA  
**Classification:** Class I – Rule 1, Annex 5  
**Intended Use:** Topical skin antiseptic before injection – single use  
**Origin:** Saudi Arabia – Sudair Industrial City  
**AR Status:** Not required (local manufacturer), but commercial license required  
**Basic UDI-DI:** 628704173xxxx  
""")
st.success("📗 SFDA / MDS-REQ1: View documentation matrix and regulatory workflow status.")

# تحميل ملف التتبع
df = pd.read_excel("FINAL_MDMA_SFDA_Tracker_With_Requirements.xlsx", sheet_name="Documentation Matrix")

# عرض الجدول
st.subheader("📄 Documentation Matrix by Classification")
st.dataframe(df, use_container_width=True)
