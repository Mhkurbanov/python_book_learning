from core.enums import PlayerAction


class ConsoleInputHandler:
    """Обработка пользовательского ввода"""

    @staticmethod
    def ask_player_action() -> PlayerAction:
        while True:
            choice = input("\nВаш ход: Брать >> [H] / [S] << Пас: ").strip().lower()

            if choice in ("h", "hit"):
                return PlayerAction.HIT
            if choice in ("s", "stand"):
                return PlayerAction.STAND

            print("❌ Некорректный ввод. Попробуйте снова.")
