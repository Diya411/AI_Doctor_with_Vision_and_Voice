# brain_of_the_doctor.py
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

# Example: use a small text generation model for free inference
model_name = "google/medgemma-4b-it"  # MedGemma (free)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, device_map="auto" if device>=0 else None)

generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=device)

def get_diagnosis(text_input, image_path=None):
    """
    Generate diagnosis text from patient input.
    For simplicity, image input is optional.
    """
    prompt = f"Patient input: {text_input}\nDiagnosis:"
    result = generator(prompt, max_length=256, do_sample=False)
    diagnosis = result[0]["generated_text"]
    return diagnosis
