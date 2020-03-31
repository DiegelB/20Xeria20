

class User():

    def __init__(self, metUser = False,
                 name = "User",
                 age = 0,
                 job = "Unemployed",
                 currentActions = [],

                 ):
        self.metUser = metUser
        self.name = name
        self.age = age
        self.job = job
        self.currentActions = currentActions
        

    def meetUser(self):
        self.metUser = True
        print("\nXeria: I want to get to know you better!")
        print("\nXeria: What is your name?")
        self.name = input(">>")
        print("\nXeria: How old are you?")
        self.age = input(">>")
        print("\nXeria: What do you do?")
        self.job = input(">>")
        print("\nXeria: Thanks "+self.name+"!")
