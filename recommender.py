def load_items():
    items = []
    with open("items.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                item, category = parts
                items.append((item, category))
    return items

def ask_preferences():
    print("What do you prefer today?")
    preference = input("Type 'action' or 'relax': ").strip().lower()
    return preference

def recommend(items, preference):
    scores = {}

    for item, category in items:
        score = 0
        if category == preference:
            score += 2
        else:
            score += 1

        scores[item] = scores.get(item, 0) + score

    best_item = max(scores, key=scores.get)
    return best_item

def main():
    items = load_items()
    preference = ask_preferences()
    result = recommend(items, preference)

    print("\nRecommendation for you:", result)

if __name__ == "__main__":
    main()
