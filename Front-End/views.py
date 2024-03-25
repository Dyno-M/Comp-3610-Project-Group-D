from flask import Blueprint, render_template
import joblib

import re
from bs4 import BeautifulSoup
import string
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from flask import Flask, request

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/emotions")
def emotions_view():
    return render_template("emotions.html")

# Load the classifier
classifier = joblib.load('/workspace/Comp-3610-Project-Ceejmo/Front-End/static/logreg_tfidf.joblib')

@views.route('/classify')
def classify():
    data = request.get_json()
    input_text = data['input']
    try:
        data = request.json
        # Assuming your classifier expects a specific format of input
        input_data = preprocess_input(data)
        # Perform prediction
        probabilities = classifier.predict_proba([input_data])[0]
        # Convert probabilities to a tuple
        probabilities_tuple = tuple(probabilities.tolist())
        # Render the 'emotions.html' template with the probabilities tuple
        return render_template('emotions.html', probabilities=probabilities_tuple)
    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({'error': str(e)}), 400

def remove_word_from_string(word, string):
    # Construct a regular expression pattern to match the word
    pattern = r'\b{}\b'.format(re.escape(word))
    # Use re.sub() to replace the matched word with an empty string
    return re.sub(pattern, '', string)


def preprocess_input(text):
    text = ' '.join(text.split())   # Remove additional white spaces
    text = re.sub(r'http\S+', '', text) # Remove links
    text = text.translate(str.maketrans('', '', punctuation)) # Remove punctuation
    text = BeautifulSoup(text, "html.parser").get_text() # Remove HTML tags
    text.lower() # Convert all text to lowercase
    words_to_remove = ['feeling', 'feel', 'like', 'im']
    for word in words_to_remove:
            text = remove_word_from_string(word, text)
    tfidf = TfidfVectorizer(stop_words = 'english')
    text_trans = tfidf.fit_transform(text)
    return text_trans

if __name__ == "__main__":
    app.run(debug=True)