import streamlit as st
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from utils.db import get_users_col
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_dev_secret_change_in_prod")

def init_session():
    defaults = {
        "logged_in": False,
        "user": None,
        "token": None,
        "messages": [],
        "current_chat_id": None,
        "theme": "dark",
        "model": "llama3-70b-8192",
        "interview_type": "Technical",
        "total_tokens": 0,
        "auth_page": "login",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def is_logged_in():
    return st.session_state.get("logged_in", False)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def signup_user(name: str, email: str, password: str):
    users = get_users_col()
    if users.find_one({"email": email}):
        return False, "Email already registered."
    hashed = hash_password(password)
    result = users.insert_one({
        "name": name,
        "email": email,
        "password": hashed,
        "provider": "email",
        "created_at": datetime.utcnow()
    })
    return True, str(result.inserted_id)

def login_user(email: str, password: str):
    users = get_users_col()
    user = users.find_one({"email": email})
    if not user:
        return False, "No account found with this email."
    if not verify_password(password, user["password"]):
        return False, "Incorrect password."
    _set_logged_in(user)
    return True, "Login successful."

def login_with_google(google_user: dict):
    users = get_users_col()
    email = google_user.get("email")
    user = users.find_one({"email": email})
    if not user:
        result = users.insert_one({
            "name": google_user.get("name", ""),
            "email": email,
            "password": "",
            "provider": "google",
            "picture": google_user.get("picture", ""),
            "created_at": datetime.utcnow()
        })
        user = users.find_one({"_id": result.inserted_id})
    _set_logged_in(user)
    return True

def _set_logged_in(user):
    st.session_state.logged_in = True
    st.session_state.user = {
        "id": str(user["_id"]),
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "picture": user.get("picture", ""),
        "provider": user.get("provider", "email"),
    }
    st.session_state.token = create_token(str(user["_id"]))

def logout():
    for key in ["logged_in", "user", "token", "messages", "current_chat_id", "total_tokens"]:
        st.session_state[key] = None if key not in ["logged_in"] else False
    st.session_state.messages = []
    st.session_state.total_tokens = 0
    st.rerun()

def handle_google_callback(code: str) -> bool:
    import requests
    import os
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
    APP_URL = os.getenv("APP_URL", "http://localhost:8501")
    
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        return False
        
    try:
        # 1. Exchange code for access token
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "code": code,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": APP_URL,
            "grant_type": "authorization_code"
        }
        token_res = requests.post(token_url, data=token_data)
        if token_res.status_code != 200:
            return False
            
        token_json = token_res.json()
        access_token = token_json.get("access_token")
        if not access_token:
            return False
            
        # 2. Get user profile details
        userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        userinfo_res = requests.get(userinfo_url, headers={"Authorization": f"Bearer {access_token}"})
        if userinfo_res.status_code != 200:
            return False
            
        user_info = userinfo_res.json()
        # 3. Log user in with Google
        return login_with_google(user_info)
    except Exception as e:
        return False
