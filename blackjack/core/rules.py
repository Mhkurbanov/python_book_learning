from enum import Enum, auto

from core.hand import Hand


class RoundResult(Enum):
    """Результат раунда"""
    PLAYER_WIN = auto()
    DEALER_WIN = auto()
    PUSH = auto()  # ничья


class BlackjackRules:
    """Правила определения победителя в блэкджеке"""

    MAX_POINTS = 21

    @staticmethod
    def determine_winner(player_hand: Hand, dealer_hand: Hand) -> RoundResult:
        """
        Определяет победителя раунда по рукам игрока и дилера
        """
        # Перебор
        if player_hand.is_bust():
            return RoundResult.DEALER_WIN

        if dealer_hand.is_bust():
            return RoundResult.PLAYER_WIN

        # Blackjack
        if player_hand.is_blackjack() and not dealer_hand.is_blackjack():
            return RoundResult.PLAYER_WIN

        if dealer_hand.is_blackjack() and not player_hand.is_blackjack():
            return RoundResult.DEALER_WIN

        # Сравнение очков
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        if player_value > dealer_value:
            return RoundResult.PLAYER_WIN
        elif dealer_value > player_value:
            return RoundResult.DEALER_WIN
        else:
            return RoundResult.PUSH
