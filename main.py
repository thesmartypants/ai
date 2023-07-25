import os
import knowledge
import random


def remove_common_words(sentence):
    remove_words = ["in", "and", "how", "do", "i", "a", "to", "is", "the", "of", "for", "python", "make", "create", "check", "you"]
    words = sentence.lower().split()  # Split the sentence into words using spaces as delimiters
    filtered_words = []
    for word in words:
        if word not in remove_words:
            filtered_words.append(word)
    return " ".join(filtered_words)



def ai(sentence):
    global prev_response

    sentence_lower = remove_common_words(sentence.lower())

    # If exact match not found, check for exact match in knowledge
    if sentence_lower in knowledge.knowledge:
        # If exact match found, return a random response from the list
        response_list = knowledge.knowledge[sentence_lower]
        prev_response = random.choice(response_list)
        return prev_response

    # If no match found and the user says "run," execute the previous response
    elif sentence_lower == "run":
        if prev_response:
            print(f"\nCode: \n{prev_response}\n\nOutput:")


            try:
                with open("previous_response.py", "w") as file:
                    file.write(prev_response)
                output = os.popen("python3 previous_response.py 2>&1").read()
                if "SyntaxError" in output:
                    print("No code to run.")
                else:
                    print(output)
            except Exception as e:
                print("An error occurred:", e)
            return None
        else:
            return "No previous input to execute."

    # If no match found, ask the user for a response
    answer = input("I don't know the answer to that. Please tell me:")
    print(answer)
    knowledge.add_to_knowledge(sentence_lower, answer)
    prev_response = answer
    return "Okay, I've learned something new!"


if __name__ == "__main__":
    prev_response = None
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ai(user_input)
        if response is not None:
            print("\nAI:\n", response, '\n')
