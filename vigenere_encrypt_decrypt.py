'''

filename: vigenere_encrypt_decrypt V 1.1.0

New feature added: Better commit messages
This program encrypts and decrypts a string in accordance to the Vigenère encryption and decryption

'''

# Create dictionary for conversion from text to num and num to text

TEXT_KEYS = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 
               'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 
               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 
               'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

NUM_KEYS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 
               6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 
               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 
               16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 
               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def encrypt(text, key):
    resultant_num = []

    text = text.lower()
    key = key.lower()

    # Take the numerical counterparts of both TEXT and KEY.
    
    numberified_text = convert_to_num(text)
    numberified_keys = convert_to_num(key)

def convert_to_num(text):
    text_to_num = []

    for letter in text:

        if letter.isalpha():
            text_to_num.append(TEXT_KEYS[letter])

        else:
            text_to_num.append(letter)

    return text_to_num