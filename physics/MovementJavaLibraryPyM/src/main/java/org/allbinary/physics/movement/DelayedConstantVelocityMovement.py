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


class DelayedConstantVelocityMovement(BasicConstantVelocityMovement):

    def _init_fields(self) -> None:
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(60)
    

    def __init__(self, basicDecimal: BasicDecimal, velocityProperties: BasicVelocityProperties) -> None:
        super().__init__(basicDecimal, velocityProperties)
        self._init_fields()
    

    def init(self, speedBasicDecimal: BasicDecimal, angle: int, otherAngle: int) -> None:
        pass
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            super().process(layer)
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


