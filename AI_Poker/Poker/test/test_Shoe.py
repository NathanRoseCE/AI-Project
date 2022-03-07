from AI_Poker.Poker.Card import Card, CardValue, CardSuit
from AI_Poker.Poker.Shoe import Shoe
import pytest

def test_shoe_one_deck():
    # there should be 52 unique cards
    shoe = Shoe(num_decks=1)
    cards = {}
    try:
        while True:
            next_card = shoe.next_card()
            assert not next_card in cards
            cards[next_card] = True
    except ValueError:
        pass
    assert len(cards) == 52
    
