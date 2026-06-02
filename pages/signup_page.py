import streamlit as st
from utils.auth import signup_user, login_user

def show():
    st.markdown("""
    <div class="login-card">
        <div style='text-align:center; margin-bottom: 24px;'>
            <div class='brand-title'>🎯 Create Account</div>
            <p style='color:var(--text2); margin-top:8px; font-size: 15px;'>Join Interview Prep AI to master your next interview.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("signup_form"):
        name = st.text_input("Full Name", placeholder="Your full name")
        email = st.text_input("Email address", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="At least 6 characters")
        confirm = st.text_input("Confirm Password", type="password", placeholder="Repeat password")
        submit = st.form_submit_button("Continue", use_container_width=True)

        if submit:
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
                    # Auto login after signup
                    login_user(email, password)
                    st.success("Account created! Welcome 🎉")
                    st.rerun()
                else:
                    st.error(result)

    st.markdown("""
        <div style='text-align:center; margin-top:24px; border-top:1px solid var(--border); padding-top:20px;'>
            <p style='color:var(--text2); font-size:14px; margin-bottom: 8px;'>Already have an account?</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Log in", key="go_to_login", use_container_width=True):
        st.session_state.auth_page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
