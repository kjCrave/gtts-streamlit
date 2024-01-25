import streamlit as st
from gtts import gTTS
import pyttsx3
import os
import tempfile
import shutil

# Initialize the Text-to-Speech engine for pyttsx3
engine = pyttsx3.init()

# Create a temporary directory to store audio files
temp_dir = tempfile.mkdtemp()

# Define a Streamlit app
def main():
    st.title("Text to Speech with Streamlit")

    # Text input for user to enter the text
    text_input = st.text_area("Enter the text to be synthesized:")

    # Radio button to select the voice category
    voice_category = st.radio("Select Voice Category:", ["Male", "Female"])

    # Dropdown menu to select the speed of the audio (limited to Normal and Slow)
    speed_options = ["Normal", "Slow"]
    selected_speed = st.selectbox("Select Speed:", speed_options)

    # Button to synthesize and play the speech
    if st.button("Synthesize and Play"):
        audio_file = None

        # Set the speech rate based on the selected speed
        speech_rate = get_speech_rate(selected_speed)

        if voice_category == "Male":
            audio_file = synthesize_speech_pyttsx3(text_input, speech_rate)
        elif voice_category == "Female":
            audio_file = synthesize_speech_gtts(text_input, speech_rate)

        if audio_file:
            st.audio(audio_file, format="audio/wav")

    # Clear temporary directory and files
    clear_temporary_files()

# Function to synthesize speech using pyttsx3 with a specified speech rate
def synthesize_speech_pyttsx3(text, speech_rate):
    engine.setProperty("rate", speech_rate)  # Set the speech rate
    audio_file = os.path.join(temp_dir, "temp.wav")
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return audio_file

# Function to synthesize speech using gtts with a specified speech rate
def synthesize_speech_gtts(text, speech_rate):
    audio_file = os.path.join(temp_dir, "temp_gtts.mp3")
    tts = gTTS(text, slow=speech_rate == 100)  # Set slow mode for "Slow" speed
    tts.save(audio_file)
    return audio_file

# Function to get the speech rate based on the selected speed
def get_speech_rate(selected_speed):
    if selected_speed == "Slow":
        return 100  # Set a slower speech rate for "Slow" speed
    else:
        return 200  # Default to Normal speed

# Function to clear temporary directory and files
def clear_temporary_files():
    shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
