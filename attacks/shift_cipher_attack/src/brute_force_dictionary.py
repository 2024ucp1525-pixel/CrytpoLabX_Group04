import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import decrypt


def load_dictionary(filename):
    words = set()

    with open(filename, "r") as file:
        for line in file:
            word = line.strip().lower()
            if word:
                words.add(word)

    return words


def brute_force(ciphertext):
    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        results.append((key, plaintext))

    return results


def dictionary_score(text, dictionary):
    words = text.lower().split()
    score = 0

    for word in words:
        clean_word = ''.join(c for c in word if c.isalpha())

        if clean_word in dictionary:
            score += 1

    return score


def dictionary_attack(ciphertext, dictionary):
    best_key = 0
    best_text = ""
    best_score = -1

    for key, plaintext in brute_force(ciphertext):
        score = dictionary_score(plaintext, dictionary)

        if score > best_score:
            best_score = score
            best_key = key
            best_text = plaintext

    return best_key, best_text, best_score


if __name__ == "__main__":

    dictionary_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "dictionary",
        "english_words.txt"
    )

    dictionary = load_dictionary(dictionary_path)

    ciphertext = input("Enter ciphertext: ")

    print("\n--- BRUTE FORCE RESULTS ---")

    for key, plaintext in brute_force(ciphertext):
        score = dictionary_score(plaintext, dictionary)
        print(f"Key {key:2}: {plaintext} | Score: {score}")

    key, plaintext, score = dictionary_attack(ciphertext, dictionary)

    print("\n--- DICTIONARY ATTACK ---")
    print("Predicted Key :", key)
    print("Plaintext     :", plaintext)
    print("Dictionary Score:", score)

