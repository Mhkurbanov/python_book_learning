from typing import List

from core.card import Card


class Hand:
    """Рука игрока или дилера"""

    def __init__(self):
        self._cards: List[Card] = []

    @property
    def cards(self) -> List[Card]:
        """Возвращает копию списка карт"""
        return self._cards.copy()

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def get_value(self) -> int:
        """
        Возвращает наилучшее значение руки,
        учитывая, что туз может быть 1 или 11
        """
        total = sum(card.value for card in self._cards)
        aces = sum(1 for card in self._cards if card.rank.name == "ACE")

        while total > 21 and aces:
            total -= 10  # превращаем туз из 11 в 1
            aces -= 1

        return total

    def is_blackjack(self) -> bool:
        return len(self._cards) == 2 and self.get_value() == 21

    def is_bust(self) -> bool:
        return self.get_value() > 21

    def clear(self) -> None:
        self._cards.clear()

    def __len__(self) -> int:
        return len(self._cards)

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self._cards)
