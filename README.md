# Comp-3610-Project-Group-D
**TOPIC:** Multi-Class Emotional Sentiment Analysis <br>

**PROBLEM STATEMENT:** <br>
The surge in digital communication, encompassing instant messaging, emails, and social media, has become increasingly prevalent. Yet, this medium often overlooks crucial aspects of non-verbal communication, such as intonation, body language, and cadence. The absence of these cues leads to frequent misinterpretations or misconstruals of text, as contextual nuances and individual speech idiosyncrasies are lost. This challenge is prominently evident in online interactions on social media, particularly when users share sarcastic messages that can be easily misunderstood by others, emphasising the limitations of solely text-based communication.

**PROPOSED SOLUTION:** <br>
In our Emotion Prediction System, we leverage sentiment analysis through sklearn libraries, Artificial Neural Networks (ANN) specifically, a Multilayer Perceptron (MLP), and Random Forest to predict the overall tone of a given text post or comment. The dataset is categorized into six distinct emotions: sadness (0), joy (1), love (2), anger (3), fear (4), and surprise (5), hence the need for a multi-class method such as MLP. We will use Recall scores to compare the results of the aforementioned classification methods and k-fold cross validation to ensure our scores are robust.
We will obtain a corpus of text from the data by undersampling each of the categories using the minority class of the label feature. TF-IDF vectorization with n-grams and stopwords will be used to refine the corpus before running the classification models.

*User Interface and Dynamic Visual Representation:* <br>
The frontend, supported by a Python backend, enables users to input up to 280 characters of text (current X tweet character limit). Upon submission, the system generates and displays probabilities for each emotion category, allowing for a better understanding of text emotions (text can carry more than one emotion). The colour of the text box dynamically changes based on the emotion with the highest probability, accompanied by emojis representing the predicted emotion. This dynamic visual representation enhances user engagement, providing an accessible and interactive experience that contributes to a deeper understanding of emotional content in textual data.


**VALUE OF THE CONCEPT TO INDUSTRY:** <br>
Given the widespread use of digital, text-centric communication channels like email and social media, this proposed solution is an applicable feature for integration by platforms such as X (formerly Twitter) and other text messaging services. These companies could implement our solution within their existing platforms, offering visual flair and a premium user experience, addressing the nuanced understanding of text emotions in a dynamic and user-friendly manner.

