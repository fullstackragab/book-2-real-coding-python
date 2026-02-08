def load_history():
    history = {"action": 0, "relax": 0}
    try:
        with open("history.txt", "r") as file:
            for line in file:
                choice = line.strip()
                if choice in history:
                    history[choice] += 1
    except FileNotFoundError:
        pass
    return history

def save_choice(choice):
    with open("history.txt", "a") as file:
        file.write(choice + "\n")

def ask_preference():
    choice = input("Do you prefer 'action' or 'relax' today? ").strip().lower()
    return choice

def recommend_based_on_history(history, today_choice):
    # Simple logic: combine today's choice with past behavior
    if history["action"] > history["relax"]:
        tendency = "action"
    else:
        tendency = "relax"

    if today_choice == tendency:
        return f"You often choose '{tendency}'. Here's something {tendency} for you."
    else:
        return f"Today you chose '{today_choice}'. Let's recommend something {today_choice}."

def main():
    history = load_history()
    print("Your past choices:", history)

    today_choice = ask_preference()
    save_choice(today_choice)

    recommendation = recommend_based_on_history(history, today_choice)
    print(recommendation)

if __name__ == "__main__":
    main()
