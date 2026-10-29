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
        self.rawRectangle: Rectangle = None
        self.xBorder: int = None
        self.yBorder: int = None
        self.rectangle: Rectangle = RectangleFactory.SINGLETON
        self.cellPosition: CellPosition = None
        self.animationX: int = 0
        self.animationY: int = 0
    

    def __init__(self, touchButtonInput: TouchButtonInput, animationInterface: AnimationInterface, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> None:
        super().__init__()
        self._init_fields()
        self.touchButtonInput = touchButtonInput
        self.animationInterface = animationInterface
        self.rawRectangle = rawRectangle
        self.cellPosition = cellPosition
        self.xBorder = xBorder
        self.yBorder = yBorder
        self.updateRectangle()
        self.logUtil.putF(str(StringMaker().append("Created: ").append(str(self))), self, self.commonStrings.CONSTRUCTOR)
    

    def paint(self, graphics: Graphics) -> None:
        self.animationInterface.paintXY(graphics, self.animationX, self.animationY)
    

    def updateRectangle(self) -> None:
        try:
            x: int = self.rawRectangle.getWidth() * self.cellPosition.getColumn()
            y: int = self.rawRectangle.getHeight() * self.cellPosition.getRow()
            pointFactory: PointFactory = PointFactory.getInstance()
            self.rectangle = Rectangle(pointFactory.createXY(x + self.xBorder, y + self.yBorder), self.rawRectangle.getWidth(), self.rawRectangle.getHeight())
            point: GPoint = self.rectangle.getPoint()
            self.animationX = point.getX()
            self.animationY = point.getY()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateRectangle", e)
    

    def getCellPositionP(self) -> CellPosition:
        return self.cellPosition
    

    def getRectangleP(self) -> Rectangle:
        return self.rectangle
    

    def getTouchButtonInput(self) -> TouchButtonInput:
        return self.touchButtonInput
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append("TouchButton: ")
        stringBuffer.append(stringUtil.toString(self.rectangle))
        stringBuffer.append(" CellPosition: ")
        stringBuffer.append(stringUtil.toString(self.cellPosition))
        stringBuffer.append(" xBorder: ")
        stringBuffer.appendint(self.xBorder)
        stringBuffer.append(" yBorder: ")
        stringBuffer.appendint(self.yBorder)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationInterface import AnimationInterface
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


