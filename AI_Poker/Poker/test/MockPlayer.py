from typing import Iterable
from ..Board import Player

#TODO update this player to inherit from the true player interface
class MockPlayer(Player):
    """
    This is a mock player that will follow pre-programmed commands
    """
    def __init__(self, start_money: float, commands = Iterable[dict]) -> None:
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
        super().__init__(start_money)
        self._commands = commands
        self._current_command = 0

    def make_decision(self, bet_minimum: float, flobal_state: dict) -> float:
        """
        makes the decisions as passed by command
        """
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
