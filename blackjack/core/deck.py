import random
from typing import List

from core.card import Card
from core.enums import Suit, Rank


class Deck:
    """Колода игральных карт"""

    def __init__(self, shuffle: bool = True):
        self._cards: List[Card] = self._create_full_deck()
        if shuffle:
            self.shuffle()

    @staticmethod
    def _create_full_deck() -> List[Card]:
        """Создаёт стандартную колоду из 52 карт"""
        return [
            Card(suit, rank)
            for suit in Suit
            for rank in Rank
        ]

    def shuffle(self) -> None:
        """Перемешивает колоду"""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Берёт одну карту из колоды"""
        if not self._cards:
            raise RuntimeError("Колода пуста")
        return self._cards.pop()

    def cards_left(self) -> int:
        return len(self._cards)

    def __len__(self) -> int:
        return len(self._cards)
