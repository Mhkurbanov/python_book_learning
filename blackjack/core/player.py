from abc import ABC, abstractmethod

from core.hand import Hand
from core.enums import PlayerAction


class Player(ABC):
    """Базовый класс игрока"""

    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()

    def take_card(self, card) -> None:
        self.hand.add_card(card)

    def reset_hand(self) -> None:
        self.hand.clear()

    @abstractmethod
    def make_decision(self) -> PlayerAction:
        """
        Возвращает действие игрока:
        HIT или STAND
        """
        pass


class HumanPlayer(Player):
    """Игрок-человек (решение приходит извне — UI)"""

    def __init__(self, name: str):
        super().__init__(name)
        self._next_action: PlayerAction | None = None

    def set_action(self, action: PlayerAction) -> None:
        """Устанавливается UI"""
        self._next_action = action

    def make_decision(self) -> PlayerAction:
        if self._next_action is None:
            raise RuntimeError("Действие игрока не задано")
        action = self._next_action
        self._next_action = None
        return action


class Dealer(Player):
    """Дилер с фиксированными правилами"""

    def __init__(self):
        super().__init__(name="Dealer")

    def make_decision(self) -> PlayerAction:
        if self.hand.get_value() < 17:
            return PlayerAction.HIT
        return PlayerAction.STAND
