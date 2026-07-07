print("Welcome to AI Chatbot!")

while True:
    user = input("You: ").lower()

    if user in("hello" , "hi" , "hey"):
        print("Bot: Hi dear ")

    elif user == "how are you":
        print("Bot: I'm doing great!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
        


