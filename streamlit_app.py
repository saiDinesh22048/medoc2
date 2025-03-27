import streamlit as st
import os
import whisper
import tempfile
from pydub import AudioSegment  # Ensure this is installed: pip install pydub

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Capture audio input
audio_file = st.audio_input("Record your response")
if audio_file is not None:
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.getbuffer())
        temp_audio_path = temp_audio.name

    st.write(f"Audio saved at: {temp_audio_path}")
    st.audio(audio_file)

    # Convert the audio to WAV format if necessary
    audio = AudioSegment.from_file(temp_audio_path)
    converted_audio_path = temp_audio_path.replace(".wav", "_converted.wav")
    audio.export(converted_audio_path, format="wav")

    # Transcribe audio
    st.write("Transcribing audio...")
    transcription = model.transcribe(converted_audio_path)

    st.write("*Transcription:*")
    st.write(transcription["text"])

    # Clean up temporary files
    os.remove(temp_audio_path)
    os.remove(converted_audio_path)
