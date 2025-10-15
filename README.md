# Simple Chatbot Web App

A minimal web-based chatbot built in Python using **Flask** and **Hugging Face Transformers**.  
This project demonstrates how to integrate an open-source **LLM** into a backend server and connect it to a simple front-end interface.

---

## Features
- Conversational AI using **facebook/blenderbot-400M-distill**
- Backend built with **Flask** and **Flask-CORS**
- Front-end chat interface (HTML, CSS, JS)
- Supports real-time message exchange between browser and AI model
- Modular architecture (can be upgraded with new models)

---

## Tech Stack
- **Python 3.10+**
- **Flask**
- **Hugging Face Transformers**
- **PyTorch**
- **HTML / CSS / JavaScript**

---

## Setup & Run

1. **Clone the repository**
   git clone https://github.com/junjiekevin/simple-chatbot.git
   cd simple-chatbot/LLM_application_chatbot

2. **Create a virtual environment**
    python -m venv my_env
    source my_env/bin/activate  # or my_env\Scripts\activate on Windows


3. **Install dependencies**
pip install -r requirements.txt

4. **Run the app**
flask --app app run

5. **Open your browser**
Visit: http://127.0.0.1:5000/
