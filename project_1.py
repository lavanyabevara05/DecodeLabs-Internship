print("Welcome to AI Chatbot!")

name = "" # if user starts by press enter name is an error so we intialize
while True:
    user = input("You: ").lower()

    if user in("hello" , "hi" , "hey"):
        print("AI : Hi dear ! Nice to meet you ")
        name = input("can u please tell me your sweer name dear: ")
        print (f"That's Beautiful name {name}")

    elif user == "":
      print(f"let's talk {name}")

    elif user == "how are you":
        print("AI : I'm doing great!")


    elif user == "what is python":
      print("AI : Python is a high-level programming language.")

    elif user =="what is github":
      print(" AI :  GitHub is an online platform that stores Git repositories")

    elif user == "bye":
        print(" AI : Thank you! Have a wonderful day.")
        break


    else:
        print("Bot: Sorry, I don't understand.")


