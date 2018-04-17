# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 04/04/2018 16:35
    @Name: 3_state_ver1.0
    @Project: neu_curriculum
"""

PID = 0


class ProcessState:
    def __init__(self):
        self.runningState = "RUNNING"
        self.blockedState = "BLOCKED"
        self.readyState = "READY"


"""
@this is the example usage of priority queue.
```
q = Q.PriorityQueue()
q.put((10 ,'process1'))
q.put((20,'process2'))
q.put((5,'process3'))

while not q.empty():
    prio, item = q.get()
    waitingQueue = item.split(' ')
    #res = waitingQueue.extend(waitingQueue)
    print(waitingQueue)
    input("test").strip()
"""

print("The 3-state model version 1.0 is now initializing...")
print("It will initial several processes and their PCB information...")
print("Initializing...")


class ProcessOperation:
    def __init__(self, processname, processid):
        self.PName = processname
        self.PID = processid

    def _op_newprocess(self):
        global PID
        print("PID starts from 0.")
        self.PID = PID+1
