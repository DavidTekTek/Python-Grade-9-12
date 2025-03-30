import random

lower_bound = 1
upper_bound = 5
max_attempts = 12
secret_number = random.randint(lower_bound, upper_bound)






def get_guess():
    while True:
        guess = int(input("Guess a number between 1 and 5: "))
        if lower_bound <= guess <= upper_bound:
            return guess
        else:
            print("Invalid input. Please enter a number within the specified range.")




def check_guess(guess, secret_number):
    if guess == secret_number:
      return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"



def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")
    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")



if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")