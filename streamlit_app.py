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
