"""File with methods for encryption"""


def caesor_cipher(text: str, step: int) -> str:
    encrypt = ""

    for letter in text:
        if letter.isupper():
            encrypt += chr((ord(letter) + step - 65) % 26 + 65)
        elif letter.islower():
            encrypt += chr((ord(letter) + step - 97) % 26 + 97)
        elif letter.isdigit():
            encrypt += str((int(letter) + step) % 10)
        else:
            encrypt += letter
    return encrypt
