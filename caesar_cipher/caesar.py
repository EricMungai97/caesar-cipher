import nltk
import ssl
import re
from nltk.corpus import words, names

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download('names', quiet=True)

words_list = words.words()
names_list = names.words()


def encrypt(plaintext, key):
    string = ""
    for char in plaintext:
        '''
         ord(char)
        changes
        letter -> number
        chr(num)
        changes
        number -> letter
        
        
        A - 65 
        Z - 90
        a - 97
        z - 122
        '''

        if char.isupper():
            # if int_character btwn 97-122
            string += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            # if int_character btwn 65-90
            string += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            string += str(char)
    return string


def decrypt(plaintext, shift):
    return encrypt(plaintext, -shift)


def crack(plaintext):
    possibilities = ''
    max_percent = 50

    for shift in range(1, 26):
        encrypted_words = decrypt(plaintext, shift)
        split_word_list = encrypted_words.split()
        count = 0
        for word in split_word_list:
            clean_word = re.sub(r"[^a-zA-Z]+", "", word).lower()

            if (clean_word in words_list) or (clean_word in names_list):
                count += 1
        percent = int(count / len(split_word_list) * 100)

        if percent > max_percent:
            most_probable_key = shift
            max_percent = percent
            possibilities = encrypted_words
            print(f"Decryption Probability: {max_percent}%")
            print(f"Most Probable Key: {most_probable_key}")
            print(possibilities)

    return possibilities


if __name__ == "__main__":
    real_sentence = "It was the best of times, it was the worst of times."
    encrypted = encrypt(real_sentence, 10)

    results = crack(encrypted)
