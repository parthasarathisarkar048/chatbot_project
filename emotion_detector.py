emotions = {
    "happy": ["good", "great", "awesome", "happy"],
    "sad": ["sad", "unhappy", "depressed"],
    "angry": ["angry", "bad", "worst", "hate"],
    "neutral": []
}

def detect_emotion(text):
    text = text.lower()
    for emotion, words in emotions.items():
        for word in words:
            if word in text:
                return emotion
    return "neutral"