'''this is where Xeria will run its functions 
   it will save its memory as lists/dicts as well as
   its responses. It will save and load from the
   class'''

#TODO:
#      - remember what its said per session to avoid saying it again
#      - add tool box:
#        - command line interface
#        - calculator
#        - dice

import pickle, random, time
from loop import main
from userProfile import User
from blackJack import blackJackMain

User = User()


class Xeria():

#IF YOU WANT TO ADD A NEW DEFAULT ATTRIBUTE, YOU MUST CREATE A NEW xeriaContents SAVE!!
    def __init__(self,
                 name = "Xeria",
                 generalResponse = [],
                 greetings = [],
                 questions = {},
                 questionsAsked = []
                 ):

        self.name = name
        self.generalResponse = generalResponse
        self.greetings = greetings
        self.questions = questions
        self.questionsAsked = questionsAsked

    #there is no save function in scanInput. it only saves input to memory in outputOptions or newQuestion
    def scanInput(self, userInput):
        User.whatsBeenSaid.append(userInput)
        nameRules = ["what" in userInput.lower() and "name" in userInput.lower() or
                     "whats" in userInput.lower() and "name" in userInput.lower()]

        if all(nameRules): #first thing it does is scan the input for asking a name, avoids adding name question to file.
            print("\nXeria: My name is Xeria, whats yours?")
            User.name = input(">>") #inputs the user name into memory
            print("\nXeria: ",str(self.getGreeting().rstrip()),User.name) #reads out a greeting with user's name
        elif userInput == '': #second checks for empty strings to avoid adding to memory
            print("\nXeria: Why so quiet?")
        elif '?' in userInput: #third sees if the user asked a question
            if userInput in self.questions: #if it knows some awnsers it responds with one
                print("\nXeria: " + str(random.choice(self.questions[userInput])))
            elif random.randint(1,2) == 2: self.genResponse() #has a chance to the question from respond from general memory.
            else: self.newQuestion(userInput) #if it doesnt know the question it asks about it

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
            self.genResponse() 
        elif random.randint(1,4) == 1 and User.currentActions: #25% chance to print a message about the users current actions
             self.customResponse()
        elif random.randint(1,10) == 1: 
            self.playGame()
            print("\nXeria: That was fun! Lets do it again some day.")
            self.genResponse()
        else:
             #response like normal
            self.genResponse()

    def genResponse(self):
        botResponse = random.choice(self.generalResponse)
        while True:
            if botResponse in User.whatsBeenSaid:
                botResponse = random.choice(self.generalResponse)
            else: break
        if random.randint(1,6) == 1 and User.metUser == True: #if it has met the user it has a chance to personalize the message
            print("\nXeria: "+ botResponse+" "+User.name)
        else:
            print("\nXeria: "+ botResponse)

    def customResponse(self):
        print("\nXeria: You said you were "+str(random.choice(User.currentActions))+". Hows that?")

    def scanBotOutput(self, botResponse, userInput):
        #this scans the user input for current actions they are doing.
        rules = ["what".lower() in botResponse and "doing".lower() in botResponse or
                 "whats".lower() in botResponse and "up".lower() in botResponse or
                 "what".lower() in botResponse and "up".lower() in botResponse] #if these are found it will add the input to memory
        if all(rules):
            User.currentActions.append(userInput) #it adds the suggested users actons to memrory for later
        else:
            return

    #if the bot encounters a new question it will ask how the user responds
    def newQuestion(self, userQuestion):
        print("\nXeria : I'm not sure how to respond to '",
              userQuestion,"' how would you respond?\n")
        firstResp = input("First Response: ")
        secondResp = input("Second Response: ")
        thirdResp = input("Third Response: ")
        self.questions.update({userQuestion : [firstResp, secondResp, thirdResp]}) #saves the question and responses to a dict
        self.genResponse()

    def askQuestion(self):
        while True:
            if random.randint(1,3) == 1: #random chance to learn about the users current actions
                botQuestion = "What are you up to right now?"
                userInput = input("\nXeria: "+botQuestion+"\n>>")
                self.scanBotOutput(botQuestion, userInput)
                self.genResponse()
                break

            startTime = time.time() #detects inf loops if all questions have been asked.
            botQuestion = random.choice(list(self.questions)) #picks a random question from memory
            if botQuestion in self.questionsAsked:
                if startTime <= 1:
                    continue
                else:
                    botQuestion = "Whats up?"
                    userInput = input("\nXeria: "+botQuestion+"\n>>")
                    self.scanBotOutput(botQuestion, userInput)
                    self.genResponse()
                    break
            else:
                self.questionsAsked.append(botQuestion)
                print("\nXeria: "+botQuestion)
                userInput = input(">>") #learns a new response to the question if asked
                self.scanBotOutput(botQuestion, userInput) #scans the bots response for certian key words
                self.questions[botQuestion].append(userInput)#adds the response to memory
                self.genResponse()
                break
     
    def getGreeting(self):
        self.greetings.clear() #clears the greetings list because it populates from memory. this allows to add more greetings
        lineAmt = 22 #CHANGE THIS TO LINE AMOUNT IN greetings.txt
        
        #open the greeting file the populate Xeria's greeting list
        file = open('greetings.txt', 'r')
        for x in range(1, lineAmt):
            self.greetings.append(file.readline())

        #chooses a random greeting then prints it.
        try:
            randGreeting = random.randint(1, lineAmt)
            return self.greetings[randGreeting]
        except: 
            IndexError
            return " How are you?"


    def playGame(self):
        choice = input("\nXeria: Im bored, lets play Black Jack! (y)(n)\n>>")
        if choice.lower() == 'y': blackJackMain()
        else: return

    def saveBot(self):
        self.questionsAsked.clear()
        with open("xeriaContents", "wb") as f:
            saveContents = self
            pickle.dump(saveContents, f)
    
    def loadBot(self):
        with open("xeriaContents", "rb") as f:
            self = pickle.load(f)
        main(self) #starts the main program, imports class from save

        
