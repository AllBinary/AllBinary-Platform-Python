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

import math
from org.allbinary.game.tracking.TrackingEventListenerInterface import TrackingEventListenerInterface
from org.allbinary.game.ag.ai.scroller.BasePatrolAI import BasePatrolAI


class PacePatrolAI(BasePatrolAI, TrackingEventListenerInterface):

    def _init_fields(self) -> None:
        self.trackingList: BasicArrayList = None
        self.firingDistance: int = 0
        self.isFollowLimitedByTerrain: bool = False
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        self._init_fields()
        TrackingEventHandler.getInstance().addListenerInterface(self)
        self.trackingList = BasicArrayListD()
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        self.update()
        direction: Direction = self.setFiringDirectionForTargetIfInRange()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if direction == directionFactory.LEFT:
            if self.lastKeyDirection != self.keyDirection or not self.isFollowLimitedByTerrain:
                super().processKeyAI(Canvas.LEFT)
            self.keyDirection = Canvas.LEFT
            self.lastKeyDirection = self.keyDirection
            self.xTotalDistance = 0
            super().processKeyAI(Canvas.KEY_NUM1)
        elif direction == directionFactory.RIGHT:
            if self.lastKeyDirection != self.keyDirection or not self.isFollowLimitedByTerrain:
                super().processKeyAI(Canvas.RIGHT)
            self.keyDirection = Canvas.RIGHT
            self.lastKeyDirection = self.keyDirection
            self.xTotalDistance = 0
            super().processKeyAI(Canvas.KEY_NUM1)
        else:
            super().processKeyAI(self.keyDirection)
    

    def setFiringDirectionForTargetIfInRange(self) -> Direction:
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        direction: Direction = directionFactory.NOT_BORDERED_WITH
        lastTrackingEvent: TrackingEvent = None
        lastTrackingLayerInterface: LayerInterface = None
        directionCompositeInterface: DirectionCompositeInterface = None
        size: int = self.trackingList.size()
        for index in range(0, size):
            lastTrackingEvent = self.trackingList.get(0)
            lastTrackingLayerInterface = lastTrackingEvent.getLayerInterface()
            x: int = lastTrackingLayerInterface.getXP()
            y: int = lastTrackingLayerInterface.getYP()
            yDistance: int = ownerLayerInterface.getYP() - y - ownerLayerInterface.getHeight()
            xDistance: int = ownerLayerInterface.getXP() - x - ownerLayerInterface.getWidth()
            absXDistance: int = abs(xDistance)
            absYDistance: int = abs(yDistance)
            if absYDistance <= 100:
                if absXDistance < int(self.getFiringDistance() / 2):
                    directionCompositeInterface = self.getOwnerLayerInterface()
                    if xDistance < 0 and directionCompositeInterface.getDirection() == directionFactory.RIGHT:
                        direction = directionFactory.RIGHT
                    elif xDistance > 0 and directionCompositeInterface.getDirection() == directionFactory.LEFT:
                        direction = directionFactory.LEFT
        return direction
    

    def disable(self) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onMovement(self, trackingEvent: TrackingEvent) -> None:
        self.trackingList.clear()
        self.trackingList.add(trackingEvent)
    

    def getFiringDistance(self) -> int:
        return self.firingDistance
    

    def setFiringDistance(self, firingDistance: int) -> None:
        self.firingDistance = firingDistance
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionCompositeInterface import DirectionCompositeInterface
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.LayerInterface import LayerInterface
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


