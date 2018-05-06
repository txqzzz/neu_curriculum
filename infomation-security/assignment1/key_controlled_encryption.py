# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 22/04/2018 03:21
    @Name: key_controlled_encryption
    @Project: neu_curriculum
"""

plaintext = None
key = None


def key_controlled(plaintext, len1, num):
    k = num - 1
    len_plaintext = len(plaintext)
    tem_s = []
    while (k < len_plaintext - 1) or (k == len_plaintext - 1):
        tem_s.append(plaintext[k])
        k = k + len1
    return "".join(tem_s)


if __name__ == '__main__':
    alphabet = [chr(i) for i in range(97, 123)]
    input_plaintext = input("please input the plaintext:")
    input_key = input("please input the key:")
    len_key = len(input_key)
    tem = 0
    for i in alphabet:
        # print i
        for k in input_key:
            tem = tem + 1
            if k == i:
                # print tem
                print(key_controlled(input_plaintext, len_key, tem) + '\n')
        tem = 0
