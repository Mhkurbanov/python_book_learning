from core.game import BlackjackGame
from core.enums import GameState
from ui.console.renderer import ConsoleRenderer
from ui.console.input_handler import ConsoleInputHandler


def main():
    print("🃏 Добро пожаловать в Blackjack!")

    name = input("Введите имя игрока: ").strip() or "Player"
    game = BlackjackGame(name)
    renderer = ConsoleRenderer()
    input_handler = ConsoleInputHandler()

    while True:
        game.start_round()

        # игровой цикл
        while game.state != GameState.FINISHED:
            renderer.show_dealer_hand(game.dealer, hide_first_card=True)
            renderer.show_player_hand(game.player)

            if game.state == GameState.PLAYER_TURN:
                action = input_handler.ask_player_action()
                game.player_action(action)

            elif game.state == GameState.DEALER_TURN:
                game.dealer_turn()

        # финал раунда
        renderer.show_dealer_hand(game.dealer, hide_first_card=False)
        renderer.show_player_hand(game.player)
        game.finish_round()
        renderer.show_result(game.result)

        again = input("\n🔁 Сыграть ещё раз? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("👋 Спасибо за игру!")
            break


if __name__ == "__main__":
    main()
