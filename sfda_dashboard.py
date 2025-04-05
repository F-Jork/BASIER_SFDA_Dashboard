
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


# --- Below is the continuation of the main dashboard logic ---


import streamlit as st
import pandas as pd

# --------- User Login ---------
def login():
    st.sidebar.title("🔐 Login Panel")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        if username == "basier_admin" and password == "sfda2024":
            st.session_state["authenticated"] = True
            st.success("✅ Login successful.")
        else:
            st.error("❌ Incorrect credentials")

    return st.session_state.get("authenticated", False)

# --------- Run App ---------
def main_app():
    st.set_page_config(page_title="SFDA Dashboard", layout="wide")

    st.title("📊 SFDA Device Registration RegCard – RA-KSA-2025-041")
    st.markdown("✅ You are now logged in. Welcome to the dashboard.")
    
    # Placeholder for loading data or displaying main UI
    st.info("This section will show the 4 dashboard tabs after login.")

# --------- Auth Guard ---------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not login():
    st.stop()

main_app()
