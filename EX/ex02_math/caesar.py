"""Caesar cipher."""


import string
alphabet = string.ascii_lowercase


def encode(message: str, shift: int) -> str:
    caesar_cipher = ""
    for char in message:
        if char in alphabet:
            code = alphabet.index(char)
            shifted_code = ((code + shift) % 26)
            encoded_message = (alphabet[shifted_code])
            caesar_cipher += encoded_message
        else:
            caesar_cipher += char
    return caesar_cipher
