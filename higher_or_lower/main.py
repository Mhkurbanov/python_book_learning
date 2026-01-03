# === ТОЧКА ВХОДА В ПРОГРАММУ ===
# Отвечает за запуск игры и консольный интерфейс.
# Вся игровая логика находится в game.py.

from game import Game

def main():
    game = Game()
    game.start()
    print('Добро Пожаловать в High/Low Card Game!')
    print()
    print("Текущая карта:", game.current_card)

    while True:
        choice = input("Будет выше или ниже? (h/l, q — выход): ").lower()
        print()

        if choice == 'q':
            print("♻️ Выход из игры.")
            break
        if choice not in ('h', 'l'):
            print("⚠️ Введите 'h' или 'l'")
            continue

        is_correct, next_card = game.guess(choice == 'h')
        print("✅ Верно!" if is_correct else "❌ Неверно!")
        print("Текущий счёт:", game.score)
        print()
        print("Следующая карта:", next_card)
        print("-" * 30)

        if len(game.deck) == 0:
            print("♻️ Карты закончились!")
            break


if __name__ == "__main__":
    main()
