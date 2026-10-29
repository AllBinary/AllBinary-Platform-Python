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
# package org.allbinary.physics.movement

from __future__ import annotations

from org.allbinary.physics.movement.BasicConstantVelocityMovement import BasicConstantVelocityMovement


class CustomGravityConstantVelocityMovement(BasicConstantVelocityMovement):

    def _init_fields(self) -> None:
        self.customGravity: int = None
        self.gravityUtil: GravityUtil = GravityUtil.getInstance()
    

    def __init__(self, speedBasicDecimal: BasicDecimal, customGravity: int) -> None:
        super().__init__(speedBasicDecimal, VelocityProperties(int(speedBasicDecimal.getUnscaled()), int(speedBasicDecimal.getUnscaled())))
        self._init_fields()
        self.customGravity = customGravity
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        super().process(layer)
        self.gravityUtil.process(self.getVelocityProperties(), self.customGravity)
        velocityProperties: VelocityProperties = self.getVelocityProperties()
        velocityProperties.limitMaxYForwardVelocity()
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.acceleration.GravityUtil import GravityUtil
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


