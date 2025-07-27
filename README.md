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

## App Screenshots

Here’s a sneak peek into the MoodOS interface:
<img width="1048" height="873" alt="Screenshot 2025-07-27 165323" src="https://github.com/user-attachments/assets/02d28145-d47e-4e96-b308-81fa6e0f20a1" />    
<img width="1031" height="836" alt="Screenshot 2025-07-27 165340" src="https://github.com/user-attachments/assets/4f8179ee-6b17-4d7d-a603-c1604bc7e3d9" />


### Journal section:
<img width="1847" height="890" alt="Screenshot 2025-07-27 172451" src="https://github.com/user-attachments/assets/83567a67-1a8f-400c-8ce3-4a0e69749787" />


-  Real-time Recording Page  
-  Emotion Confidence Chart  
-  Mood Journal Logs  
-  Personalized Suggestion Cards  

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

-  **Multilingual emotion detection**
-  **Integration with an emotional AI chatbot**
-  **Continual learning from user feedback**
-  **Enhanced visualizations and UX improvements**
-  **Longitudinal analysis of mood patterns**
- ☁ **Cloud storage & analytics for enterprise use**

---

## Contributions Welcome

If you're into **audio emotion detection**, **deep learning**, or **mental health tech**, feel free to fork and contribute!

> Let’s make MoodOS even smarter — together.

