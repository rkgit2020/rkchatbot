import streamlit as st
import ollama


st.logo("https://playwright.dev/img/playwright-logo.svg",size="large")

st.sidebar.title("Bot Settings")

with st.sidebar:
    model = st.text_input("Model Name:", value="mistral:latest", key="ollama_model")
    st.markdown("make your model available in ollama local server")
    
    

st.title("Local Chatbot")
st.caption("This is a mistral chatbot using Ollma")

# api_key = "AIzaSyCcT3JGGv3mHoR-k3hjh8Qq1NzkqPPFk5k"
# model_name = "gemini-2.5-flash"

# genai.configure(api_key=api_key)
# model = genai.GenerativeModel(model_name)

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello How can i assist you today?"}
    ]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not model:
        st.info("Please enter your Model Name in the sidebar.")
        st.stop()
    
        
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner(text="Thinking..."):
        response = ollama.chat(model=model, messages=st.session_state.messages)
        answer = response['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
    