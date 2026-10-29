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


class BasePatrolAI(BasicAI):
    MAX_DISTANCE: int = SmallIntegerSingletonFactory.getInstance().getAt(2)
    DIRECTION_ARRAY: int = SmallIntegerSingletonFactory.getInstance().getAt(3)
    FIRING_DISTANCE: int = SmallIntegerSingletonFactory.getInstance().getAt(4)
    SPEED: int = SmallIntegerSingletonFactory.getInstance().getAt(5)

    def _init_fields(self) -> None:
        self.maxDistance: int = None
        self.currentDistance: int = None
        self.xTotalDistance: int = 0
        self.lastKeyDirection: int = Canvas.RIGHT
        self.keyDirection: int = Canvas.RIGHT
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.maxDistance = hashtable.get(BasePatrolAI.MAX_DISTANCE)
        self.currentDistance = int(self.maxDistance)
    

    def update(self) -> None:
        self.updateTotalDistance()
        self.changeDirectionIfReachedPacingAreaMax()
    

    def updateTotalDistance(self) -> None:
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        velocityProperties: BasicVelocityProperties = velocityInterfaceCompositeInterface.getVelocityProperties()
        self.xTotalDistance += velocityProperties.getVelocityXBasicDecimalP().getScaled()
    

    def changeDirectionIfReachedPacingAreaMax(self) -> None:
        mathUtil: MathUtil = MathUtil.getInstance()
        totalDistance: int = mathUtil.abs(self.xTotalDistance)
        if totalDistance > self.currentDistance:
            self.nextDirection()
    

    def nextDirection(self) -> None:
        if self.lastKeyDirection == Canvas.LEFT:
            self.keyDirection = Canvas.RIGHT
            self.lastKeyDirection = self.keyDirection
            self.xTotalDistance = 0
        elif self.lastKeyDirection == Canvas.RIGHT:
            self.keyDirection = Canvas.LEFT
            self.lastKeyDirection = self.keyDirection
            self.xTotalDistance = 0
    

    def disable(self) -> None:
        pass
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.util.ABHashtable import ABHashtable


