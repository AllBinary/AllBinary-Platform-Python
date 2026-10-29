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



class AngleIncrementInfoFactory:
    instance: AngleIncrementInfoFactory = None

    def _init_fields(self) -> None:
        self.angleIncrementInfo: list[AngleIncrementInfo] = [None] * (int(AngleFactory.getInstance().TOTAL_ANGLE))

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AngleIncrementInfoFactory:
        return AngleIncrementInfoFactory.instance
    

    def getAt(self, angleIncrement: int) -> AngleIncrementInfo:
        from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
        halfAngleIncrement: int = (angleIncrement >> 1)
        angleIncrementInfo: AngleIncrementInfo = None
        angleIncrementInfoCanBeNull: AngleIncrementInfo = self.angleIncrementInfo[halfAngleIncrement]
        if angleIncrementInfoCanBeNull is None:
            angleIncrementInfo = AngleIncrementInfo(angleIncrement)
            self.angleIncrementInfo[halfAngleIncrement] = angleIncrementInfo
            return angleIncrementInfo
        else:
            angleIncrementInfo = angleIncrementInfoCanBeNull
        return angleIncrementInfo
from org.allbinary.math.AngleFactory import AngleFactory


AngleIncrementInfoFactory.instance = AngleIncrementInfoFactory()

