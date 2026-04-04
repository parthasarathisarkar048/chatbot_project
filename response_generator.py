def generate_response(intent, emotion, entities, context):

    if emotion == "angry":
        return "I am sorry for the inconvenience. I detected you are upset."

    if intent == "greeting":
        return "Hello! How can I help you today?"

    if intent == "name":
        if "name" in entities:
            return f"Nice to meet you {entities['name']}"
        else:
            return "I didn't catch your name. Can you tell me again?"

    if intent == "weather":
        city = context.get("city", None)
        if city:
            return f"Fetching weather for {city}"
        else:
            return "Please tell me your city."
        
    if intent == "menu":
        return "We have Pizza, Burger, Pasta."
    
    if intent == "order":
        return "What would you like to order?"
    
    if intent == "weather":
        if "city" in context:
            return f"Fetching weather for {context['city']}"
        else:
            return "Please tell me your city."

    if intent == "goodbye":
        return "Goodbye! Have a nice day."
    
    

    return "I did not understand. Please call this number for support 0000000000"