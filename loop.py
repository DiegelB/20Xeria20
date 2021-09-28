from os import system
from blackJack import blackJackMain

#main loop for the program. It has the start screen and the input loop for user. 
#loads chat bot in from xeriaBrain.py
def main(ChatBot): 
    system("clear")
    print("\n\tWelcome to Xeria ChatBot 2020!",
          "\n\tYou can chat with Xeria, ask it questions,",
          "\n\tand more! Just start talking to begin.",
          "\n\n\tType 'exit' to leave and 'h' for more commands.")
    print("\nXeria:", ChatBot.getGreeting()) 
    
    #this is the main loop where the user asks questions and the bot responds
    while True:
        userInput = input(">>")
        userInput = userInput.lower()
        #command help
        if userInput == 'h':
            print("Type 'exit' to exit the program\n",
                  "Type 'h' for command help\n",
                  "Type 'bj' to play BlackJack",
                  "Type 'W2W' to run the What to Watch program")
        elif userInput == 'bj': blackJackMain()
        elif userInput == 'exit': break #exit the loop
        else:
            #this scans the user input and executes certian respones in xeriaBrain.py
            ChatBot.scanInput(userInput)

    #save the bot for the next session
    print("Xeria: Thank you for chatting. I'll remember our great times!")
    ChatBot.saveBot()
