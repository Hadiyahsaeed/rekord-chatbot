import streamlit as st
import sys
import os

# Ensure Python can see and import your rag_backend.py file
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rag_backend import ask_rag_bot

# Set up a sleek web page config
st.set_page_config(page_title="Local AI Lab Terminal", page_icon="🤖", layout="centered")
st.title("🤖 Local AI Lab Terminal")
st.caption("Running completely offline on Llama 3.2 with RAG Database")

# Initialize chat history if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages from history on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept real-time user input
if prompt := st.chat_input("Ask me about any product or medicine..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to session history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate real-time assistant response
    with st.chat_message("assistant"):
        with st.spinner("Scanning local pharmaceutical catalog..."):
            # Send the question to your freshly working RAG backend
            response = ask_rag_bot(prompt)
            st.markdown(response)
        
    # Add assistant response to session history
    st.session_state.messages.append({"role": "assistant", "content": response})