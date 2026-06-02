# 🎯 Interview Prep AI

An AI-powered interview preparation platform built with Streamlit, Groq, and MongoDB.

## Features
- 🤖 AI chatbot powered by Groq (LLaMA 3, Mixtral, Gemma models)
- 🎯 Specialized coaching: Technical, HR, Non-Tech, Mixed
- 🔐 Login / Signup with email + Google OAuth
- 💾 Chat history saved to MongoDB
- 🌙 Dark / ☀️ Light theme toggle
- 🔢 Token usage counter
- 📋 Copy button on every message
- ⬇️ Download chat as Markdown or JSON
- 💡 Starter questions for each interview type

---

## Setup

### 1. Clone and install
```bash
git clone <your-repo>
cd interview_prep
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your keys
```

### 3. Get your API keys

**Groq API Key** (free):
- Go to https://console.groq.com
- Create an account and generate an API key
- Add to `.env`: `GROQ_API_KEY=your_key`

**MongoDB**:
- Local: `MONGODB_URI=mongodb://localhost:27017/interview_prep`
- Cloud (free): https://www.mongodb.com/atlas → Create cluster → Get connection string

**Google OAuth** (optional):
- Go to https://console.cloud.google.com
- Create OAuth 2.0 credentials
- Add redirect URI: `http://localhost:8501`
- Copy Client ID and Secret to `.env`

### 4. Run the app
```bash
streamlit run app.py
```

Open http://localhost:8501

---

## Project Structure
```
interview_prep/
├── app.py                  # Entry point
├── requirements.txt
├── .env.example
├── .streamlit/
│   └── config.toml         # Theme config
├── pages/
│   ├── login_page.py
│   ├── signup_page.py
│   └── chat_page.py        # Main chat UI
└── utils/
    ├── auth.py             # Login/signup/JWT
    ├── db.py               # MongoDB connection
    ├── groq_ai.py          # Groq API + prompts
    ├── chat_history.py     # Save/load chats
    └── theme.py            # CSS themes
```

## Available Models (via Groq)
| Model | Best For |
|-------|----------|
| LLaMA 3 70B | Best quality answers |
| LLaMA 3 8B | Fast responses |
| Mixtral 8x7B | Long conversations |
| Gemma 2 9B | Balanced |
| LLaMA 3.1 8B Instant | Quickest |
| LLaMA 3.3 70B Versatile | Most capable |
