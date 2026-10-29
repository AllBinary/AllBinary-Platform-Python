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


class ThreadFactoryUtil:
    instance: ThreadFactoryUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ThreadFactoryUtil:
        return ThreadFactoryUtil.instance
    

    def getInstanceGameCanvasRunnable(self, runnable: GameCanvasRunnableInterface) -> threading.Thread:
        return self.getInstanceType(runnable, runnable.getType())
    

    def getInstanceForRunnable(self, runnable: ABRunnable) -> threading.Thread:
        return self.getInstanceType(runnable, runnable.getType())
    

    def getInstanceType(self, runnable: object, type_: int) -> threading.Thread:
        from org.allbinary.thread.PrimaryThreadPool import PrimaryThreadPool
        from org.allbinary.thread.PrimaryThreadPool import PrimaryThreadPool
        commonStrings: CommonStrings = CommonStrings.getInstance()
        if J2MEUtil.isHTML():
            if type_ == DemoCanvas.TYPE or type_ == AllBinaryGameCanvas.TYPE:
                demoGameSingleThreadStartRunnable: RunnableCanvasSingleThreadStartRunnable = RunnableCanvasSingleThreadStartRunnable(runnable)
                PreLogUtil.put(str(StringMaker().append("Using Pseudo Thread for DemoCanvas/AllBinaryGameCanvas under PlayN/HTML5: ").append(StringUtil.getInstance().toString(runnable))), self, commonStrings.CONSTRUCTOR)
                primaryThreadPool: ThreadPool = PrimaryThreadPool.getInstance()
                primaryThreadPool.runTask(demoGameSingleThreadStartRunnable)
            else:
                PreLogUtil.put(str(StringMaker().append("Using Pseudo Thread for Runnable under PlayN/HTML5: ").append(StringUtil.getInstance().toString(runnable))), self, commonStrings.CONSTRUCTOR)
                primaryThreadPool: ThreadPool = PrimaryThreadPool.getInstance()
                primaryThreadPool.runTask(runnable)
        thread: threading.Thread = threading.Thread(target=runnable.run, name=str(runnable))
        self.logUtil.putF(str(thread), self, commonStrings.CONSTRUCTOR)
        return thread
    

    def start(self, thread: threading.Thread) -> None:
        thread.start()
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.displayable.canvas.DemoCanvas import DemoCanvas
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface
from org.allbinary.game.displayable.canvas.RunnableCanvasSingleThreadStartRunnable import RunnableCanvasSingleThreadStartRunnable
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


ThreadFactoryUtil.instance = ThreadFactoryUtil()

