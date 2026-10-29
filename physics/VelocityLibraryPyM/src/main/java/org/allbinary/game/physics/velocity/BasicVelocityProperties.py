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

from org.allbinary.game.physics.velocity.BasicVelocityInterface import BasicVelocityInterface


class BasicVelocityProperties(BasicVelocityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.velocityXBasicDecimal: BasicDecimal = None
        self.velocityYBasicDecimal: BasicDecimal = None
        self.velocityZBasicDecimal: BasicDecimal = None
        self.axisMathVectorUtil: AxisMathVectorUtil = AxisMathVectorUtil.getInstance()
        self.directionUtil: DirectionUtil = DirectionUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
        self.velocityXBasicDecimal = BasicDecimal(0)
        self.velocityYBasicDecimal = BasicDecimal(0)
        self.velocityZBasicDecimal = BasicDecimal(0)
    

    def zero(self) -> None:
        self.velocityXBasicDecimal.setint(0)
        self.velocityYBasicDecimal.setint(0)
        self.velocityZBasicDecimal.setint(0)
    

    def getVelocityXBasicDecimalP(self) -> BasicDecimal:
        return self.velocityXBasicDecimal
    

    def getVelocityYBasicDecimalP(self) -> BasicDecimal:
        return self.velocityYBasicDecimal
    

    def getVelocityZBasicDecimalP(self) -> BasicDecimal:
        return self.velocityZBasicDecimal
    

    def setVelocityWithBigDecimalAndDirection(self, magnitudeBasicDecimal: BasicDecimal, direction: Direction, otherDirection: Direction) -> None:
        angle: Angle = self.directionUtil.getAngle(direction)
        otherAngle: Angle = self.directionUtil.getAngle(otherDirection)
        self.setVelocityWithBigDecimal(magnitudeBasicDecimal, angle, otherAngle)
    

    def setVelocityWithDirection(self, magnitude: int, direction: Direction, otherDirection: Direction) -> None:
        angle: Angle = self.directionUtil.getAngle(direction)
        otherAngle: Angle = self.directionUtil.getAngle(otherDirection)
        self.setVelocity(magnitude, angle, otherAngle)
    

    def addVelocityWithBigDecimalAndDirection(self, magnitudeBasicDecimal: BasicDecimal, direction: Direction, otherDirection: Direction) -> None:
        angle: Angle = self.directionUtil.getAngle(direction)
        otherAngle: Angle = self.directionUtil.getAngle(otherDirection)
        self.addVelocityWithBigDecimal(magnitudeBasicDecimal, angle, otherAngle)
    

    def addVelocityWithDirection(self, magnitude: int, direction: Direction, otherDirection: Direction) -> None:
        angle: Angle = self.directionUtil.getAngle(direction)
        otherAngle: Angle = self.directionUtil.getAngle(otherDirection)
        self.addVelocity(magnitude, angle, otherAngle)
    

    def setVelocityWithBigDecimal(self, magnitudeBasicDecimal: BasicDecimal, angle: Angle, otherAngle: Angle) -> None:
        magnitude: int = magnitudeBasicDecimal.getUnscaled()
        self.setVelocity(magnitude, angle, otherAngle)
    

    def addVelocityWithBigDecimal(self, magnitudeBasicDecimal: BasicDecimal, angle: Angle, otherAngle: Angle) -> None:
        magnitude: int = magnitudeBasicDecimal.getUnscaled()
        self.addVelocity(magnitude, angle, otherAngle)
    

    def setVelocity(self, magnitude: int, angle: Angle, otherAngle: Angle) -> None:
        self.setVelocityi(magnitude, int(angle.getValue()), int(otherAngle.getValue()))
    

    def addVelocity(self, magnitude: int, angle: Angle, otherAngle: Angle) -> None:
        self.addVelocityi(magnitude, int(angle.getValue()), int(otherAngle.getValue()))
    

    def setVelocityi(self, magnitude: int, angle: int, otherAngle: int) -> None:
        xVector: int = (self.axisMathVectorUtil.calculateX(magnitude, angle) / self.velocityXBasicDecimal.getScaledFactorValue())
        yVector: int = (self.axisMathVectorUtil.calculateY(magnitude, angle) / self.velocityYBasicDecimal.getScaledFactorValue())
        zVector: int = (self.axisMathVectorUtil.calculateZ(magnitude, otherAngle) / self.velocityZBasicDecimal.getScaledFactorValue())
        self.velocityXBasicDecimal.setlong(xVector)
        self.velocityYBasicDecimal.setlong(yVector)
        self.velocityZBasicDecimal.setlong(zVector)
    

    def addVelocityi(self, magnitude: int, angle: int, otherAngle: int) -> None:
        xVector: int = (self.axisMathVectorUtil.calculateX(magnitude, angle) / self.velocityXBasicDecimal.getScaledFactorValue())
        yVector: int = (self.axisMathVectorUtil.calculateY(magnitude, angle) / self.velocityYBasicDecimal.getScaledFactorValue())
        zVector: int = (self.axisMathVectorUtil.calculateZ(magnitude, otherAngle) / self.velocityZBasicDecimal.getScaledFactorValue())
        self.velocityXBasicDecimal.addlong(xVector)
        self.velocityYBasicDecimal.addlong(yVector)
        self.velocityZBasicDecimal.addlong(zVector)
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append("Velocity ")
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.append(stringUtil.toString(self.velocityXBasicDecimal))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.append(stringUtil.toString(self.velocityYBasicDecimal))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.append(stringUtil.toString(self.velocityZBasicDecimal))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionUtil import DirectionUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.math.vector.AxisMathVectorUtil import AxisMathVectorUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.Angle import Angle
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonSeps import CommonSeps


