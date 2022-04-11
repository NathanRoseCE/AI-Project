from AI_Poker.Poker.Card import Card, CardValue, CardSuit
from AI_Poker.Poker.HandValue import HandValue
import pytest

def test_high_card() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Diamond, CardValue.Eight)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Five), 
                        Card(CardSuit.Heart, CardValue.Seven), 
                        Card(CardSuit.Diamond, CardValue.King),
                        Card(CardSuit.Heart, CardValue.Four)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 1

def test_pair() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Diamond, CardValue.Eight)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Ten), 
                        Card(CardSuit.Heart, CardValue.Three), 
                        Card(CardSuit.Diamond, CardValue.King),
                        Card(CardSuit.Heart, CardValue.Seven)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 2

def test_two_pair() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Diamond, CardValue.Eight)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Ten), 
                        Card(CardSuit.Heart, CardValue.Three), 
                        Card(CardSuit.Diamond, CardValue.King),
                        Card(CardSuit.Heart, CardValue.Eight)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 3

def test_trips() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Diamond, CardValue.Eight)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Ten), 
                        Card(CardSuit.Heart, CardValue.Three), 
                        Card(CardSuit.Diamond, CardValue.Three),
                        Card(CardSuit.Heart, CardValue.King)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 4

def test_straight() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Diamond, CardValue.Five)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Ten), 
                        Card(CardSuit.Heart, CardValue.Six), 
                        Card(CardSuit.Diamond, CardValue.King),
                        Card(CardSuit.Heart, CardValue.Four)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 5

def test_flush() -> None:
    hand = [    Card(CardSuit.Club, CardValue.Three), 
                Card(CardSuit.Club, CardValue.Five)
            ]
    community_cards = [ Card(CardSuit.Spade, CardValue.Two), 
                        Card(CardSuit.Club, CardValue.Ten), 
                        Card(CardSuit.Heart, CardValue.Six), 
                        Card(CardSuit.Club, CardValue.King),
                        Card(CardSuit.Club, CardValue.Four)
                    ]
    cards = hand + community_cards
    scorer = HandValue()
    handValue = scorer.valueHand(cards)
    assert handValue == 6