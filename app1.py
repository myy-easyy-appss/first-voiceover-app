import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(page_title="🎙️ AI Voiceover App", page_icon="🎧")

st.title("🎧 AI Voiceover App (Lite)")
st.write("Type text and generate realistic AI voices instantly!")

# Input text
text = st.text_area("Enter text:", height=150, placeholder="Type something here...")

# Select voice (only 2 for reliability)
voice = st.selectbox("Choose a voice:", [
    "en-US-AriaNeural",  # Female
    "en-US-GuyNeural"    # Male
])

# Output file name
file_name = "output.mp3"

async def generate_tts(text, voice):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(file_name)
        st.success("✅ Voice generated successfully!")
        audio_file = open(file_name, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    except Exception as e:
        st.error("⚠️ Failed to generate voice. Please try again later.")
        st.caption(f"Error details: {str(e)}")

# Generate button
if st.button("🎤 Generate Voice"):
    if text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        asyncio.run(generate_tts(text, voice))
