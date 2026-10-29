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

import time
from org.allbinary.thread.ThreadPool import ThreadPool
from org.allbinary.thread.ThreadPool import ThreadPool


class PrimaryThreadPool(ThreadPool):
    THREAD_POOL: ThreadPool = ThreadPool("Primary", 1, ThreadPool.NORMAL_PRIORITY)
    

    @staticmethod
    def getInstance() -> ThreadPool:
        return PrimaryThreadPool.THREAD_POOL
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        super().__init__(poolName, numThreads, priority)
    

    def runTask(self, task: object) -> None:
        self.logUtil.putF(str(StringMaker().append(StringUtil.getInstance().toString(task)).appendlong(int(int(time.time() * 1000)))), self, self.threadPoolStrings.ADD_TASK)
        super().runTask(task)
    

    def startTask(self, task: object) -> None:
        self.logUtil.putF(str(StringMaker().append(self.threadPoolStrings.START_TASK).append(StringUtil.getInstance().toString(task))), self, self.commonStrings.RUN)
    

    def completedTask(self, task: object) -> None:
        self.logUtil.putF(str(StringMaker().append(self.threadPoolStrings.COMPLETE_TASK).append(StringUtil.getInstance().toString(task))), self, self.commonStrings.RUN)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


