# processor.py
def get_emotion_prediction(text):
    text = text.lower()
    if any(word in text for word in ['happy', 'glad', 'joy', 'great', 'awesome']):
        return 'happy'
    elif any(word in text for word in ['sad', 'bad', 'hard', 'struggle', 'lost']):
        return 'sad'
    elif any(word in text for word in ['angry', 'frustrated', 'annoyed', 'mad']):
        return 'angry'
    elif any(word in text for word in ['confused', 'lost', 'help', 'understand', 'difficult']):
        return 'confused'
    else:
        return 'neutral'
