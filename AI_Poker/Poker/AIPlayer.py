from AI_Poker.Poker.Player import Player
from AI_Poker.Poker.Card import Card, CardSuit, CardValue
from typing import Iterable
import numpy as np
import itertools

class AIPlayer(Player):
    def __init__(self) -> None:
        pass

    def decision(self, global_state):
        pass

    def to_numpy(self, global_state: dict) -> np.array:
        bet_min = [global_state["bet_min"]]
        big_blind = [global_state["big_blind"]]
        little_blind = [global_state["little_blind"]]
        pot = [global_state["pot"]]
        card_values = self.community_cards_to_list(global_state["community_cards"])
        players = self.players_to_list(global_state["players"])
        return np.array([
            bet_min + big_blind + little_blind + pot + card_values + players
        ])
        

    def community_cards_to_list(self, cards: Iterable[Card]) -> Iterable[float]:
        if len(cards) == 0:
            return [0,0]*5
        if len(cards) == 3:
            return (
                self.handle_card(cards[0]) + 
                self.handle_card(cards[1]) + 
                self.handle_card(cards[2])
            ) + [0,0]*2
        if len(cards) == 4:
            return (
                self.handle_card(cards[0]) + 
                self.handle_card(cards[1]) + 
                self.handle_card(cards[2]) + 
                self.handle_card(cards[3])
            ) + [0,0]
        if len(cards) == 5:
            return (
                self.handle_card(cards[0]) + 
                self.handle_card(cards[1]) + 
                self.handle_card(cards[2]) + 
                self.handle_card(cards[3]) + 
                self.handle_card(cards[4])
            )
        raise ValueError("Dont know how to handle {len(cards)} cards")


    def handle_card(self, card: Card) -> None:
        return [int(card.suit), int(card.value)]

    def handle_player(self, player: dict) -> Iterable[float]:
        return [int(player["folded"]), int(player["bet"])]

    def players_to_list(self, players: Iterable[dict]) -> Iterable[float]:
        return list(itertools.chain.from_iterable([
            self.handle_player(player) for player in players
        ] + ( [0,0] * (len(players)-5) )))
