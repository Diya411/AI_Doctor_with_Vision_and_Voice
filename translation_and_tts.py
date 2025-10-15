# translation_and_tts.py
from deep_translator import GoogleTranslator
from gtts import gTTS

def translate_text(text, target_language="en"):
    """
    Translate text online using Google Translate via Deep Translator.
    """
    try:
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def text_to_speech(text, output_path="output.mp3", lang="en"):
    """
    Convert text to speech using Google Text-to-Speech (gTTS).
    """
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        return output_path
    except Exception as e:
        print(f"TTS error: {e}")
        return None
