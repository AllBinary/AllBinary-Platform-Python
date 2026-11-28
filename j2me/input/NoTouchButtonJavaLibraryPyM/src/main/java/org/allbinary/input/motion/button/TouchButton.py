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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class TouchButton(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("touchButtonInput", None)
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("rawRectangle", None)
        vars(self).setdefault("xBorder", 0)
        vars(self).setdefault("yBorder", 0)
        vars(self).setdefault("rectangle", None)
        vars(self).setdefault("cellPosition", None)
        vars(self).setdefault("animationX", 0)
        vars(self).setdefault("animationY", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.RectangleFactory import RectangleFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "touchButtonInput" not in vars(self): self.touchButtonInput: TouchButtonInput = None
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
        if "rawRectangle" not in vars(self): self.rawRectangle: Rectangle = None
        if "xBorder" not in vars(self): self.xBorder: int = 0
        if "yBorder" not in vars(self): self.yBorder: int = 0
        self.rectangle: Rectangle = RectangleFactory.SINGLETON
        if "cellPosition" not in vars(self): self.cellPosition: CellPosition = None
        if "animationX" not in vars(self): self.animationX: int = 0
        if "animationY" not in vars(self): self.animationY: int = 0
    

    def __init__(self, touchButtonInput: TouchButtonInput, animationInterface: AnimationInterface, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.animation.AnimationInterface import AnimationInterface
        from org.allbinary.graphics.CellPosition import CellPosition
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.logic.string.StringMaker import StringMaker
        super().__init__()
        __class__._init_fields(self)
        self.touchButtonInput = touchButtonInput
        self.animationInterface = animationInterface
        self.rawRectangle = rawRectangle
        self.cellPosition = cellPosition
        self.xBorder = xBorder
        self.yBorder = yBorder
        self.updateRectangle()
        self.logUtil.putF(str(StringMaker().append("Created: ").append(str(self))), self, self.commonStrings.CONSTRUCTOR)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, self.animationX, self.animationY)
    

    def updateRectangle(self) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
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
        from org.allbinary.graphics.CellPosition import CellPosition
        return self.cellPosition
    

    def getRectangleP(self) -> Rectangle:
        from org.allbinary.graphics.Rectangle import Rectangle
        return self.rectangle
    

    def getTouchButtonInput(self) -> TouchButtonInput:
        return self.touchButtonInput
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
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
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationInterface import AnimationInterface
# from org.allbinary.graphics.CellPosition import CellPosition
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.RectangleFactory import RectangleFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings


