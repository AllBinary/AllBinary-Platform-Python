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

from org.allbinary.graphics.paint.Paintable import Paintable


class TouchButton(Paintable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.touchButtonInput: TouchButtonInput = None
        self.animationInterface: Animation = None
        self.hintAnimationInterface: Animation = None
        self.rawRectangle: Rectangle = None
        self.xBorder: int = None
        self.yBorder: int = None
        self.rectangleP: Rectangle = RectangleFactory.SINGLETON
        self.cellPositionP: CellPosition = None
        self.animationX: int = 0
        self.animationY: int = 0
        self.hintAnimationY: int = 0
    

    # throws Exception
    @staticmethod
    def createButton(touchButtonInput: TouchButtonInput, touchButtonResource: TouchButtonResource, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> TouchButton:
        return TouchButton(touchButtonInput, FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.RESOURCE).getInstance(0), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.HINT).getInstance(0), rawRectangle, cellPosition, xBorder, yBorder)
    

    def __init__(self, touchButtonInput: TouchButtonInput, animationInterface: Animation, hintAnimationInterface: Animation, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> None:
        super().__init__()
        self._init_fields()
        self.touchButtonInput = touchButtonInput
        self.animationInterface = animationInterface
        self.hintAnimationInterface = hintAnimationInterface
        self.rawRectangle = rawRectangle
        self.cellPositionP = cellPosition
        self.xBorder = xBorder
        self.yBorder = yBorder
        self.updateRectangle()
        self.logUtil.putF(str(StringMaker().append("Created: ").append(str(self))), self, self.commonStrings.CONSTRUCTOR)
    

    def paintHint(self, graphics: Graphics) -> None:
        self.hintAnimationInterface.paintXY(graphics, self.animationX, self.hintAnimationY)
    

    def paint(self, graphics: Graphics) -> None:
        self.animationInterface.paintXY(graphics, self.animationX, self.animationY)
    

    def updateRectangle(self) -> None:
        try:
            pointFactory: PointFactory = PointFactory.getInstance()
            x: int = self.rawRectangle.getWidth() * self.cellPositionP.getColumn()
            y: int = self.rawRectangle.getHeight() * self.cellPositionP.getRow()
            self.rectangleP = Rectangle(pointFactory.createXY(x + self.xBorder, y + self.yBorder), self.rawRectangle.getWidth(), self.rawRectangle.getHeight())
            point: GPoint = self.rectangleP.getPoint()
            self.animationX = point.getX()
            self.animationY = point.getY()
            self.hintAnimationY = self.animationY - 32
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateRectangle", e)
    

    def getCellPosition(self) -> CellPosition:
        return self.cellPositionP
    

    def getRectangle(self) -> Rectangle:
        return self.rectangleP
    

    def getTouchButtonInput(self) -> TouchButtonInput:
        return self.touchButtonInput
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append("TouchButton: ")
        stringBuffer.append(stringUtil.toString(self.getRectangle()))
        stringBuffer.append(" CellPosition: ")
        stringBuffer.append(stringUtil.toString(self.cellPositionP))
        stringBuffer.append(" xBorder: ")
        stringBuffer.appendint(self.xBorder)
        stringBuffer.append(" yBorder: ")
        stringBuffer.appendint(self.yBorder)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


