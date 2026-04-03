import streamlit as st
import pickle
from utils import clean_message, find_suspicious_words

# load trained model (NO training here)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def rule_based_check(text):
    suspicious = ["win", "won", "free", "prize", "offer", "iphone", "cash"]
    return any(word in text.lower() for word in suspicious)

st.set_page_config(page_title="Scam Detector", layout="centered")

st.title("Scam Message Detector")

user_input = st.text_area("Enter your message")

if st.button("Check Message"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        cleaned = clean_message(user_input)
        vector_input = vectorizer.transform([cleaned])

        prediction = model.predict(vector_input)[0]
        probability = model.predict_proba(vector_input)[0][1]

        # decision logic
        if rule_based_check(user_input):
            st.error("Scam detected (rule-based)")
        elif prediction == 1:
            st.error(f"Scam detected | Confidence: {probability:.2f}")
        else:
            st.success(f"Safe message | Confidence: {1 - probability:.2f}")

        # suspicious words
        words = find_suspicious_words(user_input)
        if words:
            st.write("Suspicious words:", ", ".join(words))
        else:
            st.write("No suspicious keywords detected.")

        # save history safely
        try:
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"{user_input} | Pred: {prediction} | Prob: {probability:.2f}\n")
        except:
            pass