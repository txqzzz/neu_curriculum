import os

test_times = 20
for i in range(test_times):
    os.system("echo process 3 message %s > /tmp/pipe.in" % i)
    pass
