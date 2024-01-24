import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(f"{filename}.mp3")

# Streamlit UI components
st.title('Text to Speech Converter')

filename = st.text_input("Enter file name")

text = st.text_area("Enter Text", height=300)
if st.button('Convert'):
    text_to_speech(text, filename)
    st.success("Conversion Successful!")

    with open(f"{filename}.mp3", "rb") as file:
        st.download_button(
            label="Download Audio File",
            data=file,
            file_name=f"{filename}.mp3",
            mime="audio/mpeg"
        )
