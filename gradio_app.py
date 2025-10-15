# gradio_app.py
import gradio as gr
from voice_of_the_patient import transcribe_audio
from brain_of_the_doctor import get_diagnosis
from translation_and_tts import translate_text, text_to_speech

def process_inputs(audio_filepath, image_filepath=None, output_language="Original"):
    # 1️⃣ Transcribe audio
    speech_text, detected_language = transcribe_audio(audio_filepath)

    # 2️⃣ Translate to English for MedGemma
    english_text = translate_text(speech_text, target_language="en")

    # 3️⃣ Get diagnosis (English)
    diagnosis_english = get_diagnosis(english_text, image_filepath)

    # 4️⃣ Translate diagnosis back to patient language if needed
    diagnosis_local = diagnosis_english
    if detected_language != "en" and output_language == "Original":
        diagnosis_local = translate_text(diagnosis_english, target_language=detected_language)

    # 5️⃣ Convert to speech
    audio_local_path = text_to_speech(diagnosis_local, output_path="diagnosis_local.mp3", lang=detected_language)
    audio_english_path = text_to_speech(diagnosis_english, output_path="diagnosis_english.mp3", lang="en")

    return speech_text, diagnosis_local, diagnosis_english, audio_local_path, audio_english_path

# ---------------- Gradio UI ----------------
languages = ["Original", "English"]

with gr.Blocks() as demo:
    gr.Markdown("## 🏥 AI Doctor (Free Version — Whisper + MedGemma + Google Translate + gTTS)")
    audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Speak Here")
    image_input = gr.Image(type="filepath", label="🩻 Optional: Upload Medical Image")
    output_lang_choice = gr.Radio(languages, label="Output Language for Doctor's Voice", value="Original")

    text_output = gr.Textbox(label="📝 Transcribed Speech")
    diagnosis_local_output = gr.Textbox(label="🩺 Diagnosis (Patient Language)")
    diagnosis_english_output = gr.Textbox(label="🩺 Diagnosis (English)")
    audio_local_output = gr.Audio(label="Doctor’s Voice (Patient Language)")
    audio_english_output = gr.Audio(label="Doctor’s Voice (English)")

    submit = gr.Button("🔍 Diagnose")
    submit.click(
        process_inputs,
        inputs=[audio_input, image_input, output_lang_choice],
        outputs=[
            text_output,
            diagnosis_local_output,
            diagnosis_english_output,
            audio_local_output,
            audio_english_output
        ]
    )

demo.launch(share=False, server_name="127.0.0.1", server_port=7860)
