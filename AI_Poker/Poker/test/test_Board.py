from copy import deepcopy
from AI_Poker.Poker.Deck import Deck
from AI_Poker.Poker.Board import Board, Player, RuleScoring

def test_deal_cards() -> None:
    players = [
        Player(
            start_money=10000
        ),
        Player(
            start_money=10000
        ),
        Player(
            start_money=10000
        )
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
        deck=deck
    )
    cards = deepcopy(deck._active_cards)
    board._deal_cards()
    assert cards[0] in players[0].hand 
    assert cards[1] in players[1].hand 
    assert cards[2] in players[2].hand 
    assert cards[3] in players[0].hand 
    assert cards[4] in players[1].hand 
    assert cards[5] in players[2].hand 
