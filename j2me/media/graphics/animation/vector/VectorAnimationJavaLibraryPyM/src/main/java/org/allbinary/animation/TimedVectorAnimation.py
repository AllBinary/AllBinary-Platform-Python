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
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.animation.VectorAnimation import VectorAnimation


class TimedVectorAnimation(VectorAnimation):

    def _init_fields(self) -> None:
        self.timeElapsedHelper: TimeDelayHelper = TimeDelayHelper(200)
    

    def __init__(self, currentPoints: list[list[list[int]]], basicColor: BasicColor, animationBehavior: AnimationBehavior) -> None:
        super().__init__(currentPoints, basicColor, animationBehavior)
        self._init_fields()
    

    def nextFrame(self) -> None:
        if self.timeElapsedHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            super().nextFrame()
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


