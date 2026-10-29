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
    ROOT_NAME: str = "-PooledThread-"
    NORMAL_PRIORITY: int = 5
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.NULL_RUNNABLE: NullRunnable = NullRunnable.getInstance()
        self.threadPoolStrings: ThreadPoolStrings = ThreadPoolStrings.getInstance()
        self.threadObjectUtil: ThreadObjectUtil = ThreadObjectUtil.getInstance()
        self.poolName: str = None
        self.priority: int = None
        self.isAlive: bool = False
        self.taskQueue: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.threadID: int = 0
        self.numThreads: int = None
        self.runningTask: bool = False
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        self._init_fields()
        self.poolName = poolName
        self.priority = priority
        self.numThreads = numThreads
    

    def init(self) -> None:
        from org.allbinary.thread.PooledThread import PooledThread
        if not self.isAlive:
            self.isAlive = True
            self.taskQueue = BasicArrayListD()
            pooledThread: PooledThread = None
            for i in range(0, self.numThreads):
                pooledThread = PooledThread(self)
                pooledThread.setPriority(self.priority)
                pooledThread.start()
    

    # throws Exception
    def runAPriorityTask(self) -> None:
        raise RuntimeError()
    

    def runTaskWithPriority(self, task: PriorityRunnable) -> None:
        with self._lock:  # synchronized (self)
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
                self.notify()
    

    def runTask(self, task: object) -> None:
        with self._lock:  # synchronized (self)
            if not self.isAlive:
                self.init()
            if task is not None:
                self.taskQueue.add(task)
                self.notify()
    

    # throws InterruptedException
    def getTask(self) -> object:
        with self._lock:  # synchronized (self)
            while self.taskQueue.size() == 0:
                if not self.isAlive:
                    return self.NULL_RUNNABLE
                self.wait()
            runnable: object = self.taskQueue.removeAt(0)
            return runnable
    

    def clear(self) -> None:
        with self._lock:  # synchronized (self)
            if self.isAlive:
                self.taskQueue.clear()
    

    def close(self) -> None:
        with self._lock:  # synchronized (self)
            if self.isAlive:
                self.isAlive = False
                self.taskQueue.clear()
    

    def join(self) -> None:
        with self._lock:  # synchronized (self)
            self.isAlive = False
            self.taskQueue.clear()
            self.notifyAll()
    

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
    

    def startTask(self, task: object) -> None:
        pass
    

    def completedTask(self, task: object) -> None:
        pass
    

    def createName(self) -> str:
        return str(StringMaker().append(self.poolName).append(ThreadPool.ROOT_NAME).appendint(((setattr(self, "threadID", self.threadID + 1) or self.threadID) - 1)))
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.thread.NullRunnable import NullRunnable
from org.allbinary.thread.ThreadPoolStrings import ThreadPoolStrings
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil


