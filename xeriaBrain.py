'''this is where Xeria will run its functions 
   it will save its memory as lists/dicts as well as
   its responses. It will save and load from the
   class'''

import pickle, random
from loop import main
from userProfile import User

User = User()

class Xeria():

    def __init__(self,
                 name = "Xeria",
                 generalResponse = [],
                 greetings = [],
                 questions = {},
                 ):

        self.name = name
        self.generalResponse = generalResponse
        self.greetings = greetings
        self.questions = questions
    
    def scanInput(self, userInput):
        if '?' in userInput: #sees if the user asked a question
            if userInput in self.questions: #if it knows some awnsers it responds with one
                print("\nXeria: " + str(random.choice(self.questions[userInput])))
            else: self.newQuestion(userInput, userInput) #if it doesnt know the question it asks about it
        elif userInput == '': #checks for empty strings to avoid adding to memory
            print("Xeria: Why so quiet?")
        else: #if all input conditions are not met then it runs the output funciton
            self.outputOptions(userInput)
            
    #this chooses the type of output that the chatbot sends out
    def outputOptions(self, userInput):
        if userInput not in self.generalResponse: #checks to see if user input already in memory 
            self.generalResponse.append(userInput) #adds the users input to general memory if above is tru  
        if random.randint(1,4) == 1: #bot has 25% chance of asking a question from memory
            self.askQuestion()
        elif random.randint(1,5) == 1 and User.metUser == False: #chance to get to know the user
            User.meetUser()
            self.genResponse(userInput) 
        elif random.randint(1,4) == 1 and User.currentActions: #25% chance to print a message about the users current actions
             self.customResponse()
        else:
             #response like normal
            self.genResponse(userInput)

    def genResponse(self, userInput):
        botResponse = random.choice(self.generalResponse)
        self.scanBotOutput(botResponse, userInput) #scans the bots response for certian key words
        if random.randint(1,6) == 1 and User.metUser == True: #if it has met the user it has a chance to personalize the message
            print("\nXeria: "+ botResponse+" "+User.name)
        else:
            print("\nXeria: "+ botResponse)

    def customResponse(self):
        print("\nXeria: You said you were "+str(random.choice(User.currentActions))+". Hows that?")

    def scanBotOutput(self, botResponse, userInput):
        rules = ["what".lower() in botResponse and "doing".lower() in botResponse or
                 "whats".lower() in botResponse and "up".lower() in botResponse or
                 "what".lower() in botResponse and "up".lower() in botResponse] #if these are found it will add the input to memory
        if all(rules):
            User.currentActions.append(userInput) #it adds the suggested users actons to memrory for later
        else:
            return

    #if the bot encounters a new question it will ask how the user responds
    def newQuestion(self, userQuestion, userInput):
        print("\nXeria : I'm not sure how to respond to '",
              userQuestion,"' how would you respond?\n")
        firstResp = input("First Response: ")
        secondResp = input("Second Response: ")
        thirdResp = input("Third Response: ")
        self.questions.update({userQuestion : [firstResp, secondResp, thirdResp]}) #saves the question and responses to a dict
        self.genResponse(userInput)

    def askQuestion(self):
        botQuestion = random.choice(list(self.questions)) #picks a random question from memory
        print("\nXeria: "+botQuestion)
        userInput = input(">>") #learns a new response to the question if asked
        self.questions[botQuestion].append(userInput)#adds the response to memory
        self.genResponse(userInput)
  
    def getGreeting(self):
        self.greetings.clear() #clears the greetings list because it populates from memory. this allows to add more greetings
        lineAmt = 22 #CHANGE THIS TO LINE AMOUNT IN greetings.txt
        
        #open the greeting file the populate Xeria's greeting list
        file = open('greetings.txt', 'r')
        for x in range(1, lineAmt):
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
        main(self) #starts the main program, imports class from save

        
