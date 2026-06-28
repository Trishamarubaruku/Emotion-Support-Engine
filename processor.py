# processor.py
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

EMOTION_KEYWORDS = {
    'frustrated': 'frustration', 'angry': 'frustration',
    'confused': 'confusion', 'lost': 'confusion',
    'happy': 'joy', 'excited': 'joy'
}

def clean_and_boost(text):
    text = text.lower()
    tokens = word_tokenize(text)
    scores = {cat: 1.0 for cat in set(EMOTION_KEYWORDS.values())}
    for word in tokens:
        if word in EMOTION_KEYWORDS:
            scores[EMOTION_KEYWORDS[word]] += 10.0 # 10x Boost Logic
    return scores