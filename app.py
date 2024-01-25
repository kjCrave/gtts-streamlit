import streamlit as st
import pyttsx3
import tempfile
import os

# Function to convert text to speech using pyttsx3
def text_to_speech_pyttsx3(text, filename, speech_rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', speech_rate)
    engine.save_to_file(text, filename)
    engine.runAndWait()

# Streamlit UI components
st.title('Text to Speech Converter with Pyttsx3')

text_input = st.text_area("Enter Text", height=300)
speech_rate = st.selectbox("Select Speech Rate", ["Normal", "Slow"])

if st.button('Convert'):
    # Create a temporary directory to save the audio file
    temp_dir = tempfile.mkdtemp()
    
    # Define the file path for the pyttsx3 audio
    pyttsx3_filename = os.path.join(temp_dir, "output_audio.wav")
    
    # Convert text to speech using pyttsx3
    speech_rate = 200 if speech_rate == "Normal" else 100  # Adjust speech rate as needed
    text_to_speech_pyttsx3(text_input, pyttsx3_filename, speech_rate)
    
    # Download button for the pyttsx3 audio
    st.markdown("## Download Audio")
    with open(pyttsx3_filename, "rb") as pyttsx3_file:
        st.download_button(
            label="Download Audio",
            data=pyttsx3_file,
            file_name="output_audio.wav",
            mime="audio/wav"
        )
