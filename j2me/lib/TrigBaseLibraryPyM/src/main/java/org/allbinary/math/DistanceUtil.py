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
# package org.allbinary.math

from __future__ import annotations



class DistanceUtil:
    instance: DistanceUtil = None

    def _init_fields(self) -> None:
        self.mathUtil: MathUtil = MathUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> DistanceUtil:
        return DistanceUtil.instance
    

    def getDistance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        dx: int = x1 - x2
        dy: int = y1 - y2
        return int(self.mathUtil.sqrt((dx * dx) + (dy * dy)))
from org.allbinary.logic.math.MathUtil import MathUtil


DistanceUtil.instance = DistanceUtil()

