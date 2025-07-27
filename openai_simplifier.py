from tts_generator import format_scheme_for_audio
from googletrans import Translator

translator = Translator()

def simplify_scheme(raw_scheme_list, category_name, language="English"):
    text = format_scheme_for_audio(category_name, raw_scheme_list)
    
    if language.lower() == "hindi":
        translated = translator.translate(text, src='en', dest='hi')
        return translated.text
    
    elif language.lower() == "kannada":
        translated = translator.translate(text, src='en', dest='kn')
        return translated.text
    
    else:
        return text
