# === МОДУЛЬ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА ===
# Этот файл отвечает за отображение игры High/Low в окне GUI.
# Использует классы из game.py (Card, Deck, Game) для игровой логики.
# Вся логика игры остаётся в отдельном модуле, ввод/вывод через Tkinter

from PIL import Image, ImageTk
from game import Game
import tkinter as tk
import os

# создаём объект игры
game = Game()
game.start()

# создаём окно
root = tk.Tk()
root.title("High / Low Card Game")


# Возвращает PhotoImage карты для Tkinter card - объект Card width/height - размер в пикселях
def get_card_image(card, width=200, height=285):
    path = os.path.join("images/cards", f"{card.rank.lower()}_of_{card.suit.lower()}.png")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл карты не найден: {path}")

    img = Image.open(path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


# Изначально загружаем изображение первой карты
current_card_image = get_card_image(game.current_card)
card_label = tk.Label(root, image=current_card_image)
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
    global current_card_image  # нужно, чтобы Tkinter не удалял изображение
    # Обновляем изображение карты
    current_card_image = get_card_image(next_card)
    card_label.config(image=current_card_image)

    # Обновляем счёт
    score_label.config(text=f"Очки: {game.score}")

    # Проверка конца игры
    if len(game.deck) == 0:
        card_label.config(text="Карты закончились!", image="")
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")
    elif game.score <= 0:
        card_label.config(text="Очки закончились!", image="")
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")


# Кнопки
higher_button = tk.Button(root, text="Выше", command=guess_higher, width=10)
higher_button.pack(side="left", padx=20, pady=20)

lower_button = tk.Button(root, text="Ниже", command=guess_lower, width=10)
lower_button.pack(side="right", padx=20, pady=20)

root.mainloop()

