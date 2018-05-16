# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/16 18:57
    @Name: rand_page
    @Project: neu_curriculum
"""

import random

series_size = 10
random_size = 10


def rand_page_series():
    # print("Randomly generating access series now.")

    with open('data.txt', 'w') as f:
        for i in range(series_size):
            f.write(random.randint(0, random_size))
        f.close()


def random_list(start, stop, length):
    if length >= 0:
        length = int(length)

    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

