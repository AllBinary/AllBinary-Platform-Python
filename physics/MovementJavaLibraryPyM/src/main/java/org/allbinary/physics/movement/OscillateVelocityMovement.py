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


class OscillateVelocityMovement(BasicConstantVelocityMovement):

    def _init_fields(self) -> None:
        self.oscillateMin: int = None
        self.oscillateMax: int = None
        self.oscillate: int = 0
        self.oscillatePositive: bool = False
    

    def __init__(self, speedBasicDecimal: BasicDecimal, oscillateMin: int, oscillateMax: int) -> None:
        super().__init__(speedBasicDecimal, VelocityProperties(int(speedBasicDecimal.getUnscaled()), int(speedBasicDecimal.getUnscaled())))
        self._init_fields()
        self.oscillateMin = oscillateMin
        self.oscillateMax = oscillateMax
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        super().process(layer)
        if self.oscillate < self.oscillateMin:
            self.oscillatePositive = True
        elif self.oscillate > self.oscillateMax:
            self.oscillatePositive = False
        if self.oscillatePositive:
            self.oscillate += 1
            self.getVelocityProperties().getVelocityXBasicDecimalP().addint(2000)
        else:
            self.oscillate -= 1
            self.getVelocityProperties().getVelocityXBasicDecimalP().subtractint(2000)
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


