# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/16 19:35
    @Name: lru
    @Project: neu_curriculum
"""
import rand_page

series_size = 20
random_size = 7


def lru(access_series):
    memory_list = []
    memory_max = 3
    missing_count = 0
    # flag = 0

    print("LRU algorithms:\n")
    for x in access_series:
        if x not in memory_list:
            missing_count += 1
            flag = 1
            if len(memory_list) < memory_max:
                memory_list.append(x)
            else:
                memory_list.pop(0)
                memory_list.extend([x])
        else:
            flag = 0
            memory_list.remove(x)
            memory_list.append(x)
        print(x, ' ', memory_list, "MISSING " if flag else "NOT MISSING")

    missing_rate = missing_count / len(access_series)
    print('lru missing rate is: \n', missing_rate)


# def main():
    # access_series = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    # access_series = rand_page.random_list(0, random_size, series_size)
    # lru(access_series)
