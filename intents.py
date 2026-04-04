intents = {
    "greeting": ["hello", "hi", "hey"],
    "name": ["my name is", "i am", "name"],
    "booking": ["book", "booking", "reservation"],
    "menu": ["menu", "food", "items"],
    "order": ["order", "pizza", "burger"],
    "weather": ["weather", "temperature"],
    "goodbye": ["bye", "goodbye"]
}

def detect_intent(text):
    text = text.lower()
    for intent, keywords in intents.items():
        for word in keywords:
            if word in text:
                return intent
    return "unknown"