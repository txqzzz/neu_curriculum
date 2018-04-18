# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 18/04/2018 21:59
    @Name: producer-consumer-list.py
    @Project: neu_curriculum
"""

"""
      buffer
      | | | |

p              c
-----------------------------------
p:
if buffer is not full , just append, count+1
if buffer is full , add p_count

c:
if buffer is not empty, just pop
if buffer is empty, 
                  |====> if p_count > 0, p_count - 1 and pop buffer[0] buffer[0] = count
                         if p_count = 0, add c_count

"""


def main():
    print("please input 'p'/'c'/'e' for producer process/consumer process/exit")
    count = 1
    buffer_list = []
    buffer_max = 8
    p_count = 0
    c_count = 0
    index = 1
    while (True):
        operation = input()
        if operation == "p":
            if len(buffer_list) < buffer_max:
                buffer_list.append(count)
                count += 1
            else:
                p_count += 1
            print("buffer_list: %r\nindex:%s\ncount:%s\np_count:%s\nc_count:%s\n" % (
                buffer_list, index, count, p_count, c_count))

        elif operation == "c":
            if len(buffer_list) > 0:
                if len(buffer_list) <= 8 and p_count > 0:
                    p_count -= 1
                    # print(buffer_list[index - 1])
                    buffer_list[index - 1] = count
                    # print(buffer_list[index - 1])
                    index = (index + 1) % buffer_max
                    count += 1
                else:
                    print("now consuming product %s\n   " % buffer_list[0])
                    buffer_list.pop(0)
                    index = (index - 1) % buffer_max
            else:
                if p_count > 0:
                    p_count -= 1
                    index = (index + 1) % buffer_max
                    print("consuming product %s" % buffer_list[index - 1])
                    buffer_list.pop(0)
                    buffer_list = count
                    count += 1
                if p_count == 0:
                    c_count += 1
            print("buffer_list: %r\nindex:%s\ncount:%s\np_count:%s\nc_count:%s\n" % (
                buffer_list, index, count, p_count, c_count))

        elif operation == "e":
            exit()


if __name__ == "__main__":
    main()
