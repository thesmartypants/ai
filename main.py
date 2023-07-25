import knowledge
import random


def remove_common_words(sentence):
    remove_words = ["in", "and", "how", "do", "i", "a", "to", "is", "the", "of", "for", "python", "make", "create", "check", "you"]
    words = sentence.lower().split()  # Split the sentence into words using spaces as delimiters
    filtered_words = [word for word in words if word not in remove_words]
    return " ".join(filtered_words)


def ai(sentence):
    sentence_lower = remove_common_words(sentence.lower())

    # If exact match not found, check for exact match in knowledge
    if sentence_lower in knowledge.knowledge:
        # If exact match found, return a random response from the list
        response_list = knowledge.knowledge[sentence_lower]
        return random.choice(response_list)

    # If no match found, ask the user for a response
    answer = input("I don't know the answer to that. Please tell me:\n")

    # Replace escaped newlines "\\n" with actual newlines "\n"
    answer = answer.replace("\\n", "\n")

    knowledge.add_to_knowledge(sentence_lower, answer)
    return "Okay, I've learned something new!"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ai(user_input)
        print("\nAI:\n", response, '\n')
