import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

_client = None

def get_db():
    global _client
    if _client is None:
        uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/interview_prep")
        _client = MongoClient(uri)
    return _client["interview_prep"]

def get_users_col():
    return get_db()["users"]

def get_chats_col():
    return get_db()["chats"]
