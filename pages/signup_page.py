import streamlit as st
from utils.auth import signup_user, login_user

def show():
    st.markdown("""
    <div style="text-align:center; padding: 32px 0 20px 0;">
        <div style="font-size:2rem; font-weight:800; letter-spacing:-1px;
                    background:linear-gradient(135deg,#10a37f,#56e39f);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            🎯 Interview Prep AI
        </div>
        <p style="color:var(--text-muted); margin-top:8px; font-size:15px;">
            Create your account to get started.
        </p>
    </div>
    """, unsafe_allow_html=True)

    name     = st.text_input("Full Name",        placeholder="Your full name",       key="signup_name")
    email    = st.text_input("Email address",    placeholder="you@example.com",      key="signup_email")
    password = st.text_input("Password",         type="password", placeholder="At least 6 characters", key="signup_password")
    confirm  = st.text_input("Confirm Password", type="password", placeholder="Repeat password",        key="signup_confirm")

    if st.button("Create Account", use_container_width=True, key="signup_btn"):
        if not all([name, email, password, confirm]):
            st.error("Please fill in all fields.")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")
        elif password != confirm:
            st.error("Passwords do not match.")
        else:
            with st.spinner("Creating your account..."):
                success, result = signup_user(name, email, password)
            if success:
                login_user(email, password)
                st.success("Account created! Welcome 🎉")
                st.rerun()
            else:
                st.error(result)

    st.markdown("<hr style='margin:20px 0;border:0;border-top:1px solid var(--border);'>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--text-muted);font-size:14px;text-align:center;margin-bottom:8px;'>Already have an account?</p>", unsafe_allow_html=True)
    if st.button("Log in", key="go_to_login", use_container_width=True):
        st.session_state.auth_page = "login"
        st.rerun()
