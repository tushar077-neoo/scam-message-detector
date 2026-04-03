import re
import string

def clean_message(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

scam_words = [
    "win", "free", "urgent", "money", "offer",
    "click", "link", "claim", "prize", "lottery"
]

def find_suspicious_words(text):
    words = text.lower().split()
    return [w for w in words if w in scam_words]