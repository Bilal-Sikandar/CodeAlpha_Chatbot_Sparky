import streamlit as st
from matcher import FAQMatcher

# Page config
st.set_page_config(page_title="Sparky - AI FAQ Chatbot", page_icon="⚡", layout="centered")

# Title and description
st.markdown(
    """
    <div style="text-align:center; padding: 10px;">
        <h1 style="color:#20B2AA; font-family: 'Trebuchet MS', sans-serif; letter-spacing:1px;">
            ⚡ Sparky ⚡
        </h1>
        <p style="font-size:16px; color:#5f5f5f; max-width:600px; margin:auto;">
            Meet <b>Sparky</b>, your AI-powered assistant ⚡ trained on frequently asked questions about Artificial Intelligence.  
            Ask anything about AI concepts, applications, and trends — Sparky will spark up the answers instantly!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load matcher
matcher = FAQMatcher("faqs.json")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.chat_input("Type your AI question here...")

if user_input:
    answer = matcher.get_answer(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Sparky", answer))

# Chat container
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("💬 Conversation with Sparky")

chat_container = st.container()

with chat_container:
    for sender, message in st.session_state.history:
        if sender == "You":
            # User Question bubble → Light Grey
            st.markdown(
                f"""
                <div style="display:flex; justify-content:flex-end; margin:5px;">
                    <div style="background:#E6E6E6; padding:10px 15px; border-radius:15px; 
                                max-width:70%; text-align:right; 
                                color:#333333; 
                                font-family:'Segoe UI', sans-serif;
                                box-shadow:0 2px 5px rgba(0,0,0,0.05);">
                        <b>{sender}:</b> {message}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Bot Answer bubble → Sea Green to Blue gradient
            st.markdown(
                f"""
                <div style="display:flex; justify-content:flex-start; margin:5px;">
                    <div style="background: linear-gradient(135deg, #20B2AA, #87CEFA); 
                                padding:10px 15px; border-radius:15px; 
                                max-width:70%; text-align:left; 
                                color:white;
                                font-family:'Segoe UI', sans-serif;
                                box-shadow:0 2px 5px rgba(0,0,0,0.05);">
                        <b>{sender}:</b> {message}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
