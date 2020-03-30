

class User():

    def __init__(self, name = "User",
                 age = 0,
                 job = "Unemployed",
                 metUser = False
                 ):
        self.name = name
        self.age = age
        self.job = job
        self.metUser = metUser

    def meetUser(self):
        self.metUser = True
        print("Xeria: I want to get to know you better!")
        print("Xeria: What is your name?")
        self.name = input(">>")
        print("Xeria: How old are you?")
        self.age = input(">>")
        print("Xeria: What do you do?")
        self.job = input(">>")
        print("Xeria: Thank you :)")
        