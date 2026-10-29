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
from org.allbinary.thread.ThreadPool import ThreadPool
from org.allbinary.thread.ThreadPool import ThreadPool


#This is mainly for network communications.
class ImageThreadPool(ThreadPool):
    instance: ThreadPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ThreadPool:
        return ImageThreadPool.instance
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        super().__init__(poolName, numThreads, priority)
        self._init_fields()
    

    def runTask(self, task: object) -> None:
        with self._lock:
            return self._runTask_unlocked(task)

    def _runTask_unlocked(self, task: object) -> None:
        super().runTask(task)
    

    def startTask(self, task: object) -> None:
        pass
    

    def completedTask(self, task: object) -> None:
        pass
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil


ImageThreadPool.instance = ImageThreadPool("ImageLoader", 1, ThreadPool.NORMAL_PRIORITY)

