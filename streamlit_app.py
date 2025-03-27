import streamlit as st
import os
import whisper
from streamlit_webrtc import webrtc_streamer  # WebRTC for live recording

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Save the recorded audio in the root directory
audio_file = st.audio_input("Record your response")
if audio_file is not None:
    audio_save_path = "recorded_response.wav"  # Directly in the root directory
    
    with open(audio_save_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.write(f"Audio saved at: {audio_save_path}")
    st.audio(audio_file)

    # Transcribe audio
    st.write("Transcribing audio...")
    transcription = model.transcribe(audio_save_path)
    
    st.write("*Transcription:*")
    st.write(transcription["text"])
