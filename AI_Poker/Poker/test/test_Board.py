import pytest
import functools
from copy import deepcopy
from AI_Poker.Poker.Deck import Deck
from AI_Poker.Poker.Board import Board, RuleScorer
from AI_Poker.Poker.Card import Card, CardValue, CardSuit
from .MockPlayer import MockPlayer, MinPlayer


def test_deal_cards() -> None:
    players = [
        MinPlayer(
            name="test", money=10000
        ),
        MinPlayer(
            name="test", money=10000
        ),
        MinPlayer(
            name="test", money=10000
        )
    ]
    deck = Deck()
    board = Board(
        players=players,        
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
    
    assert cards[7] in board._community_cards
    assert cards[8] in board._community_cards
    assert cards[9] in board._community_cards
    assert cards[10] in board._community_cards
    assert cards[11] in board._community_cards

def test_starting_player() -> None:
    player_one = MinPlayer(
        name="test", money=10000
    )
    player_two = MinPlayer(
        name="test", money=10000
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    assert board.starting_player == 0
    board.hand()
    assert board.starting_player == 1
    board.hand()
    assert board.starting_player == 2
    board.hand()
    assert board.starting_player == 0
    board.hand()

    

def test_big_blind() -> None:
    player_one = MinPlayer(
        name="test", money=10000
    )
    player_two = MinPlayer(
        name="test", money=10000
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    assert board.global_state["big_blind"] == 0
    board.hand()
    assert board.global_state["big_blind"] == 1
    board.hand()
    assert board.global_state["big_blind"] == 2
    board.hand()
    assert board.global_state["big_blind"] == 0
    board.hand()

    

def test_little_blind() -> None:
    player_one = MinPlayer(
        name="test", money=10000
    )
    player_two = MinPlayer(
        name="test", money=10000
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    assert board.global_state["little_blind"] == 1
    board.hand()
    assert board.global_state["little_blind"] == 2
    board.hand()
    assert board.global_state["little_blind"] == 0
    board.hand()
    assert board.global_state["little_blind"] == 1
    board.hand()

def test_big_blind_default() -> None:
    player_one = MinPlayer(
        name="test", money=10000
    )
    player_two = MinPlayer(
        name="test", money=10000
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )
    assert board.big_blind_ammount == 30
    

def test_little_blind_default() -> None:
    player_one = MinPlayer(
        name="test", money=10000
    )
    player_two = MinPlayer(
        name="test", money=10000
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )
    assert board.little_blind_ammount == 20

def test_ask_player_for_big_blind_bet_min() -> None:
    """
    tests on the ask_player_for_bid function
    """
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 30
            }
        ]   
    )
    players = [
        player_one
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.big_blind == 0
    assert board.big_blind_ammount == 30

    #test
    bet, new_global = board.ask_player_for_bid(0, 0)
    assert bet == 30
    assert new_global == 0
    
    
def test_ask_player_for_big_blind_bet_above() -> None:
    """
    tests on the ask_player_for_bid function
    """
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 40
            }
        ]   
    )
    players = [
        player_one
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.big_blind == 0
    assert board.big_blind_ammount == 30

    #test
    bet, new_global = board.ask_player_for_bid(0, 0)
    assert bet == 40
    assert new_global == 40


def test_ask_player_for_little_blind_bet_min() -> None:
    """
    tests on the ask_player_for_bid function
    """
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 20
            }
        ]   
    )
    players = [
        player_one,
        player_two
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.little_blind == 1
    assert board.little_blind_ammount == 20

    #test
    bet, new_global = board.ask_player_for_bid(1, 0)
    assert bet == 20
    assert new_global == 0
    
def test_ask_player_for_little_blind_bet_above() -> None:
    """
    tests on the ask_player_for_bid function
    """
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 40
            }
        ]   
    )
    players = [
        player_one,
        player_two
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.little_blind == 1
    assert board.little_blind_ammount == 20

    #test
    bet, new_global = board.ask_player_for_bid(1, 0)
    assert bet == 40
    assert new_global == 40

def test_non_blind_player_pass():
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MinPlayer(
        name="test", money=10000,
    )
    player_three = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "pass"
            }
        ]   
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.little_blind != 2
    assert board.big_blind != 2

    #test
    bet, new_global = board.ask_player_for_bid(2, 0)
    assert bet == 0
    assert new_global == 0

def test_non_blind_player_underbid():
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MinPlayer(
        name="test", money=10000,
    )
    player_three = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "fold"
            }
        ]   
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.little_blind != 2
    assert board.big_blind != 2

    #test
    success = True
    try:
        board._ask_for_bets(0)
        success = False
    except AssertionError:
        pass
    print([player for player in board.global_state["players"]])
    assert len([player for player in board.global_state["players"] if player["folded"]]) == 1

def test_zero_bet_min_non_blind():
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MinPlayer(
        name="test", money=10000,
    )
    player_three = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "pass"
            }
        ]   
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.little_blind != 2
    assert board.big_blind != 2

    #test
    bet, new_global = board.ask_player_for_bid(2, 0)
    assert bet == 0
    assert new_global == 0

