import streamlit as st
import json
from streamlit_webrtc import webrtc_streamer  # WebRTC for live recording
import whisper
import tempfile
import os

#audio_value = st.audio_input("Record a voice message")

#if audio_value:
    #st.audio(audio_value)"""

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Ensure directory for storing audio responses
AUDIO_SAVE_PATH = "audio_responses"
os.makedirs(AUDIO_SAVE_PATH,exist_ok=True)
audio_file = st.audio_input("Record your response")
if audio_file is not None:
    # Save the recorded audio
    audio_save_path = os.path.join(AUDIO_SAVE_PATH, "/")
    with open(audio_save_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.write(f"Audio saved at: {audio_save_path}")
    st.audio(audio_file)

    # Transcribe audio
    st.write("Transcribing audio...")
    transcription = model.transcribe(audio_save_path)
    
    st.write("*Transcription:*")
    st.write(transcription["text"])
