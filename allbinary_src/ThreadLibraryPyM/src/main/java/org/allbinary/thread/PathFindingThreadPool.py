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

from org.allbinary.thread.ThreadPool import ThreadPool


#This is mainly for network communications.
class PathFindingThreadPool(ThreadPool):
    instance: ThreadPool = None
    

    @staticmethod
    def getInstance() -> ThreadPool:
        return PathFindingThreadPool.instance
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        from org.allbinary.thread.ThreadPool import ThreadPool
        super().__init__(poolName, numThreads, ThreadPool.NORMAL_PRIORITY)
    

    def runTaskWithPriority(self, task: PriorityRunnable) -> None:
        super().runTaskWithPriority(task)
    

    def runTask(self, task: object) -> None:
        super().runTask(task)
    

    def startTask(self, task: object) -> None:
        pass
    

    def completedTask(self, task: object) -> None:
        pass


PathFindingThreadPool.instance = PathFindingThreadPool("PathFinding", 1, 1)

