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
# package org.allbinary.logic.math

from __future__ import annotations



class BasicDecimal:
    ZERO_BIGDECIMAL: BasicDecimal = None

    def _init_fields(self) -> None:
        self.units: int = None
        self.scaled: int = 0
        self.factor: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_FACTOR
        self.factorValue: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_VALUE
    

    @staticmethod
    def createBigDecimal(bigDecimal: BasicDecimal) -> BasicDecimal:
        return BasicDecimal(bigDecimal.getUnscaled())
    

    def __init__(self, units: int) -> None:
        self._init_fields()
        self.units = units
        self.updateScaled()
    

    def setint(self, value: int) -> None:
        self.units = value
        self.updateScaled()
    

    def setlong(self, value: int) -> None:
        self.units = value
        self.updateScaled()
    

    def set(self, bigDecimal: BasicDecimal) -> None:
        self.units = bigDecimal.getUnscaled()
        self.updateScaled()
    

    def addint(self, value: int) -> None:
        self.units = self.units + value
        self.updateScaled()
    

    def addlong(self, value: int) -> None:
        self.units = self.units + value
        self.updateScaled()
    

    def add(self, bigDecimal: BasicDecimal) -> None:
        self.units = self.units + bigDecimal.getUnscaled()
        self.updateScaled()
    

    def subtractint(self, value: int) -> None:
        self.units = self.units - value
        self.updateScaled()
    

    def subtractlong(self, value: int) -> None:
        self.units = self.units - value
        self.updateScaled()
    

    def subtract(self, bigDecimal: BasicDecimal) -> None:
        self.units = self.units - bigDecimal.getUnscaled()
        self.updateScaled()
    

    def multiplyint(self, value: int) -> None:
        self.units = self.units * value
        self.updateScaled()
    

    def multiplylong(self, value: int) -> None:
        self.units = self.units * value
        self.updateScaled()
    

    def multiply(self, bigDecimal: BasicDecimal) -> None:
        self.units = self.units * bigDecimal.getUnscaled()
        self.updateScaled()
    

    def divideint(self, value: int) -> None:
        self.units = int(self.units / value)
        self.updateScaled()
    

    def dividelong(self, value: int) -> None:
        self.units = int(self.units / value)
        self.updateScaled()
    

    def divide(self, bigDecimal: BasicDecimal) -> None:
        self.units = self.units / bigDecimal.getUnscaled()
        self.updateScaled()
    

    def getUnscaled(self) -> int:
        return self.units
    

    def updateScaled(self) -> None:
        self.scaled = (int(self.units / self.factorValue))
    

    def getScaled(self) -> int:
        return self.scaled
    

    def toString(self) -> str:
        return str(self.units)

    def __str__(self) -> str:
        return self.toString()
    

    def getScaledFactor(self) -> int:
        return self.factor
    

    def getScaledFactorValue(self) -> int:
        return self.factorValue
from org.allbinary.logic.math.ScaleFactorFactory import ScaleFactorFactory


BasicDecimal.ZERO_BIGDECIMAL = BasicDecimal(0)

