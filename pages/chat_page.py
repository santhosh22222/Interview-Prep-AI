import streamlit as st
from utils.auth import logout
from utils.groq_ai import chat_with_groq, GROQ_MODELS, INTERVIEW_SYSTEM_PROMPTS
from utils.chat_history import (
    save_chat, load_chat_history, load_chat,
    delete_chat, export_chat_as_text, export_chat_as_json
)
from utils.theme import apply_theme
import time
import json
import base64
from datetime import datetime
import streamlit.components.v1 as components

INTERVIEW_TYPES = list(INTERVIEW_SYSTEM_PROMPTS.keys())

STARTER_QUESTIONS = {
    "Technical": [
        "Data Structures Quiz\nPractice linked lists, trees, and graphs",
        "LeetCode Problem\nSolve a coding challenge with hints",
        "System Design\nHow to design scalable systems",
        "Big O Notation\nExplain time & space complexity",
    ],
    "HR": [
        "HR Practice\nTell me about yourself",
        "Strengths/Weaknesses\nAnswer hr behavioral questions",
        "STAR Method\nStructure behavioral answers",
        "Why Should We Hire You?\nAlign your value proposition",
    ],
    "Non-Tech": [
        "Role Prep\nMarketing or Product Management",
        "Finance Analyst\nPrep for valuation & models",
        "Present Portfolio\nShowcase design & user experience",
        "Sales Interview\nPractice pitching & closing",
    ],
    "Mixed": [
        "Mock Session\nFull technical + soft skills mock",
        "Resume Review\nPrep bullet point explanations",
        "Top 10 Questions\nMaster the standard questions",
        "Prep Strategy\nCreate a custom interview roadmap",
    ]
}

STARTER_PROMPTS_MAPPING = {
    "Data Structures Quiz\nPractice linked lists, trees, and graphs": "Practice a mock technical interview question on core Data Structures (linked lists, trees, or graphs) and quiz me step-by-step.",
    "LeetCode Problem\nSolve a coding challenge with hints": "Give me a medium difficulty LeetCode-style coding question and guide me through solving it. Ask for my approach first before giving hints.",
    "System Design\nHow to design scalable systems": "Let's do a mock system design interview. Ask me to design a popular service (like Uber, Netflix, or TinyURL) and coach me step-by-step.",
    "Big O Notation\nExplain time & space complexity": "Explain Big O notation and time/space complexity analysis in a simple, intuitive way with examples. Then, quiz me with 2 simple code snippets.",
    
    "HR Practice\nTell me about yourself": "Let's practice the 'Tell me about yourself' question. I will give you my response, and you give me feedback on my tone, structure, and STAR method alignment.",
    "Strengths/Weaknesses\nAnswer hr behavioral questions": "Help me practice answering HR behavioral questions like 'What is your greatest strength?' or 'What is your greatest weakness?'. Let's do it step-by-step.",
    "STAR Method\nStructure behavioral answers": "Teach me how to structure my answers using the STAR method (Situation, Task, Action, Result) with a concrete example, then give me a practice prompt.",
    "Why Should We Hire You?\nAlign your value proposition": "Help me practice the 'Why should we hire you?' question. Tell me the key components of a great answer, then let me pitch my background.",
    
    "Role Prep\nMarketing or Product Management": "Let's do a mock interview for a non-technical role like Product Management or Marketing. Ask me a common situational or case question.",
    "Finance Analyst\nPrep for valuation & models": "Let's practice common corporate finance or investment banking questions, focusing on valuation models, DCF, and financial statements.",
    "Present Portfolio\nShowcase design & user experience": "Guide me on how to present my UI/UX or design portfolio during an interview. What are the key stages, and how do I address user-centric decisions?",
    "Sales Interview\nPractice pitching & closing": "Let's do a mock sales interview. Ask me to sell a product to you, and test my objection handling, discovery, and closing techniques.",
    
    "Mock Session\nFull technical + soft skills mock": "Let's start a full, comprehensive mock interview session combining technical concepts, system design, and soft skills.",
    "Resume Review\nPrep bullet point explanations": "Let's practice explaining the bullet points on my resume. I'll provide an experience, and you show me how to present it impactfully.",
    "Top 10 Questions\nMaster the standard questions": "Give me the list of the top 10 most common interview questions across technical and behavioral rounds, and let's practice them one by one.",
    "Prep Strategy\nCreate a custom interview roadmap": "Help me design a personalized 30-day interview preparation roadmap. Ask me about my target role, experience level, and timeline."
}

