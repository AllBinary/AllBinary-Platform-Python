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

from org.allbinary.game.ag.ai.scroller.BasePatrolAI import BasePatrolAI


class RandomPatrolAI(BasePatrolAI):

    def _init_fields(self) -> None:
        self.changedDirection: bool = True
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        self._init_fields()
        self.updateRandomDistance()
    

    def updateRandomDistance(self) -> None:
        self.currentDistance = MyRandomFactory.getInstance().getAbsoluteNextInt(int(self.maxDistance))
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        super().update()
        super().processKeyAI(self.keyDirection)
        if self.changedDirection:
            super().processKeyAI(Canvas.KEY_NUM1)
            self.updateRandomDistance()
            self.changedDirection = False
    

    def nextDirection(self) -> None:
        super().nextDirection()
        self.changedDirection = True
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.util.ABHashtable import ABHashtable


