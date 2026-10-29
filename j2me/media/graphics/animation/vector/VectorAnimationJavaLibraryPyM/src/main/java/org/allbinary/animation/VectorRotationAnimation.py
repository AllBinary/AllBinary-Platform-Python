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

from org.allbinary.animation.VectorBaseRotationAnimation import VectorBaseRotationAnimation


class VectorRotationAnimation(VectorBaseRotationAnimation):
    

    def __init__(self, currentPoints: list[list[list[int]]], basicColor: BasicColor, animationBehavior: AnimationBehavior) -> None:
        super().__init__(AngleInfo.getInstance(((int((AngleFactory.getInstance().TOTAL_ANGLE / len(currentPoints))) + 32768) % 65536 - 32768)), currentPoints, basicColor, animationBehavior)
        self.angleInfo.adjustAngle(self.getFrame())
    

    def setFrameByDirection(self, direction: Direction) -> None:
        angle: Angle = self.directionUtil.getFrameAngle(direction)
        self.adjustFrameToAngle(angle)
    

    def setFrameToAngle(self, angle: Angle) -> None:
        self.adjustFrameToAngle(angle)
    

    def setFrame(self, index: int) -> None:
        super().setFrame(index)
        self.angleInfo.adjustAngle(self.getFrame())
    

    def adjustFrame(self, newAngle: int) -> None:
        self.setFrame(self.frameUtil.getFrameForAngle(newAngle, int(self.angleInfo.getAngleIncrementInfo().getAngleIncrement())))
    

    def adjustFrameToAngle(self, newAngle: Angle) -> None:
        self.adjustFrame(newAngle.getValue())
from org.allbinary.direction.Direction import Direction
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo


