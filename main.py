import streamlit as st
from pathlib import Path

st.set_page_config(page_title="MP4 Player")

st.title("🎥 Padlet BDR Video 🎥")
st.write("What's something you know more about than most people you know?")

# Resolve a file in the same folder as this script
VIDEO_NAME = "BDR Question.mp4"
video_path = Path(__file__).parent / VIDEO_NAME

if not video_path.exists():
    st.error(f"File not found: {video_path}")
else:
    st.video(str(video_path))  # cast Path -> str for Streamlit