import random

QUESTIONS = {
    1: [
        ("What color is the sky on a clear day?", "blue"),
        ("2 + 2 = ?", "4"),
    ],
    2: [
        ("Which planet is known as the Red Planet?", "mars"),
        ("5 * 6 = ?", "30"),
    ],
    3: [
        ("What gas do plants breathe in?", "carbon dioxide"),
        ("12 * 8 = ?", "96"),
    ],
}

def ask_question(level):
    question, answer = random.choice(QUESTIONS[level])
    user_answer = input(question + " ").strip().lower()
    return user_answer == answer

def play_quiz():
    level = 1
    score = 0

    print("Welcome to the Adaptive Quiz!")
    print("Answer correctly to get harder questions.")
    print("Type 'quit' at any time to stop.\n")

    while True:
        correct = ask_question(level)

        if correct:
            score += 1
            level = min(3, level + 1)
            print("Correct! Level up.\n")
        else:
            level = max(1, level - 1)
            print("Wrong. Let's try an easier one.\n")

        print("Current level:", level, "| Score:", score)

        cont = input("Press Enter to continue, or type 'quit' to stop: ").strip().lower()
        if cont == "quit":
            break

    print("\nQuiz finished.")
    print("Final score:", score)

def main():
    play_quiz()

if __name__ == "__main__":
    main()
