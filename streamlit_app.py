import streamlit as st
import json
from streamlit_webrtc import webrtc_streamer  # WebRTC for live recording
#import whisper
#import tempfile
import os

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