def test_player_public_info() -> None:
    """
    checks to make sure the players public bet is correct
    """
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 50
            },
            {
                "command": "bet",
                "bet": 100
            }
        ],
    )
    player_two = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 100
            }
        ]   
    )

    players = [
        player_one,
        player_two
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )

    #assumption for the test
    assert board.big_blind == 0

    #test
    board.round()
    print(player_one.last_global_state)
    assert player_one.last_global_state["players"][1] == {
        "bet": 100,
        "folded": False
    }
    assert player_one.last_global_state["players"][0] == {
        "bet": 50,
        "folded": False
    }

    
def test_board_public_cards_after_initial_deal():
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[],
    )
    players = [
        player_one
    ]
    deck = Deck()
    board = Board(
        players=players,
        deck=deck
    )
    board._deal_cards()
    # after dealing cards, no public community cards
    assert len(board.global_state["community_cards"]) == 0
    
def test_board_public_cards_round_one():
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 50
            },
            {
                "command": "bet",
                "bet": 50
            }
        ],
    )
    players = [
        player_one
    ]
    deck = Deck()
    # two cards to player[0:2]
    # one card burnt [2:3]
    public_cards = [
        deck._active_cards[3],
        deck._active_cards[4],
        deck._active_cards[5],
        deck._active_cards[6],
        deck._active_cards[7],
    ]
    board = Board(
        players=players,
        deck=deck
    )
    board._deal_cards()
    board.round()
    assert len(board.global_state["community_cards"]) == 3
    assert public_cards[0] in board.global_state["community_cards"]
    assert public_cards[1] in board.global_state["community_cards"]
    assert public_cards[2] in board.global_state["community_cards"]
    
def test_board_public_cards_round_two():
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 50
            },
            {
                "command": "bet",
                "bet": 50
            }
        ],
    )
    players = [
        player_one
    ]
    deck = Deck()
    # two cards to player[0:2]
    # one card burnt [2:3]
    public_cards = [
        deck._active_cards[3],
        deck._active_cards[4],
        deck._active_cards[5],
        deck._active_cards[6],
        deck._active_cards[7],
    ]
    board = Board(
        players=players,
        deck=deck
    )
    board._deal_cards()
    board.round()
    board.round()
    assert len(board.global_state["community_cards"]) == 4
    assert public_cards[0] in board.global_state["community_cards"]
    assert public_cards[1] in board.global_state["community_cards"]
    assert public_cards[2] in board.global_state["community_cards"]
    assert public_cards[3] in board.global_state["community_cards"]
    
def test_board_public_cards_round_two():
    player_one = MockPlayer(
        name="test", money=10000,
        commands=[
            {
                "command": "bet",
                "bet": 50
            },
            {
                "command": "bet",
                "bet": 50
            },
            {
                "command": "bet",
                "bet": 50
            }
        ],
    )
    players = [
        player_one
    ]
    deck = Deck()
    # two cards to player[0:2]
    # one card burnt [2:3]
    public_cards = [
        deck._active_cards[3],
        deck._active_cards[4],
        deck._active_cards[5],
        deck._active_cards[6],
        deck._active_cards[7],
    ]
    board = Board(
        players=players,
        deck=deck
    )
    board._deal_cards()
    board.round()
    board.round()
    board.round()
    assert len(board.global_state["community_cards"]) == 5
    assert public_cards[0] in board.global_state["community_cards"]
    assert public_cards[1] in board.global_state["community_cards"]
    assert public_cards[2] in board.global_state["community_cards"]
    assert public_cards[3] in board.global_state["community_cards"]
    assert public_cards[4] in board.global_state["community_cards"]
    
def test_rule_scorer():
    community_cards = [
        Card(CardSuit.Spade, CardValue.Two), 
        Card(CardSuit.Club, CardValue.Five), 
        Card(CardSuit.Heart, CardValue.Six), 
        Card(CardSuit.Diamond, CardValue.King), 
        Card(CardSuit.Diamond, CardValue.Queen), 
    ]
    player_one = MinPlayer(name="test", money=0)
    player_one.setCard(
        Card(CardSuit.Spade, CardValue.Ace), 
    )
    player_one.setCard(
        Card(CardSuit.Heart, CardValue.King), 
    )
    player_two = MinPlayer(name="test", money=0)
    player_two.setCard(
        Card(CardSuit.Spade, CardValue.Three), 
    )
    player_two.setCard(
        Card(CardSuit.Spade, CardValue.Four), 
    )
    player_three = MinPlayer(name="test", money=0)
    player_three.setCard(
        Card(CardSuit.Spade, CardValue.Jack), 
    )
    player_three.setCard(
        Card(CardSuit.Heart, CardValue.Ten), 
    )
    scorer = RuleScorer()
    winner = scorer.score(
        community_cards,
        [player_one, player_two, player_three]
    )
    assert winner == 1 #player_two
    
def test_simple_hand():
    """
    just a simple can we get thorugh a simple hand?
    """
    player_one = MinPlayer(
        name="test", money=10000,
    )
    player_two = MinPlayer(
        name="test", money=10000,
    )
    player_three = MinPlayer(
        name="test", money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,        
        deck=deck
    )
    board.hand()
    
    # no money has vanished or appeared
    assert functools.reduce(lambda a, b: a+b, [player.money for player in players]) == 30000

    # assert that money has changed hands
    assert False in [10000 == player.money for player in players]
    
