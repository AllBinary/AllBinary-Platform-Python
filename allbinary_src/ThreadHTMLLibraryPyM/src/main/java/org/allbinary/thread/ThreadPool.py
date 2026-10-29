#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.thread

from __future__ import annotations

import threading


class ThreadPool:
    NORMAL_PRIORITY: int = 5
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.NULL_RUNNABLE: NullRunnable = NullRunnable.getInstance()
        self.threadPoolStrings: ThreadPoolStrings = ThreadPoolStrings.getInstance()
        self.threadObjectUtil: ThreadObjectUtil = ThreadObjectUtil.getInstance()
        self.isAlive: bool = False
        self.taskQueue: BasicArrayList = BasicArrayListD()
        self.numThreads: int = 0
        self.runningTask: bool = False
        self.currentPriorityRunnable: PriorityRunnable = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        self._init_fields()
    

    # throws Exception
    def runAPriorityTask(self) -> None:
        if not self.currentPriorityRunnable.isDone():
            self.currentPriorityRunnable.run()
        else:
            runnable: object = self.getTask()
            if runnable == self.NULL_RUNNABLE:
                return
            self.currentPriorityRunnable = runnable
            if not (self.currentPriorityRunnable == self.threadObjectUtil.NULL_PRIORITY_RUNNABLE):
                self.currentPriorityRunnable.reset()
                self.currentPriorityRunnable.run()
    

    # throws Exception
    def runATask(self) -> None:
        runnable: object = self.getTask()
        if runnable is not None:
            runnable.run()
    

    def init(self) -> None:
        if not self.isAlive:
            self.isAlive = True
            self.taskQueue = BasicArrayListD()
    

    def runTaskWithPriority(self, task: PriorityRunnable) -> None:
        with self._lock:
            return self._runTaskWithPriority_unlocked(task)

    def _runTaskWithPriority_unlocked(self, task: PriorityRunnable) -> None:
        if not self.isAlive:
            self.init()
        if task is not None:
            size: int = self.taskQueue.size()
            runnable: PriorityRunnable = None
            lowerPriorityRunnable: PriorityRunnable = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
            for index in range(0, size):
                runnable = self.taskQueue.get(index)
                if runnable.getPriority() > task.getPriority():
                    lowerPriorityRunnable = runnable
                    break
            if lowerPriorityRunnable == self.threadObjectUtil.NULL_PRIORITY_RUNNABLE:
                self.taskQueue.add(task)
            else:
                index: int = self.taskQueue.indexOf(lowerPriorityRunnable)
                self.taskQueue.addAt(index, task)
    

    def runTask(self, task: object) -> None:
        with self._lock:
            return self._runTask_unlocked(task)

    def _runTask_unlocked(self, task: object) -> None:
        if not self.isAlive:
            self.init()
        if task is not None:
            self.taskQueue.add(task)
    

    # throws InterruptedException
    def getTask(self) -> object:
        with self._lock:
            return self._getTask_unlocked()

    def _getTask_unlocked(self) -> object:
        if self.taskQueue.isEmpty():
            return self.NULL_RUNNABLE
        return self.taskQueue.removeAt(0)
    

    def clear(self) -> None:
        with self._lock:
            return self._clear_unlocked()

    def _clear_unlocked(self) -> None:
        self.taskQueue.clear()
    

    def close(self) -> None:
        with self._lock:
            return self._close_unlocked()

    def _close_unlocked(self) -> None:
        if self.isAlive:
            self.isAlive = False
            self.taskQueue.clear()
            self.currentPriorityRunnable = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
    

    def join(self) -> None:
        self.isAlive = False
        self.taskQueue.clear()
        self.currentPriorityRunnable = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
    

    def isBusy(self) -> bool:
        if not self.isAlive:
            return False
        if self.taskQueue.size() > 0:
            return True
        if self.runningTask:
            return True
        return False
    

    def threadStarted(self) -> None:
        pass
    

    def threadStopped(self) -> None:
        if self.numThreads == 1:
            self.isAlive = False
            self.taskQueue.clear()
            self.currentPriorityRunnable = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
    

    def startTask(self, task: object) -> None:
        pass
    

    def completedTask(self, task: object) -> None:
        pass
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.thread.NullRunnable import NullRunnable
from org.allbinary.thread.ThreadPoolStrings import ThreadPoolStrings
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil


