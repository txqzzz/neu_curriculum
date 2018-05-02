# coding: utf-8
import os
import sys

path = "/tmp/write_in.pipe"

try:
    os.mkfifo(path)
except OSError:
    print("Failed to create pipe.\n")
else:
    fifo = open(path, "w")

print("New pipe is created successfully!\n")
