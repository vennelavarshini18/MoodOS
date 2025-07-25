import streamlit as st
import uuid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mic_input import record_audio
from emotion_predictor import predict_emotion  
from plot import show_confidence_chart, show_waveform
from journal import save_to_journal, show_journal

st.set_page_config(page_title="🎙️ Track your mood", layout="centered")
st.markdown("""
    <h1 style='text-align: center;'>🎧 MoodOS</h1>
    <p style='text-align: center;'>Your operating system for emotional clarity, powered by deep learning.</p>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ Options")
option = st.sidebar.radio("Choose an action:", ["Upload Audio", "Record Mic", "View Journal"])

if option == "Upload Audio":
    st.markdown("### 🎵 Upload a WAV file to begin:")
    uploaded_file = st.file_uploader("Upload your speech sample", type=["wav"], label_visibility="collapsed")

    if uploaded_file:
        unique_id = str(uuid.uuid4())
        audio_dir = "audio"
        os.makedirs(audio_dir, exist_ok=True)
        audio_path = os.path.join(audio_dir, f"{unique_id}.wav")

        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())

        st.audio(audio_path, format="audio/wav")
        show_waveform(audio_path)

        emotion, prediction = predict_emotion(audio_path)

        st.markdown("### 🧠 Detected Emotion: **<span style='color:#3c82f6;'>{}</span>**".format(emotion.upper()), unsafe_allow_html=True)

        with st.expander("💡 Click for personalized suggestions", expanded=True):
            from utils.suggestions import emotion_reactions
            for idea in emotion_reactions.get(emotion.lower(), ["💪 Stay strong and take care of yourself."]):
                st.markdown(f"- {idea}")

        st.markdown("### 📊 Emotion Probabilities")
        show_confidence_chart(prediction)

        save_to_journal(emotion, prediction)

elif option == "Record Mic":
    st.markdown("### 🎤 Record from Microphone")
    if st.button("Start Recording"):
        file_path = record_audio()
        st.audio(file_path, format="audio/wav")
        show_waveform(file_path)

        emotion, prediction = predict_emotion(file_path)

        st.text("Raw prediction vector:")
        st.json(prediction)

        st.markdown("### 🧠 Detected Emotion: **<span style='color:#3c82f6;'>{}</span>**".format(emotion.upper()), unsafe_allow_html=True)

        with st.expander("💡 Click for personalized suggestions", expanded=True):
            from utils.suggestions import emotion_reactions
            for idea in emotion_reactions.get(emotion.lower(), ["💪 Stay strong and take care of yourself."]):
                st.markdown(f"- {idea}")

        st.markdown("### 📊 Emotion Probabilities")
        show_confidence_chart(prediction)

        save_to_journal(emotion, prediction)

elif option == "View Journal":
    show_journal()