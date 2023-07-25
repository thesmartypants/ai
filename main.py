import os
import knowledge
import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

prev_response = ""

def remove_common_words(sentence):
    remove_words = ["in", "and", "how", "do", "i", "a", "to", "is", "the", "of", "for", "python", "make", "create", "check", "you"]
    words = sentence.lower().split()
    filtered_words = [word for word in words if word not in remove_words]
    return " ".join(filtered_words)

def ai(sentence):
    global prev_response

    sentence_lower = remove_common_words(sentence.lower())

    if sentence_lower in knowledge.knowledge:
        response_list = knowledge.knowledge[sentence_lower]
        prev_response = random.choice(response_list)
        return prev_response

    elif sentence_lower == "run":
        if prev_response:
            with open("previous_response.py", "w") as file:
                file.write(prev_response)
            try:
                output = os.popen("python3 previous_response.py").read()
                return "Output:\n" + output
            except Exception as e:
                return "Error: Unable to run the previous response."

        else:
            return "No previous input to execute."

    # If the AI doesn't know the answer, return a special response
    answer = input("I don't know the answer to that. Please tell me:")
    knowledge.add_to_knowledge(sentence_lower, answer)
    prev_response = answer
    return "ASK_USER"

@app.route("/process_input/<sentence>", methods=["GET"])
def process_input(sentence):
    user_input = sentence.strip()

    if user_input.lower() == "exit":
        return jsonify({"response": "Exiting AI..."})

    response = ai(user_input)
    if response == "ASK_USER":
        return jsonify({"response": "ASK_USER"})
    else:
        return jsonify({"response": response})

@app.route("/run/<code>", methods=["GET"])
def process_code(code):
    try:
        output = os.popen("python3 -c \"{}\"".format(code)).read()
        return jsonify({"response": "Output:\n" + output})
    except Exception as e:
        return jsonify({"response": "Error: Unable to execute the code."})

if __name__ == "__main__":
    app.run(port=5000)
