from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Available languages (for cycling translations)
languages = ["fr", "de", "zh-cn", "ru", "es", "hi", "ar", "en"]

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get("text", "")
    cycles = int(data.get("cycles", 5))

    if not text:
        return jsonify({"error": "Text is required"}), 400

    current_text = text
    for i in range(cycles):
        lang = languages[i % len(languages)]  # Cycle through different languages
        current_text = translator.translate(current_text, dest=lang).text

    final_text = translator.translate(current_text, dest="en").text  # Convert back to English
    return jsonify({"original": text, "translated": final_text})

if __name__ == '__main__':
    app.run(debug=True)