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


class ThreadUtil:
    instance: ThreadUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.JOIN: str = "join"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ThreadUtil:
        return ThreadUtil.instance
    

    def isRunning(self, thread: threading.Thread) -> bool:
        if thread is not None and thread.isAlive():
            return True
        else:
            return False
    

    # throws Exception
    def join(self, thread: threading.Thread) -> None:
        if ThreadUtil.getInstance().isRunning(thread):
            self.logUtil.putF("Waiting for Thread To Join/End", self, self.JOIN)
            thread.join()
from org.allbinary.logic.communication.log.LogUtil import LogUtil


ThreadUtil.instance = ThreadUtil()

