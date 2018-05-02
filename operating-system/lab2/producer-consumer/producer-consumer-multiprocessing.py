# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 18/04/2018 18:54
    @Name: producer-consumer-multiprocessings
    @Project: neu_curriculum
"""
import random
import multiprocessing
import time

import queue


buffer_queue = queue.Queue(maxsize=8)
count = 1
buffer_list = []
buffer_max = 8


def producer(name):
    global count
    global buffer_queue
    buffer_queue = queue.Queue(buffer_max)
    while True:
        buffer_queue.put(count)  # 将值放入队列中 默认block为True，无数据时调用线程暂停，否则抛出异常
        buffer_list.append(count)
        print("%s produces process %d\n" % (name, count))
        count += 1
        print(buffer_list)
        time.sleep(0.5)


def consumer(name):
    while True:
        count_con = buffer_queue.get()  # 从队列中取值 默认block为True，无数据时调用线程暂停，否则抛出异常
        print(buffer_list[0])
        buffer_list.pop(0)
        print("%s consumes process %d\n" % (name, count_con))
        time.sleep(2)


# pro = multiprocessing.Process(target=producer, args=("producer_program",))
# con = multiprocessing.Process(target=consumer, args=("consumer_program",))
# con2 = threading.Thread(target=consumer, args=("sx",))

def main():
    print("please input 'p'/'c' for producer process/consumer process")
    global count
    global buffer_queue
    while True:
        operation = input()
        # pro = multiprocessing.Process(target=producer, args=("producer_program",))
        # con = multiprocessing.Process(target=consumer, args=("consumer_program",))
        if operation == "p":
            print(count)
            pro = multiprocessing.Process(target=producer, args=("producer_program",))
            pro.start()
            time.sleep(random.randint(1, 3))
            pro.terminate()
            time.sleep(0.1)
            print("is process still running?:\n", pro.is_alive())

        elif operation == "c":
            con = multiprocessing.Process(target=consumer, args=("consumer_program",))
            con.start()
            time.sleep(random.randint(1, 3))
            con.terminate()
            time.sleep(10)

if __name__ == "__main__":
    main()


