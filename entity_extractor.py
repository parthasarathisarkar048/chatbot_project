import re

def extract_entities(text):
    entities = {}

    name = re.findall(r"(?:my name is|i am|name)\s(\w+)", text.lower())
    if name:
        entities["name"] = name[0]

    city = re.findall(r"in (\w+)", text.lower())
    if city:
        entities["city"] = city[0]

    return entities