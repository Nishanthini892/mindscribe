import streamlit as st
from transformers import pipeline
import text2emotion as te

# Use a lightweight summarization model compatible with Streamlit Cloud
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# UI Setup
st.set_page_config(page_title="MindScribe - AI Thought Notepad", page_icon="🧠")
st.title("🧠 MindScribe – AI Thought-to-Notes")
st.markdown("Type your thoughts below. MindScribe will summarize them and detect your emotion. 📝🧠")

# Text Input
user_input = st.text_area("🗣️ Your Thoughts Here", height=200)

# Button to trigger summarization and emotion detection
if st.button("🧠 Generate Smart Note"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        # Summarize the text
        summary = summarizer(user_input, max_length=60, min_length=25, do_sample=False)[0]['summary_text']

        # Detect emotions
        emotions = te.get_emotion(user_input)
        main_emotion = max(emotions, key=emotions.get)

        # Suggestions based on emotion
        suggestions = {
            "Happy": "Keep spreading positivity! 🌈",
            "Sad": "Take a short walk or talk to a friend. You got this 💪",
            "Angry": "Take deep breaths and try journaling your thoughts ✍️",
            "Fear": "You're stronger than your fears. Face them step by step 💫",
            "Surprise": "Embrace new things with curiosity 🤩"
        }

        # Display results
        st.success(f"📝 **Summary:** {summary}")
        st.info(f"💡 **Detected Emotion:** {main_emotion}")
        st.write(f"✅ **Suggestion:** {suggestions.get(main_emotion, 'Stay mindful and take care!')}")

