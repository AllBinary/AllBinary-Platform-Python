# Generated Code Do Not Modify
# package org.allbinary.thread

from __future__ import annotations

import threading


class ThreadObjectUtil:
    instance: ThreadObjectUtil = None

    def _init_fields(self) -> None:
        self.NULL_PRIORITY_RUNNABLE: PriorityRunnable = NullPriorityRunnable()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ThreadObjectUtil:
        return ThreadObjectUtil.instance
    

    def notifyObject(self, anyType: object) -> None:
        anyType.notify()
    

    # throws Exception
    def waitObject(self, anyType: object) -> None:
        anyType.wait()
    

    # throws Exception
    def waitObjectFor(self, anyType: object, delay: int) -> None:
        TsUtil.getInstance().waitFor(anyType, delay)
    

    def processThread(self, runnable: object) -> None:
        thread: threading.Thread = threading.Thread(target=runnable.run)
        thread.start()
from org.allbinary.TsUtil import TsUtil
from org.allbinary.thread.NullPriorityRunnable import NullPriorityRunnable


ThreadObjectUtil.instance = ThreadObjectUtil()

