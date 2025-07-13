
# 🎧 MoodOS: Your Emotional Operating System

**MoodOS** is a deep learning–powered web application that detects your **inner emotional state** using your **voice** — whether through uploading `.wav` files or recording real-time microphone input.

Unlike traditional models that rely on words, **MoodOS is sentence-agnostic** — it listens to **your tone, pitch, rhythm, and frequency** patterns to determine how you feel.

---

## 🚀 Features

- 🎤 **Real-time microphone emotion detection**
- 📁 **.wav file upload support**
- 🧠 **Wav2Vec2 + CNN deep learning backend**
- 📊 **Emotion prediction with confidence scores**
- 📈 **Mood Journal to track your emotional patterns**
- 💡 **Personalized suggestions based on detected emotion**
- 🌈 **Clean UI with waveform visualization**

---

## 🧠 How It Works

MoodOS uses a **pretrained speech embedding model** (Wav2Vec2) to extract powerful voice features like:

- **Prosody**
- **Tone modulation**
- **Spectral energy**
- **Voice intensity**

These are passed through a trained classifier to detect emotions like:

> `Happy, Sad, Angry, Fearful, Neutral, Disgust`

---

## 📂 Folder Structure

```

MoodOS/
├── app/                 # Streamlit UI and main logic
├── model/               # Trained models and label mappings
├── utils/               # Suggestions, plots, and helpers
├── audio/               # Temporary saved recordings
├── logs/                # Journal history (JSON)
├── mic\_input.py         # Microphone recorder
├── emotion\_predictor.py # Wav2Vec2 feature extractor + predictor

```

---

## 💡 Why Use MoodOS?

> Sometimes, we don’t say what we feel — but our voice does.

MoodOS acts like a mirror to your emotions. Whether you're tracking mental health or building emotion-aware applications, this tool helps you understand and visualize **how your voice reflects your mood**.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit**
- **TensorFlow / Keras**
- **Wav2Vec2 (via HuggingFace)**
- **Librosa & SoundDevice**
- **Matplotlib / Plotly for visualizations**

---

## 👩‍💻 Author

By [Vennela Varshini Anasoori](https://github.com/vennelavarshini18)

---

## 🚧 Ongoing Improvements

MoodOS is a work in progress —  it's being actively optimizing the model for **greater emotional accuracy**, **robustness across diverse voices**, and **real-time performance**.

---

## 🤝 Contributions Welcome

If you're passionate about **speech emotion recognition**, **deep learning**, or **audio processing**, and have ideas to improve the model or the app, feel free to fork the repo and submit a pull request.

> 💡 Let’s make MoodOS smarter — together!

