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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.thread.ThreadPool import ThreadPool


#This is mainly for network communications.
@java_inherited_overloads
class ImageThreadPool(ThreadPool):
    instance: ThreadPool = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ThreadPool:
        return ImageThreadPool.instance
    

    def __init__(self, poolName: str, numThreads: int, priority: int) -> None:
        __class__._java_defaults(self)
        super().__init__(poolName, numThreads, priority)
        __class__._init_fields(self)
    

    def runTask(self, task: object) -> None:
        with self._lock:
            return __class__.__dict__["_runTask_unlocked"].__get__(self, __class__)(task)

    def _runTask_unlocked(self, task: object) -> None:
        java_super_call(super(), "runTask", task)
    

    def startTask(self, task: object) -> None:
        pass
    

    def completedTask(self, task: object) -> None:
        pass
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _ImageThreadPool_instance() -> object:
    from org.allbinary.thread.ThreadPool import ThreadPool
    return ImageThreadPool("ImageLoader", 1, ThreadPool.NORMAL_PRIORITY)

lazy_static(ImageThreadPool, "instance", _ImageThreadPool_instance)

