def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "how are you" in message:
        return "I'm just a simple program, but I'm doing fine!"

    elif "name" in message:
        return "I don't have a real name, but you can call me ChatBot."

    elif "help" in message:
        return "You can say hello, ask how I am, or ask my name."

    elif "bye" in message or "quit" in message:
        return "Goodbye! It was nice talking to you."

    else:
        return "I don't understand that yet."

def main():
    print("Simple Chatbot")
    print("Type 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
