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
    
    assert cards[6] in board.global_state["community_cards"]
    assert cards[7] in board.global_state["community_cards"]
    assert cards[8] in board.global_state["community_cards"]
    assert cards[9] in board.global_state["community_cards"]
    assert cards[10] in board.global_state["community_cards"]

def test_starting_player() -> None:
    player_one = Player(
        start_money=10000
    )
    player_two = Player(
        start_money=10000
    )
    player_three = Player(
        start_money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
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
    player_one = Player(
        start_money=10000
    )
    player_two = Player(
        start_money=10000
    )
    player_three = Player(
        start_money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
        deck=deck
    )

    assert board.big_blind == 0
    board.hand()
    assert board.big_blind == 1
    board.hand()
    assert board.big_blind == 2
    board.hand()
    assert board.big_blind == 0
    board.hand()

    

def test_little_blind() -> None:
    player_one = Player(
        start_money=10000
    )
    player_two = Player(
        start_money=10000
    )
    player_three = Player(
        start_money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
        deck=deck
    )

    assert board.little_blind == 1
    board.hand()
    assert board.little_blind == 2
    board.hand()
    assert board.little_blind == 0
    board.hand()
    assert board.little_blind == 1
    board.hand()

def test_big_blind_default() -> None:
    player_one = Player(
        start_money=10000
    )
    player_two = Player(
        start_money=10000
    )
    player_three = Player(
        start_money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
        deck=deck
    )
    assert board.big_blind_ammount == 30
    

def test_little_blind_default() -> None:
    player_one = Player(
        start_money=10000
    )
    player_two = Player(
        start_money=10000
    )
    player_three = Player(
        start_money=10000
    )
    players = [
        player_one,
        player_two,
        player_three
    ]
    deck = Deck()
    board = Board(
        players=players,
        scoring_rules=[],
        deck=deck
    )
    assert board.little_blind_ammount == 20
