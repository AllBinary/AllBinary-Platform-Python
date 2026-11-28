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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.physics.movement.BasicConstantVelocityMovement import BasicConstantVelocityMovement


@java_inherited_overloads
class OscillateVelocityMovement(BasicConstantVelocityMovement):
    def _java_defaults(self):
        vars(self).setdefault("oscillateMin", 0)
        vars(self).setdefault("oscillateMax", 0)
        vars(self).setdefault("oscillate", 0)
        vars(self).setdefault("oscillatePositive", False)

    def _init_fields(self) -> None:
        if "oscillateMin" not in vars(self): self.oscillateMin: int = 0
        if "oscillateMax" not in vars(self): self.oscillateMax: int = 0
        if "oscillate" not in vars(self): self.oscillate: int = 0
        if "oscillatePositive" not in vars(self): self.oscillatePositive: bool = False
    

    def __init__(self, speedBasicDecimal: BasicDecimal, oscillateMin: int, oscillateMax: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
        from org.allbinary.logic.math.BasicDecimal import BasicDecimal
        super().__init__(speedBasicDecimal, VelocityProperties(int(speedBasicDecimal.getUnscaled()), int(speedBasicDecimal.getUnscaled())))
        __class__._init_fields(self)
        self.oscillateMin = oscillateMin
        self.oscillateMax = oscillateMax
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
        java_super_call(super(), "process", layer)
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
# from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
# from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
# from org.allbinary.logic.math.BasicDecimal import BasicDecimal


