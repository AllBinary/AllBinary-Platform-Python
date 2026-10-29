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

from org.allbinary.ai.ArtificialIntelligenceTransitionInterface import ArtificialIntelligenceTransitionInterface
from org.allbinary.game.ai.BasicAI import BasicAI


class HorizontaRotationManeuverAI(BasicAI, ArtificialIntelligenceTransitionInterface):

    def _init_fields(self) -> None:
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(10, 2147483647)
        self.currentSpeedDivisor: int = 5
        self.rotationAnimationInterface: IndexedAnimation = None
        self.baseVelocityInterface: BasicVelocityProperties = None
        self.velocityInterface: VelocityInterface = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.rotationAnimationInterface = rotationAnimationInterfaceCompositeInterface.getRotationAnimationInterface()
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.baseVelocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
        self.velocityInterface = self.baseVelocityInterface
        rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
    

    def transition(self) -> None:
        rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
        rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
        allbinaryLayer: AllBinaryLayer = self.getOwnerLayerInterface()
        allbinaryLayer.setPosition(allbinaryLayer.getXP(), 1, allbinaryLayer.getZP())
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        rotationAnimationInterface: RotationAnimationInterface = (self.rotationAnimationInterface)
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        frame: int = self.rotationAnimationInterface.getFrame()
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        if ownerLayerInterface.getXP() - ownerLayerInterface.getWidth() <= 0 and frame == int(angleIncrementInfo.LEFT_FRAME):
            self.reverse()
            self.drop()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if ownerLayerInterface.getX2() + ownerLayerInterface.getWidth() > displayInfo.getLastWidth() and frame == int(angleIncrementInfo.RIGHT_FRAME):
            self.reverse()
            self.accelerate()
            self.drop()
        index: int = self.circularIndexUtil.getIndex()
        if index % self.currentSpeedDivisor == 0 and index % 2 == 0:
            super().processKeyAI(Canvas.UP)
            self.velocityInterface.limitMaxXYVelocity(self.velocityInterface.getMaxForwardVelocity() / self.currentSpeedDivisor)
        self.circularIndexUtil.next()
        if frame == int(angleIncrementInfo.LEFT_FRAME):
            super().processKeyAI(Canvas.KEY_NUM0)
        elif frame == int(angleIncrementInfo.RIGHT_FRAME):
            super().processKeyAI(Canvas.KEY_POUND)
    

    def reverse(self) -> None:
        rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        frame: int = self.rotationAnimationInterface.getFrame()
        if frame == int(angleIncrementInfo.LEFT_FRAME):
            rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
            rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
            self.baseVelocityInterface.zero()
        elif frame == int(angleIncrementInfo.RIGHT_FRAME):
            rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
            rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.LEFT_FRAME))
            self.baseVelocityInterface.zero()
    

    def accelerate(self) -> None:
        if self.currentSpeedDivisor > 1:
            self.currentSpeedDivisor -= 1
    

    def drop(self) -> None:
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        y: int = ownerLayerInterface.getYP()
        if ownerLayerInterface.getY2() + ownerLayerInterface.getHeight() > displayInfo.getLastHeight():
            y = 0
        else:
            y += ownerLayerInterface.getHeight() + 1
        ownerLayerInterface.setPosition(ownerLayerInterface.getXP(), y, ownerLayerInterface.getZP())
    

    def getId(self) -> int:
        return ArtificialIntelligence.AI_ID
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


