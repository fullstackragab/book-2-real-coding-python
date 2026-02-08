def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def main():
    print("Simple Notes App")
    print("1. View notes")
    print("2. Add a note")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        notes = read_notes()
        if notes:
            print("\nYour notes:")
            for n in notes:
                print("-", n.strip())
        else:
            print("\nNo notes yet.")

    elif choice == "2":
        note = input("Write your note: ")
        save_note(note)
        print("Note saved.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
