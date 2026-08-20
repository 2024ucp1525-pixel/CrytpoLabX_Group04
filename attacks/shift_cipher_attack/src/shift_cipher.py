def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


if __name__ == "__main__":
    text = "HELLO WORLD"
    key = 3

    cipher = encrypt(text, key)
    plain = decrypt(cipher, key)

    print("Plaintext :", text)
    print("Key       :", key)
    print("Ciphertext:", cipher)
    print("Decrypted :", plain)
