
#step1 : Install Google SDK > pip install -q -U google-genai
#step2 : Import Google GenAI SDK > pip install google-generativeai
#step3 : Writer a message on the screen
#step4 : Added sidebar to take Gemini API key and model as input
#step5 : Grant the user to select model and enter their Gemini API key

import streamlit as st
import google.generativeai as genai

st.logo("https://playwright.dev/img/playwright-logo.svg",size="large")

st.sidebar.title("Think Chatbot Settings")

with st.sidebar:
    model = st.selectbox("Select Model:", ["gemini-2.5-flash", "gemini-1.5-turbo", "gemini-1.5-flash"], index=0, key="gemini_model")
    gemini_api_key = st.text_input("Enter your Gemini API Key:", key="gemini_api_key", type="password")

st.title("Think Chatbot with Google GenAI")
st.caption("This is a simple chatbot using Google GenAI")

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
    if not gemini_api_key:
        st.info("Please enter your Gemini API Key in the sidebar.")
        st.stop()
        
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel(model)
        
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.chat_message("assistant").write(response.text)
    
    

    