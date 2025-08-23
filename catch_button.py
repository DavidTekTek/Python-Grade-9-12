import tkinter as tk
import random

# Global variables
score = 0
time_left = 30  # seconds

# Function to move the button
def move_button():
    if time_left > 0:
        x = random.randint(50, 300)
        y = random.randint(50, 300)
        button.place(x=x, y=y)

# Function when button is clicked
def button_clicked():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_button()

# Countdown timer
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}")
        window.after(1000, countdown)
    else:
        button.place_forget()
        timer_label.config(text="Time's up!")
        game_over_label = tk.Label(window, text="Game Over!", font=("Arial", 20), fg="red")
        game_over_label.pack(pady=20)

# Initialize the GUI window
window = tk.Tk()
window.title("Catch the Button!")
window.geometry("400x400")

# Labels
score_label = tk.Label(window, text="Score: 0", font=("Arial", 14))
score_label.pack()

timer_label = tk.Label(window, text=f"Time Left: {time_left}", font=("Arial", 14))
timer_label.pack()

# The button to catch
button = tk.Button(window, text="Catch me!", font=("Arial", 12), command=button_clicked)
button.place(x=150, y=150)

# Start countdown
window.after(1000, countdown)

# Start the GUI event loop
window.mainloop()