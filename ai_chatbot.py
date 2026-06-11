print("Bot: Hello! I am Codmetric Bot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Codmetric Bot.")

    elif user == "help":
        print("Bot: You can ask me simple questions.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")