from os import system

def main(ChatBot):
    system("clear")
    print("\n\tWelcome to Xeria ChatBot 2020!",
          "\n\tYou can chat with Xeria, ask it questions,",
          "\n\tand more! Just start talking to begin.",
          "\n\n\tType 'exit' to leave and 'h' for more commands.\n")
    print("Xeria:", ChatBot.getGreeting()) 
    
    #this is the main loop where the user asks questions and the bot responds
    while True:
        userInput = input(">>")
        #command help
        if userInput == 'h':
            print("Type 'exit' to exit the program\n",
                  "Type 'h' for command help")
        elif userInput == 'exit': break #exit the loop
        else:
            #this scans the user input and executes certian respones in xeriaBrain.py
            print()
            ChatBot.scanInput(userInput)

    #save the bot for the next session
    print("Xeria: Thank you for chatting. I'll remember our great times!")
    ChatBot.saveBot()
