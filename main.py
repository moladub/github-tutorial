# Original Segun Adebayo's game script
import random

def play_game(): Segun Adebayo's first Effort
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    Efforts = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 100): "))
        Efforts += 1

        if guess < secret_number:
            print("Try higher!")
        elif guess > secret_number:
            print("Try lower!")
        else:
            print(f"Congratulations! You guessed the number in {Efforts} Efforts.")
            break

if __name__ == "__main__":
    play_game()
