# Original Segun's game script
import random

def play_game(): Segun's first ATTEMPT
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 60)
    ATTEMPTs = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 60): "))
        ATTEMPTs += 1

        if guess < secret_number:
            print("Try higher!")
        elif guess > secret_number:
            print("Try lower!")
        else:
            print(f"Congratulations! You guessed the number in {ATTEMPTs} ATTEMPTs.")
            break

if__name__ == "__main__":
    play_game()
