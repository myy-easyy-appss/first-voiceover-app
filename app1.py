import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(page_title="AI Voiceover Generator", page_icon="🎙️")

st.title("🎙️ AI Voiceover Generator")
st.write("Type your text and instantly generate a realistic AI voice!")

# Input text
text = st.text_area("Enter your text below:", height=150)

# Select voice
accent = st.selectbox("Select accent:", ["US", "UK", "India", "Australia", "Canada"])
voice_dict = {
    "US": ["en-US-GuyNeural", "en-US-JennyNeural", "en-US-AriaNeural", "en-US-DavisNeural"],
    "UK": ["en-GB-RyanNeural", "en-GB-SoniaNeural"],
    "India": ["en-IN-NeerjaNeural", "en-IN-PrabhatNeural"],
    "Australia": ["en-AU-NatashaNeural", "en-AU-WilliamNeural"],
    "Canada": ["en-CA-ClaraNeural", "en-CA-LiamNeural"]
}
voice = st.selectbox("Choose a voice:", voice_dict[accent])

# File name
file_name = "output.mp3"

async def tts(text, voice):
    if text.strip() == "":
        st.warning("Please enter some text!")
        return
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_name)
    st.success("✅ Voice generated successfully!")
    audio_file = open(file_name, "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Button to trigger
if st.button("Generate Voice 🎧"):
    asyncio.run(tts(text, voice))
