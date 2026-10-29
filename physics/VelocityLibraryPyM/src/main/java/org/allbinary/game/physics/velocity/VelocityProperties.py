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
# package org.allbinary.game.physics.velocity

from __future__ import annotations

from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface


class VelocityProperties(BasicVelocityProperties, VelocityInterface):
    NULL_VELOCITY_PROPERTIES: VelocityProperties = None

    def _init_fields(self) -> None:
        self.maxForwardVelocity: int = 0
        self.maxReverseVelocity: int = 0
    

    def __init__(self, maxForwardVelocity: int, maxReverseVelocity: int) -> None:
        super().__init__()
        self._init_fields()
        self.setMaxForwardVelocity(maxForwardVelocity)
        self.setMaxReverseVelocity(maxReverseVelocity)
    

    def getMaxForwardVelocity(self) -> int:
        return self.maxForwardVelocity
    

    def setMaxForwardVelocity(self, maxForwardVelocity: int) -> None:
        self.maxForwardVelocity = maxForwardVelocity
    

    def getMaxReverseVelocity(self) -> int:
        return self.maxReverseVelocity
    

    def setMaxReverseVelocity(self, maxReverseVelocity: int) -> None:
        self.maxReverseVelocity = maxReverseVelocity
    

    def limitMaxXYForwardVelocity(self) -> None:
        self.limitMaxXYVelocity(self.getMaxForwardVelocity())
    

    def limitMaxXYReverseVelocity(self) -> None:
        self.limitMaxXYVelocity(self.getMaxReverseVelocity())
    

    def limitMaxYForwardVelocity(self) -> None:
        self.limitMaxYVelocity(self.getMaxForwardVelocity())
    

    def limitMaxYReverseVelocity(self) -> None:
        self.limitMaxYVelocity(self.getMaxReverseVelocity())
    

    def limitMaxXForwardVelocity(self) -> None:
        self.limitMaxXVelocity(self.getMaxForwardVelocity())
    

    def limitMaxXReverseVelocity(self) -> None:
        self.limitMaxXVelocity(self.getMaxReverseVelocity())
    

    def isOverXYMaxForwardVelocity(self) -> bool:
        return self.isOverXYMaxVelocity(self.getMaxForwardVelocity())
    

    def isOverXYMaxReverseVelocity(self) -> bool:
        return self.isOverXYMaxVelocity(self.getMaxReverseVelocity())
    

    def limitXYToForwardAndReverseMaxVelocity(self) -> None:
        self.limitMaxXYForwardVelocity()
        self.limitMaxXYReverseVelocity()
    

    def limitMaxXYVelocity(self, maxVelocity: int) -> None:
        self.limitMaxXVelocity(maxVelocity)
        self.limitMaxYVelocity(maxVelocity)
    

    def limitMaxPositiveYVelocity(self, maxVelocity: int) -> None:
        if self.velocityYBasicDecimal.getUnscaled() > maxVelocity:
            self.velocityYBasicDecimal.setint(maxVelocity)
    

    def limitMaxNegativeYVelocity(self, maxVelocity: int) -> None:
        if self.velocityYBasicDecimal.getUnscaled() < -maxVelocity:
            self.velocityYBasicDecimal.setint(-maxVelocity)
    

    def limitMaxYVelocity(self, maxVelocity: int) -> None:
        self.limitMaxPositiveYVelocity(maxVelocity)
        self.limitMaxNegativeYVelocity(maxVelocity)
    

    def limitMaxXVelocity(self, maxVelocity: int) -> None:
        if self.velocityXBasicDecimal.getUnscaled() > maxVelocity:
            self.velocityXBasicDecimal.setint(maxVelocity)
        if self.velocityXBasicDecimal.getUnscaled() < -maxVelocity:
            self.velocityXBasicDecimal.setint(-maxVelocity)
    

    def isOverXYMaxVelocity(self, maxVelocity: int) -> bool:
        if self.velocityXBasicDecimal.getUnscaled() > maxVelocity:
            return True
        if self.velocityXBasicDecimal.getUnscaled() < -maxVelocity:
            return True
        if self.velocityYBasicDecimal.getUnscaled() > maxVelocity:
            return True
        if self.velocityYBasicDecimal.getUnscaled() < -maxVelocity:
            return True
        return False
    

    def setVelocityi(self, magnitude: int, angle: int, otherAngle: int) -> None:
        super().setVelocityi(magnitude, angle, otherAngle)
        self.limitXYToForwardAndReverseMaxVelocity()
    

    def addVelocityi(self, magnitude: int, angle: int, otherAngle: int) -> None:
        super().addVelocityi(magnitude, angle, otherAngle)
        self.limitXYToForwardAndReverseMaxVelocity()


VelocityProperties.NULL_VELOCITY_PROPERTIES = VelocityProperties(0, 0)

