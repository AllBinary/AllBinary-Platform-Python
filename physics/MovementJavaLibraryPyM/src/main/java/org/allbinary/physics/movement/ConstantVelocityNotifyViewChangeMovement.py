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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.physics.movement.Movement import Movement


@java_inherited_overloads
class ConstantVelocityNotifyViewChangeMovement(Movement):
    def _java_defaults(self):
        vars(self).setdefault("basicVelocityProperties", None)
        vars(self).setdefault("speedBasicDecimal", None)
        vars(self).setdefault("axisMathVectorUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.math.vector.AxisMathVectorUtil import AxisMathVectorUtil
        if "basicVelocityProperties" not in vars(self): self.basicVelocityProperties: BasicVelocityProperties = None
        if "speedBasicDecimal" not in vars(self): self.speedBasicDecimal: BasicDecimal = None
        self.axisMathVectorUtil: AxisMathVectorUtil = AxisMathVectorUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
        from org.allbinary.logic.math.BasicDecimal import BasicDecimal
        super().__init__()
        __class__._init_fields(self)
        self.speedBasicDecimal = BasicDecimal.ZERO_BIGDECIMAL
        self.basicVelocityProperties = BasicVelocityProperties()
    

    def init(self, speedBasicDecimal: BasicDecimal, angle: int, otherAngle: int) -> None:
        from org.allbinary.logic.math.BasicDecimal import BasicDecimal
        from org.allbinary.math.AngleFactory import AngleFactory
        self.speedBasicDecimal = speedBasicDecimal
        angleFactory: AngleFactory = AngleFactory.getInstance()
        self.basicVelocityProperties.setVelocityWithBigDecimal(speedBasicDecimal, angleFactory.getAt(angle), angleFactory.getAt(otherAngle))
    

    def moveOutsideRadius(self, layer: AllBinaryLayer, radius: int, angle: int, otherAngle: int) -> None:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        scaleFactorValue: int = self.speedBasicDecimal.getScaledFactorValue()
        xVector: int = int((java_divide(self.axisMathVectorUtil.calculateX(radius, angle), scaleFactorValue)))
        yVector: int = int((java_divide(self.axisMathVectorUtil.calculateY(radius, angle), scaleFactorValue)))
        zVector: int = int((java_divide(self.axisMathVectorUtil.calculateZ(radius, otherAngle), scaleFactorValue)))
        layer.moveDXYZ(xVector, yVector, zVector)
    

    # throws Exception
    def process(self, layer: AllBinaryGameLayer) -> None:
        from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
        x: int = self.basicVelocityProperties.getVelocityXBasicDecimalP().getScaled()
        y: int = self.basicVelocityProperties.getVelocityYBasicDecimalP().getScaled()
        z: int = self.basicVelocityProperties.getVelocityZBasicDecimalP().getScaled()
        layer.moveDXYZ(x, y, z)
        if x != 0 or y != 0 or z != 0:
            layer.onViewPositionChangeEvent()
    

    def stop(self) -> None:
        self.basicVelocityProperties.zero()
# from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
# from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.math.BasicDecimal import BasicDecimal
# from org.allbinary.logic.math.vector.AxisMathVectorUtil import AxisMathVectorUtil
# from org.allbinary.math.AngleFactory import AngleFactory


