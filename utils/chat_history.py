import streamlit as st
from datetime import datetime
from bson import ObjectId
from utils.db import get_chats_col
import json

def save_chat(user_id: str, messages: list, title: str = None):
    chats = get_chats_col()
    if not title and messages:
        first_user_msg = next((m["content"] for m in messages if m["role"] == "user"), "New Chat")
        title = first_user_msg[:50] + ("..." if len(first_user_msg) > 50 else "")

    chat_id = st.session_state.get("current_chat_id")

    if chat_id:
        chats.update_one(
            {"_id": ObjectId(chat_id)},
            {"$set": {"messages": messages, "title": title, "updated_at": datetime.utcnow()}}
        )
        return chat_id
    else:
        result = chats.insert_one({
            "user_id": user_id,
            "title": title or "New Chat",
            "messages": messages,
            "interview_type": st.session_state.get("interview_type", "Technical"),
            "model": st.session_state.get("model", "llama3-70b-8192"),
            "total_tokens": st.session_state.get("total_tokens", 0),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        })
        st.session_state.current_chat_id = str(result.inserted_id)
        return str(result.inserted_id)

def load_chat_history(user_id: str):
    chats = get_chats_col()
    return list(chats.find(
        {"user_id": user_id},
        {"messages": 0}
    ).sort("updated_at", -1).limit(50))

def load_chat(chat_id: str):
    chats = get_chats_col()
    return chats.find_one({"_id": ObjectId(chat_id)})

def delete_chat(chat_id: str):
    chats = get_chats_col()
    chats.delete_one({"_id": ObjectId(chat_id)})

def export_chat_as_text(messages: list, title: str = "Chat") -> str:
    lines = [f"# {title}", f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}", "---\n"]
    for msg in messages:
        role = "You" if msg["role"] == "user" else "AI Coach"
        lines.append(f"**{role}:**\n{msg['content']}\n")
    return "\n".join(lines)

def export_chat_as_json(messages: list, title: str = "Chat") -> str:
    data = {
        "title": title,
        "exported_at": datetime.now().isoformat(),
        "messages": messages
    }
    return json.dumps(data, indent=2)
