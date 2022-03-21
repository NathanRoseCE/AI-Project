from selectors import EpollSelector
from AI_Poker.Poker.Card import Card, CardSuit, CardValue

class HandValue:
    """
    Implements all the logic for evalulting a hand and determining a score
    """

    def __init__(self):
        self.cards = []
        self.cardValues = dict()
        self.suits = []
        for suit in range(4):
            self.suits.append(CardSuit(suit))
        self.cardSuits  = dict()

    def evalCardValues(self):
        self.cardValues = dict.fromkeys([2,3,4,5,6,7,8,9,10,11,12,13,14], 0)
        self.cardSuits  = dict.fromkeys(self.suits, 0)
        for card in self.cards:
            #logic for parsing hand
            self.cardValues[card.value]+=1
            self.cardSuits[card.suit]+=1
            # print()
        
    def isRoyalFlush(self):
        print("Royal Flush")
        for suit in self.cardSuits:
            if (self.cardSuits[suit]==5):
                for i in range(10, 15):
                    if (self.cardValues!=1):
                        return False
                return True
            else:
                return False

    #this feels gross and clunky but good enough for now
    #might want to break up into is straight function but will only be used twice....
    def isStraightFlush(self):
        print("Straight Flush")
        for suit in self.cardSuits:
            if (self.cardSuits[suit]==5):
                for i in range(2, 14):
                    if (self.cardValues[i]==1):
                        for j in range(i+1, i+4):
                            if (self.cardValues[j]!=1):
                                return False
                        return True
            else:
                return False


    def isQuads(self):
        print("Quads")
        for card in self.cardValues:
            if (self.cardValues[card]==4):
                return True
            else:
                return False

    def isFullHouse(self):
        print("Full House")


    def isFlush(self):
        print("Flush")
        for suit in self.cardSuits:
            if(self.cardSuits[suit]==5):
                return True
            else:
                return False

    def isStraight(self):
        print("Straight")
        for i in range(2, 14):
            if (self.cardValues[i]==1):
                for j in range(i+1, i+4):
                    if (self.cardValues[j]!=1):
                        return False
                return True

    def isTrips(self):
        print("Trips")
        for card in self.cardValues:
            if (self.cardValues[card]==3):
                return True
            else:
                return False

    def isTwoPair(self):
        print("Two Pair")

    def isPair(self):
        print("Pair")
        for card in self.cardValues:
            if (self.cardValues[card]==2):
                return True
            else:
                return False

    def isHighCard(self):
        print("High Card")

    def determineHandValue(self):
        self.evalCardValues()

        if (self.isRoyalFlush()):
            print(10)
        elif (self.isStraightFlush()):
            print(9)
        elif (self.isQuads()):
            print(8)
        elif (self.isFullHouse()):
            print(7)
        elif (self.isFlush()):
            print(6)
        elif (self.isStraight()):
            print(5)
        elif (self.isTrips()):
            print(4)
        elif (self.isTwoPair()):
            print(3)
        elif (self.isPair()):
            print(2)
        elif (self.isHighCard()):
            print(1)




    def valueHand(self, cards):
        self.cards = cards
        self.determineHandValue()
