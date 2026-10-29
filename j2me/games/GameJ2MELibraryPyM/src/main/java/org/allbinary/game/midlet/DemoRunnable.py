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
# package org.allbinary.game.midlet

from __future__ import annotations



class DemoRunnable(object):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.demoGameMidlet: DemoGameMidlet = None
        self.startDemoGameMidletEvent: DemoGameMidletEvent = None
    

    def __init__(self, demoGameMidlet: DemoGameMidlet) -> None:
        from org.allbinary.game.midlet.DemoGameMidletEvent import DemoGameMidletEvent
        from org.allbinary.game.midlet.DemoGameMidletStateFactory import DemoGameMidletStateFactory
        self._init_fields()
        self.demoGameMidlet = demoGameMidlet
        self.startDemoGameMidletEvent = DemoGameMidletEvent(self.demoGameMidlet, DemoGameMidletStateFactory.getInstance().START_DEMO)
    

    def run(self) -> None:
        from org.allbinary.game.midlet.DemoGameMidletEventHandler import DemoGameMidletEventHandler
        try:
            self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append("GameCanvasRunnableInterface")), self, self.commonStrings.RUN)
            self.demoGameMidlet.commandAction(MyCommandsFactory.getInstance().SET_DISPLAYABLE, ProgressCanvasFactory.getInstance())
            self.demoGameMidlet.setGameCanvasRunnableInterface(self.demoGameMidlet.createDemoGameCanvasRunnableInterface())
            self.demoGameMidlet.demoSetup()
            DemoGameMidletEventHandler.getInstance().fireEvent(self.startDemoGameMidletEvent)
            self.demoGameMidlet.startGameCanvasRunnableInterface()
            self.demoGameMidlet.postDemoSetup()
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


