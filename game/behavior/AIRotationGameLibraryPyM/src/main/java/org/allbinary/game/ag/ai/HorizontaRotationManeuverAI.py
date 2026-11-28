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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.ai.ArtificialIntelligenceTransitionInterface import ArtificialIntelligenceTransitionInterface
from org.allbinary.game.ai.BasicAI import BasicAI


@java_inherited_overloads
class HorizontaRotationManeuverAI(*java_bases(BasicAI, ArtificialIntelligenceTransitionInterface)):
    def _java_defaults(self):
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("currentSpeedDivisor", 0)
        vars(self).setdefault("rotationAnimationInterface", None)
        vars(self).setdefault("baseVelocityInterface", None)
        vars(self).setdefault("velocityInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(10, 2147483647)
        self.currentSpeedDivisor: int = 5
        if "rotationAnimationInterface" not in vars(self): self.rotationAnimationInterface: IndexedAnimation = None
        if "baseVelocityInterface" not in vars(self): self.baseVelocityInterface: BasicVelocityProperties = None
        if "velocityInterface" not in vars(self): self.velocityInterface: VelocityInterface = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
        from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface
        from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
        super().__init__(ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.rotationAnimationInterface = rotationAnimationInterfaceCompositeInterface.getRotationAnimationInterface()
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.baseVelocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
        self.velocityInterface = self.baseVelocityInterface
        rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
    

    def transition(self) -> None:
        from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
        from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
        rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
        angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
        rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
        rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
        allbinaryLayer: AllBinaryLayer = self.getOwnerLayerInterface()
        allbinaryLayer.setPosition(allbinaryLayer.getXP(), 1, allbinaryLayer.getZP())
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
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
            java_super_call(super(), "processKeyAI", Canvas.UP)
            self.velocityInterface.limitMaxXYVelocity(java_divide(self.velocityInterface.getMaxForwardVelocity(), self.currentSpeedDivisor)
            )
        self.circularIndexUtil.next()
        if frame == int(angleIncrementInfo.LEFT_FRAME):
            java_super_call(super(), "processKeyAI", Canvas.KEY_NUM0)
        elif frame == int(angleIncrementInfo.RIGHT_FRAME):
            java_super_call(super(), "processKeyAI", Canvas.KEY_POUND)
    

    def reverse(self) -> None:
        from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
        from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
        from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
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
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        y: int = ownerLayerInterface.getYP()
        if ownerLayerInterface.getY2() + ownerLayerInterface.getHeight() > displayInfo.getLastHeight():
            y = 0
        else:
            y += ownerLayerInterface.getHeight() + 1
        ownerLayerInterface.setPosition(ownerLayerInterface.getXP(), y, ownerLayerInterface.getZP())
    

    def getId(self) -> int:
        from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
        return ArtificialIntelligence.AI_ID
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
# from org.allbinary.animation.IndexedAnimation import IndexedAnimation
# from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
# from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
# from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface
# from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


