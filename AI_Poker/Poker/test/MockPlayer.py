from typing import Iterable
from AI_Poker.Poker.Player import Player

class MockPlayer(Player):
    """
    This is a mock player that will follow pre-programmed commands
    """
    def __init__(self, name: str, money: float, commands = Iterable[dict]) -> None:
        """
        command_options:
        {
          "command": "pass"
        } - results in a bet of 0
        {
          "command": "fold"
        } - results in a fold(NOT IMPLIMENTED)
        {
          "command": "bet",
          "bet": $BET_AMMOUNT
        } - results in a bet of $BET_AMMOUNT, $BET_AMMOUNT should be float castable
        """
        super().__init__(name, money)
        self._commands = commands
        self._current_command = 0
        self.last_global_state = {}

    def decision(self, global_state: dict) -> float:
        """
        makes the decisions as passed by command
        """
        self.last_global_state = global_state
        bet_minimum = global_state["bet_min"]
        bet = 0
        if self._current_command >= len(self._commands):
            raise ValueError(f"Not enough commands listed for MockPlayer, num={len(self._commands)}")
        if self._commands[self._current_command]["command"] == "pass":
            pass
        elif self._commands[self._current_command]["command"] == "fold":
            raise NotImplimentedError()
        elif self._commands[self._current_command]["command"] == "bet":
            bet = self._commands[self._current_command]["bet"]
        self._current_command += 1
        return bet

    
class MinPlayer(Player):
    """
    A player that always bets the minimum, useful for testing
    """
    def __init__(self, name: str, money: float) -> None:
        super().__init__(name, money)

    def decision(self, global_state: dict) -> float:
        return global_state["bet_min"]
