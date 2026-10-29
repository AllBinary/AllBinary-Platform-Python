# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.behavior.topview

from __future__ import annotations

from org.allbinary.game.layer.behavior.GameLayerBehavior import GameLayerBehavior


class TopViewGameLayerBehavior(GameLayerBehavior):

    def _init_fields(self) -> None:
        self.maxGravityActionIndex: int = None
        self.isJumpAction: bool = True
        self.isJumpOver: bool = False
        self.isFallingWithoutJumpAttempt: bool = False
        self.gravityActionIndex: int = 0
    

    def __init__(self, maxGravityActionIndex: int) -> None:
        super().__init__()
        self._init_fields()
        self.maxGravityActionIndex = maxGravityActionIndex
    

    def gravity(self) -> None:
        if self.gravityActionIndex == 0:
            self.gravityActionIndex += 1
            self.isFallingWithoutJumpAttempt = True
    

    def land(self, velocityProperties: VelocityProperties) -> None:
        velocityProperties.getVelocityYBasicDecimalP().setint(0)
        self.landReset()
    

    def landReset(self) -> None:
        self.gravityActionIndex = 0
        self.isFallingWithoutJumpAttempt = False
        self.isJumpAction = True
        self.isJumpOver = False
    

    def up(self, velocityProperties: VelocityProperties, acceleration: BasicAccelerationProperties, jumpBehavior: InitialJumpBehavior, accelerationMultiplier: int) -> None:
        if not self.isJumpOver:
            if self.gravityActionIndex < self.maxGravityActionIndex:
                acceleration2: int = -acceleration.getForward() * accelerationMultiplier
                velocityProperties.getVelocityYBasicDecimalP().addint(acceleration2)
                velocityProperties.limitXYToForwardAndReverseMaxVelocity()
                self.gravityActionIndex += 1
            else:
                pass
        else:
            pass
        if self.isJumpAction:
            jumpBehavior.process()
            self.isJumpAction = False
    

    def inputFrames(self, velocityProperties: VelocityProperties) -> None:
        if self.gravityActionIndex > 0 and velocityProperties.getVelocityYBasicDecimalP().getUnscaled() > 0:
            self.isJumpOver = True
from org.allbinary.game.physics.acceleration.BasicAccelerationProperties import BasicAccelerationProperties
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties


