import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghigklmnopqrstuvwxyz"
    s = list(plaintext)
    for i in s:
        if i in letters:
            n = letters.index(i)
            x = n + shift
            if x > len(letters):
                x = x % 26
            ciphertext = ciphertext + letters[x]
        elif i in LETTERS:
            n = LETTERS.index(i)
            x = n + shift
            if x > len(LETTERS):
                x = x % 26
            ciphertext = ciphertext + LETTERS[x]
        else:
            ciphertext = ciphertext + i 
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghigklmnopqrstuvwxyz"
    s = list(ciphertext)
    for i in s:
        if i in letters:
            n = letters.index(i)
            x = n - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext + letters[x]
        elif i in LETTERS:
            n = LETTERS.index(i)
            x = n - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext + LETTERS[x]
        else:
            plaintext = plaintext + i 
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
