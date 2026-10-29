# Generated Code Do Not Modify
# package org.allbinary.physics.movement

from __future__ import annotations

from org.allbinary.physics.movement.BasicConstantVelocityMovement import BasicConstantVelocityMovement


class PreciseConstantVelocityMovement(BasicConstantVelocityMovement):

    def _init_fields(self) -> None:
        self.accumulatedX: int = 0
        self.accumulatedY: int = 0
        self.accumulatedZ: int = 0
        self.factorValue: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_VALUE
    

    def __init__(self, basicDecimal: BasicDecimal, velocityProperties: BasicVelocityProperties) -> None:
        super().__init__(basicDecimal, velocityProperties)
        self._init_fields()
    

    def init(self, speedBasicDecimal: BasicDecimal, angle: int, otherAngle: int) -> None:
        pass
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        mathUtil: MathUtil = MathUtil.getInstance()
        velocityProperties: BasicVelocityProperties = self.getVelocityProperties()
        self.accumulatedX = int((self.accumulatedX + velocityProperties.getVelocityXBasicDecimalP().getUnscaled()))
        self.accumulatedY = int((self.accumulatedY + velocityProperties.getVelocityYBasicDecimalP().getUnscaled()))
        self.accumulatedZ = int((self.accumulatedZ + velocityProperties.getVelocityZBasicDecimalP().getUnscaled()))
        layer.moveDXYZ(int(self.accumulatedX / self.factorValue), int(self.accumulatedY / self.factorValue), int(self.accumulatedZ / self.factorValue))
        if mathUtil.abs(self.accumulatedX) > self.factorValue:
            self.accumulatedX = 0
        if mathUtil.abs(self.accumulatedY) > self.factorValue:
            self.accumulatedY = 0
        if mathUtil.abs(self.accumulatedZ) > self.factorValue:
            self.accumulatedZ = 0
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.logic.math.ScaleFactorFactory import ScaleFactorFactory


