import matplotlib.pyplot as plt
import streamlit as st
import librosa
import librosa.display
import pandas as pd

def show_waveform(file_path):
    y, sr = librosa.load(file_path)
    fig, ax = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set_title("Audio Waveform")
    st.pyplot(fig)

def show_confidence_chart(predictions_dict):
    df = pd.DataFrame({
        "Emotion": list(predictions_dict.keys()),
        "Probability": list(predictions_dict.values())
    }).sort_values(by="Probability", ascending=False)
    st.bar_chart(data=df.set_index("Emotion"))