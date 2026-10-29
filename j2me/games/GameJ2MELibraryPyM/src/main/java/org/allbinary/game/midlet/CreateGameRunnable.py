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



class CreateGameRunnable(object):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.demoGameMidlet: DemoGameMidlet = None
        self.hashtable: ABHashtable[object, object] = None
        self.startGameMidletEvent: DemoGameMidletEvent = None
    

    def __init__(self, demoGameMidlet: DemoGameMidlet, hashtable: ABHashtable[object, object]) -> None:
        from org.allbinary.game.midlet.DemoGameMidletEvent import DemoGameMidletEvent
        from org.allbinary.game.midlet.DemoGameMidletStateFactory import DemoGameMidletStateFactory
        self._init_fields()
        self.demoGameMidlet = demoGameMidlet
        self.hashtable = hashtable
        self.startGameMidletEvent = DemoGameMidletEvent(self, DemoGameMidletStateFactory.getInstance().START_GAME)
    

    def run(self) -> None:
        from org.allbinary.game.midlet.DemoGameMidletEventHandler import DemoGameMidletEventHandler
        try:
            self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            self.demoGameMidlet.commandAction(MyCommandsFactory.getInstance().SET_DISPLAYABLE, progressCanvas)
            self.demoGameMidlet.stopGameCanvasRunnableInterface()
            self.demoGameMidlet.setGameCanvasRunnableInterface(self.demoGameMidlet.createGameCanvasRunnableInterface())
            self.demoGameMidlet.getGameCanvasRunnableInterface().setLoadStateHashtable(self.hashtable)
            self.demoGameMidlet.startGameCanvasRunnableInterface()
            DemoGameMidletEventHandler.getInstance().fireEvent(self.startGameMidletEvent)
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


