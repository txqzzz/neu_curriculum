# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 04/04/2018 11:39
    @Name: state_transition_demo
    @Project: neu_curriculum
"""


class ProcessState:
    def changeState(self, context):
        context.changeState(self)

    def getStateName(self):
        return self.StateName


class RunningState(ProcessState):
    __instance = None

    def __init__(self):
        __instance = self
        self.StateName = 'RUNNING'

    def instance(self):
        if (RunningState.__instance == None):
            RunningState.__instance = RunningState()
        return RunningState.__instance

    def eventWait(self, context):
        print('In Runing.eventWait() do some context switching')
        ProcessState.changeState(BlockedState().instance(), context)

    def timeout(self, context):
        print('In Running.timeout() do some context switching')
        ProcessState.changeState(ReadyState().instance(), context)


class BlockedState(ProcessState):
    __instance = None

    def __init__(self):
        __instance = self
        self.StateName = 'BLOCKED'

    def instance(self):
        if (BlockedState.__instance == None):
            BlockedState.__instance = BlockedState()
        return BlockedState.__instance

    def eventOccur(self, context):
        print('In BlockedState.eventOccur() do some context switching')

        ProcessState.changeState(ReadyState().instance(), context)


class ReadyState(ProcessState):
    __instance = None

    def __init__(self):
        __instance = None
        self.StateName = 'READY'

    def instance(self):
        if (ReadyState.__instance == None):
            ReadyState.__instance = ReadyState()
        return ReadyState.__instance

    def dispatch(self, context):
        print('In ReadyState.dispatch() do some context switching')
        ProcessState.changeState(RunningState().instance(), context)


class ProcessContext:
    def __init__(self):
        self._state = ReadyState().instance()

    def changeState(self, state):
        self._state = state

    def eventWait(self):
        self._state.eventWait(self)

    def timeout(self):
        self._state.timeout(self)

    def eventOccur(self):
        self._state.eventOccur(self)

    def dispatch(self):
        self._state.dispatch(self)

    def prtStateName(self):
        print('now the state of process is ', self._state.getStateName())
    
    def prtInitializationMenu(self):
        print("==============================================================\n")
        print("The 3-state model version 1.0 is now initializing...\n")
        print("It will initial several processes and their PCB information...\n")
        print("Initializing...\n")
        print("==============================================================\n")
        print("Done...\n")
        print("Choose different operations with corresponding number now...\n")
        print("* 1 New a process.\n")
        print("* 2 Dispatch.\n")
        print("* 3 Event Wait.\n")
        print("* 4 Event Occur.\n")
        print("* 5 Timeout.\n")
        print("* 6 PrintProcessStates.\n")

class Client:
    def initialize(self):
        ctx = ProcessContext()
        ctx.prtInitializationMenu()
    def test(self):
        ctx = ProcessContext()
        ctx.prtStateName()
        ctx.dispatch()
        ctx.prtStateName()
        ctx.eventWait()
        ctx.prtStateName()
        ctx.eventOccur()
        ctx.prtStateName()
        ctx.dispatch()
        ctx.prtStateName()
        ctx.timeout()
        ctx.prtStateName()

class PCB:
    def __init__(self):
        self.process_state = "READY"
        self.process_name = ""
        self.process_id = 0




def new_process():
    global PID
    a = PCB()
    a.process_id = PID+1
    a.process_name = input("please input your process name.")
    a.process_state = input("Please input your process state('READY'/'BLOCKED'/'RUNNING'")

    if a.process_state == "READY":
        readyQueue.append(a.process_name)
    elif a.process_state == "BLOCKED":
        blockedQueue.append(a.process_name)
    elif a.process_state == "RUNNING":
        runningQueue.append(a.process_name)

if __name__ == "__main__":
    readyQueue, runningQueue, blockedQueue = [], [], []
    global PID
    PID = 0
    client = Client()
    client.initialize()
    init_process_amount = int(input("Please input your initialized processes amount.."))
    for _ in range(init_process_amount):
        a = PCB()
        a.process_id = _
        a.process_name = input("please input your process name.")
        a.process_state = input("Please input your process state('READY'/'BLOCKED'/'RUNNING'")

        PID = a.process_id

        if a.process_state == "READY":
            readyQueue.append(a.process_name)
        elif a.process_state == "BLOCKED":
            blockedQueue.append(a.process_name)
        elif a.process_state == "RUNNING":
            runningQueue.append(a.process_name)

    print("===================Process Status======================================\n")
    print("|     QueueName  |     QueueList    \n")
    print("|     ReadyQ               " + str(readyQueue)+"\n")
    print("|     RunningQ             " + str(runningQueue) + "\n")
    print("|     BlockedQ             " + str(blockedQueue) + "\n")
    # client.test()
    while True:
        operation_choice = input("Please choose your operations now....")
        print("==================Process Operation====================================\n")
        print("* 1 New a process.\n")
        print("* 2 Dispatch.\n")
        print("* 3 Event Wait.\n")
        print("* 4 Event Occur.\n")
        print("* 5 Timeout.\n")
        print("* 6 PrintProcessStates.\n")

        if operation_choice == "1":
            new_process()
        elif operation_choice == "2":
            if not runningQueue:
                runningQueue.append(readyQueue.pop())
            elif runningQueue:
                raise Exception
        elif operation_choice == "3":
            if not runningQueue:
                blockedQueue.append(runningQueue.pop())
            elif runningQueue:
                raise Exception
        elif operation_choice == "4":
            readyQueue.append(blockedQueue.pop())
        elif operation_choice == "5":
            if not runningQueue:
                readyQueue.append(runningQueue.pop())
                runningQueue.append((readyQueue.pop()))
            elif runningQueue:
                raise Exception
        elif operation_choice == "6":
            print("===================Process Status======================================\n")
            print("|     QueueName  |     QueueList    \n")
            print("|     ReadyQ               " + str(readyQueue) + "\n")
            print("|     RunningQ             " + str(runningQueue) + "\n")
            print("|     BlockedQ             " + str(blockedQueue) + "\n")




    print("===================Process Status======================================\n")
    print("|     QueueName  |     QueueList    \n")
    print("|     ReadyQ               " + str(readyQueue) + "\n")
    print("|     RunningQ             " + str(runningQueue) + "\n")
    print("|     BlockedQ             " + str(blockedQueue) + "\n")

    # remember that '3' and '5' operations need filling empty running queue


