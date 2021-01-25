def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for l in range(len(plaintext)):
        keyword = keyword.upper()
        pos = l % len(keyword)
        shift = ord(keyword[pos]) - ord("A")
        if "a" <= plaintext[l] <= "z" or "A" <= plaintext[l] <= "Z":
            if plaintext[l].isupper() and chr(ord(plaintext[l]) + shift) > "Z":
                ciphertext += chr(ord(plaintext[l]) - 26 + shift)
            elif "a" <= plaintext[l] <= "z" < chr(ord(plaintext[l]) + shift):
                ciphertext += chr(ord(plaintext[l]) - 26 + shift)
            else:
                ciphertext += chr(ord(plaintext[l]) + shift)
        else:
            ciphertext += plaintext[l]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for l in range(len(ciphertext)):
        keyword = keyword.upper()
        pos = l % len(keyword)
        shift = ord(keyword[pos]) - ord("A")
        if "a" <= ciphertext[l] <= "z" or "A" <= ciphertext[l] <= "Z":
            if ciphertext[l].isupper() and chr(ord(ciphertext[l]) - shift) < "A":
                plaintext += chr(ord(ciphertext[l]) + 26 - shift)
            elif chr(ord(ciphertext[l]) - shift) < "a" <= ciphertext[l] <= "z":
                plaintext += chr(ord(ciphertext[l]) + 26 - shift)
            else:
                plaintext += chr(ord(ciphertext[l]) - shift)
        else:
            plaintext += ciphertext[l]
    return plaintext
