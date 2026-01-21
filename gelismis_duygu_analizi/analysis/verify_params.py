
import os
import torch
from transformers import BertForSequenceClassification

# Disable extensive logging
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

model_path = 'analysis/ml_models/duygu_analizi_modeli2'
try:
    print(f"Loading model from {model_path}...")
    model = BertForSequenceClassification.from_pretrained(model_path)
    
    params = model.num_parameters()
    print(f"ACTUAL_PARAM_COUNT: {params}")
    
    config = model.config
    print(f"VOCAB: {config.vocab_size}")
    print(f"LAYERS: {config.num_hidden_layers}")
    
except Exception as e:
    print(f"Error: {e}")
