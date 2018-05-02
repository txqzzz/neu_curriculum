# encoding: utf-8

import os
import time

write_path = "/tmp/pipe.in"
read_path = "/tmp/pipe.out"

count = 1

wf = os.open(write_path, os.O_SYNC | os.O_CREAT | os.O_RDWR)
rf = None

times = 10
buffer_size = 1024
for i in range(times):
    msg = "msg " + str(i)
    msg2 = "msg2 " + str(i)
    os.write(wf, msg)
    os.write(wf, msg2)
    print("sent message:\n%s" % msg)
    print("sent message:\n%s" % msg2)

    if rf is None:
        rf = os.open(read_path, os.O_RDONLY)

    s = os.read(rf, buffer_size)
    if len(s) == 0:
        break
    print("received message:\n%s" % s)

    time.sleep(1)

os.write(wf, "exit")

os.close(rf)
os.close(wf)

#
