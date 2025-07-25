import numpy as np
import librosa
import tensorflow as tf
import logging
import os
import transformers
from transformers import Wav2Vec2Processor, Wav2Vec2Model
import torch
import torchaudio

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "wav2vec_classifier3.keras")
LABEL_PATH = os.path.join(BASE_DIR, "..", "model", "label_classes3.npy")

model = tf.keras.models.load_model(MODEL_PATH)
label_classes = np.load(LABEL_PATH)

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base")
wav2vec = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
wav2vec = wav2vec.to(DEVICE)

def extract_wav2vec_features(file_path):
    waveform, sr = torchaudio.load(file_path)
    waveform = waveform.squeeze(0)
    inputs = processor(waveform, sampling_rate=sr, return_tensors="pt", padding=True)
    with torch.no_grad():
        embeddings = wav2vec(**inputs.to(DEVICE)).last_hidden_state.mean(dim=1)  

    return embeddings.cpu().numpy()

def predict_emotion(file_path):
    features = extract_wav2vec_features(file_path)
    prediction = model.predict(features, verbose=0)[0]
    emotion = label_classes[np.argmax(prediction)]

    print(f"[INFO] Prediction complete for: {file_path}")
    print(f"[INFO] Detected Emotion: {emotion}")

    return emotion, dict(zip(label_classes, prediction.tolist()))