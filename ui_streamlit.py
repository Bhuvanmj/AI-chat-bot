import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 Free AI Chatbot (Groq + FastAPI)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        res = requests.post("http://localhost:8000/chat", json={"message": user_input})
        bot_reply = res.json().get("response", "")
        st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
