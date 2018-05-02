# encoding: utf-8

import os
import time

read_path = "/tmp/pipe.in"
write_path = "/tmp/pipe.out"

# new path every time
if os.path.exists(read_path):
    os.remove(read_path)
if os.path.exists(write_path):
    os.remove(write_path)

os.mkfifo(write_path)
os.mkfifo(read_path)

# try:
#     os.mkfifo(write_path)
#     os.mkfifo(read_path)
# except OSError as e:
#     print("mkfifo error:", e)
# else:
#     print("You have already a new pipe..\n")

rf = os.open(read_path, os.O_RDONLY)
wf = os.open(write_path, os.O_SYNC | os.O_CREAT | os.O_RDWR)

buffer_size = 1024
while True:
    message = os.read(rf, buffer_size)
    print(message)
    if len(message) == 0:
        time.sleep(1)
        continue

    if "exit" in message:
        break

    os.write(wf, message)

os.close(wf)
os.close(rf)
