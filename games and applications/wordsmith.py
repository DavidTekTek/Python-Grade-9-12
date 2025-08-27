import tkinter as tk
import random

# List of (word, hint) pairs
words_with_hints = [
    ("banana", "It's a fruit"),
    ("elephant", "It's a large animal"),
    ("guitar", "It's a musical instrument"),
    ("sunshine", "It's bright and comes from the sky"),
    ("turtle", "It's a slow-moving animal"),
    ("puzzle", "You solve it for fun"),
    ("rocket", "It goes to space"),
    ("island", "Land surrounded by water"),
    ("monkey", "An animal that swings from trees"),
    ("python", "A type of programming language and a snake")
]

# Choose a word and hint
chosen_word, word_hint = random.choice(words_with_hints)
hidden_word = ["_"] * len(chosen_word)
attempts = 10
guessed_letters = set()
hint_used = False

# === Functions ===

def guess_letter():
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter or len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Enter a single letter.")
        return

    if letter in guessed_letters:
        result_label.config(text="Already guessed!")
        return

    guessed_letters.add(letter)

    if letter in chosen_word:
        for idx, char in enumerate(chosen_word):
            if char == letter:
                hidden_word[idx] = letter
        word_label.config(text=" ".join(hidden_word))
        result_label.config(text="Nice guess!")
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts Left: {attempts}")
        result_label.config(text=f"'{letter}' is not in the word.")
        draw_hangman()

    if "_" not in hidden_word:
        result_label.config(text=f"You Win! The word was '{chosen_word}'")
        disable_game()
    elif attempts == 0:
        result_label.config(text=f"You Lost! It was '{chosen_word}'")
        disable_game()

def show_hint():
    global hint_used
    if not hint_used:
        hint_label.config(text=f"Hint: {word_hint}")
        hint_used = True
    else:
        hint_label.config(text="Hint already used.")

def disable_game():
    entry.config(state='disabled')
    guess_button.config(state='disabled')
    hint_button.config(state='disabled')

def restart_game():
    global chosen_word, word_hint, hidden_word, attempts, guessed_letters, hint_used
    chosen_word, word_hint = random.choice(words_with_hints)
    hidden_word = ["_"] * len(chosen_word)
    attempts = 10
    guessed_letters = set()
    hint_used = False

    word_label.config(text=" ".join(hidden_word))
    result_label.config(text="")
    attempts_label.config(text=f"Attempts Left: {attempts}")
    hint_label.config(text="")
    entry.config(state='normal')
    guess_button.config(state='normal')
    hint_button.config(state='normal')
    canvas.delete("all")
    draw_gallows()

# === GUI Setup ===

window = tk.Tk()
window.title("Wordsmith Game")
window.geometry("500x500")

title_label = tk.Label(window, text="Wordsmith Game!", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

word_label = tk.Label(window, text=" ".join(hidden_word), font=("Arial", 24))
word_label.pack(pady=5)

entry = tk.Entry(window, font=("Arial", 16), justify='center')
entry.pack()

guess_button = tk.Button(window, text="Guess Letter", command=guess_letter)
guess_button.pack(pady=5)

hint_button = tk.Button(window, text="Hint", command=show_hint)
hint_button.pack(pady=5)

attempts_label = tk.Label(window, text=f"Attempts Left: {attempts}", font=("Arial", 12))
attempts_label.pack()

hint_label = tk.Label(window, text="", font=("Arial", 12), fg="green")
hint_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

restart_button = tk.Button(window, text="Restart Game", command=restart_game)
restart_button.pack(pady=5)

# Canvas for Hangman drawing
canvas = tk.Canvas(window, width=200, height=250)
canvas.pack(pady=10)

def draw_gallows():
    canvas.create_line(20, 230, 180, 230)   # Base
    canvas.create_line(50, 230, 50, 30)     # Pole
    canvas.create_line(50, 30, 120, 30)     # Top beam
    canvas.create_line(120, 30, 120, 50)    # Rope

def draw_hangman():
    parts = [
        lambda: canvas.create_oval(100, 50, 140, 90),                 # Head
        lambda: canvas.create_line(120, 90, 120, 150),                # Body
        lambda: canvas.create_line(120, 100, 90, 130),                # Left arm
        lambda: canvas.create_line(120, 100, 150, 130),               # Right arm
        lambda: canvas.create_line(120, 150, 90, 190),                # Left leg
        lambda: canvas.create_line(120, 150, 150, 190),               # Right leg
        lambda: canvas.create_oval(110, 60, 116, 66)                  # Eye (last life)
    ]
    wrong_index = 6 - attempts
    if 0 <= wrong_index < len(parts):
        parts[wrong_index]()

# Start with gallows
draw_gallows()

window.mainloop()
