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
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghigklmnopqrstuvwxyz"
    s = list(plaintext)
    le = (len(plaintext) // len(keyword)) + 1 
    keyword = keyword.upper() * le
    num = -1
    for i in s:
        num += 1
        if i in letters:
            ind = letters.index(i)
            shift = LETTERS.find(keyword[num]) 
            x = ind + shift
            if x >= len(letters):
                x = x % 26
            ciphertext = ciphertext + letters[x]
        elif i in LETTERS:
            ind = LETTERS.index(i)
            shift = LETTERS.find(keyword[num]) 
            x = ind + shift
            if x >= len(LETTERS):
                x = x % 26
            ciphertext = ciphertext + LETTERS[x]
        else:
            ciphertext = ciphertext + i 
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
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghigklmnopqrstuvwxyz"
    s = list(ciphertext)
    le = (len(ciphertext) // len(keyword)) + 1 
    keyword = keyword.upper() * le
    num = -1
    for i in s:
        num += 1
        if i in letters:
            ind = letters.index(i)
            shift = LETTERS.find(keyword[num]) 
            x = ind - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext + letters[x]
        elif i in LETTERS:
            ind = LETTERS.index(i)
            shift = LETTERS.find(keyword[num]) 
            x = ind - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext + LETTERS[x]
        else:
            plaintext = plaintext + i 
    return plaintext
