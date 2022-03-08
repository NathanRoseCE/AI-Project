from AI_Poker.Poker.Card import Card, CardSuit

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
            print()
        


    def determineHandValue(self):
        self.evalCardValues()


    def valueHand(self, cards):
        self.cards = cards
