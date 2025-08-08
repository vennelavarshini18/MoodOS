# main.py
import os
<<<<<<< HEAD
import sys
import uuid
import streamlit as st

# 1) Page config MUST be first
st.set_page_config(page_title="🎙️ Track your mood", layout="wide")

# 2) Inject CSS immediately (before other UI renders)
# Try to locate the style.css in the .streamlit folder relative to this file
css_paths = [
    os.path.join(os.path.dirname(__file__), ".streamlit", "style.css"),
    ".streamlit/style.css"
]

css_loaded = False
for p in css_paths:
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            css_loaded = True
            break
        except Exception as e:
            st.warning(f"Failed to load CSS from {p}: {e}")
if not css_loaded:
    st.warning("Could not find .streamlit/style.css — create it as shown in the instructions.")

# 3) Add project path so local imports work
=======

>>>>>>> 9b1d091c3a4408c968e85b98da94acdff3c3de6e
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 4) Import app logic (after CSS injection)
from mic_input import record_audio
from emotion_predictor import predict_emotion
from plot import show_confidence_chart, show_waveform
from journal import save_to_journal, show_journal

<<<<<<< HEAD
# 5) Theme detection + accent
theme = st.get_option("theme.base") or "light"

accent = "#06B6D4"  # turquoise (same for both light/dark to preserve brand)

# Hero Header
=======
st.set_page_config(page_title="🎙️ Track your mood", layout="centered")

>>>>>>> 9b1d091c3a4408c968e85b98da94acdff3c3de6e
st.markdown("""
    <style>
      .hero-container {
        background: linear-gradient(
            135deg,
            rgba(6,182,212,0.10),  /* lighter teal */
            rgba(30,64,175,0.10)   /* lighter blue */
        );
        padding: 2.8rem;
        border-radius: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
        max-width: 850px;
        margin: auto;
        border: 1px solid rgba(255,255,255,0.12);
        backdrop-filter: blur(5px);
    }
        .hero-title {
            font-size: 3.4em;
            font-weight: 900;
            background: linear-gradient(90deg, #06B6D4, #3B82F6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.4rem;
            text-shadow: 0 2px 8px rgba(0,0,0,0.25);
        }
        .hero-subtitle {
            font-size: 1.2em;
            font-weight: 400;
            color: rgba(255,255,255,0.95);
            line-height: 1.6;
        }
      .stApp {
            background: linear-gradient(
                135deg,
                #d0f4ff 0%,
                #a0e8ff 25%,
                #80dfff 50%,
                #a0e8ff 75%,
                #d0f4ff 100%
            );
            background-attachment: fixed;
            background-size: cover;
        }
    </style>
    <div class="hero-container">
        <h1 class="hero-title">🎧 MoodOS</h1>
        <p class="hero-subtitle">
            Your operating system for emotional clarity,<br>
            powered by deep learning.
        </p>
    </div>
""", unsafe_allow_html=True)




# 7) Tabs + app body
tabs = st.tabs(["🎵 Upload Audio", "🎤 Record Mic", "📖 View Journal"])

# ========== Upload Audio ==========
with tabs[0]:
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

        st.success(f"✅ Emotion Detected: {emotion.upper()}")

        st.markdown(f"### 🧠 Detected Emotion: <span style='color:{accent}; font-weight:bold;'>{emotion.upper()}</span>", unsafe_allow_html=True)

        with st.expander("💡 Click for personalized suggestions", expanded=True):
            from utils.suggestions import emotion_reactions
            for idea in emotion_reactions.get(emotion.lower(), ["💪 Stay strong and take care of yourself."]):
                st.markdown(f"- {idea}")

        st.markdown("### 📊 Emotion Probabilities")
        show_confidence_chart(prediction)

        save_to_journal(emotion, prediction)

# ========== Record Mic ==========
with tabs[1]:
    st.markdown("### 🎤 Record from Microphone")

    try:
        if st.button("Start Recording"):
            file_path = record_audio()
            if file_path:
                st.audio(file_path, format="audio/wav")
                show_waveform(file_path)

<<<<<<< HEAD
        st.success(f"✅ Emotion Detected: {emotion.upper()}")

        st.markdown(f"### 🧠 Detected Emotion: <span style='color:{accent}; font-weight:bold;'>{emotion.upper()}</span>", unsafe_allow_html=True)
=======
                emotion, prediction = predict_emotion(file_path)

                st.text("Raw prediction vector:")
                st.json(prediction)
>>>>>>> 9b1d091c3a4408c968e85b98da94acdff3c3de6e

                st.markdown("### 🧠 Detected Emotion: **<span style='color:#3c82f6;'>{}</span>**".format(emotion.upper()), unsafe_allow_html=True)

                with st.expander("💡 Click for personalized suggestions", expanded=True):
                    from utils.suggestions import emotion_reactions
                    for idea in emotion_reactions.get(emotion.lower(), ["💪 Stay strong and take care of yourself."]):
                        st.markdown(f"- {idea}")

                st.markdown("### 📊 Emotion Probabilities")
                show_confidence_chart(prediction)

                save_to_journal(emotion, prediction)
            else:
                st.info("🎙️ Microphone recording is not available in this environment. Try uploading a `.wav` file instead.")
    except Exception as e:
        st.error(f"Microphone feature not available: {e}")

<<<<<<< HEAD
# ========== View Journal ==========
with tabs[2]:
=======
elif option == "View Journal":
>>>>>>> 9b1d091c3a4408c968e85b98da94acdff3c3de6e
    show_journal()
