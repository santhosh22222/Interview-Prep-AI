import streamlit as st
from utils.auth import login_user
import os

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
APP_URL = os.getenv("APP_URL") or os.getenv("GOOGLE_REDIRECT_URI") or "http://localhost:8501"

def show():
    st.markdown("""
    <div class="login-card">
        <div style='text-align:center; margin-bottom: 24px;'>
            <div class='brand-title'>🎯 Interview Prep AI</div>
            <p style='color:var(--text2); margin-top:8px; font-size: 15px;'>Welcome back. Log in to your account to continue.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        email = st.text_input("Email address", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Continue", use_container_width=True)

        if submit:
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                with st.spinner("Logging in..."):
                    success, msg = login_user(email, password)
                if success:
                    st.success("Welcome back!")
                    st.rerun()
                else:
                    st.error(msg)

    # Google Sign In
    if GOOGLE_CLIENT_ID:
        google_auth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={GOOGLE_CLIENT_ID}"
            f"&redirect_uri={APP_URL}"
            f"&response_type=code"
            f"&scope=openid%20email%20profile"
            f"&access_type=offline"
        )
        st.markdown(f"""
        <div style='display:flex; align-items:center; margin: 20px 0; color:var(--text2); font-size:12px;'>
            <div style='flex:1; height:1px; background:var(--border);'></div>
            <div style='padding:0 10px;'>OR</div>
            <div style='flex:1; height:1px; background:var(--border);'></div>
        </div>
        <div style='text-align:center; margin: 16px 0;'>
            <a href='{google_auth_url}' target='_self' style='
                display: inline-flex; align-items: center; justify-content: center; gap: 10px;
                background: #fff; color: #3c4043; border: 1px solid #dadce0;
                border-radius: 10px; padding: 10px 24px; text-decoration: none;
                font-weight: 500; font-size: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                width: 100%; box-sizing: border-box; transition: all 0.2s;
            '>
                <img src='https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg' width='20'>
                Continue with Google
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align:center; margin-top:24px; border-top:1px solid var(--border); padding-top:20px;'>
            <p style='color:var(--text2); font-size:14px; margin-bottom: 8px;'>Don't have an account?</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Sign up", key="go_to_signup", use_container_width=True):
        st.session_state.auth_page = "signup"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
