🎙️ SwarSetu

SwarSetu is a voice-enabled web application designed to make government schemes more accessible. Users can select a category (e.g., Women, Farmers, Students), choose a language, and hear a simplified explanation of the relevant schemes using text-to-speech technology.

🚀 Features
🔍 Category-based scheme search (e.g., Women, Farmers)
🧠 Scheme simplification using OpenAI
🗣️ Text-to-Speech (TTS) in regional languages
🌐 Responsive frontend (HTML, CSS, JS)


🏗️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python, Flask
AI Simplification: OpenAI GPT-4
TTS: gTTS or pyttsx3
Deployment: Render


🔧 Installation
# Clone the repo
git clone https://github.com/your-username/swarsetu.git
cd swarsetu

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
