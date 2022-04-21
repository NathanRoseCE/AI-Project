import pytest
from AI_Poker.Poker.Card import Card, CardSuit, CardValue
from AI_Poker.Poker.AIPlayer import AIPlayer
import numpy as np

def test_to_numpy():
    player = AIPlayer("ai", 10000)
    result = player.to_numpy({
        "bet_min": 1,
        "big_blind": 2,
        "little_blind": 3,
        "pot": 4,
        "community_cards": [
            Card(
                CardSuit.Spade,
                CardValue.Four
            ),
            Card(
                CardSuit.Club,
                CardValue.Five
            ),
            Card(
                CardSuit.Heart,
                CardValue.Seven
            ),
            Card(
                CardSuit.Diamond,
                CardValue.Ten
            ),
            Card(
                CardSuit.Spade,
                CardValue.King
            )
        ],
        "players": [
            {
                "folded": False,
                "bet": 123
            },
            {
                "folded": True,
                "bet": 1234
            },
            {
                "folded": False,
                "bet": 5432
            },
            {
                "folded": True,
                "bet": 2345
            },
            {
                "folded": False,
                "bet": 443
            },
        ]
    })
    correct = np.array([
        1,2,3,4,
        1,4, 2,5, 4,7, 3,10, 1,13, 
        0,123, 1,1234, 0,5432, 1,2345, 0,443, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 5
    ])

    assert np.any(result == correct)
