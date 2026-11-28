# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading


@java_inherited_overloads
class PooledThread(JavaThread):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("threadObjectUtil", None)
        vars(self).setdefault("threadPool", None)
        vars(self).setdefault("INTERRUPT_EXCEPTION", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.threadObjectUtil: ThreadObjectUtil = ThreadObjectUtil.getInstance()
        if "threadPool" not in vars(self): self.threadPool: ThreadPool = None
        self.INTERRUPT_EXCEPTION: str = "Exit InterruptedException"
    

    def __init__(self, threadPool: ThreadPool) -> None:
        __class__._java_defaults(self)
        super().__init__(name=threadPool.createName())
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.threadPool = threadPool
    

    def run(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.threadPool.threadStarted()
        while True:
            task2: object = self.threadObjectUtil.NULL_PRIORITY_RUNNABLE
            try:
                task2 = self.threadPool.getTask()
                self.threadPool.runningTask = True
                self.threadPool.startTask(task2)
            except InterruptedError as ex:
                logUtil: LogUtil = LogUtil.getInstance()
                logUtil.putF(self.INTERRUPT_EXCEPTION, self, self.commonStrings.RUN)
                break
            if task2 == self.threadObjectUtil.NULL_PRIORITY_RUNNABLE:
                break
            try:
                task2.run()
                self.threadPool.completedTask(task2)
                self.threadPool.runningTask = False
            except Exception as e:
                logUtil: LogUtil = LogUtil.getInstance()
                logUtil.put(str(StringMaker().append(self.commonStrings.EXCEPTION_LABEL).append(StringUtil.getInstance().toString(task2))), self, self.commonStrings.RUN, e)
        self.threadPool.threadStopped()
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil


