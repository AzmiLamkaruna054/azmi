import requests
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, jsonify

app = Flask(__name__)

MODEL_URL = "https://www.dropbox.com/scl/fi/zare7lltsj94cwjlmb6z9/PISANG16CLASS.h5?rlkey=5ohf9ddgxo1j8753tzx8igtim&st=9pi4643l&dl=1"
MODEL_PATH = "models/PISANG16CLASS.h5"

def download_model():
    """Unduh model dari Dropbox jika belum ada"""
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Dropbox...")
        os.makedirs("models", exist_ok=True)
        try:
            response = requests.get(MODEL_URL, stream=True)
            response.raise_for_status()  # Cek jika ada error saat mengunduh
            with open(MODEL_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Model downloaded successfully.")
        except requests.RequestException as e:
            print(f"Error downloading model: {e}")
            exit(1)  # Keluar dari program jika gagal mengunduh

# Unduh model jika belum ada
download_model()

# Load model setelah berhasil diunduh
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)  # Keluar jika gagal memuat model

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running!"})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
