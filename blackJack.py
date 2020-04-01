"""
Black jack game for chatBot to play with user.
"""
import random
from os import system

#TODO: 
    # - Add betting, split, insurance
    # - Add play against dealer
    # - Add Xeria functionality
    # - Basically finish programming the game b/c all i have rn is the framework lol 


class Dealer:

    def __init__(self,
                 mainHand = [],
                 deck = [],
                 chips = 10000):
        self.mainHand = mainHand
        self.deck = deck
        self.chips = chips

    def buildDeck(self):
        self.deck.clear() #clears the deck in between uses to avoid over populating
        cardValues = [2,3,4,5,6,7,8,9,10,'Ace','Jack','Queen','King']
        faceValues = [" of hearts", " of diamonds", " of spades", " of clubs"]
        for x in range(0,13): #adds in the card items. 
            for y in range(0,4):
                cardName = str(cardValues[x]) + str(faceValues[y])
                self.deck.append(cardName)

    def dealCards(self, amount): #deals any amount of cards and the removes them from the deck
        cards = []
        for x in range(amount):
            currentCard = random.choice(self.deck)
            cards.append(currentCard)
            self.removeCard(currentCard)
        return cards
    
    def removeCard(self, cardToRemove):
        self.deck.remove(cardToRemove)


class PlayerHand:

    def __init__(self,
                 mainHand = [],
                 handValue = 0,
                 splitHand = [],
                 chips = 100):

        self.mainHand = mainHand
        self.handValue = handValue
        self.splitHand = splitHand
        self.chips = chips

    #adds cards from dealer into their hand
    def getCards(self, cards):
        self.mainHand.extend(cards)

    #totals all the cards in the mainHand
    def getCardValue(self):
        royals = ['Jack','Queen','King']
        for x in self.mainHand:
            for word in x.split():
                if word.isdigit(): #checks for the number values then adds them
                    self.handValue += int(word)
                if word in royals: #checks for jacks queens and kings adds ten
                    self.handValue += 10
                if 'Ace' in word: #checks for aces and prompts the user to add 11 or 1
                    while True:
                        choice = input("\nAce can be an (11) or (1)?\n>>")
                        if choice == '11': 
                            self.handValue += 11 
                            break
                        elif choice == '1': 
                            self.handValue += 1 
                            break
                        else: print("\nYou did not choose correctly")

    #simple win condition to end the game
    def winCondition(self):
        system("clear")
        self.getCardValue()
        print("Your cards were ",str(self.mainHand))
        print("With a total of: ",self.handValue)
        if self.handValue <= 21:
            print("You win!")
        else:
            print("You lose!")

#creates the classes            
Dealer = Dealer()
Player = PlayerHand()

#main loop of the program
def blackJackMain():
    Dealer.buildDeck()
    Player.getCards(Dealer.dealCards(2))

    while True:
        system("clear")
        print("\nYou cards: ", str(Player.mainHand))
        choice = input("\nType 'h' to get another card or 's' to stay\n>>")
        if choice.lower() == 'h':
            Player.getCards(Dealer.dealCards(1))
        elif choice.lower() == 's':
            Player.winCondition()
            break

blackJackMain()


