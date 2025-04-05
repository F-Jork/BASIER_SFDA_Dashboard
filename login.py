
# login.py — Simple login logic

import streamlit as st

# --- User Login Section ---
def login():
    st.sidebar.header("🔐 Login Panel")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        if username == "basier_admin" and password == "sfda2024":
            st.session_state["authenticated"] = True
            st.success("✅ Login successful.")
        else:
            st.session_state["authenticated"] = False
            st.error("❌ Incorrect username or password.")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()