STARTER_ICONS = {
    # Technical
    "Data Structures Quiz": ":material/psychology:",
    "LeetCode Problem": ":material/code:",
    "System Design": ":material/schema:",
    "Big O Notation": ":material/analytics:",
    # HR
    "HR Practice": ":material/forum:",
    "Strengths/Weaknesses": ":material/fitness_center:",
    "STAR Method": ":material/track_changes:",
    "Why Should We Hire You?": ":material/work:",
    # Non-Tech
    "Role Prep": ":material/trending_up:",
    "Finance Analyst": ":material/payments:",
    "Present Portfolio": ":material/palette:",
    "Sales Interview": ":material/handshake:",
    # Mixed
    "Mock Session": ":material/rocket_launch:",
    "Resume Review": ":material/description:",
    "Top 10 Questions": ":material/mic:",
    "Prep Strategy": ":material/tips_and_updates:",
}

def show():
    user = st.session_state.user
    apply_theme()
    _render_sidebar(user)
    _render_chat_area(user)

def _render_sidebar(user):
    with st.sidebar:
        # 1. Top Brand Row (FAQBot + Theme Toggle on the right)
        with st.container():
            st.markdown('<div class="sidebar-brand-container"></div>', unsafe_allow_html=True)
            col_brand, col_theme = st.columns([3, 1])
            with col_brand:
                st.markdown('<div style="font-weight: 700; font-size: 18px; display:flex; align-items:center; gap:8px; color: var(--text);">'
                            '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; color: var(--accent);"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8.01" y2="16"/><line x1="16" y1="16" x2="16.01" y2="16"/></svg>'
                            'FAQBot</div>', unsafe_allow_html=True)
            with col_theme:
                theme = st.session_state.get("theme", "dark")
                theme_icon = ":material/light_mode:" if theme == "dark" else ":material/dark_mode:"
                if st.button("", icon=theme_icon, key="sidebar_theme_toggle"):
                    st.session_state.theme = "light" if theme == "dark" else "dark"
                    st.rerun()

        # 2. New chat + Search chats buttons
        with st.container():
            st.markdown('<div class="sidebar-new-chat-btn"></div>', unsafe_allow_html=True)
            if st.button("New chat", icon=":material/edit:", key="new_chat_btn", use_container_width=True):
                st.session_state.messages = []
                st.session_state.current_chat_id = None
                st.session_state.total_tokens = 0
                st.session_state.search_query = ""
                st.rerun()

        st.session_state.search_query = ""

        # Subtle separator
        st.markdown("<hr style='margin: 8px 8px; border: 0; border-top: 1px solid var(--border); opacity: 0.4;'>", unsafe_allow_html=True)

        # 3. RECENTS Header (Recents ∨)
        st.markdown('<div style="font-size:14px; font-weight:600; color:var(--text); padding: 0px; margin: 16px 0 12px 0px; display: flex; align-items: center; gap: 4px;">Recents ∨</div>', unsafe_allow_html=True)

        # Scrollable container for recent history logs
        history_placeholder = st.container()
        with history_placeholder:
            st.markdown('<div class="history-logs-container"></div>', unsafe_allow_html=True)
            try:
                history = load_chat_history(user["id"])
                search_q = st.session_state.get("search_query", "").lower().strip()
                if search_q:
                    history = [c for c in history if search_q in c.get("title", "").lower()]
                if not history:
                    st.caption("  No chats yet. Start a session!")

                for chat in history:
                    chat_id = str(chat["_id"])
                    is_active = (st.session_state.current_chat_id == chat_id)
                    title = chat.get("title", "Untitled")

                    with st.container():
                        marker = 'active-chat-row' if is_active else 'history-item-row'
                        st.markdown(f'<div class="{marker}"></div>', unsafe_allow_html=True)

                        col_title, col_dots = st.columns([5, 1])
                        with col_title:
                            if st.button(title, key=f"hist_{chat_id}", use_container_width=True):
                                loaded = load_chat(chat_id)
                                if loaded:
                                    st.session_state.messages = loaded.get("messages", [])
                                    st.session_state.current_chat_id = chat_id
                                    st.session_state.interview_type = loaded.get("interview_type", "Technical")
                                    st.session_state.total_tokens = loaded.get("total_tokens", 0)
                                    st.rerun()
                        with col_dots:
                            with st.popover("···", use_container_width=False):
                                if st.button("Delete", icon=":material/delete:", key=f"del_{chat_id}", use_container_width=True):
                                    delete_chat(chat_id)
                                    if st.session_state.current_chat_id == chat_id:
                                        st.session_state.messages = []
                                        st.session_state.current_chat_id = None
                                    st.rerun()

            except Exception as e:
                st.caption(f"History unavailable: {str(e)[:40]}")

        # Spacer to push bottom contents
        st.markdown("<div style='flex-grow: 1; min-height: 80px;'></div>", unsafe_allow_html=True)

        # Generate Avatar Initials (e.g. "SK")
        initials = ""
        name_parts = user['name'].split()
        if len(name_parts) >= 2:
            initials = (name_parts[0][0] + name_parts[-1][0]).upper()
        elif len(name_parts) == 1:
            initials = name_parts[0][:2].upper()
        else:
            initials = "SK"

        # Sticky Bottom Footer container
        with st.container():
            st.markdown('<div class="sidebar-footer-container"></div>', unsafe_allow_html=True)
            col_avatar, col_name = st.columns([1.2, 3.8])
            with col_avatar:
                st.markdown(f'<div class="user-avatar">{initials}</div>', unsafe_allow_html=True)
            with col_name:
                role = user.get("role", "Go")
                st.markdown(f"""
                <div class="profile-card-text">
                    <div class="profile-card-name">{user['name']}</div>
                    <div class="profile-card-plan">{role}</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Logout button directly below the profile info (full width inline)
            if st.button("Logout", icon=":material/logout:", key="menu_logout", use_container_width=True):
                logout()

def _render_chat_area(user):
    interview_type = st.session_state.interview_type

    # 2. Fixed Top Header Bar (Float viewport, aligned to sidebar)
    st.markdown(f"""
    <div class="fixed-top-header">
        <div style="font-weight: 700; font-size: 16px; display:flex; align-items:center; gap:8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; color: var(--accent);"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
            <span>Interview Prep AI</span>
            <span style="font-size: 11px; font-weight: 500; color: var(--accent); background: rgba(16,163,127,0.1); border: 1px solid var(--accent); border-radius: 12px; padding: 2px 10px; margin-left: 8px;">{interview_type}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Render Export/Share button if we have messages
    if st.session_state.messages:
        col_dummy, col_download, col_share = st.columns([10, 1, 1])
        with col_download:
            md_content = export_chat_as_text(st.session_state.messages, f"Interview_Prep_{st.session_state.interview_type}")
            st.download_button(
                label="",
                data=md_content,
                file_name=f"chat_{st.session_state.interview_type.lower()}_{int(time.time())}.md",
                mime="text/markdown",
                icon=":material/download:",
                key="download_history_btn",
                help="Download chat history",
                use_container_width=True
            )
        with col_share:
            if st.button(label="", icon=":material/ios_share:", key="share_history_btn", help="Share chat", use_container_width=True):
                st.session_state["_clipboard"] = md_content
                st.session_state["_clipboard_key"] = "share_history"
                st.rerun()

    # Starter prompts if no messages - padding-top lowered to remove blank space
    if not st.session_state.messages:
        st.markdown("""
        <div style='text-align:center; padding-top:10px; max-width:768px; margin:0 auto;'>
            <h1 style='font-size: 2.3rem; font-weight: 700; letter-spacing: -1px; margin-bottom: 8px;'>What can I help with?</h1>
        </div>
        """, unsafe_allow_html=True)

        # Tab selector for interview types
        st.markdown('<div style="max-width: 600px; margin: 12px auto 20px auto;">', unsafe_allow_html=True)
        cols_tab = st.columns(4)
        type_icons = {
            "Technical": ":material/code:",
            "HR": ":material/forum:",
            "Non-Tech": ":material/assignment:",
            "Mixed": ":material/extension:"
        }
        for idx, t_name in enumerate(INTERVIEW_TYPES):
            with cols_tab[idx]:
                is_selected = (st.session_state.interview_type == t_name)
                btn_icon = type_icons.get(t_name, ":material/extension:")
                if st.button(t_name, icon=btn_icon, key=f"tab_select_{t_name}", type="primary" if is_selected else "secondary", use_container_width=True):
                    st.session_state.interview_type = t_name
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align:center; max-width:768px; margin:0 auto 12px auto;'>
            <p style='color:var(--text-muted); font-size:15px;'>Select a starter topic to practice with your AI coach:</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="starter-container">', unsafe_allow_html=True)
        starters = STARTER_QUESTIONS.get(interview_type, STARTER_QUESTIONS["Mixed"])
        cols = st.columns(2)
        for i, q in enumerate(starters):
            with cols[i % 2]:
                title = q.split('\n')[0].strip()
                icon = STARTER_ICONS.get(title, ":material/help:")
                if st.button(q, icon=icon, key=f"starter_{i}", use_container_width=True):
                    # Get the rich, detailed prompt from our mapping
                    rich_prompt = STARTER_PROMPTS_MAPPING.get(q, q)
                    _send_message(rich_prompt, user)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat messages list
    for idx, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"], avatar=":material/person:" if msg["role"] == "user" else ":material/smart_toy:"):
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user-message">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])
                # Footer row: timestamp + copy button
                ts = msg.get("timestamp", datetime.now().strftime("%I:%M %p"))
                col_time, col_copy = st.columns([6, 1])
                with col_time:
                    st.markdown(f'<div class="msg-time">{ts}</div>', unsafe_allow_html=True)
                with col_copy:
                    if st.button("", icon=":material/content_copy:", key=f"copy_{idx}", help="Copy message"):
                        st.session_state["_clipboard"] = msg["content"]
                        st.session_state["_clipboard_key"] = f"copy_{idx}"
                        st.rerun()

    # Chat input
    if prompt := st.chat_input("Ask your interview question..."):
        _send_message(prompt, user)

    # Footer warning note (matches ChatGPT)
    st.markdown("""
    <div class="chat-footer-text">
        Interview Prep AI can make mistakes.
    </div>
    """, unsafe_allow_html=True)

    # Global auto-copy handler
    if st.session_state.get("_clipboard_key") is not None:
        b64 = base64.b64encode(st.session_state["_clipboard"].encode("utf-8")).decode()
        components.html(f"""
        <script>
        (function() {{
            var text = new TextDecoder().decode(
                Uint8Array.from(atob('{b64}'), c => c.charCodeAt(0))
            );
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text);
            }} else {{
                var ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                document.body.appendChild(ta);
                ta.focus(); ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
            }}
        }})();
        </script>
        """, height=0)
        st.toast("Copied to clipboard!", icon=":material/check:")
        st.session_state["_clipboard_key"] = None

def _send_message(prompt: str, user: dict):
    # Ensure default model is always set behind the scenes
    if "model" not in st.session_state or not st.session_state.model:
        st.session_state.model = "llama-3.3-70b-versatile"
    elif st.session_state.model == "llama3-70b-8192":
        st.session_state.model = "llama-3.3-70b-versatile"

    now = datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({"role": "user", "content": prompt, "timestamp": now})

    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(f'<div class="chat-user-message">{prompt}</div>', unsafe_allow_html=True)

    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        with st.spinner("Thinking..."):
            try:
                response, tokens = chat_with_groq(
                    st.session_state.messages,
                    st.session_state.model,
                    st.session_state.interview_type
                )
                st.session_state.total_tokens += tokens
            except Exception as e:
                response = f"**Error:** {str(e)}\n\nMake sure your GROQ_API_KEY is set in the .env file."
                tokens = 0

        st.markdown(response)
        ts = datetime.now().strftime("%I:%M %p")
        col_time, col_copy = st.columns([6, 1])
        with col_time:
            st.markdown(f'<div class="msg-time">{ts}</div>', unsafe_allow_html=True)
        with col_copy:
            live_key = f"copy_live_{len(st.session_state.messages)}"
            if st.button("", icon=":material/content_copy:", key=live_key, help="Copy message"):
                st.session_state["_clipboard"] = response
                st.session_state["_clipboard_key"] = live_key

    st.session_state.messages.append({"role": "assistant", "content": response, "timestamp": datetime.now().strftime("%I:%M %p")})

    # Auto-save to MongoDB
    try:
        save_chat(user["id"], st.session_state.messages)
    except Exception:
        pass

    st.rerun()

