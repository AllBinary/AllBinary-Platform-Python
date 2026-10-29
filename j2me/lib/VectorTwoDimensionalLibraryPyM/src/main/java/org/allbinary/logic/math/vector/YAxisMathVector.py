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
# package org.allbinary.logic.math.vector

from __future__ import annotations

from org.allbinary.logic.math.vector.MathVector import MathVector


class YAxisMathVector(MathVector):
    

    def __init__(self, magnitudeBasicDecimal: BasicDecimal, direction: int) -> None:
        super().__init__(magnitudeBasicDecimal, direction)
        self.calculate()
    

    def getResult(self) -> BasicDecimal:
        return self.resultBasicDecimal
    

    def calculate(self) -> None:
        from org.allbinary.logic.math.vector.YAxisMathVectorUtil import YAxisMathVectorUtil
        result: int = YAxisMathVectorUtil.calculate(self.getMagnitude().getUnscaled(), self.getDirection())
        self.resultBasicDecimal = BasicDecimal(result)
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


