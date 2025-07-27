from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from scheme_data import schemes
from tts_generator import text_to_speech
from openai_simplifier import simplify_scheme
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

@app.route('/get_scheme_audio', methods=['POST'])
def get_scheme_audio():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON received."}), 400

    category = data.get("category")
    keyword = (data.get("keyword") or "").lower().strip()
    language = (data.get("language") or "English").lower()

    print(f"Incoming Request - Category: {category}, Keyword: {keyword}, Language: {language}")

    lang_map = {
        'english': 'en',
        'hindi': 'hi',
        'kannada': 'kn'
    }
    lang_code = lang_map.get(language, 'en')

    try:
        if category == "search" and keyword:
            matched_schemes = []
            for cat, scheme_list in schemes.items():
                for scheme in scheme_list:
                    if keyword in scheme['name'].lower() or keyword in scheme['description'].lower():
                        matched_schemes.append(scheme)

            if not matched_schemes:
                return jsonify({"error": f"No schemes found matching keyword '{keyword}'."}), 404

            simplified_text = simplify_scheme(matched_schemes, f"Search results for '{keyword}'", language)
            filename = f"search_{keyword}_{language}".replace(" ", "_")
        else:
            if not category:
                return jsonify({"error": "Please provide a category."}), 400
            if category not in schemes:
                return jsonify({"error": f"No schemes found for category '{category}'."}), 404

            raw_data = schemes[category]
            simplified_text = simplify_scheme(raw_data, category, language)
            filename = f"{category}_{language}".replace(" ", "_")

        audio_path = text_to_speech(simplified_text, filename, lang=lang_code)
        return jsonify({
            "message": simplified_text,
            "audio_path": f"/audio/{os.path.basename(audio_path)}"
        })

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
