# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/16 18:52
    @Name: fifo
    @Project: neu_curriculum
"""
import rand_page

series_size = 20
random_size = 7


def fifo(buffer, access_s):
    lst = []
    count = 0
    # flag = 0

    print("FIFO algorithm:\n")
    for s in access_s:
        if s in lst[::2]:
            list_a = lst[::2]
            lst[list_a.index(s) * 2 + 1] += 1
            print(s, ' ', lst[::2])
            continue
        else:
            list_b = lst[1::2]

            if len(lst) < 2 * buffer:
                lst.append(s)
                lst.append(1)
            else:
                c = list_b.index(max(list_b))
                lst[2 * c] = s
                lst[2 * c + 1] = 1
            print(s, ' ', lst[::2], 'MISSING ')
            count += 1
    print("memory_size is : {}".format(buffer))
    print("fifo missing rate is:{:.2f}\n".format(count / len(access_s)))


# def main():
    # access_series = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    # access_series = rand_page.random_list(0, random_size, series_size