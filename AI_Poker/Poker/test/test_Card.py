from AI_Poker.Poker.Card import Card, CardValue, CardSuit
import pytest

def test_card_init() -> None:
    jack_of_spades = Card(CardSuit.Spade, CardValue.Jack)
    assert jack_of_spades.value == CardValue.Jack
    assert jack_of_spades.suit == CardSuit.Spade

def test_jack_is_better_than_two() -> None:
    assert CardValue.Jack > CardValue.Two
    assert CardValue.Two < CardValue.Jack
