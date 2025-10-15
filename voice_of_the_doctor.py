# translation_and_tts.py
from gtts import gTTS
from deep_translator import GoogleTranslator

def translate_text(text, target_language="en"):
    """
    Translate text using Deep Translator.
    Returns translated text.
    """
    try:
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        print("Translation error:", e)
        return text

def text_to_speech(text, output_path="output.mp3", lang="en"):
    """
    Convert text to speech using gTTS.
    """
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        return output_path
    except Exception as e:
        print("TTS error:", e)
        return None
