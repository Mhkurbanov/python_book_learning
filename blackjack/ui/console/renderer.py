from core.player import Player


class ConsoleRenderer:
    """Отвечает только за вывод в консоль"""

    # Словарь для перевода результата на русский
    RESULT_RU = {
        "PLAYER_WIN": "🎉 Вы выиграли!",
        "DEALER_WIN": "😞 Вы проиграли!",
        "PUSH": "🤝 Ничья!"
    }

    @staticmethod
    def show_player_hand(player: Player) -> None:
        """Показывает карты игрока"""
        print(f"\n🧑 {player.name}:")
        print(f"  Карты: {player.hand}")
        print(f"  Очки: {player.hand.get_value()}")

    @staticmethod
    def show_dealer_hand(dealer: Player, hide_first_card: bool = True) -> None:
        """Показывает карты дилера, можно скрыть первую карту"""
        print("\n🤵 Дилер:")
        cards = dealer.hand.cards

        if hide_first_card and cards:
            print("  Карты: 🂠, " + ", ".join(str(card) for card in cards[1:]))
            print("  Очки: ?")
        else:
            print(f"  Карты: {dealer.hand}")
            print(f"  Очки: {dealer.hand.get_value()}")

    @staticmethod
    def show_result(result) -> None:
        """Вывод результата раунда по-русски"""
        print("\n🏁 Результат раунда:")
        # Получаем текст из словаря, если нет — оставляем оригинал
        text = ConsoleRenderer.RESULT_RU.get(result.name, result.name)
        print(f"  {text}")
