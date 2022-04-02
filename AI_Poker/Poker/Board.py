from typing import Iterable, Tuple
from AI_Poker.Poker.Card import Card
from AI_Poker.Poker.Deck import Deck
from AI_Poker.Poker.Player import Player
import numpy as np
import logging


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

class PlayerWrapper:
    """
    This class is a simple wrapper to handle the player and 
    grab some extra meta data about the player
    """
    def __init__(self, player: Player) -> None:
        self._player = player
        self._bet_ammount = 0

    @property
    def public_info(self) -> dict:
        """
        Gets the public information about the player
        """
        return {
            "bet": self._bet_ammount
        }

    def decision(self, *args, **dargs):
        """
        returns the bet the player would like to make
        """
        self._bet_ammount = self._player.decision(*args, **dargs)
        return self._bet_ammount

    def close_hand(self, money_won: float=0) -> None:
        """
        closes the hand, using the money won as a increase in the bet ammount
        """
        self._player.money += money_won
        self._bet_ammount = 0

    @property
    def hand(self) -> Iterable[Card]:
        """
        gets the hand from the player object
        """
        return self._player.hand

    @hand.setter
    def hand(self, hand: Iterable[Card]) -> None:
        """
        sets the hand for the player object
        """
        self._player.hand = hand

    


class Board:
    """
    This is the main class that tracks all of the information and runs a game
    """
    MAX_PLAYERS=5
    def __init__(self,
                 players: Iterable[Player],
                 scoring_rules: Iterable[RuleScoring],
                 deck: Deck,
                 big_blind_ammount=30,
                 little_blind_ammount=20
                 ) -> None:
        if len(players) > Board.MAX_PLAYERS:
            raise ValueError(f"Cant play with more than {Board.MAX_PLAYERS}")
        self._active_players = [
            PlayerWrapper(player) for player in players
        ]
        self._rules = scoring_rules
        self._deck = deck
        self._community_cards = []
        self._starting_player = 0
        self._big_blind_ammount = big_blind_ammount
        self._little_blind_ammount = little_blind_ammount
        self._round = 0

    def hand(self) -> None:
        """
        plays one hand of poker, assume the deck is set up correctly
        """
        self._round = 0
        self._deal_cards()
        self._end_hand()

    def round(self) -> None:
        """
        Handles one betting round within a hand
        """
        self._ask_for_bets(self.big_blind)
        self._round += 1

    def _deal_cards(self) -> None:
        """
        deals the cards to the players
        """
        logging.info(f"dealing cards to {len(self._active_players)} players")
        hands = []
        # TODO start with small blind
        # TODO do a rotate little_blind positions then iterate through it twice
        # to start dealing with little blind
        for _ in range(len(self._active_players)):
            hands.append([self._deck.next_card()])
        for i, _ in enumerate(range(len(self._active_players))):
            hands[i].append(self._deck.next_card())
            
        for i, player in enumerate(self._active_players):
            player.hand = hands[i]

        #TODO create hidden cards
        #burn a card
        self._deck.next_card()
        self._community_cards = []
        for _ in range(5):
            self._community_cards.append(self._deck.next_card())
    
    def _ask_for_bets(self, starting_player: int) -> None:
        """
        Ask all of the players for thier bets
        """
        ask_player = starting_player
        bet_min = 0
        highest_bet_index=-1
        while True:
            if highest_bet_index == ask_player:
                break
            bet, new_bet_min = self.ask_player_for_bid(ask_player, bet_min)
            if new_bet_min > bet_min:
                bet_min = new_bet_min
                highest_bet_index = ask_player
            ask_player = self._next_player_from(ask_player)

    @property
    def starting_player(self) -> int:
        """
        Gets the player who has to put the big blind down
        """
        #todo have this rotate after each hand
        return self._starting_player

    def _next_player_from(self, start_from: int) -> int:
        """
        gets the next player(with rollover)
        """
        next_player = start_from+1
        if next_player >= len(self._active_players):
            next_player = 0
        return next_player

    def _end_hand(self) -> None:
        """
        This function is used for any logic that is used at the end of a hand
        """
        self._starting_player = self._next_player_from(self.starting_player)
        

    def is_game_over(self) -> bool:
        """
        Check to see if the game is over
        """
        # is there only one player left?
        return len(self._active_players) == 1

    @property
    def global_state(self) -> dict:
        """
        Gets all information and puts it in a dictionary for either
        a human player or an AI
        """
        return {
            "community_cards": self._global_state_community_cards,
            "big_blind": self.big_blind,
            "little_blind": self.little_blind,
            "players": [
                player.public_info for player in self._active_players
            ]
        }

    @property
    def _global_state_community_cards(self) -> Iterable[Card]:
        if self._round == 0:
            return []
        elif self._round == 1:
            return self._community_cards[0:3]
        elif self._round == 2:
            return self._community_cards[0:4]
        elif self._round == 3:
            return self._community_cards[0:5]
        else:
            raise LogicError("Poker does not have 5 rounds of betting")

    @property
    def big_blind(self) -> int:
        """
        returns the index of the big blind for the current hand
        """
        return self.starting_player

    @property
    def little_blind(self) -> int:
        """
        returns the index of the little blind for the current hand
        """
        return self._next_player_from(self.starting_player)

    @property
    def big_blind_ammount(self) -> float:
        """
        Returns the big blind ammount for this hand
        """
        return self._big_blind_ammount
    
    @property
    def little_blind_ammount(self) -> float:
        """
        Returns the little blind ammount for this hand
        """
        return self._little_blind_ammount

    def ask_player_for_bid(self, player_index: int, global_min: float) -> Tuple[float, float]:
        """
        asks the player for thier bid(taking into account big and little blind), 
        returns bid_ammount, new_global_min
        """
        bet_min = global_min
        if player_index == self.big_blind:
            bet_min = self.big_blind_ammount if self.big_blind_ammount > bet_min else bet_min
        if player_index == self.little_blind:
            bet_min = self.little_blind_ammount if self.little_blind_ammount > bet_min else bet_min
            
        global_state = self.global_state
        global_state["bet_min"] = bet_min
        
        # todo allow for three attempts before assuming fold
        bet = self._active_players[player_index].decision(
            global_state
        )
        
        assert bet >= bet_min
        new_global_min = bet
        if (player_index == self.big_blind) and (bet == self.big_blind_ammount):
            new_global_min = global_min
        if (player_index == self.little_blind) and (bet == self.little_blind_ammount):
            new_global_min = global_min
        return bet, new_global_min
