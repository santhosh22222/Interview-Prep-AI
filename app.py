import streamlit as st
from utils.auth import init_session, is_logged_in
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

if not is_logged_in():
    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"
    
    if st.session_state.auth_page == "login":
        login_page.show()
    else:
        signup_page.show()
else:
    chat_page.show()
