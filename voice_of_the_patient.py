# voice_of_the_patient.py
from transformers import pipeline
import torch

# Use GPU if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

# Load Whisper-small ASR model
asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    device=device
)

def transcribe_audio(audio_filepath):
    """
    Transcribe patient audio into text.
    Returns:
        text: transcribed text
        detected_language: detected language code (default "en")
    """
    try:
        result = asr(audio_filepath)
        text = result.get("text", "")
        detected_language = result.get("language", "en")
        return text, detected_language
    except Exception as e:
        print(f"Transcription error: {e}")
        return "", "en"
