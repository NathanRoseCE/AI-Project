from AI_Poker.Poker.Card import Card, CardValue, CardSuit
from itertools import permutations
from itertools import product
import numpy as np

class Deck:
    """
    impliments all the logic for a shoe(card handler) can handle any number of shoes
    """
    def __init__(self, shuffled:bool=True) -> None:
        shuffle=bool(shuffled)
        self._active_cards = []
        self._used_cards = []
        self._active_cards += [
            Card(suit, value) for value, suit in list(product(CardValue, CardSuit))
        ]
        if shuffle:
            self.shuffle()
                
    def shuffle(self, active_only:bool=False) -> None:
        """
        shuffles the deck
        if active_only is false, then all discarded cards are marked as active and shuffled too
        """
        if not active_only:
            self._active_cards += self._used_cards
            self._used_cards = []
        np.random.shuffle(self._active_cards)

    def next_card(self) -> Card:
        """
        Gets the next card, marking it as discarded
        """
        if len(self._active_cards) == 0:
            raise ValueError("The deck is empty, consider shuffling it")
        next_card = self._active_cards.pop(0)
        self._used_cards += [next_card]
        return next_card
