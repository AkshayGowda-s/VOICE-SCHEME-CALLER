from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')  # Use 'en' for English, 'kn' for Kannada
    path = f"audio/{filename}.mp3"
    tts.save(path)
    return path

