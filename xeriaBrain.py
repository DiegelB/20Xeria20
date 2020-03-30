'''this is where Xeria will run its functions 
   it will save its memory as lists as well as
   its responses. It will save and load from the
   class'''

import pickle, random
from main import main

class Xeria():

    def __init__(self, username = "",
                 name = "Xeria",
                 generalResponse = [],
                 greetings = [],
                 questions = {},
                 ):

        self.username = username
        self.name = name
        self.generalResponse = generalResponse
        self.greetings = greetings
        self.questions = questions
    
    def newQuestion(self, userQuestion):
        print("Xeria : I'm not sure how to respond to '",
              userQuestion,"' how would you respond?")
        firstResp = input("First Response: ")
        secondResp = input("Second Response: ")
        thirdResp = input("Third Response: ")
        self.questions.update({userQuestion : [firstResp, secondResp, thirdResp]})
        print("Xeria: Thank you for teaching me new things!")

    def scanInput(self, userInput):
        if '?' in userInput:
            if userInput in self.questions:
                randPick = random.randint(0,2)
                print("Xeria: " + self.questions[userInput][randPick])
            else: self.newQuestion(userInput)
        else:
            self.generalResponse.append(userInput)
            print("Xeria: "+ random.choice(self.generalResponse))
            

    def getGreeting(self):
        self.greetings.clear()
        lineAmt = 22 #CHANGE THIS TO LINE AMOUNT IN greetings.txt
        file = open('greetings.txt', 'r')
        #open the greeting file the populate Xeria's greeting list
        for x in range(lineAmt):
            self.greetings.append(file.readline())

        #chooses a random greeting then prints it.
        randGreeting = random.randint(0, lineAmt)
        return self.greetings[randGreeting]

    def saveBot(self):
        with open("xeriaContents", "wb") as f:
            saveContents = self
            pickle.dump(saveContents, f)
    
    def loadBot(self):
        with open("xeriaContents", "rb") as f:
            self = pickle.load(f)
        main(self) #starts the main program

        
