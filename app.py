import streamlit as st
import text2emotion as te
import nltk
from nltk.tokenize import sent_tokenize
import os

# Ensure NLTK uses pre-downloaded punkt tokenizer
nltk_data_path = os.path.expanduser('~/.nltk_data')
nltk.data.path.append(nltk_data_path)

# Web App Setup
st.set_page_config(page_title="MindScribe - AI Thought Notepad", page_icon="🧠")
st.title("🧠 MindScribe – AI Thought-to-Notes")
st.markdown("Type your thoughts below. MindScribe will summarize them and detect your emotion. 📝🧠")

# Summarize Function (using first 2 sentences)
def summarize_text(text):
    sentences = sent_tokenize(text)
    if len(sentences) <= 2:
        return text
    return ' '.join(sentences[:2])

# User Input
user_input = st.text_area("🗣️ Your Thoughts Here", height=200)

# On Button Click
if st.button("🧠 Generate Smart Note"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        summary = summarize_text(user_input)
        emotions = te.get_emotion(user_input)
        main_emotion = max(emotions, key=emotions.get)

        suggestions = {
            "Happy": "Keep spreading positivity! 🌈",
            "Sad": "Take a short walk or talk to a friend. You got this 💪",
            "Angry": "Take deep breaths and try journaling your thoughts ✍️",
            "Fear": "You're stronger than your fears. Face them step by step 💫",
            "Surprise": "Embrace new things with curiosity 🤩"
        }

        st.success(f"📝 **Summary:** {summary}")
        st.info(f"💡 **Detected Emotion:** {main_emotion}")
        st.write(f"✅ **Suggestion:** {suggestions.get(main_emotion, 'Stay mindful and take care!')}")
