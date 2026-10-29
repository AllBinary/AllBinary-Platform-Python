# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

import threading


class StupidTimer:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.nullUtil: NullUtil = NullUtil.getInstance()
        self.threadObjectUtil: ThreadObjectUtil = ThreadObjectUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def visitBool(self, visitorInterface: Visitor) -> bool:
        result: bool = visitorInterface.visit(self.nullUtil.NULL_OBJECT)
        result2: bool = result
        return result2
    

    # throws Exception
    def visit(self, visitorInterface: Visitor, timeDelayHelper: TimeDelayHelper) -> None:
        tookTooLong: bool = False
        WAITING_FOR: str = "Waiting for: "
        PreLogUtil.put(str(StringMaker().append(WAITING_FOR).append(StringUtil.getInstance().toString(visitorInterface))), self, self.commonStrings.VISIT)
        index: int = 0
        while self.visitBool(visitorInterface):
            if index % 10 == 0:
                PreLogUtil.put(str(StringMaker().append(WAITING_FOR).appendint(index)), self, self.commonStrings.VISIT)
            index += 1
            with self._lock:  # synchronized (self)
                self.threadObjectUtil.waitObjectFor(self, 1800)
            if timeDelayHelper.isTimeTNT():
                tookTooLong = True
                break
        if tookTooLong:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.VISIT, Exception(str(StringMaker().append("Took Too Long: ").append(StringUtil.getInstance().toString(visitorInterface)))))
        else:
            PreLogUtil.put(str(timeDelayHelper), self, self.commonStrings.VISIT)
    

    # throws Exception
    def stopWaiting(self) -> None:
        with self._lock:  # synchronized (self)
            self.threadObjectUtil.notifyObject(self)
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil


