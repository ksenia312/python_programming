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
    
    ciphertext=list(plaintext)
    keyword=list(keyword)
    
    for i in range(len(keyword)):
        keyword[i]=ord(keyword[i])
       
        if 65 <= keyword[i] <= 90:
            keyword[i]-=65
        elif 97 <= keyword[i] <= 122:
            keyword[i]-=97
    for i in range(len(ciphertext)):
        ciphertext[i]=ord(ciphertext[i])
        k=keyword[i%len(keyword)]
       
        if 65 <= ciphertext[i] <= (90-k) or 97 <= ciphertext[i] <= (122-k):
            ciphertext[i]=ciphertext[i]+k
            
        elif (90-k+1) <= ciphertext[i] <= 90 or (122-k+1) <= ciphertext[i] <= 122:
            ciphertext[i]=ciphertext[i]-(26-k)      
        ciphertext[i]=chr(ciphertext[i])
    ciphertext=''.join(ciphertext)
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
    
    
    plaintext=list(ciphertext)
    keyword=list(keyword)
    
    for i in range(len(keyword)):
        keyword[i]=ord(keyword[i])
       
        if 65 <= keyword[i] <= 90:
            keyword[i]-=65
        elif 97 <= keyword[i] <= 122:
            keyword[i]-=97
    for i in range(len(plaintext)):
        plaintext[i]=ord(plaintext[i])
        k=keyword[i%len(keyword)]
        if (65+k) <= plaintext[i] <= 90 or (97+k) <= plaintext[i] <= 122:
            plaintext[i]=plaintext[i]-k
            
        elif 65 <= plaintext[i] <= (65+k-1) or 97 <= plaintext[i] <= (97+k-1):
            plaintext[i]=plaintext[i]+26-k
        plaintext[i]=chr(plaintext[i])
    plaintext=''.join(plaintext)
    return plaintext
