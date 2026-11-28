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
        vars(self).setdefault("hintAnimationInterface", None)
        vars(self).setdefault("rawRectangle", None)
        vars(self).setdefault("xBorder", 0)
        vars(self).setdefault("yBorder", 0)
        vars(self).setdefault("rectangleP", None)
        vars(self).setdefault("cellPositionP", None)
        vars(self).setdefault("animationX", 0)
        vars(self).setdefault("animationY", 0)
        vars(self).setdefault("hintAnimationY", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.RectangleFactory import RectangleFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "touchButtonInput" not in vars(self): self.touchButtonInput: TouchButtonInput = None
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
        if "hintAnimationInterface" not in vars(self): self.hintAnimationInterface: Animation = None
        if "rawRectangle" not in vars(self): self.rawRectangle: Rectangle = None
        if "xBorder" not in vars(self): self.xBorder: int = 0
        if "yBorder" not in vars(self): self.yBorder: int = 0
        self.rectangleP: Rectangle = RectangleFactory.SINGLETON
        if "cellPositionP" not in vars(self): self.cellPositionP: CellPosition = None
        if "animationX" not in vars(self): self.animationX: int = 0
        if "animationY" not in vars(self): self.animationY: int = 0
        if "hintAnimationY" not in vars(self): self.hintAnimationY: int = 0
    

    # throws Exception
    @staticmethod
    def createButton(touchButtonInput: TouchButtonInput, touchButtonResource: TouchButtonResource, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> TouchButton:
        from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
        from org.allbinary.graphics.CellPosition import CellPosition
        from org.allbinary.graphics.Rectangle import Rectangle
        return TouchButton(touchButtonInput, FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.RESOURCE).getInstance(0), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(touchButtonResource.HINT).getInstance(0), rawRectangle, cellPosition, xBorder, yBorder)
    

    def __init__(self, touchButtonInput: TouchButtonInput, animationInterface: Animation, hintAnimationInterface: Animation, rawRectangle: Rectangle, cellPosition: CellPosition, xBorder: int, yBorder: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.graphics.CellPosition import CellPosition
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.logic.string.StringMaker import StringMaker
        super().__init__()
        __class__._init_fields(self)
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
        from javax.microedition.lcdui.Graphics import Graphics
        self.hintAnimationInterface.paintXY(graphics, self.animationX, self.hintAnimationY)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, self.animationX, self.animationY)
    

    def updateRectangle(self) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
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
        from org.allbinary.graphics.CellPosition import CellPosition
        return self.cellPositionP
    

    def getRectangle(self) -> Rectangle:
        from org.allbinary.graphics.Rectangle import Rectangle
        return self.rectangleP
    

    def getTouchButtonInput(self) -> TouchButtonInput:
        return self.touchButtonInput
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
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
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
# from org.allbinary.graphics.CellPosition import CellPosition
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.RectangleFactory import RectangleFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings


