# 🎧 MoodOS: Your Emotional Operating System

**MoodOS** is a deep learning–powered web application that detects your **inner emotional state** from your **voice** — either through uploading `.wav` files or recording in real-time.

Unlike traditional NLP-based sentiment models, **MoodOS is sentence-agnostic** — it listens to **tone, pitch, rhythm, and frequency** patterns rather than the words you say.

---

## Features

- **Real-time microphone emotion detection**
- **.wav file upload support**
- **Custom CNN architecture trained on MFCC features**
- **Emotion prediction with confidence scores**
- **Mood Journal to track your emotional patterns**
- **Personalized suggestions based on detected emotion**
- **Clean UI with waveform and probability visualizations**

---

## How It Works

MoodOS uses **MFCC-based preprocessing** to extract important audio features like:

- **Pitch modulation**
- **Spectral energy**
- **Voice intensity**
- **Mel-frequency cepstral coefficients (MFCCs)**

These are passed into a **Convolutional Neural Network (CNN)** trained on a diverse emotional speech dataset. The model achieved **99.9% validation accuracy** during training.

It detects the following emotions:

> `Happy, Sad, Angry, Fearful, Neutral, Disgust`

---

## App Interface

Here’s a sneak peek into the MoodOS interface:

> https://drive.google.com/file/d/1vKxsZ_m1jYFnsWsRy6CGAJPg_pXPX7xG/view?usp=sharing

-  Real-time Recording Page  
-  Emotion Confidence Chart  
-  Mood Journal Logs  
-  Personalized Suggestion Cards  

---

## Live Demo

> Find here : https://trackyourmood.onrender.com  (wait for few minutes to load)
--- 

## Why Use MoodOS?

> "We don’t always say what we feel — but our voice does."

MoodOS acts like a mirror to your emotions. Whether you're working on mental wellness, emotional journaling, or voice-based AI systems, **MoodOS helps you understand how your voice reflects your feelings**.

---

## Tech Stack

- **Python 3.10+**
- **Streamlit**
- **TensorFlow / Keras**
- **Librosa** for audio feature extraction (MFCCs)
- **SoundDevice** for microphone recording
- **Matplotlib / Seaborn / Plotly** for visualizations

---

## Model Performance

-  **Accuracy:** 99.9% on validation set  
-  **Dataset:** Cleaned a large dataset with wide variety of audio files
-  **Preprocessing:** MFCCs with zero-padding and time-frequency normalization  
-  **Architecture:** Custom 1D CNN with dropout and batch normalization layers

---

## Author

Developed by [Vennela Varshini Anasoori](https://github.com/vennelavarshini18)

---

## Ongoing Improvements

MoodOS is evolving with the following goals in mind:

-  **Integration with an emotional AI chatbot**
-  **Continual learning from user feedback**
-  **Enhanced visualizations and UX improvements**
-  **Longitudinal analysis of mood patterns**
-  **Cloud storage & analytics for enterprise use**

---

## Contributions Welcome

If you're into **audio emotion detection**, **deep learning**, or **mental health tech**, feel free to fork and contribute!

> 💡 Let’s make MoodOS even smarter — together.

