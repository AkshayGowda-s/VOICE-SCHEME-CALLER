from flask import Flask, request, jsonify
from scheme_data import schemes
from tts_generator import text_to_speech
from openai_simplifier import simplify_scheme

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Voice Scheme Caller API is running!"

@app.route('/get_scheme_audio', methods=['POST'])
def get_scheme_audio():
    data = request.json
    category = data.get("category")

    if category not in schemes:
        return jsonify({"error": "Category not found"}), 404

    raw_text = schemes[category]
    simplified = simplify_scheme(raw_text, language="English")
    audio_path = text_to_speech(simplified, category)

    return jsonify({
        "message": simplified,
        "audio_path": audio_path
    })

if __name__ == '__main__':
    app.run(debug=True)
