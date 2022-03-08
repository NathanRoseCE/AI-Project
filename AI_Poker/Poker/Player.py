from numpy import minimum
from AI_Poker.Poker.Card import Card

"""
Assumptions

return money used during action to the board
0 is check 
-1 is fold
pos int is money for bet or raise
"""



class Player:
    """
    impliement player object
    """
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money

    """
    sets a card in the player's hand

    accepts card object
    """
    def setCard(self, card):
        self.hand.append(card)


    """
    Returns players hand 
    Array of two card objects
    """
    def getHand(self):
        return self.hand

    """
    Clears players hand
    """
    def clearHand(self):
        self.hand = []

    """
    Player folds, clear hand
    """
    def fold(self):
        self.clearHand()
        return -1

    """
    Remove `amount` from players money
    If `amount` is greater than players money set players money to 0 
    """
    def deduct_money(self, amount):
        if (self.money>=amount):
            self.money -= amount
            return amount
        else:
            money = self.money
            self.money = 0
            return money


    """
    Players calling action
    `current_bet` is the amount the player is calling
    """
    def call(self, current_bet):
        return self.deduct_money(current_bet)
    
    """
    Players raise action
    `current_bet` is the amount the player is current bet of the table
    `raise_amouint` is the amount the player wants to raise by
    `minimum_bet` is the min bet of the game
    """
    def raise_action(self, current_bet, raise_amount, min_bet):
        if(raise_amount >= min_bet):
            return self.deduct_money(current_bet+raise_amount)
        else:
            raise ValueError("Raise is too small must be at least min bet")

    """
    Players betting action
    `bet_amount` is the amount the player is betting
    """
    def bet(self, bet_amount, min_bet):
        if(bet_amount>=min_bet):
            return self.deduct_money(bet_amount)
        else:
            raise ValueError("Bet is too small must be at least min bet")

    """
    Players check action
    """
    def check(self):
        return 0


    """
    Handles player decision logic, what they can and cant do based on board state
    """
    def decision(self, board):



