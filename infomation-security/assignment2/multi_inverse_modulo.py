# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/6 23:00
    @Name: multi_inverse_modulo
    @Project: neu_curriculum
"""

def get_gcd(a, b):
    k = a // b
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        k = a // b
        remainder = a % b
    return b


def get_(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        remainder = a % b
        x1, y1 = get_(b, remainder)
        x, y = y1, x1 - k * y1
    return x, y


if __name__ == '__main__':
    print("Here you can calculate the multiplicative inverse modulo[m^-1 mod p]:")
    a = input("please input the a:")
    b = input("please input the b:")
    a, b = int(a), int(b)

    if b < 0:
        m = abs(b)
    else:
        m = b
    flag = get_gcd(a, b)

    if flag == 1:
        x, y = get_(a, b)
        x0 = x % m
        print("a^-1 mod b is:", x0)
    else:
        print("No inverse modulo fit.")

