import numpy as np
import librosa
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "best_model.h5")

label_classes = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad']

model = tf.keras.models.load_model(MODEL_PATH)

def extract_features(file_path, max_len=173):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    pad_width = max_len - mfccs.shape[1]
    if pad_width > 0:
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfccs = mfccs[:, :max_len]
    return mfccs.T[np.newaxis, ...]

def predict_emotion(file_path):
    features = extract_features(file_path)
    prediction = model.predict(features, verbose=0)[0]
    emotion = label_classes[np.argmax(prediction)]

    print(f"[INFO] Prediction complete for: {file_path}")
    print(f"[INFO] Detected Emotion: {emotion}")

    return emotion, dict(zip(label_classes, prediction.tolist()))
