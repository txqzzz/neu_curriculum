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

    def waitSth(self, context):
        print
        'In Runing.waitSth() do some context switching'
        ProcessState.changeState(BlockedState().instance(), context)

    def goReady(self, context):
        print
        'In Running.goReady() do some context switching'
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

    def sthHappened(self, context):
        print
        'In BlockedState.sthHappened() do some context switching'
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

    def goRunning(self, context):
        print
        'In ReadyState.goRunning() do some context switching'
        ProcessState.changeState(RunningState().instance(), context)


class ProcessContext:
    def __init__(self):
        self._state = ReadyState().instance()

    def changeState(self, state):
        self._state = state

    def waitSth(self):
        self._state.waitSth(self)

    def goReady(self):
        self._state.goReady(self)

    def sthHappened(self):
        self._state.sthHappened(self)

    def goRunning(self):
        self._state.goRunning(self)

    def prtStateName(self):
        print
        'now the state of process is ', self._state.getStateName()


class Client:
    def run(self):
        ctx = ProcessContext()
        ctx.prtStateName()
        ctx.goRunning()
        ctx.prtStateName()
        ctx.waitSth()
        ctx.prtStateName()
        ctx.sthHappened()
        ctx.prtStateName()
        ctx.goRunning()
        ctx.prtStateName()
        ctx.goReady()
        ctx.prtStateName()


if (__name__ == "__main__"):
    client = Client()
    client.run()




