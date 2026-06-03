import streamlit as st
from utils.auth import login_user
import os

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
APP_URL = os.getenv("GOOGLE_REDIRECT_URI") or os.getenv("APP_URL", "http://localhost:8501")

def show():
    st.markdown("""
    <div style="text-align:center; padding: 32px 0 20px 0;">
        <div style="font-size:2rem; font-weight:800; letter-spacing:-1px;
                    background:linear-gradient(135deg,#10a37f,#56e39f);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            🎯 Interview Prep AI
        </div>
        <p style="color:var(--text-muted); margin-top:8px; font-size:15px;">
            Welcome back. Log in to continue.
        </p>
    </div>
    """, unsafe_allow_html=True)

    email    = st.text_input("Email address", placeholder="you@example.com", key="login_email")
    password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")

    if st.button("Continue", use_container_width=True, key="login_btn"):
        if not email or not password:
            st.error("Please fill in all fields.")
        else:
            with st.spinner("Logging in..."):
                success, msg = login_user(email, password)
            if success:
                st.rerun()
            else:
                st.error(msg)

    # Google Sign In
    if GOOGLE_CLIENT_ID:
        google_auth_url = (
            "https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={GOOGLE_CLIENT_ID}"
            f"&redirect_uri={APP_URL}"
            "&response_type=code"
            "&scope=openid%20email%20profile"
            "&access_type=offline"
        )
        st.markdown(f"""
        <div style="display:flex;align-items:center;margin:16px 0;color:var(--text-muted);font-size:12px;">
            <div style="flex:1;height:1px;background:var(--border);"></div>
            <div style="padding:0 10px;">OR</div>
            <div style="flex:1;height:1px;background:var(--border);"></div>
        </div>
        <a href="{google_auth_url}" target="_self" style="
            display:flex;align-items:center;justify-content:center;gap:10px;
            background:#fff;color:#3c4043;border:1px solid #dadce0;
            border-radius:10px;padding:10px 24px;text-decoration:none;
            font-weight:500;font-size:14px;box-shadow:0 1px 3px rgba(0,0,0,0.1);
            width:100%;box-sizing:border-box;">
            <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" width="20">
            Continue with Google
        </a>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:20px 0;border:0;border-top:1px solid var(--border);'>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--text-muted);font-size:14px;text-align:center;margin-bottom:8px;'>Don't have an account?</p>", unsafe_allow_html=True)
    if st.button("Sign up for free", key="go_to_signup", use_container_width=True):
        st.session_state.auth_page = "signup"
        st.rerun()
