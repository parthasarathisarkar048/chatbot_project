from intents import detect_intent
from entity_extractor import extract_entities
from emotion_detector import detect_emotion
from dialogue_manager import update_context, get_context
from response_generator import generate_response

print("Chatbot Started (type 'bye' to exit)")

while True:
    user_input = input("You: ")

    intent = detect_intent(user_input)
    entities = extract_entities(user_input)
    emotion = detect_emotion(user_input)

    update_context(entities)
    context = get_context()

    response = generate_response(intent, emotion, entities, context)

    print("Bot:", response)

    if intent == "goodbye":
        break