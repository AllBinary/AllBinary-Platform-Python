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

from org.allbinary.logic.math.vector.MathVectorInterface import MathVectorInterface


class MathVector(MathVectorInterface):

    def _init_fields(self) -> None:
        self.magnitudeBasicDecimal: BasicDecimal = None
        self.direction: int = None
        self.resultBasicDecimal: BasicDecimal = None
    

    def __init__(self, magnitudeBasicDecimal: BasicDecimal, direction: int) -> None:
        self._init_fields()
        self.magnitudeBasicDecimal = magnitudeBasicDecimal
        self.direction = direction
    

    def getMagnitude(self) -> BasicDecimal:
        return self.magnitudeBasicDecimal
    

    def getDirection(self) -> int:
        return self.direction
    

    def getResult(self) -> BasicDecimal:
        return self.resultBasicDecimal
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


