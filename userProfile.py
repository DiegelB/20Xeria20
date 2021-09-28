

class User():

    def __init__(self, metUser = False,
                 name = "User",
                 age = 0,
                 job = "Unemployed",
                 currentActions = [],
                 whatsBeenSaid = []
                 ):
        self.metUser = metUser
        self.name = name
        self.age = age
        self.job = job
        self.currentActions = currentActions
        self.whatsBeenSaid = whatsBeenSaid
        

    def meetUser(self):
        self.metUser = True #sets this to true to avoid calling this fuction twice.
        print("\nXeria: I want to get to know you better!")
        if self.name == "User": #if the user already told the bot their name it skips asking again
            print("\nXeria: What is your name?")
            self.name = input(">>")
        
        print("\nXeria: How old are you?")
        self.age = input(">>")
        print("\nXeria: What do you do?")
        self.job = input(">>")
        print("\nXeria: Thanks "+self.name+"!")
