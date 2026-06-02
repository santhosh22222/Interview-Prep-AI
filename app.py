import streamlit as st
from utils.auth import init_session, is_logged_in, handle_google_callback
from utils.theme import apply_theme
from pages import login_page, signup_page, chat_page

st.set_page_config(
    page_title="Interview Prep AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_session()
apply_theme()

# Handle Google OAuth redirect callback
query_params = st.query_params
if "code" in query_params:
    auth_code = query_params["code"]
    with st.spinner("Logging in with Google..."):
        success = handle_google_callback(auth_code)
    if success:
        st.toast("Welcome back! Google Sign-In successful! 🎉", icon="✅")
    else:
        st.error("Google Sign-In failed. Please try again.")
    st.query_params.clear()
    st.rerun()

if not is_logged_in():
    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"
    
    if st.session_state.auth_page == "login":
        login_page.show()
    else:
        signup_page.show()
else:
    chat_page.show()
