from flask import Blueprint, render_template
import joblib
import pandas as pd
import numpy as np
import random
import re
from bs4 import BeautifulSoup
import string
from string import punctuation
from flask import Flask, jsonify, request
from joblib import load

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/emotions", methods=['POST'])
def emotions_view():
    return render_template("emotions.html")

@views.route('/process_text', methods=['POST'])
def process_text():
    if request.method == 'POST':
        text = request.form['user_input']
        orgtext = text
        loaded_model = load('/workspace/Comp-3610-Project-Ceejmo/Front-End/static/logreg_tfidf.joblib')
        loaded_vectr = load('/workspace/Comp-3610-Project-Ceejmo/Front-End/static/tfidf_for_logreg.joblib')

        text = ' '.join(text.split())   # Remove additional white spaces
        text = re.sub(r'http\S+', '', text) # Remove links
        text = text.translate(str.maketrans('', '', punctuation)) # Remove punctuation
        text = BeautifulSoup(text, "html.parser").get_text() # Remove HTML tags
        text.lower() # Convert all text to lowercase
        
        words_to_remove = ['feeling', 'feel', 'like', 'im'] # Remove common words
        for word in words_to_remove:
                pattern = r'\b{}\b'.format(re.escape(word))
                text = re.sub(pattern, '', text)
        
        text_trans = loaded_vectr.transform([text])
        pred_probs = loaded_model.predict_proba(text_trans)

        labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

        # Create a dictionary to store the probabilities with labels
        probs_dict = {}

        # Iterate over the probabilities array and labels simultaneously
        for label, prob in zip(labels, pred_probs[0]):
            probs_dict[label] = round(prob*100,5)

        return render_template("emotions.html", probs_dict=probs_dict, orgtext=orgtext)

if __name__ == "__main__":
    app.run(debug=True)