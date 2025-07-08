import streamlit as st
from transformers import pipeline
from pydub import AudioSegment
import os
import tempfile
from io import BytesIO
import time

# ------------------------------
# 🔌 Load Pretrained ASR Model
# ------------------------------
st.set_page_config(page_title="Speech Recognition", layout="centered")
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] {
        font-size: 1.2rem;
        padding: 0.75rem 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🗣️ Speech Recognition Tool")
st.caption("Built with 🤗 Transformers + Streamlit")

@st.cache_resource
def load_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-small")

asr = load_model()

# ------------------------------
# 🔄 Convert and Transcribe
# ------------------------------
def convert_to_wav(input_bytes, format):
    audio = AudioSegment.from_file(input_bytes, format=format)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio.export(tmp.name, format="wav")
        return tmp.name

def transcribe(path):
    result = asr(path)
    return result["text"]

# ------------------------------
# 🚀 Audio Input Tabs
# ------------------------------
tabs = st.tabs(["🎧 Upload Audio File", "🎤 Record Your Voice"])

transcript_upload = None
transcript_record = None

# Tab 1: Upload
with tabs[0]:
    uploaded_file = st.file_uploader("Upload .mp3 or .wav", type=["mp3", "wav"])
    if uploaded_file:
        with st.spinner("🔄 Transcribing uploaded audio..."):
            file_format = uploaded_file.name.split(".")[-1]
            file_path = convert_to_wav(uploaded_file, format=file_format)
            st.audio(file_path)
            transcript_upload = transcribe(file_path)
            os.remove(file_path)

    if transcript_upload:
        st.success("Transcription Complete")
        st.text_area("📝 Transcript:", value=transcript_upload, height=200, disabled=True)
        b = BytesIO()
        b.write(transcript_upload.encode())
        b.seek(0)
        st.download_button(
            label="📥 Download Transcript as .txt",
            data=b,
            file_name="transcript.txt",
            mime="text/plain"
        )

# Tab 2: Record
with tabs[1]:
    audio_value = st.audio_input("🎤 Record a voice message")
    if audio_value:
        st.audio(audio_value)
        with st.spinner("🔄 Transcribing recorded audio..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_value.read())
                tmp_path = tmp.name
            transcript_record = transcribe(tmp_path)
            os.remove(tmp_path)

    if transcript_record:
        st.success("Transcription Complete")
        st.text_area("📝 Transcript:", value=transcript_record, height=200, disabled=True)
        b = BytesIO()
        b.write(transcript_record.encode())
        b.seek(0)
        st.download_button(
            label="📥 Download Transcript as .txt",
            data=b,
            file_name="transcript.txt",
            mime="text/plain"
        )