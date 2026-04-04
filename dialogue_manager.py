context = {}

def update_context(entities):
    for key, value in entities.items():
        context[key] = value

def get_context():
    return context