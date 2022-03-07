from AI_Poker.Poker.Card import Card, CardValue, CardSuit
import pytest

def test_card_init() -> None:
    jack_of_spades = Card(CardSuit.Spade, CardValue.Jack)
    assert jack_of_spades.value == CardValue.Jack
    assert jack_of_spades.suit == CardSuit.Spade

def test_jack_is_better_than_two() -> None:
    assert CardValue.Jack > CardValue.Two
    assert CardValue.Two < CardValue.Jack

def test_equality() -> None:
    jack_of_spades = Card(CardSuit.Spade, CardValue.Jack)
    jack_of_spades_two = Card(CardSuit.Spade, CardValue.Jack)
    three_of_clubs = Card(CardSuit.Club, CardValue.Three)
    assert jack_of_spades == jack_of_spades_two
    assert jack_of_spades != three_of_clubs
