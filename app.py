import streamlit as st
import base64
from backend.gemini_client import GeminiClient
from backend.memory import ConversationMemory
from config.settings import SYSTEM_PROMPT

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎓",
    layout="centered"
)

# ---------------- BACKGROUND IMAGE ----------------
def set_background(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            .block-container {{
                background: rgba(255, 255, 255, 0.88);
                padding: 2rem;
                border-radius: 15px;
                backdrop-filter: blur(6px);
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass  # Prevent crash if image missing


# Set background image (place image inside assets/)
set_background("assets/background.png")

# ---------------- TITLE ----------------
st.title("🎓 AI Career Advisor Chatbot")

# ---------------- SESSION STATE ----------------
if "client" not in st.session_state:
    st.session_state.client = GeminiClient()

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask your career question...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)

    # Save user message
    st.session_state.memory.add_user_message(user_input)

    # Get conversation (token optimized)
    conversation_context = st.session_state.memory.get_conversation()[-2000:]

    # Build prompt
    final_prompt = f"""
{SYSTEM_PROMPT}

Recent Conversation:
{conversation_context}

User: {user_input}
"""

    # Generate response safely
    with st.spinner("Thinking..."):
        response = st.session_state.client.generate_response(final_prompt)

    # Save bot message
    st.session_state.memory.add_bot_message(response)

    # Show assistant reply
    st.chat_message("assistant").markdown(response)