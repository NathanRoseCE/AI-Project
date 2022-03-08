from typing import Iterable
from AI_Poker.Poker.Card import Card
from AI_Poker.Poker.Deck import Deck
import numpy as np
import logging

#TODO remove these with the actual object
class Player:
    def __init__(self, start_money: float) -> None:
        self.money = start_money
        self.hand = []

    def make_decision(bet_minimum: float, global_state: dict) -> float:
        """
        returns the bet the player would like to make
        """
        return bet_minimum

class RuleScoring:
    """
    This contains information for the rules of texas holdem
    """
    def __init__(self, score:int=0) -> None:
        self._score = score
        
    def score(self, cards: Iterable[Card]) -> int:
        """
        This is a simple method that returns the score if the 
        condition is met, and 0 if nothing is met
        """
        return self._score

class Board:
    """
    This is the main class that tracks all of the information and runs a game
    """
    MAX_PLAYERS=5
    def __init__(self,
                 players: Iterable[Player],
                 scoring_rules: Iterable[RuleScoring],
                 deck: Deck
                 ) -> None:
        if len(players) > Board.MAX_PLAYERS:
            raise ValueError(f"Cant play with more than {Board.MAX_PLAYERS}")
        self._active_players = players
        self._rules = scoring_rules
        self._deck = deck
        self._community_cards = []

    def hand(self) -> None:
        """
        plays one hand of poker, assume the deck is set up correctly
        """
        self._deal_cards()
        

    def _deal_cards(self) -> None:
        """
        deals the cards to the players
        """
        logging.info(f"dealing cards to {len(self._active_players)} players")
        hands = []
        for _ in range(len(self._active_players)):
            hands.append([self._deck.next_card()])
        for i, _ in enumerate(range(len(self._active_players))):
            hands[i].append(self._deck.next_card())
            
        #TODO start with small blind
        for i, player in enumerate(self._active_players):
            player.hand = hands[i]

        #TODO create hidden cards
        self._community_cards = []
        for _ in range(5):
            self._community_cards.append(self._deck.next_card())
    
    def _ask_for_bets(self, starting_player: int) -> None:
        """
        Ask all of the players for thier bets
        """
        ask_player = starting_player
        bet_min = -1#TODO: set up big and little blind
        highest_bet_index=-1
        while True:
            if highest_bet_index == ask_player:
                break
            bet = self._active_players[ack_player].make_decision(
                self.global_state(), bet_min
            )
            if bet > bet_min:
                min_bet = bet
                highest_bet_index = ask_player
            ask_player = self._next_player_from(ask_player)

    def _starting_player(self) -> int:
        """
        Gets the player who has to put the big blind down
        """
        #todo have this rotate after each hand
        return 0

    def _next_player_from(self, start_from: int) -> int:
        """
        gets the next player(with rollover)
        """
        next_player = start_from+1
        if next_player >= len(self._active_players):
            next_player = 0
        return next_player

    def is_game_over(self) -> bool:
        """
        Check to see if the game is over
        """
        # is there only one player left?
        return len(self._active_players) == 1

    def global_state(self) -> np.array:
        """
        Gets all information and puts it in a dictionary for either
        a human player or an AI
        """
        return {
            "community_cards": self._community_cards
        }
                                 
