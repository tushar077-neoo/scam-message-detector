import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from utils import clean_message

def train_model():
    data = pd.read_csv("data/spam.csv")

    data['label'] = data['label'].map({'ham': 0, 'spam': 1})
    data['message'] = data['message'].apply(clean_message)

    X = data['message']
    y = data['label']

    vectorizer = TfidfVectorizer(stop_words='english')
    X_vectors = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vectors, y)

    return model, vectorizer