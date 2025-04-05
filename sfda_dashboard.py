import streamlit as st
import pandas as pd
from PIL import Image
from login import login

# ✅ يجب أن يكون أول شيء في الكود
st.set_page_config(page_title="SFDA Registration Dashboard – MLAS201", layout="wide")

# 🎨 تحميل التنسيق
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🔐 تسجيل الدخول
if not login():
    st.stop()

# 🖼️ الشعار
logo = Image.open("logo.png")
st.sidebar.image(logo, width=120)

# 📚 تحميل البيانات من Excel
data = pd.read_excel("Superior_SFDA_Tracker.xlsx", sheet_name=None)
doc_matrix = data.get("Requirements Matrix", pd.DataFrame())
submission = data.get("Client Submission Tracker", pd.DataFrame())
gaps = data.get("Gap Analysis", pd.DataFrame())

# 🧭 القائمة الجانبية
page = st.sidebar.radio("📘 اختر واجهة العرض:", (
    "🔎 Project Overview",
    "✅ Workflow Tracker (Editable)",
    "👁️ Client Summary View",
    "🧠 Regulatory Gap Analysis"
))

# 🔎 1. واجهة المشروع العامة
if page.startswith("🔎"):
    st.title("🔎 Project Overview")
    st.markdown("""
    #### Client: Superior Business Co.  
    #### Device: Alcohol Swabs  
    #### Classification: Class I – Rule 1, Annex 5  
    #### Intended Use: Topical skin disinfection – single use  
    #### Origin: KSA – Sudair City  
    #### Submission Pathway: GHAD
    """)
    st.markdown("---")
    st.subheader("📄 Documentation Matrix")
    st.dataframe(doc_matrix, use_container_width=True)

    st.subheader("📊 Submission Progress")
    total = submission.shape[0]
    done = submission[submission["تم استلامها"] == "✅"].shape[0]
    percent = int((done / total) * 100) if total else 0
    st.progress(percent / 100)
    st.write(f"**{percent}% Complete**")

# ✅ 2. التعديل المباشر داخل Workflow Tracker
elif page.startswith("✅"):
    st.title("✅ Workflow Tracker (Editable)")
    editable_df = submission.copy()
    edited = st.data_editor(editable_df, num_rows="dynamic", use_container_width=True)
    st.success("📝 You can edit this view directly. Changes are temporary unless saved manually.")

# 👁️ 3. عرض العميل – عرض فقط
elif page.startswith("👁️"):
    st.title("👁️ Client Summary View")
    st.markdown("View-only dashboard for client review.")
    display = submission[["Document", "تم استلامها", "المراجعة الفنية التنظيمية"]]
    st.dataframe(display, use_container_width=True)

# 🧠 4. تحليل الفجوات التنظيمية
elif page.startswith("🧠"):
    st.title("🧠 Regulatory Gap Analysis")
    st.dataframe(gaps, use_container_width=True)

# ⚠️ تذييل
st.markdown("""
---
<small>🔒 Developed by <strong>BASIER</strong> – SFDA Support Dashboard | Version 1.0</small>
""", unsafe_allow_html=True)
