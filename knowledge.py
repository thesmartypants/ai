import json

knowledge = {}  # Initialize the knowledge dictionary

def add_to_knowledge(sentence, answer):
    global knowledge
    sentence_lower = sentence.lower().strip()

    # Check if the sentence key already exists in knowledge
    if sentence_lower in knowledge:
        # If it exists and the value is already a list, append the new answer
        if isinstance(knowledge[sentence_lower], list):
            knowledge[sentence_lower].append(answer)
        else:
            # If it exists but the value is not a list, convert it to a list and add the new answer
            knowledge[sentence_lower] = [knowledge[sentence_lower], answer]
    else:
        # If the sentence key does not exist, add it with the new answer as a list
        knowledge[sentence_lower] = [answer]

    # Save the response to the knowledge dictionary and the JSON file
    save_knowledge()

def save_knowledge():
    global knowledge
    with open('knowledge.json', 'w', encoding='utf-8') as f:
        json.dump(knowledge, f, ensure_ascii=False, indent=4)

def load_knowledge():
    global knowledge
    try:
        with open('knowledge.json', 'r', encoding='utf-8') as f:
            knowledge = json.load(f)
    except FileNotFoundError:
        knowledge = {}  # Return an empty dictionary if the file is not found

# Load the knowledge from the file when this module is imported
load_knowledge()
