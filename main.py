import os
from datetime import datetime
def display_menu():
    print("\n" + "=" * 40)
    print("          Welcome to CryptoLabX")
    print("=" * 40)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")
    print("=" * 40)

def log_activity(option):
    os.makedirs("outputs", exist_ok=True)

    log_path = os.path.join("outputs", "log.txt")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{current_time} | {option}\n")

def encrypt():
    print("\n[Encrypt Module]")
    print("Coming Soon...")


def decrypt():
    print("\n[Decrypt Module]")
    print("Coming Soon...")


def attack():
    print("\n[Attack Module]")
    print("Coming Soon...")


def analyze():
    print("\n===== File Analysis =====")

    filename = input("Enter the filename (example: sample1.txt): ")

    filepath = os.path.join("datasets", filename)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        print("\nFile loaded successfully!")

        characters = len(text)
        words = len(text.split())
        lines = len(text.splitlines())
        unique_characters = len(set(text))

        print(f"Characters        : {characters}")
        print(f"Words             : {words}")
        print(f"Lines             : {lines}")
        print(f"Unique Characters : {unique_characters}")

        frequency = {}

        for letter in "abcdefghijklmnopqrstuvwxyz":
            frequency[letter] = 0

        for ch in text.lower():
            if ch.isalpha():
                frequency[ch] += 1

        print("\nLetter Frequency")
        print("-" * 20)

        for letter in frequency:
            print(f"{letter.upper()} : {frequency[letter]}")

    except FileNotFoundError:
        print("Error: File not found.")

def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            log_activity("Encrypt")
            encrypt()

        elif choice == "2":
            log_activity("Decrypt")
            decrypt()

        elif choice == "3":
            log_activity("Attack")
            attack()

        elif choice == "4":
            log_activity("Analyze")
            analyze()

        elif choice == "5":
            log_activity("Exit")
            print("\nThank you for using CryptoLabX.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()