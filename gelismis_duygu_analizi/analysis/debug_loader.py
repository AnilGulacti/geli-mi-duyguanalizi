
import os
import sys
import django
from django.conf import settings
import joblib
import tensorflow as tf

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def try_load():
    model_path = os.path.join(settings.BASE_DIR, 'analysis', 'ml_models', 'duygu_analizi_modeli2')
    print(f"Checking path: {model_path}")
    
    if not os.path.exists(model_path):
        print("File does NOT exist.")
        return

    print(f"File exists. Size: {os.path.getsize(model_path)} bytes")
    
    # Try Keras
    try:
        print("Attempting Keras load_model...")
        model = tf.keras.models.load_model(model_path)
        print("SUCCESS: Loaded with Keras")
        return
    except Exception as e:
        print(f"Keras failed: {e}")

    # Try Joblib
    try:
        print("Attempting Joblib load...")
        model = joblib.load(model_path)
        print("SUCCESS: Loaded with Joblib")
        return
    except Exception as e:
        print(f"Joblib failed: {e}")
        
    print("FATAL: Could not load model with any method.")

if __name__ == "__main__":
    try_load()
