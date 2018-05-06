# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 21/04/2018 18:11
    @Name: double_rail_encryption
    @Project: neu_curriculum
"""
import re


def decryption(plaintext):
    odd_list = []
    even_list = []
    for i in range(len(plaintext)):
        if i % 2 == 0:
            odd_list.append(plaintext[i])
        else:
            even_list.append((plaintext[i]))
    ciphertext = "".join(odd_list) + " "+"".join(even_list)
    print("Ciphertext is:" + ciphertext)


if __name__ == "__main__":
    plaintext = input("please input your plaintext:\n")
    processed_plaintext = re.sub('\s', '', plaintext)
    decryption(processed_plaintext)
