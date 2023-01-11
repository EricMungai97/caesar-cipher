# LAB - Class 19

## Project: caesar-cipher

### Author: Eric Mungai Kinuthia

### About

This project includes three cryptography methods:

* encrypt() - takes plaintext and an integer key, and returns text encrypted with a Caesar Cipher shifted by the provided key.

* decrypt() - takes plaintext and an integer key, and decrypts Caesar Cipher-encrypted text.

* crack() - takes Caesar Cipher-encrypted text and uses a brute force technique to decode and return the decrypted text.

### How to initialize application

`python3.11 caesar_cipher/caesar.py`

### Tests

To run tests run `pytest tests/test_caesar.py`

Tests include:

1. Can encrypt plaintext with whitespaces

2. Can encrypt plaintext that is upper case to upper case

3. Can encrypt phrases with special characters

4. Returns empty string for a phrase that doesn't make sense

5. Can bruteforce an encrypted text



