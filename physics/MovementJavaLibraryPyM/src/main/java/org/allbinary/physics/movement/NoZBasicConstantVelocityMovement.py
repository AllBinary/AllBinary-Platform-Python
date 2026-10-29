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

from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.physics.movement.Movement import Movement


class NoZBasicConstantVelocityMovement(Movement, VelocityInterfaceCompositeInterface):

    def _init_fields(self) -> None:
        self.velocityProperties: BasicVelocityProperties = None
        self.speedBasicDecimal: BasicDecimal = BasicDecimal.ZERO_BIGDECIMAL
        self.axisMathVectorUtil: AxisMathVectorUtil = AxisMathVectorUtil.getInstance()
    

    def __init__(self, basicDecimal: BasicDecimal, velocityProperties: BasicVelocityProperties) -> None:
        super().__init__()
        self._init_fields()
        self.setSpeedBasicDecimal(basicDecimal)
        self.velocityProperties = velocityProperties
    

    def init(self, speedBasicDecimal: BasicDecimal, angle: int, otherAngle: int) -> None:
        self.speedBasicDecimal = speedBasicDecimal
        angleFactory: AngleFactory = AngleFactory.getInstance()
        self.velocityProperties.setVelocityWithBigDecimal(speedBasicDecimal, angleFactory.getAt(angle), angleFactory.getAt(otherAngle))
    

    def moveOutsideRadius(self, layer: AllBinaryLayer, radius: int, angle: int, otherAngle: int) -> None:
        scaleFactorValue: int = self.speedBasicDecimal.getScaledFactorValue()
        xVector: int = int((self.axisMathVectorUtil.calculateX(radius, angle) / scaleFactorValue))
        yVector: int = int((self.axisMathVectorUtil.calculateY(radius, angle) / scaleFactorValue))
        layer.moveDXYZ(xVector, yVector, 0)
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        layer.moveDXYZ(self.velocityProperties.getVelocityXBasicDecimalP().getScaled(), self.velocityProperties.getVelocityYBasicDecimalP().getScaled(), 0)
    

    def toString(self) -> str:
        return str(self.velocityProperties)

    def __str__(self) -> str:
        return self.toString()
    

    def stop(self) -> None:
        self.velocityProperties.zero()
    

    def getVelocityProperties(self) -> BasicVelocityProperties:
        return self.velocityProperties
    

    def setVelocityProperties(self, velocityProperties: BasicVelocityProperties) -> None:
        self.velocityProperties = velocityProperties
    

    def setSpeedBasicDecimal(self, speedBasicDecimal: BasicDecimal) -> None:
        self.speedBasicDecimal = speedBasicDecimal
    

    def getSpeedBasicDecimal(self) -> BasicDecimal:
        return self.speedBasicDecimal
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.math.vector.AxisMathVectorUtil import AxisMathVectorUtil
from org.allbinary.math.AngleFactory import AngleFactory


