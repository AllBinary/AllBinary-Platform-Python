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
# package org.allbinary.game.init

from __future__ import annotations

import time
import threading
from org.allbinary.game.configuration.event.GameInitializedListenerInterface import GameInitializedListenerInterface


class DefaultGameInitializationListener(GameInitializedListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.swtJOGLProcessor: SWTJOGLProcessor = SWTJOGLProcessor.getInstance()
        self.firstTime: bool = True
    

    def __init__(self) -> None:
        self._init_fields()
        gameInitializedEventHandler: GameInitializedEventHandler = GameInitializedEventHandler.getInstance()
        gameInitializedEventHandler.removeAllListeners()
        gameInitializedEventHandler.addListenerInterface(self)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onGameInitialized(self, gameInitializedEvent: GameInitializedEvent) -> None:
        ON_GAME_INITIALIZED: str = "onGameInitialized"
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            self.logUtil.putF(commonStrings.START, self, ON_GAME_INITIALIZED)
            while not self.swtJOGLProcessor.isHolderCreated():
                self.logUtil.putF(commonStrings.UPDATE, self, ON_GAME_INITIALIZED)
                time.sleep((20) / 1000)
            FeatureResourceInitializationUtil.getInstance().init(gameInitializedEvent.getLevel())
            if self.firstTime:
                self.firstTime = False
            else:
                self.swtJOGLProcessor.onSurfaceChanged()
        except Exception as e:
            self.logUtil.put(commonStrings.EXCEPTION, self, ON_GAME_INITIALIZED, e)
from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
from org.allbinary.game.configuration.event.GameInitializedEventHandler import GameInitializedEventHandler
from org.allbinary.game.resource.FeatureResourceInitializationUtil import FeatureResourceInitializationUtil
from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings


