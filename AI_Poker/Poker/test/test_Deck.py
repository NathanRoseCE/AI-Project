from AI_Poker.Poker.Card import Card, CardValue, CardSuit
from AI_Poker.Poker.Deck import Deck
import pytest

def test_deck_one_deck():
    # there should be 52 unique cards
    deck = Deck()
    cards = {}
    try:
        while True:
            next_card = deck.next_card()
            assert not next_card in cards
            cards[next_card] = True
    except ValueError:
        pass
    assert len(cards) == 52
    
