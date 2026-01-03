# === МОДУЛЬ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА ===
# Этот файл отвечает за отображение игры High/Low в окне GUI.
# Использует классы из game.py (Card, Deck, Game) для игровой логики.
# Вся логика игры остаётся в отдельном модуле, ввод/вывод через Tkinter

import tkinter as tk
from game import Game

# создаём объект игры
game = Game()
game.start()

# создаём окно
root = tk.Tk()
root.title("High / Low Card Game")

# Лейблы для карты и счёта в окне
card_label = tk.Label(root, text=f"Текущая карта: {game.current_card}", font=("Arial", 16))
card_label.pack(pady=10)

score_label = tk.Label(root, text=f"Очки: {game.score}", font=("Arial", 14))
score_label.pack(pady=10)

# Функции для кнопок
def guess_higher():
    is_correct, next_card = game.guess(True)
    update_ui(next_card)

def guess_lower():
    is_correct, next_card = game.guess(False)
    update_ui(next_card)

def update_ui(next_card):
    card_label.config(text=f"Следующая карта: {next_card}")
    score_label.config(text=f"Очки: {game.score}")

    if len(game.deck) == 0:
        card_label.config(text="Карты закончились!")
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")

    elif game.score <= 0:
        card_label.config(text="Очки закончились!")
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")

# Кнопки
higher_button = tk.Button(root, text="Выше", command=guess_higher, width=10)
higher_button.pack(side="left", padx=20, pady=20)

lower_button = tk.Button(root, text="Ниже", command=guess_lower, width=10)
lower_button.pack(side="right", padx=20, pady=20)

root.mainloop()
