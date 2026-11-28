# Generated Code Do Not Modify
# package org.allbinary.thread

from __future__ import annotations

from java.lang.JavaMonitor import java_monitor, java_wait
from java.lang.JavaThread import JavaThread
import threading
from java.lang.JavaRuntimeStatic import lazy_static


class ThreadObjectUtil:
    instance: ThreadObjectUtil = None

    def _init_fields(self) -> None:
        self.NULL_PRIORITY_RUNNABLE: PriorityRunnable = NullPriorityRunnable()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> ThreadObjectUtil:
        return ThreadObjectUtil.instance
    

    def notifyObject(self, anyType: object) -> None:
        java_monitor(anyType).notify()
    

    # throws Exception
    def waitObject(self, anyType: object) -> None:
        java_wait(anyType)
    

    # throws Exception
    def waitObjectFor(self, anyType: object, delay: int) -> None:
        from org.allbinary.TsUtil import TsUtil
        TsUtil.getInstance().waitFor(anyType, delay)
    

    def processThread(self, runnable: object) -> None:
        thread: JavaThread = JavaThread(target=runnable.run)
        thread.start()
# from org.allbinary.TsUtil import TsUtil
from org.allbinary.thread.NullPriorityRunnable import NullPriorityRunnable


def _ThreadObjectUtil_instance() -> object:
    return ThreadObjectUtil()

lazy_static(ThreadObjectUtil, "instance", _ThreadObjectUtil_instance)

