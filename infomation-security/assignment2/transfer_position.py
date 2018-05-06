# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/6 23:27
    @Name: transfer_position
    @Project: neu_curriculum
"""


def encrypt(plaintext, t):
    result = []
    length = len(t)
    temp = [plaintext[i:i + length] for i in range(0, len(plaintext), length)]

    for item in temp[:-1]:
        newitem = ''
    for i in t:
        newitem = newitem + item[i - 1]
        result.append(newitem)
    return ''.join(result) + temp[-1]


p = input("Please input your plaintext:")

c = encrypt(p, (1, 4, 3, 2))
print(c)
