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


class BasePatrolAI(BasicAI):
    MAX_DISTANCE: int = None
    DIRECTION_ARRAY: int = None
    FIRING_DISTANCE: int = None
    SPEED: int = None

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        self.maxDistance: int = None
        self.currentDistance: int = None
        self.xTotalDistance: int = 0
        self.lastKeyDirection: int = Canvas.RIGHT
        self.keyDirection: int = Canvas.RIGHT
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.ABHashtable import ABHashtable
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.maxDistance = hashtable.get(BasePatrolAI.MAX_DISTANCE)
        self.currentDistance = int(self.maxDistance)
    

    def update(self) -> None:
        self.updateTotalDistance()
        self.changeDirectionIfReachedPacingAreaMax()
    

    def updateTotalDistance(self) -> None:
        from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
        from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        velocityProperties: BasicVelocityProperties = velocityInterfaceCompositeInterface.getVelocityProperties()
        self.xTotalDistance += velocityProperties.getVelocityXBasicDecimalP().getScaled()
    

    def changeDirectionIfReachedPacingAreaMax(self) -> None:
        from org.allbinary.logic.math.MathUtil import MathUtil
        mathUtil: MathUtil = MathUtil.getInstance()
        totalDistance: int = mathUtil.abs(self.xTotalDistance)
        if totalDistance > self.currentDistance:
            self.nextDirection()
    

    def nextDirection(self) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
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
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
# from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.math.MathUtil import MathUtil
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.util.ABHashtable import ABHashtable


def _BasePatrolAI_MAX_DISTANCE() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(2)

lazy_static(BasePatrolAI, "MAX_DISTANCE", _BasePatrolAI_MAX_DISTANCE)

def _BasePatrolAI_DIRECTION_ARRAY() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(3)

lazy_static(BasePatrolAI, "DIRECTION_ARRAY", _BasePatrolAI_DIRECTION_ARRAY)

def _BasePatrolAI_FIRING_DISTANCE() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(4)

lazy_static(BasePatrolAI, "FIRING_DISTANCE", _BasePatrolAI_FIRING_DISTANCE)

def _BasePatrolAI_SPEED() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(5)

lazy_static(BasePatrolAI, "SPEED", _BasePatrolAI_SPEED)

