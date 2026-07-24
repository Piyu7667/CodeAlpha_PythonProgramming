def bot ():
    while True :
        msg = input("You: ").lower()
        if msg == "hello":
            print("Bot: Hi!")
        elif msg == "how are you" :
            print("Bot: GoodBye!")
            break
        else:
            print("Bot: I don't understand.")

bot()