from deep_translator import GoogleTranslator
# Flask imports
from flask import Flask, request
from flask_cors import CORS
import json
import re

translator = GoogleTranslator(source='en', target='fr')

def translate(keywords, captions):
    translated_keywords = []

    regex = r'<span>[\ ]?(.*?)[\ ]?' + re.escape('</span>')

    for keyword, prob in keywords:
        copy = ' ' + ' \n '.join(captions) + ' '
        copy = copy.replace(' ' + keyword + ' ', ' <span> {} </span> '.format(keyword))

        translated_copy = translator.translate(text=copy)
        result = re.findall(regex, translated_copy)
        if result:
            translated_keywords.append([keyword, prob, list(set(result))])
        else: 
            translated_keywords.append([keyword, prob, []])
    
    translated_captions = translator.translate('\n'.join(captions)).split('\n')     
    
    return { 'tags': translated_keywords, 'captions': [(caption, translated) for caption, translated in zip(captions, translated_captions)]}


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def handle_request():
    if request.method == "POST":
        request_data = request.get_json()
        translated_data = translate(request_data["tags"], request_data["english_cap"])
        return translated_data
    else:
        return "This endpoint only accepts POST requests", 400

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5000)
    app.run(host="0.0.0.0", port=80)