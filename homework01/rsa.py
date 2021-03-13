import random
import typing as tp


def is_prime(n: int) -> bool:
    for a in range(2, n):
        if n % a == 0:
            return False
    if n != 1:
        return True
    else:
        return False


def gcd(a: int, b: int) -> int:
    if b != 0:
        while a % b != 0:
            a, b = b, a % b
        return b
    else:
        return a


def multiplicative_inverse(e: int, phi: int) -> int:
    phi1 = phi
    line = -1
    matrix = []
    while phi % e != 0:
        matrix.append([phi, e, phi % e, phi // e])
        c = phi % e
        phi = e
        e = c
        line += 1
    x = 0
    y = 1
    while line >= 0:
        c = x - y * matrix[line][3]
        x = y
        y = c
        line -= 1
    d = y % phi1
    return d


def generate_keypair(a: int, b: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(a) and is_prime(b)):
        raise ValueError("Both numbers must be prime.")
    elif a == b:
        raise ValueError("p and q cannot be equal")
    n = a * b
    phi = (a - 1) * (b - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
