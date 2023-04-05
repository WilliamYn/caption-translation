# Translation imports
from deep_translator import GoogleTranslator
import re

# Flask imports
from flask import Flask, request
from flask_cors import CORS

# Initialise the translator with Google Translate as driver
translator = GoogleTranslator(source='en', target='fr')

def translate(keywords, captions):
    """
    Translates the given keywords based on their context in the captions. 
    Uses a feature from the GoogleTranslator that allows traduction of <span> blocks in html pages.

    :keywords:      A list of [keyword, percentage] to translate. 
    :captions:      A list of captions the keywords were generated from.
    :return:        A JSON object of the translated keywords and captions
    """
    translated_keywords = []

    # Initialise the regex to detect keyword span block
    regex = r'<span>[\ ]?(.*?)[\ ]?' + re.escape('</span>')

    for keyword, prob in keywords:
        copy = ' ' + ' \n '.join(captions) + ' '
        copy = copy.replace(' ' + keyword + ' ', ' <span> {} </span> '.format(keyword))

        translated_copy = translator.translate(text=copy)
        result = re.findall(regex, translated_copy)
        result = [word for word in result if word.strip() != ""]
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
    """
    Route handler. Get a POST request with a JSON in the body and return a translated JSON. 
    """
    if request.method == "POST":
        request_data = request.get_json()
        translated_data = translate(request_data["tags"], request_data["english_cap"])
        return translated_data
    else:
        return "This endpoint only accepts POST requests", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
