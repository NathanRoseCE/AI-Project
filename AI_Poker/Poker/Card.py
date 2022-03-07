from __future__ import annotations
"""
Defines all card related items
"""
from enum import Enum, IntEnum


class CardValue(IntEnum):
    """
    The face value on the card, Ace is High(the one true way)
    """
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
    

class CardSuit(Enum):
    """
    handler for the different suits
    """
    Spade=1
    Club=2
    Diamond=3
    Heart=4

class Card:
    """
    A simple card
    """
    def __init__(self, suit: CardSuit, value: CardValue) -> None:
        assert isinstance(suit, CardSuit)
        assert isinstance(value, CardValue)
        self._suit = suit
        self._value = value

    @property
    def suit(self) -> CardSuit:
        """
        Gets the cards suit
        """
        return self._suit

    @property
    def value(self) -> CardValue:
        """
        gets the card's value
        """
        return self._value

    def __eq__(self, o: Card) -> None:
        if not isinstance(o, Card):
            return False
        return ( (o.suit == self.suit) and
                 (o.value == self.value))
    
    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
    
    def __hash__(self):
      return hash((self.value, self.suit))
