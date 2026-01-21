from django.apps import AppConfig
import os
from django.conf import settings

class AnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analysis'
    model = None

    def ready(self):
        # Prevent double loading in debug mode
        if os.environ.get('RUN_MAIN', None) != 'true':
            return
            
        model_path = os.path.join(settings.BASE_DIR, 'analysis', 'ml_models', 'duygu_analizi_modeli2')
        
        print(f"Loading model from {model_path}...")
        try:
            from transformers import BertTokenizer, BertForSequenceClassification
            import torch
            
            # Load specific BERT components
            self.tokenizer = BertTokenizer.from_pretrained(model_path)
            self.model = BertForSequenceClassification.from_pretrained(model_path)
            self.model.eval() # Set to evaluation mode
            
            print("Model loaded successfully (BertForSequenceClassification)")
        except Exception as e:
            print(f"Failed to load model: {e}")
            self.model = None
            self.tokenizer = None
