import os
from dotenv import load_dotenv
import streamlit as st
from pdf_processing.extractor import extract_text_from_pdf
from chatbot.bot import Chatbot

def set_page_config():
    st.set_page_config(
        page_title="Chatbot",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="expanded"
    )

def apply_custom_css():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput > div > div > input {
            font-size: 1.2rem;
            padding: 1rem;
            border: 2px solid #1E88E5;
            border-radius: 8px;
        }
        .stButton > button {
            width: 100%;
            height: 3rem;
            font-size: 1.2rem;
            margin-top: 1rem;
            background-color: #1E88E5;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #1565C0;
        }
        .chat-message {
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            background-color: #e3f2fd;
            border: 1px solid #90caf9;
        }
        .chat-title {
            text-align: center;
            color: #1E88E5;
            margin-bottom: 2rem;
            font-size: 2rem;
            font-weight: bold;
        }
        .sidebar-info {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #90caf9;
        }
        </style>
    """, unsafe_allow_html=True)

def create_interface(chatbot):
    st.markdown('<h1 class="chat-title">📚 ChatbotF</h1>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown('<h2 class="chat-title">👋 ¡Hola! Espero que tengas bonito día</h2>', unsafe_allow_html=True)


    # Barra lateral con información
    with st.sidebar:
        st.markdown("### Sobre el Chatbot")
        st.markdown("""
        <div class="sidebar-info">
        Este chatbot está diseñado para responder preguntas sobre conceptos contables básicos.
        <br><br>
        Desarrollado por la estudiante fernanda
        </div>
        """, unsafe_allow_html=True)

    # Área principal de chat
    chat_container = st.container()
    with chat_container:
        question = st.text_input("", 
                                 key="user_question")

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("📤"):
                if question.strip():
                    with st.spinner('Procesando tu pregunta...'):
                        response = chatbot.chat(question)

                    st.markdown(f"""
                    <div class="chat-message">
                        <strong>🙋 Tú:</strong><br>{question}
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="chat-message">
                        <strong>🤖 Chatbot:</strong><br>{response}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning("⚠️ Por favor, escribe una pregunta válida.")

def main():
    set_page_config()
    apply_custom_css()
    chatbot = Chatbot()
    create_interface(chatbot)

if __name__ == "__main__":
    main()