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
    shift=shift%26
    ciphertext=list(plaintext)
    for i in range(len(ciphertext)):
        
        ciphertext[i]=ord(ciphertext[i])
        if 65 <= ciphertext[i] <= (90-shift) or 97 <= ciphertext[i] <= (122-shift):
            ciphertext[i]=ciphertext[i]+shift
            
        elif (90-shift+1) <= ciphertext[i] <= 90 or (122-shift+1) <= ciphertext[i] <= 122:
            ciphertext[i]=ciphertext[i]-(26-shift)
            
        ciphertext[i]=chr(ciphertext[i])
    ciphertext=''.join(ciphertext)
        
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
    shift=shift%26
    plaintext=list(ciphertext)
    for i in range(len(plaintext)):
        
        plaintext[i]=ord(plaintext[i])
        
        if (65+shift) <= plaintext[i] <= 90 or (97+shift) <= plaintext[i] <= 122:
            plaintext[i]=plaintext[i]-shift
            
        elif 65 <= plaintext[i] <= (65+shift-1) or 97 <= plaintext[i] <= (97+shift-1):
            plaintext[i]=plaintext[i]+26-shift
            
        plaintext[i]=chr(plaintext[i])
    plaintext=''.join(plaintext)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
