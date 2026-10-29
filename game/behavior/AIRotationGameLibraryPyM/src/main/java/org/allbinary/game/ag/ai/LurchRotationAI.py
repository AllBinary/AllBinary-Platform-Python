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

from org.allbinary.game.ag.ai.tactical.LurchAI import LurchAI


class LurchRotationAI(LurchAI):

    def _init_fields(self) -> None:
        self.rotationAnimationInterface: IndexedAnimation = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.rotationAnimationInterface = rotationAnimationInterfaceCompositeInterface.getRotationAnimationInterface()
        self.update()
    

    def reverse(self) -> None:
        super().reverse()
        self.update()
    

    def update(self) -> None:
        if self.currentRelativeAngle == 0:
            rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
            angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
            rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
            rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.RIGHT_FRAME))
        elif self.currentRelativeAngle == 180:
            rotationAnimationInterface: RotationAnimationInterface = self.rotationAnimationInterface
            angleIncrementInfo: AngleIncrementInfo = rotationAnimationInterface.getAngleInfoP().getAngleIncrementInfo()
            rotationAnimationInterfaceCompositeInterface: RotationAnimationInterfaceCompositeInterface = self.getOwnerLayerInterface()
            rotationAnimationInterfaceCompositeInterface.setFrame(int(angleIncrementInfo.LEFT_FRAME))
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface
from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo


