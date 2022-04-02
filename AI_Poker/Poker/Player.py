"""
Assumptions

return money used during action to the board
0 is check 
-1 is fold
pos int is money for bet or raise
"""
from numpy import minimum
from AI_Poker.Poker.Card import Card


class Player:
    """
    impliement player object
    """
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money


    def setCard(self, card):
        """
        sets a card in the player's hand

        accepts card object
        """
        self.hand.append(card)



    def getHand(self):
        """
        Returns players hand 
        Array of two card objects
        """
        return self.hand


    def clearHand(self):
        """
        Clears players hand
        """
        self.hand = []


    def fold(self):
        """
        Player folds, clear hand
        """
        self.clearHand()
        return -1


    def deduct_money(self, amount):
        """
        Remove `amount` from players money
        If `amount` is greater than players money set players money to 0 
        """
        if (self.money>=amount):
            self.money -= amount
            return amount
        else:
            money = self.money
            self.money = 0
            return money



    def call(self, current_bet):
        """
        Players calling action
        `current_bet` is the amount the player is calling
        """
        return self.deduct_money(current_bet)
    

    def raise_action(self, current_bet, raise_amount, min_bet):
        """
        Players raise action
        `current_bet` is the amount the player is current bet of the table
        `raise_amouint` is the amount the player wants to raise by
        `minimum_bet` is the min bet of the game
        """
        if(raise_amount >= min_bet):
            return self.deduct_money(current_bet+raise_amount)
        else:
            raise ValueError("Raise is too small must be at least min bet")


    def bet(self, bet_amount, min_bet):
        """
        Players betting action
        `bet_amount` is the amount the player is betting
        """
        if(bet_amount>=min_bet):
            return self.deduct_money(bet_amount)
        else:
            raise ValueError("Bet is too small must be at least min bet")


    def check(self):
        """
        Players check action
        """
        return 0



    def decision(self, board):
        """
        Handles player decision logic, what they can and cant do based on board state
        """
        raise NotImplementedError
