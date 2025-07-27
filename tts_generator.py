from gtts import gTTS
import os
from scheme_data import schemes

def format_scheme_for_audio(category_name, scheme_list):
    output = f"Here are some important government schemes for {category_name}:\n"
    for scheme in scheme_list:
        output += f"\nScheme: {scheme['name']}.\n"
        output += f"Description: {scheme['description']}\n"
        output += f"Eligibility: {scheme['eligibility']}\n"
        output += "Documents required: " + ", ".join(scheme['documents_required']) + ".\n"
    return output

def text_to_speech(text, filename, lang='en'):
    if not os.path.exists("audio"):
        os.makedirs("audio")
    tts = gTTS(text=text, lang=lang)
    path = f"audio/{filename}.mp3"
    tts.save(path)
    return path

