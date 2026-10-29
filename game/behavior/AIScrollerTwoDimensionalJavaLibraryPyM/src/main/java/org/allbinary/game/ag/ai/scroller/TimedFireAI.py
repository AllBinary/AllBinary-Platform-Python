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

from org.allbinary.game.ai.BasicAI import BasicAI
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


class TimedFireAI(BasicAI):
    TIME: int = SmallIntegerSingletonFactory.getInstance().getAt(1)

    def _init_fields(self) -> None:
        self.maxFireDelayTimeHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.delay: int = None
    

    def __init__(self, delay: int, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.delay = delay
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        timeFiredInterface: TimeFiredInterface = self.getOwnerLayerInterface()
        if self.maxFireDelayTimeHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime) and timeFiredInterface.getLastFireTime() + self.maxFireDelayTimeHelper.delay < self.maxFireDelayTimeHelper.getStartTime():
            super().processKeyAI(Canvas.KEY_NUM1)
            self.maxFireDelayTimeHelper.delay = self.delay
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


