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


class BasicGravityConstantVelocityMovement(BasicConstantVelocityMovement):

    def _init_fields(self) -> None:
        self.gravityUtil: GravityUtil = GravityUtil.getInstance()
    

    def __init__(self, speedBasicDecimal: BasicDecimal) -> None:
        super().__init__(speedBasicDecimal, VelocityProperties(int(speedBasicDecimal.getUnscaled()), int(speedBasicDecimal.getUnscaled())))
        self._init_fields()
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        super().process(layer)
        self.gravityUtil.process(self.getVelocityProperties(), self.gravityUtil.GAME_GRAVITY_VELOCITY)
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.acceleration.GravityUtil import GravityUtil
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


