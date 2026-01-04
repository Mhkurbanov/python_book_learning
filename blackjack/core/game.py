from core.deck import Deck
from core.player import HumanPlayer, Dealer
from core.rules import BlackjackRules, RoundResult
from core.enums import GameState, PlayerAction


class BlackjackGame:
    """Управление игровым процессом блэкджека"""

    def __init__(self, player_name: str):
        self.deck = Deck()
        self.player = HumanPlayer(player_name)
        self.dealer = Dealer()
        self.state = GameState.INIT
        self.result: RoundResult | None = None

    def start_round(self) -> None:
        """Начинает новый раунд"""
        self.state = GameState.INIT
        self.result = None

        self.player.reset_hand()
        self.dealer.reset_hand()

        self.deck = Deck()

        # начальная раздача
        for _ in range(2):
            self.player.take_card(self.deck.draw_card())
            self.dealer.take_card(self.deck.draw_card())

        self.state = GameState.PLAYER_TURN

    def player_action(self, action: PlayerAction) -> None:
        """Обрабатывает действие игрока"""
        if self.state != GameState.PLAYER_TURN:
            return

        if action == PlayerAction.HIT:
            self.player.take_card(self.deck.draw_card())
            if self.player.hand.is_bust():
                self.state = GameState.FINISHED

        elif action == PlayerAction.STAND:
            self.state = GameState.DEALER_TURN

    def dealer_turn(self) -> None:
        """Ход дилера по правилам"""
        if self.state != GameState.DEALER_TURN:
            return

        while self.dealer.make_decision() == PlayerAction.HIT:
            self.dealer.take_card(self.deck.draw_card())

        self.state = GameState.FINISHED

    def finish_round(self) -> None:
        """Определяет результат раунда"""
        if self.state != GameState.FINISHED:
            return

        self.result = BlackjackRules.determine_winner(
            self.player.hand,
            self.dealer.hand
        )
