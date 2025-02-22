import requests
import os
import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_URL = "https://www.dropbox.com/scl/fi/zare7lltsj94cwjlmb6z9/PISANG16CLASS.h5?rlkey=5ohf9ddgxo1j8753tzx8igtim&st=9pi4643l&dl=1"
MODEL_PATH = "models/PISANG16CLASS.h5"

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Dropbox...")
    os.makedirs("models", exist_ok=True)
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)

# Load model
model = load_model(MODEL_PATH)

