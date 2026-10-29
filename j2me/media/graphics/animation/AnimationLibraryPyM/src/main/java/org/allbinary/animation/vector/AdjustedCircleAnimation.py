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
# package org.allbinary.animation.vector

from __future__ import annotations

from org.allbinary.animation.vector.CircleAnimation import CircleAnimation


class AdjustedCircleAnimation(CircleAnimation):

    def _init_fields(self) -> None:
        self.xAdjustment: int = 0
        self.yAdjustment: int = 0
    

    @staticmethod
    def createAnimation(width: int, height: int, xAdjustment: int, yAdjustment: int, basicColor: BasicColor) -> AdjustedCircleAnimation:
        adjustedCircleAnimation: AdjustedCircleAnimation = AdjustedCircleAnimation(width, height, basicColor)
        adjustedCircleAnimation.initXY(xAdjustment, yAdjustment)
        return adjustedCircleAnimation
    

    @staticmethod
    def createW(width: int, height: int, innerWidth: int, basicColor: BasicColor) -> AdjustedCircleAnimation:
        adjustedCircleAnimation: AdjustedCircleAnimation = AdjustedCircleAnimation(width, height, basicColor)
        adjustedCircleAnimation.init(innerWidth)
        return adjustedCircleAnimation
    

    def __init__(self, width: int, height: int, basicColor: BasicColor) -> None:
        super().__init__(width, height, basicColor)
        self._init_fields()
    

    def initXY(self, xAdjustment: int, yAdjustment: int) -> None:
        self.xAdjustment = xAdjustment
        self.yAdjustment = yAdjustment
    

    def init(self, innerWidth: int) -> None:
        if AndroidUtil.isAndroid():
            widthPortion: int = (int(((int(innerWidth / 3)) * 10) / 7))
            self.xAdjustment = -((self.width >> 1) - widthPortion)
            self.yAdjustment = self.xAdjustment
        else:
            self.xAdjustment = -((self.width >> 1) - innerWidth)
            self.yAdjustment = self.xAdjustment
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        graphics.drawArc(x + self.xAdjustment, y + self.yAdjustment, self.width, self.height, 0, self.TOTAL_ANGLE)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.graphics.color.BasicColor import BasicColor


