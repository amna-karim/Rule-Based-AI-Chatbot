while True:

    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "python":
        print("Bot: Python is a powerful programming language.")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "thanks":
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: You can ask me:")
        print("- hi")
        print("- hello")
        print("- how are you")
        print("- what is ai")
        print("- python")
        print("- what is your name")
        print("- thanks")
        print("- bye")

    elif user == "who created you":
        print("Bot: I was created by an AI Intern using Python.")

    elif user == "internship":
        print("Bot: Internship helps students gain practical experience.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")