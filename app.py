import streamlit as st
import google.generativeai as genai
import datetime
from processor import get_emotion_prediction
from logger import save_to_csv

# 1. FIX: Use st.secrets instead of hardcoding.
# Make sure you have added API_KEY = "your_key" in Streamlit Cloud Settings > Secrets
try:
    api_key = st.secrets["API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    # Fallback to hardcoded key only for testing if secrets are missing
    # Use this, NOT the key itself!
    genai.configure(api_key=st.secrets["API_KEY"])

models = [m for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
model = genai.GenerativeModel(models[0].name)
print(f"Using model: {models[0].name}")

# Professional UI Setup
st.set_page_config(page_title="CELA Engine", layout="wide")
st.title("🎓 AI Learning Support Engine")
st.sidebar.header("System Architecture")
st.sidebar.info("Integrating Sentiment Analysis with LLM-based Pedagogical Guidance for optimized student support.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Interaction Flow
if prompt := st.chat_input("How are you feeling about your study today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Analyze Sentiment
    emotion = get_emotion_prediction(prompt)
    save_to_csv({"text": prompt, "emotion": emotion, "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    
    # Professional AI Response
    full_prompt = f"The student is feeling {emotion}. They said: '{prompt}'. Act as a supportive, professional mentor. Provide a warm, short, and encouraging response that validates their state and offers a constructive next step for their learning."
    
    # 3. FIX: Simple call without complex parameters that trigger InvalidArgument
    response = model.generate_content(full_prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})

# Render UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
