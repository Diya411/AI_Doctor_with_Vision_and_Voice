# 🩺 AI Doctor with Vision and Voice

An interactive, multimodal healthcare assistant that simulates preliminary medical consultations. By integrating automatic speech recognition, computer vision, and multimodal Large Language Models (LLMs), this project enables users to report medical symptoms via voice audio or medical images and receive real-time, synthesized diagnostic feedback through text and speech.

---

## 📌 Project Overview

* **Project Title:** AI Doctor with Vision and Voice
* **Degree:** Bachelor of Technology in Computer Engineering
* **Subject:** Artificial Intelligence
* **Academic Year:** 2024–2025

---

## ✨ Features

- **Voice-Based Symptom Input:** Transcribes patient speech into text using OpenAI Whisper.
- **Visual Medical Analysis:** Processes uploaded medical images or visual symptoms via Meta's Llama-4 multimodal architecture.
- **Multimodal AI Diagnosis:** Generates preliminary clinical insights, preliminary diagnoses, and medical advice via Groq API.
- **Automated Voice Feedback:** Converts textual medical replies into natural speech using Google Text-to-Speech (`gTTS`).
- **Interactive UI:** Provides a seamless user experience using Gradio for dual text display and synchronized audio playback.

---

## 🛠️ System Architecture & Workflow

The system operates on a modular three-phase processing pipeline: 
```text
              ┌──────────────────────┐
              │ Patient Inputs       │
              │ (Voice / Image)      │
              └──────────┬───────────┘
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
┌─────────────────┐               ┌─────────────────┐
│ Speech-to-Text  │               │ Computer Vision │
│ (OpenAI Whisper)│               │  (Image Model)  │
└────────┬────────┘               └────────┬────────┘
         │                                 │
         └────────────────┬────────────────┘
                          │ (Text Transcript + Visual Embeddings)
                          ▼
          ┌─────────────────────────────┐
          │  Multimodal Reasoning Engine│
          │ (Llama-4-Scout via Groq)    │
          └──────────────┬──────────────┘
                         │ (Diagnostic Advice)
        ┌────────────────┴────────────────┐
        ▼                                 ▼
  ┌─────────────────┐               ┌─────────────────┐
  │ Text Output     │               │ Text-to-Speech  │
  │ (Gradio UI)     │               │     (gTTS)      │
  └─────────────────┘               └────────┬────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │ Audio Output    │
                                    │   (MP3 Play)    │
                                    └─────────────────┘
```

1. **Input Phase:** The patient uploads a medical image or records voice input.
2. **Speech & Vision Processing:**
   - **OpenAI Whisper** converts the spoken audio into a text transcript.
   - **Vision Model / Encoder** extracts visual feature embeddings from uploaded medical images.
3. **Multimodal Inference (Groq API):**
   - **Meta Llama-4-Scout-17B-16E-Instruct** combines textual transcripts with image embeddings using early modality fusion.
   - The Mixture-of-Experts (MoE) layers execute contextual reasoning to generate diagnostic feedback.
4. **Speech Synthesis & Interaction:**
   - **gTTS** synthesizes the diagnostic text response into an `output.mp3` file.
   - **Gradio UI** displays textual advice and plays synthesized voice output simultaneously.

---

## 🧰 Tools and Technologies Used

| Component | Technology / Model | Purpose |
| :--- | :--- | :--- |
| **Programming Language** | Python 3.10+ | Core project implementation logic |
| **Speech-to-Text (STT)** | OpenAI Whisper | Audio transcription of patient symptoms |
| **Multimodal LLM** | Meta Llama-4-Scout-17B-16E-Instruct | Multimodal context reasoning and diagnostic advice |
| **Inference Backend** | GROQ API | High-speed model inference and execution |
| **Text-to-Speech (TTS)** | Google Text-to-Speech (`gTTS`) | Generates synthesized audio replies |
| **Image Processing** | OpenCV (`opencv-python`) | Image preprocessing and visual inputs handling |
| **Frontend UI** | Gradio | Interactive web interface for web and audio rendering |

---

## 🤖 Deep Dive: Model Architectures

### 1. Meta Llama-4-Scout-17B-16E-Instruct
- **Architecture:** Transformer decoder with Mixture-of-Experts (MoE).
- **Parameters:** 17 billion active parameters with 16 specialized expert networks (scaling to a total parameter pool of ~109B).
- **Early Modality Fusion:** Merges textual and visual inputs at early stages prior to decoder routing.
- **Top-k Routing:** A trainable gating network dynamically routes tokens to specific expert subnetworks to maximize computational efficiency.
- **Context Window:** Handles up to 10 million tokens for extensive conversational context.

### 2. OpenAI Whisper
- **Architecture:** Encoder-Decoder ASR Transformer.
- **Process:** Converts raw audio signals into log-mel spectrograms, applies convolutional feature extraction, and decodes spectrograms into structured text.

### 3. Google Text-to-Speech (gTTS)
- **Pipeline:** Converts output text through linguistic normalization, generates mel-spectrograms via neural acoustic modeling, and synthesizes final audio waveforms via WaveNet vocoders.

---
