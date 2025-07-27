import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os
import datetime
import soundfile as sf
import librosa
import streamlit as st

def record_audio(duration=4, fs=16000, output_dir="audio"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(output_dir, f"mic_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.wav")

    try:
        st.toast("Recording started...", icon="🎙️")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
        sd.wait()
        recording = recording.squeeze()

        # Normalize audio to -1 to 1
        max_val = np.max(np.abs(recording))
        if max_val > 0:
            recording = recording / max_val

        sf.write(filename, recording, fs)
        st.toast("Recording complete!", icon="✅")

    except Exception as e:
        st.error(f"Microphone recording failed: {e}")
        return None

    return filename