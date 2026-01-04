from core.enums import Suit, Rank


class Card:
    """Одна игральная карта"""

    __slots__ = ("_suit", "_rank")

    def __init__(self, suit: Suit, rank: Rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self) -> Suit:
        return self._suit

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def value(self) -> int:
        """Базовое значение карты (туз = 11, корректируется в Hand)"""
        return self._rank.value

    def __str__(self) -> str:
        return f"{self._rank.name.title()} {self._suit.value}"

    def __repr__(self) -> str:
        return f"Card({self._rank.name}, {self._suit.name})"
