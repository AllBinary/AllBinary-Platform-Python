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
# package org.allbinary.game.ag.ai.scroller

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.ai.BasicAI import BasicAI


class TimedFireAI(BasicAI):
    TIME: int = None

    def _init_fields(self) -> None:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.maxFireDelayTimeHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.delay: int = None
    

    def __init__(self, delay: int, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.delay = delay
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        timeFiredInterface: TimeFiredInterface = self.getOwnerLayerInterface()
        if self.maxFireDelayTimeHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime) and timeFiredInterface.getLastFireTime() + self.maxFireDelayTimeHelper.delay < self.maxFireDelayTimeHelper.getStartTime():
            super().processKeyAI(Canvas.KEY_NUM1)
            self.maxFireDelayTimeHelper.delay = self.delay
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


def _TimedFireAI_TIME() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(1)

lazy_static(TimedFireAI, "TIME", _TimedFireAI_TIME)

