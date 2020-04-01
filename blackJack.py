"""
Black jack game for chatBot to play with user.
"""
import random
from os import system

#TODO: 
    # - Add split
    # - Add Xeria functionality


class Dealer:

    def __init__(self,
                 mainHand = [],
                 deck = [],
                 chips = 10000):
        self.mainHand = mainHand
        self.deck = deck
        self.chips = chips

    #builds the 52 card deck
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

    #the dealer deals cards to itself until it hits a soft 17. 
    def dealerTurn(self):
        dealerAmt = getCardValue(self.mainHand, user = "dealer")
        while dealerAmt < 17:
            addToHand(self.mainHand, 1)
            dealerAmt = getCardValue(self.mainHand, user = "dealer")
        return dealerAmt



class PlayerHand:

    def __init__(self,
                 mainHand = [],
                 splitHand = [],
                 chips = 100,
                 betAmount = 0,
                 insuranceBet = 0):

        self.mainHand = mainHand
        self.splitHand = splitHand
        self.chips = chips
        self.betAmount = betAmount
        self.insuranceBet = insuranceBet



#creates the classes            
Dealer = Dealer()
Player = PlayerHand()

#main loop of the program
def blackJackMain():
    print("\n\tWelcome to Black Jack! Try and beat the dealer and make $$$.")
    while True:
        system("clear")
        resetGame() #resets the hands and bet amounts
        Player.betAmount = int(input("\nHow much would you like to bet? Total chips :"+str(Player.chips)+"\n>>"))

        while True: #this is the main loop for the player
            printHand(Player.mainHand)
            choice = input("\nType 'h' to hit, 's' to stay, 'i' for insurance\n>>")
            if choice.lower() == 'h': #adds a card to player hand
                addToHand(Player.mainHand, 1)
            elif choice.lower() == 'i': #pays 2:1 for betting the dealer will get 21
                if Player.insuranceBet != 0:
                    print("\nYou already have insurance!", str(Player.insuranceBet))
                    input("Press enter\n")
                else:
                    Player.insuranceBet = int(input("\nHow much do you bet that Dealer gets 21?\n>>"))
                    Player.chips -= Player.insuranceBet
            elif choice.lower() == 's':
                winCondition()
                break

#resets all the saved values
def resetGame():
    Dealer.buildDeck()
    Player.mainHand.clear()
    Dealer.mainHand.clear()
    addToHand(Player.mainHand, 2)
    addToHand(Dealer.mainHand, 2)
    Player.insuranceBet = 0

#adds any cards to players or dealers hand
def addToHand(hand, amountOfCards):
    hand.extend(Dealer.dealCards(amountOfCards))

#totals all the cards in the mainHand
def getCardValue(cards, user):
    handValue = 0
    royals = ['Jack','Queen','King']
    for x in cards:
        for word in x.split():
            if word.isdigit(): #checks for the number values then adds them
                handValue += int(word)
            if word in royals: #checks for jacks queens and kings adds ten
                handValue += 10
            if 'Ace' in word and user == "player": #checks for aces and prompts the user to add 11 or 1
                while True:
                    printHand(cards)
                    choice = input("\nAce can be an (11) or (1)?\n>>")
                    if choice == '11': 
                        handValue += 11 
                        break
                    elif choice == '1': 
                        handValue += 1 
                        break
                    else: print("\nYou did not choose correctly")
            elif 'Ace' in word and user == "dealer": #checks for dealers aces and makes them auto 11s
                handValue += 11
                break
    return handValue

#this prints the player and dealers hand with bet amount
def printHand(hand):
    system("clear")
    print("\n\tDealer Cards: ")
    for x in Dealer.mainHand: print("\t"+x)    
    print("\n\nYour cards:\tYour bet: ", str(Player.betAmount))
    for x in hand: print("\t"+x)

#simple win condition to end the game
def winCondition():
    playerHandValue = getCardValue(Player.mainHand, user = "player") #these get the card values of the player and dealer
    dealerHandValue = Dealer.dealerTurn()
    printHand(Player.mainHand)
    print("\nPlayer Total: ",playerHandValue,
          "\tDealer Total:", dealerHandValue)
    if dealerHandValue == 21: #if dealer gets 21 you lose unless you had an insurance bet
        if Player.insuranceBet == 0:
            lose()
        else:
            print("\nYou win! Here's ", str(Player.betAmount), " chips.")
            print("\nAnd for betting insurance heres ", str(Player.insuranceBet*2), " chips.")
            Player.chips += int(Player.betAmount)
            Player.chips += int(Player.insuranceBet*2)
    elif dealerHandValue > playerHandValue and dealerHandValue <= 21: #lose if dealer has higher card # 
        lose() 
    elif playerHandValue > 21: #lose if you bust
        lose()
    elif playerHandValue == 21: #3:1 payout for winning 21
        print("\n21! You win 3:1 of your bet amount!\nHere's ", str(Player.betAmount*3), " chips.")
        Player.chips += int(Player.betAmount*3)
    else:
        print("\nYou win! Here's ", str(Player.betAmount), " chips.")
        Player.chips += int(Player.betAmount)
    
    choice = input("\nAgain? (y)(n)\n>>")
    if choice.lower() == 'y':
        return
    else: exit()

def lose():
    print("\nYou lose! Thank you for ", str(Player.betAmount), " chips.")
    Player.chips -= int(Player.betAmount)


blackJackMain()


