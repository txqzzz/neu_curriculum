# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/7 00:02
    @Name: vigenere
    @Project: neu_curriculum
"""


def vigenere_encrypt(plaintext, key):
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet = alphabet + alphabet
    plaintext_ord = ord(plaintext) - 97
    k = ord(key) - 97
    return alphabet[k + plaintext_ord]


if __name__ == '__main__':
    plaintext = "foryouandme"
    key = "xingqitang"
    ciphertext = []
    while len(key) < len(plaintext):
        key = key + key
    for i in range(len(plaintext)):
        ciphertext.append(vigenere_encrypt(plaintext[i], key[i]))
    print("The Ciphertext is:  " + "".join(ciphertext))

