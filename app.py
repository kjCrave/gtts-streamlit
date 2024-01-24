import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

# Streamlit UI components
st.title('Text to Speech Converter')
text = st.text_area("Enter Text", height=300)
if st.button('Convert'):
    text_to_speech(text)
    st.success("Conversion Successful!")

    with open("output.mp3", "rb") as file:
        st.download_button(
            label="Download Audio File",
            data=file,
            file_name="output.mp3",
            mime="audio/mpeg"
        )
