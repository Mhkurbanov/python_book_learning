from enum import Enum, auto


class Suit(Enum):
    """Масти игральных карт"""
    SPADES = "♠"
    HEARTS = "♥"
    CLUBS = "♣"
    DIAMONDS = "♦"


class Rank(Enum):
    """Ранги карт и их базовые значения в блэкджеке"""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11  # значение 1 или 11 будет решаться в Hand


class GameState(Enum):
    """Состояние игрового раунда"""
    INIT = auto()
    PLAYER_TURN = auto()
    DEALER_TURN = auto()
    FINISHED = auto()


class PlayerAction(Enum):
    """Действия, доступные игроку"""
    HIT = auto()
    STAND = auto()
