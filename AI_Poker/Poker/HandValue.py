# from selectors import EpollSelector
from AI_Poker.Poker.Card import Card, CardSuit, CardValue

class HandValue:
    """
    Implements all the logic for evalulting a hand and determining a score
    """

    def __init__(self):
        self.cards = []
        self.cardValues = dict()
        self.suits = []
        for suit in CardSuit:
            self.suits.append(CardSuit(suit))
        self.cardSuits  = dict()

    def evalCardValues(self):
        self.cardValues = dict.fromkeys([2,3,4,5,6,7,8,9,10,11,12,13,14], 0)
        self.cardSuits  = dict.fromkeys(self.suits, 0)
        self.sortCards()
        for card in self.cards:
            #logic for parsing hand
            self.cardValues[card.value]+=1
            self.cardSuits[card.suit]+=1
            # print()

        print(self.cardValues)
        print(self.cardSuits)

    def sortCards(self):
        self.cards = sorted(self.cards, key = lambda x : (x.suit, x.value))
        for card in self.cards:
            print(card.suit, " ",card.value)
        
    def isRoyalFlush(self):
        print("Royal Flush")
        if(self.isStraightFlush()):
            for i in range(10, 15):
                if (self.cardValues[i]==0):
                    return False
            return True
        else:
            return False

    def isStraightFlush(self):
        print("Straight Flush")
        straightFlushCounter = 0
        if (self.isFlush() and self.isStraight()):
            for i in range(0,len(self.cards)-1):
                if(self.cards[i].suit==self.cards[i+1].suit) and (self.cards[i].value==self.cards[i+1].value-1):
                    straightFlushCounter+=1
                if(straightFlushCounter==4):
                    return True
        else:
            return False

    def isQuads(self):
        print("Quads")
        for card in self.cardValues:
            if (self.cardValues[card]==4):
                return True
        return False

    def isFullHouse(self):
        print("Full House")
        if(self.isTrips() and self.isPair()):
            return True
        else:
            return False

    def isFlush(self):
        print("Flush")
        for suit in self.cardSuits:
            if(self.cardSuits[suit]==5):
                return True
        return False

    def isStraight(self):
        print("Straight")
        for i in range(2, 11):
            if (self.cardValues[i]>=1):
                straightCounter = 0
                for j in range(i+1, i+5):
                    if (self.cardValues[j]>=1):
                        straightCounter+=1
                if(straightCounter==4):
                    return True
        return False

    def isTrips(self):
        print("Trips")
        for card in self.cardValues:
            if (self.cardValues[card]==3):
                return True
        return False

    def isTwoPair(self):
        print("Two Pair")
        numOfPairs = 0
        for card in self.cardValues:
            if (self.cardValues[card]==2):
                numOfPairs+=1
        return numOfPairs==2

    def isPair(self):
        print("Pair")
        for card in self.cardValues:
            if (self.cardValues[card]==2):
                return True
        return False

    def isHighCard(self):
        print("High Card")
        maxValue = 0
        for card in self.cardValues:
            if (self.cardValues[card]==1 and card>maxValue):
                maxValue=card
        print("Highest Card is: ", maxValue)
        return True

    def determineHandValue(self):
        self.evalCardValues()

        if (self.isRoyalFlush()):
            return 10
        elif (self.isStraightFlush()):
            return 9
        elif (self.isQuads()):
            return 8
        elif (self.isFullHouse()):
            return 7
        elif (self.isFlush()):
            return 6
        elif (self.isStraight()):
            return 5
        elif (self.isTrips()):
            return 4
        elif (self.isTwoPair()):
            return 3
        elif (self.isPair()):
            return 2
        elif (self.isHighCard()):
            return 1

    def valueHand(self, cards) -> int:
        self.cards = cards
        return self.determineHandValue()
