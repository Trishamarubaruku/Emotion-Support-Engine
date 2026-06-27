import streamlit as st
import google.generativeai as genai

# 1. Configuration
# Replace 'YOUR_API_KEY' with your actual key from Google AI Studio
API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI Setup
st.set_page_config(page_title="AI Learning Support", page_icon="🎓")
st.title("🎓 AI Learning Support Engine")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Logic
def get_guidance(user_query):
    # Mocking emotion detection for simplicity
    emotion = "Confused" 
    prompt = f"The student is feeling {emotion}. Their query is: '{user_query}'. Provide a 3-step supportive guide."
    response = model.generate_content(prompt)
    return response.text

# 4. Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Describe your study challenge..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_guidance(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})