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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.input.motion.button.TouchButton import TouchButton


class FullTouchButton(TouchButton):
    

    # throws Exception
    @staticmethod
    def createButton(touchButtonInput: TouchButtonInput, touchButtonResource: TouchButtonResource, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> FullTouchButton:
        return FullTouchButton(touchButtonInput, FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.RESOURCE).getInstance(0), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.HINT).getInstance(0), rawRectangle, cellPosition, xBorder, yBorder)
    

    def __init__(self, touchButtonInput: TouchButtonInput, animationInterface: Animation, hintAnimationInterface: Animation, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> None:
        super().__init__(touchButtonInput, animationInterface, hintAnimationInterface, rawRectangle, cellPosition, xBorder, yBorder)
    

    def updateRectangle(self) -> None:
        try:
            pointFactory: PointFactory = PointFactory.getInstance()
            x: int = self.rawRectangle.getWidth() * self.cellPositionP.getColumn()
            y: int = self.rawRectangle.getHeight() * self.cellPositionP.getRow()
            self.rectangleP = Rectangle(pointFactory.createXY(x, y), self.rawRectangle.getWidth() + (2 * self.xBorder), self.rawRectangle.getHeight() + (2 * self.yBorder))
            point: GPoint = self.rectangleP.getPoint()
            self.animationX = point.getX() + self.xBorder
            self.animationY = point.getY() + self.yBorder
            self.hintAnimationY = self.animationY - self.rectangleP.getHeight() >> 1
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateRectangle", e)
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle


