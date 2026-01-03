# === МОДУЛЬ С ИГРОВОЙ ЛОГИКОЙ ===
# Здесь находятся все основные классы игры.
# Файл не содержит ввода/вывода и не зависит от интерфейса.
import random

class Card:
    """ Одна игральная карта """

    RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def value(self) -> int:
        """Числовое значение карты (Ace = 1)"""
        return Card.RANKS.index(self.rank) + 1

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    """ Колода игральных карт """
    def __init__(self):
        self._cards: list[Card] = []   # Это для IDE, Этот список должен содержать обьекты класса Card

    def populate(self) -> None:
        """Создаёт стандартную колоду из 52 карт"""
        self._cards.clear()
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        """Перемешивает колоду"""
        random.shuffle(self._cards)

    def draw(self) -> Card:
        """Берёт одну карту из колоды"""
        return self._cards.pop()

    def __len__(self) -> int:
        """Количество карт в колоде"""
        return len(self._cards)


class Game:
    """ Логика и правила игры """
    pass
