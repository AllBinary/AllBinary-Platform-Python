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
# package org.allbinary.canvas

from __future__ import annotations

import time
import threading
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.thread.RunnableInterface import RunnableInterface


class RunnableCanvas(MyCanvas, RunnableInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.nullUtil: NullUtil = NullUtil.getInstance()
        self.stdUtil: StdUtil = StdUtil.getInstance()
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.thread: threading.Thread = NullThread.NULL_THREAD
        self.currentThread: threading.Thread = NullThread.NULL_THREAD
        self.running: bool = False
        self.loopTimeHelper: TimeDelayHelper = TimeDelayHelper(NullWaitGameRunnable.getInstance().WAIT)
        self.runnableCanvasRefreshHelper: Processor = Processor.getInstance()
        self.commonLabels: CommonLabels = CommonLabels.getInstance()
        self.threadObjectUtil: ThreadObjectUtil = ThreadObjectUtil.getInstance()
        self.SET_RUNNING: str = "setRunning"
        self.IS_RUNNING: str = "isRunning"
        self.THREAD: str = "Thread: "
        self.NOT_EQUAL: str = " != "
        self.PAUSE_SLEEP: str = "pause sleep"
        self.START_PAUSE: str = "start pause - game thread sleep at: "
        self.END_PAUSE: str = "end pause - game thread sleep at: "
        self.PROCESS_LOOP_SLEEP: str = "processLoopSleep"
        self.pauseWait: int = 0
        self.notified: bool = False
    

    def __init__(self, commandListener: CommandListener, childNameList: BasicArrayList, hasParam: bool) -> None:
        from org.allbinary.canvas.RunnableCanvasRefreshHelper import RunnableCanvasRefreshHelper
        super().__init__(CommonStrings.getInstance().UNKNOWN, childNameList)
        self._init_fields()
        self.logUtil.putF(str(StringMaker().append("RunnableCanvas delay: ").appendint(int(self.loopTimeHelper.delay))), self, self.commonStrings.CONSTRUCTOR)
        self.runnableCanvasRefreshHelper = RunnableCanvasRefreshHelper(self)
        if commandListener is not None:
            self.initCommands(commandListener)
        elif hasParam:
            self.logUtil.putF("commandListener was null", self, "initCommands")
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.logUtil.putF(self.commonStrings.NOT_IMPLEMENTED, self, "initCommands")
    

    def isMainCanvas(self) -> bool:
        if self.getCustomCommandListener() is not None:
            return True
        else:
            return False
    

    def setThread(self, thread: threading.Thread) -> None:
        self.thread = thread
    

    def setRunning(self, running: bool) -> None:
        self.running = running
        if not self.running:
            self.thread = NullThread.NULL_THREAD
            with self._lock:  # synchronized (self)
                self.threadObjectUtil.notifyObject(self)
        self.logUtil.putF(str(StringMaker().append(self.IS_RUNNING).appendboolean(self.running)), self, self.SET_RUNNING)
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        if self.thread == self.currentThread:
            return self.running
        else:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.THREAD)
            if self.thread is not None:
                stringBuffer.append(str(self.thread))
            stringBuffer.append(self.NOT_EQUAL)
            if self.currentThread is not None:
                stringBuffer.append(StringUtil.getInstance().toString(self.currentThread))
            self.logUtil.putF(str(stringBuffer), self, self.IS_RUNNING)
            return False
    

    def getLoopTimeHelperP(self) -> TimeDelayHelper:
        return self.loopTimeHelper
    

    def setWait(self, wait: int) -> None:
        self.loopTimeHelper.delay = wait
        self.pauseWait = wait * 3
        self.logUtil.putF(str(StringMaker().append("setWait - delay: ").appendint(int(self.loopTimeHelper.delay))), self, self.commonStrings.CONSTRUCTOR)
    

    def getWait(self) -> int:
        return self.loopTimeHelper.delay
    

    def setCurrentThread(self) -> None:
        self.currentThread = threading.current_thread()
    

    def setCurrentThreadFake(self) -> None:
        self.currentThread = self.thread
    

    def showNotify(self) -> None:
        try:
            self.stopWaiting()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "showNotify", e)
    

    # throws Exception
    def stopWaiting(self) -> None:
        self.notified = True
        with self._lock:  # synchronized (self)
            self.threadObjectUtil.notifyObject(self)
        self.repaint()
    

    # throws Exception
    def waitOnNotify(self, wait: int) -> None:
        with self._lock:
            return self._waitOnNotify_unlocked(wait)

    def _waitOnNotify_unlocked(self, wait: int) -> None:
        if not self.notified:
            if wait > 0:
                self.threadObjectUtil.waitObjectFor(self, wait)
            else:
                self.threadObjectUtil.waitObject(self)
    

    # throws Exception
    def processSleep(self) -> None:
        time.sleep((self.pauseWait) / 1000)
    

    def isPausable(self) -> bool:
        return False
    

    # throws Exception
    def processGameSleep(self, sleep: int) -> None:
        time.sleep((sleep) / 1000)
    

    # throws Exception
    def processLoopSleep(self) -> None:
        self.runnableCanvasRefreshHelper.process()
        if self.isPaused():
            stringMaker: StringMaker = StringMaker()
            if self.isRunning() and not self.isSingleThread():
                stringMaker.delete(0, stringMaker.length())
                currentTimeMillis: int = self.systemWrapper.currentTimeMillis()
                self.logUtil.putF(str(stringMaker.append(self.START_PAUSE).appendlong(currentTimeMillis).append(self.PAUSE_SLEEP).appendlong(self.pauseWait)), self, self.PROCESS_LOOP_SLEEP)
                while self.isPaused() and self.isRunning() and not self.isSingleThread():
                    self.processSleep()
                    if not self.isPausable():
                        stringMaker.delete(0, stringMaker.length())
                        self.logUtil.putF(str(stringMaker.append(self.END_PAUSE).appendlong(currentTimeMillis)), self, self.PROCESS_LOOP_SLEEP)
                        return
        elapsedTime: int = self.loopTimeHelper.getElapsedTNT()
        wait: int = int(self.loopTimeHelper.delay)
        if elapsedTime > wait:
            elapsedTime = wait
        else:
            self.processGameSleep(wait - elapsedTime)
    

    def isSingleThread(self) -> bool:
        return False
    

    def run(self) -> None:
        self.setCurrentThread()
    

    # throws Exception
    def end2(self) -> None:
        pass
    

    def getType(self) -> int:
        return -1
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.TsUtil import TsUtil
from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.NullThread import NullThread
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.canvas.Processor import Processor


