import streamlit as st
from gtts import gTTS
import pyttsx3
import tempfile
import os

# Function to convert text to speech using gtts
def text_to_speech_gtts(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Function to convert text to speech using pyttsx3
def text_to_speech_pyttsx3(text, filename, speech_rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', speech_rate)
    engine.save_to_file(text, filename)
    engine.runAndWait()

# Streamlit UI components
st.title('Text to Speech Converter')

text_input = st.text_area("Enter Text", height=300)
speech_rate = st.selectbox("Select Speech Rate", ["Normal", "Slow"])

if st.button('Convert'):
    # Create a temporary directory to save audio files
    temp_dir = tempfile.mkdtemp()
    
    # Define the file paths for both gtts and pyttsx3 audio
    gtts_filename = os.path.join(temp_dir, "female_voice.mp3")
    pyttsx3_filename = os.path.join(temp_dir, "male_voice.wav")
    
    # Convert text to speech using gtts
    text_to_speech_gtts(text_input, gtts_filename)
    
    # Convert text to speech using pyttsx3
    speech_rate = 200 if speech_rate == "Normal" else 100  # Adjust speech rate as needed
    text_to_speech_pyttsx3(text_input, pyttsx3_filename, speech_rate)
    
    # Download buttons for both gtts and pyttsx3 audio
    st.markdown("## Download Audio Files")
    st.markdown("### Female Voice (gtts Audio)")
    with open(gtts_filename, "rb") as gtts_file:
        st.download_button(
            label="Download Female Voice (gtts) Audio",
            data=gtts_file,
            file_name="female_voice.mp3",
            mime="audio/mpeg"
        )

    st.markdown("### Male Voice (Pyttsx3 Audio)")
    with open(pyttsx3_filename, "rb") as pyttsx3_file:
        st.download_button(
            label="Download Male Voice (Pyttsx3) Audio",
            data=pyttsx3_file,
            file_name="male_voice.wav",
            mime="audio/wav"
        )
