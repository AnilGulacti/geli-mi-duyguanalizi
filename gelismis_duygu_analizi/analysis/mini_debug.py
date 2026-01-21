
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

try:
    print("Loading...")
    model = tf.keras.models.load_model('analysis/ml_models/duygu_analizi_modeli2')
    print("SUCCESS")
except Exception as e:
    print(f"ERROR: {e}")
