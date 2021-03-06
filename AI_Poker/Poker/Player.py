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
        if amount < 0:
            return 0
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
        if bet_amount > self.money:
            bet_amount = self.money
        if bet_amount < 0:
            bet_amount = 0
        return self.deduct_money(bet_amount)


    def check(self):
        """
        Players check action
        """
        return 0



    def decision(self, board):
        """
        Handles player decision logic, what they can and cant do based on board state
        Assumptions

        return money used during action to the board
        0 is check 
        -1 is fold
        pos int is money for bet or raise
        """
        # raise NotImplementedError
        # board.global_state
        global_state = board.global_state
        if (global_state["current_bet"] == 0):
            #check or bet
            decision = int(input("Either check(0) or bet(Enter amount, min bet: "+ str(global_state["bet_min"])+")"))
            if (decision==0):
                return self.check()
            elif(decision>=global_state["bet_min"]):
                self.bet(decision, global_state["bet_min"])
            
        elif (global_state["current_bet"]>0):
            #call or raise or fold
            decision = int(input("Either: Fold(-1), call(0) or raise(Enter amount, min raise: "+ str(global_state["current_bet"]+global_state["bet_min"])+")"))
            if (decision==-1):
                return self.fold()
            elif(decision==0):
                self.call(global_state["current_bet"])
                return decision
            elif(decision>=global_state["current_bet"]+global_state["bet_min"]):
                self.raise_action(global_state["current_bet"], decision, global_state["current_bet"]+global_state["bet_min"])
                return decision
            

