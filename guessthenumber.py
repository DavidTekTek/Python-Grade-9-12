import tkinter as tk
import random

# Global variables
target_number = random.randint(1, 100)
attempts_left = 7
wins = 0

# Function to check the guess
def check_guess():
    global attempts_left, target_number, wins
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            result_label.config(text="Enter a number between 1 and 100")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return

    attempts_left -= 1
    attempts_label.config(text=f"Attempts Left: {attempts_left}")

    if guess < target_number:
        result_label.config(text="Too low! Try again.")
    elif guess > target_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Correct! 🎉 The number was {target_number}")
        wins += 1
        win_label.config(text=f"Wins: {wins}")
        disable_game()

    if attempts_left == 0 and guess != target_number:
        result_label.config(text=f"Out of attempts! The number was {target_number}")
        disable_game()

    entry.delete(0, tk.END)

def disable_game():
    entry.config(state='disabled')
    guess_button.config(state='disabled')

def reset_game():
    global target_number, attempts_left
    target_number = random.randint(1, 100)
    attempts_left = 7
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    result_label.config(text="Guess a number between 1 and 100")
    entry.config(state='normal')
    guess_button.config(state='normal')
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Guess the Number")
window.geometry("400x300")

title_label = tk.Label(window, text="Guess the Number!", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

instructions_label = tk.Label(window, text="I'm thinking of a number between 1 and 100...", font=("Arial", 12))
instructions_label.pack()

entry = tk.Entry(window, font=("Arial", 14), justify='center')
entry.pack(pady=10)

guess_button = tk.Button(window, text="Guess", font=("Arial", 12), command=check_guess)
guess_button.pack()

result_label = tk.Label(window, text="Start guessing!", font=("Arial", 12))
result_label.pack(pady=10)

attempts_label = tk.Label(window, text=f"Attempts Left: {attempts_left}", font=("Arial", 12))
attempts_label.pack()

win_label = tk.Label(window, text=f"Wins: {wins}", font=("Arial", 12))
win_label.pack()

reset_button = tk.Button(window, text="Restart Game", font=("Arial", 10), command=reset_game)
reset_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
