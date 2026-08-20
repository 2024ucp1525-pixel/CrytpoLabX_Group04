# shift_cipher.py

def encrypt(text, key):
    """
    Encrypt text using Shift (Caesar) Cipher.

    key: integer from 0 to 25
    """

    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        else:
            # Keep spaces, numbers and punctuation unchanged
            result += char

    return result


def decrypt(text, key):
    """
    Decrypt text using Shift (Caesar) Cipher.
    """

    return encrypt(text, -key)


# Test the cipher
if __name__ == "__main__":

    plaintext = "HELLO WORLD"
    key = 3

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("Plaintext :", plaintext)
    print("Key       :", key)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", decrypted)
