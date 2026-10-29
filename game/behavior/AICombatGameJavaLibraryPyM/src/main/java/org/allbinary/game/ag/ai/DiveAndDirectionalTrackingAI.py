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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from org.allbinary.game.ai.BasicAI import BasicAI
from org.allbinary.game.combat.destroy.event.DestroyedEventListenerInterface import DestroyedEventListenerInterface
from org.allbinary.game.tracking.TrackingEventListenerInterface import TrackingEventListenerInterface


class DiveAndDirectionalTrackingAI(BasicAI, TrackingEventListenerInterface, DestroyedEventListenerInterface):

    def _init_fields(self) -> None:
        self.mathUtil: MathUtil = MathUtil.getInstance()
        self.directionFactory: DirectionFactory = DirectionFactory.getInstance()
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(500)
        self.list_: BasicArrayList = BasicArrayListD()
        self.directionalInterface: DirectionalInterface = None
        self.velocityInterface: BasicVelocityProperties = None
        self.directionToKeyMap: list[int] = [Canvas.LEFT, Canvas.DOWN, Canvas.UP, Canvas.RIGHT]
        self.initialDropped: bool = False
        self.diveP: bool = False
        self.directionOfTarget: Direction = Direction.getInstance(0)
        self.MIN_DISTANCE: int = 40
        self.lastTrackingLayerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
        self.artificialIntelligenceInterface: ArtificialIntelligenceInterface = None
        self.aiVistor: Visitor = None
        self.lastDirection: Direction = DirectionFactory.getInstance().NO_DIRECTION
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, artificialIntelligenceInterface: ArtificialIntelligenceInterface, gameInput: GameInput, visitor: Visitor) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.aiVistor = visitor
        self.artificialIntelligenceInterface = artificialIntelligenceInterface
        directionalCompositeInterface: DirectionalCompositeInterface = self.getOwnerLayerInterface()
        self.directionalInterface = directionalCompositeInterface.getDirectionalInterface()
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.velocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
        DestroyedEventHandler.getInstance().addListenerInterface(self)
        self.init()
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.isBeyondTarget():
            self.init()
            self.velocityInterface.zero()
        if not self.diveP:
            self.target(allBinaryLayerManager)
        else:
            self.dive()
            self.attack()
        self.list_.clear()
    

    def init(self) -> None:
        self.diveP = False
        self.directionOfTarget = DirectionFactory.getInstance().NOT_BORDERED_WITH
        TrackingEventHandler.getInstance().addListenerInterface(self)
    

    # throws Exception
    def target(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.list_.size() == 0:
            return
        lastTrackingEvent: TrackingEvent = self.list_.removeAt(0)
        self.lastTrackingLayerInterface = lastTrackingEvent.getLayerInterface()
        layerInterface: AllBinaryLayer = self.lastTrackingLayerInterface
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        if layerInterface.getGroupInterface() == ownerLayerInterface.getGroupInterface():
            return
        x: int = self.lastTrackingLayerInterface.getXP()
        y: int = self.lastTrackingLayerInterface.getYP()
        yDistance: int = ownerLayerInterface.getYP() - y - ownerLayerInterface.getHeight()
        xDistance: int = ownerLayerInterface.getXP() - x - ownerLayerInterface.getWidth()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if self.mathUtil.abs(yDistance) > self.mathUtil.abs(xDistance):
            if yDistance > self.MIN_DISTANCE:
                self.directionOfTarget = directionFactory.UP
            elif yDistance < -self.MIN_DISTANCE:
                self.directionOfTarget = directionFactory.DOWN
        else:
            if xDistance > self.MIN_DISTANCE:
                self.directionOfTarget = directionFactory.LEFT
            elif xDistance < -self.MIN_DISTANCE:
                self.directionOfTarget = directionFactory.RIGHT
        if not self.initialDropped and self.directionOfTarget != directionFactory.NOT_BORDERED_WITH:
            self.drop()
        if self.initialDropped:
            if self.directionOfTarget == directionFactory.UP or self.directionOfTarget == directionFactory.DOWN:
                self.verticalTargeting(x)
            elif self.directionOfTarget == directionFactory.LEFT or self.directionOfTarget == directionFactory.RIGHT:
                self.horizontalTargeting(y)
            else:
                self.artificialIntelligenceInterface.processAI(allBinaryLayerManager)
    

    # throws Exception
    def verticalTargeting(self, x: int) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        if ownerLayerInterface.getXP() < x:
            self.moveRight()
        if ownerLayerInterface.getXP() > x:
            self.moveLeft()
        if ownerLayerInterface.getXP() > x - 3 and ownerLayerInterface.getXP() < x + 3:
            self.setDive()
    

    # throws Exception
    def horizontalTargeting(self, y: int) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        if ownerLayerInterface.getYP() < y:
            self.moveDown()
        if ownerLayerInterface.getYP() > y:
            self.moveUp()
        if ownerLayerInterface.getYP() > y - 3 and ownerLayerInterface.getYP() < y + 3:
            self.setDive()
    

    def setDive(self) -> None:
        self.diveP = True
        self.velocityInterface.zero()
        TrackingEventHandler.getInstance().removeListener(self)
    

    # throws Exception
    def moveRight(self) -> None:
        self.setLastDirection(self.directionFactory.RIGHT)
        self.directionalInterface.setFrameByDirection(self.lastDirection)
        self.aiVistor.visit(self)
    

    # throws Exception
    def moveLeft(self) -> None:
        self.setLastDirection(self.directionFactory.LEFT)
        self.directionalInterface.setFrameByDirection(self.lastDirection)
        self.aiVistor.visit(self)
    

    # throws Exception
    def moveDown(self) -> None:
        self.setLastDirection(self.directionFactory.DOWN)
        self.directionalInterface.setFrameByDirection(self.lastDirection)
        self.aiVistor.visit(self)
    

    # throws Exception
    def moveUp(self) -> None:
        self.setLastDirection(self.directionFactory.UP)
        self.directionalInterface.setFrameByDirection(self.lastDirection)
        self.aiVistor.visit(self)
    

    # throws Exception
    def dive(self) -> None:
        self.directionalInterface.setFrameByDirection(self.directionOfTarget)
        self.aiVistor.visit(self)
    

    # throws Exception
    def attack(self) -> None:
        super().processKeyAI(Canvas.KEY_NUM1)
    

    # throws Exception
    def drop(self) -> None:
        if self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            self.initialDropped = True
            self.aiVistor.visit(self)
    

    def isBeyondTarget(self) -> bool:
        if self.directionOfTarget == self.directionFactory.DOWN:
            if self.getOwnerLayerInterface().getYP() > self.lastTrackingLayerInterface.getYP() + self.MIN_DISTANCE:
                return True
            else:
                return False
        elif self.directionOfTarget == self.directionFactory.UP:
            if self.getOwnerLayerInterface().getYP() < self.lastTrackingLayerInterface.getYP() + self.MIN_DISTANCE:
                return True
            else:
                return False
        elif self.directionOfTarget == self.directionFactory.RIGHT:
            if self.getOwnerLayerInterface().getXP() > self.lastTrackingLayerInterface.getXP() + self.MIN_DISTANCE:
                return True
            else:
                return False
        elif self.directionOfTarget == self.directionFactory.LEFT:
            if self.getOwnerLayerInterface().getXP() < self.lastTrackingLayerInterface.getXP() + self.MIN_DISTANCE:
                return True
            else:
                return False
        else:
            return False
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onMovement(self, trackingEvent: TrackingEvent) -> None:
        self.list_.add(trackingEvent)
    

    def onDestroyed(self, destroyedEvent: DestroyedEvent) -> None:
        if self.getOwnerLayerInterface() == destroyedEvent.getLayerInterface():
            TrackingEventHandler.getInstance().removeListener(self)
            DestroyedEventHandler.getInstance().removeListener(self)
    

    def setLastDirection(self, lastDirection: Direction) -> None:
        self.lastDirection = lastDirection
        value: int = self.getLastDirection().getValue()
        if value < 4:
            super().setLastKey(self.directionToKeyMap[value])
    

    def setLastKey(self, lastKey: int) -> None:
        super().setLastKey(lastKey)
        if self.getLastKey() == Canvas.LEFT:
            self.lastDirection = DirectionFactory.getInstance().LEFT
        elif self.getLastKey() == Canvas.DOWN:
            self.lastDirection = DirectionFactory.getInstance().DOWN
        elif self.getLastKey() == Canvas.UP:
            self.lastDirection = DirectionFactory.getInstance().UP
        elif self.getLastKey() == Canvas.RIGHT:
            self.lastDirection = DirectionFactory.getInstance().RIGHT
    

    def getLastDirection(self) -> Direction:
        return self.lastDirection
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        stringBuffer.append(" LastDirection: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getLastDirection()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.direction.DirectionalCompositeInterface import DirectionalCompositeInterface
from org.allbinary.direction.DirectionalInterface import DirectionalInterface
from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
from org.allbinary.game.combat.destroy.event.DestroyedEventHandler import DestroyedEventHandler
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


