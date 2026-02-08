import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        guess_text = input("Enter your guess: ")

        if not guess_text.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print("Correct! You guessed the number in", attempts, "attempts.")
            break

def main():
    play_game()

if __name__ == "__main__":
    main()
