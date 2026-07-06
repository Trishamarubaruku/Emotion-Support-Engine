# 💙 Emotion Support Engine

An AI-powered, 24/7 empathetic conversational web application designed to provide immediate emotional comfort and non-judgmental support. 
Built using **Python**, **Streamlit**, and the **Google Gemini API**.

## 📌 Features

- 💬 **Real-time Conversational UI:** Clean, chat-like interface built natively with Streamlit.
- 🧠 **AI Emotion Analysis:** Processes user text via Gemini API to generate highly empathetic responses.
- 📚 **Contextual Chat Memory:** Maintains active chat history utilizing Streamlit's session state.
- 🔄 **Session Reset:** Instantly wipe chat history for privacy and a fresh start.
- 🌍 **Multilingual Support:** Understands and responds to emotional prompts in various languages.
- 📱 **Responsive Web Design:** Seamlessly adapts to both desktop and mobile screens.
- 🔒 **Secure API Routing:** Protects API keys using Streamlit's local secret management.
- 🛡️ **Error Handling & Fallbacks:** Prevents application crashes during API timeouts.

## 🏗️ Project Architecture

User
  ↓
Streamlit Frontend (Web Interface)
  ↓
Python Backend (State Management & Logic)
  ↓
Google Gemini API (Generative AI Engine)

📂 Project Structure


Emotion_Support_Engine/
│
├── .streamlit/
│   └── secrets.toml         # Secure configuration file for API keys
│
├── app.py                   # Main Streamlit application source code
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation

⚙️ Technologies Used

Technology,Purpose
Python 3.9+,Core Programming Language
Streamlit,Frontend UI & Backend State Management
Google Gemini API,Generative AI & Natural Language Processing
Git & GitHub,Version Control
Streamlit Community Cloud,Web Hosting & Deployment

🚀 Installation & Setup

1. Clone the Repository

git clone https://github.com/Trishamarubaruku/Emotion-Support-Engine
cd Emotion_Support_Engine

2. Create and Activate Virtual Environment

Windows:
python -m venv venv
.\venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt
(Note: Ensure streamlit and google-generativeai are in your requirements.txt)

4. Configure API Key securely
Create a hidden folder named .streamlit in your root directory, and create a file inside it named secrets.toml. Add your Google Gemini API key:

API_KEY = "your_google_gemini_api_key_here"

▶️ Run the Application

Start the Streamlit server:

python -m streamlit run app.py

The application will automatically open in your default browser at http://localhost:8501

🌟 Future Enhancements

Voice-to-Text Integration: Allow users to speak their feelings naturally for better accessibility.

Crisis Detection Routing: Automatically route severe distress keywords to professional human helplines.

Personalized Support Dashboard: Add secure user accounts (OAuth) to track mood trends over time.

Native Mobile App Deployment: Convert the web application into iOS/Android apps for global reach.

👨‍💻 Author

Trisha Marubaruku

trishamarubaruku@gmail.com
GitHub:https://github.com/Trishamarubaruku/Emotion-Support-Engine


Akshaya Geddam

akshayageddam93@gmail.com



Alekhya Kapudasi

alekhyak321@gmail.com



Bhuvaneswari Manda

bhuvana7709@gmail.com



Ghantasala Vamsi Krishna

hackervamsi3@gmail.com


📜 License

This project was developed for educational purposes as part of the AI/ML and GenAI Track.






