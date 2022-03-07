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
    
def test_shoe_two_decks():
    # there should be 52  cards with two copies of each
    shoe = Shoe(num_decks=2)
    cards = {}
    i = 0
    try:
        while True:
            next_card = shoe.next_card()
            if next_card in cards:
                assert not cards[next_card]
                cards[next_card] = True
            else:
                cards[next_card] = False
            i +=1
    except ValueError:
        pass
    assert len(cards) == 52
    for key, val in cards.items():
        assert val
    
