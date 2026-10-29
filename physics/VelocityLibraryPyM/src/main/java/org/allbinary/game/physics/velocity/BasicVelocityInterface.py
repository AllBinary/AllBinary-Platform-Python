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



# Java interface
class BasicVelocityInterface:
    

    def getVelocityXBasicDecimalP(self) -> BasicDecimal:
        raise NotImplementedError()
    

    def getVelocityYBasicDecimalP(self) -> BasicDecimal:
        raise NotImplementedError()
    

    def zero(self) -> None:
        raise NotImplementedError()
    

    def setVelocityWithBigDecimalAndDirection(self, magnitudeBasicDecimal: BasicDecimal, direction: Direction, otherDirection: Direction) -> None:
        raise NotImplementedError()
    

    def addVelocityWithBigDecimalAndDirection(self, magnitudeBasicDecimal: BasicDecimal, direction: Direction, otherDirection: Direction) -> None:
        raise NotImplementedError()
    

    def setVelocityWithDirection(self, magnitude: int, direction: Direction, otherDirection: Direction) -> None:
        raise NotImplementedError()
    

    def addVelocityWithDirection(self, magnitude: int, direction: Direction, otherDirection: Direction) -> None:
        raise NotImplementedError()
    

    def setVelocityWithBigDecimal(self, magnitudeBasicDecimal: BasicDecimal, angle: Angle, otherAngle: Angle) -> None:
        raise NotImplementedError()
    

    def addVelocityWithBigDecimal(self, magnitudeBasicDecimal: BasicDecimal, angle: Angle, otherAngle: Angle) -> None:
        raise NotImplementedError()
    

    def setVelocity(self, magnitude: int, angle: Angle, otherAngle: Angle) -> None:
        raise NotImplementedError()
    

    def addVelocity(self, magnitude: int, angle: Angle, otherAngle: Angle) -> None:
        raise NotImplementedError()
    

    def addVelocityi(self, magnitude: int, angle: int, otherAngle: int) -> None:
        raise NotImplementedError()
from org.allbinary.direction.Direction import Direction
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.math.Angle import Angle


