# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


@java_inherited_overloads
class SelectionHudPaintable(*java_bases(InitUpdatePaintable, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("y", 0)
        vars(self).setdefault("primitiveLongUtil", None)
        vars(self).setdefault("updateMyFontProcessor", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("x", 0)
        vars(self).setdefault("textX", 0)
        vars(self).setdefault("imageX", 0)
        vars(self).setdefault("basicColor", None)
        vars(self).setdefault("color", 0)
        vars(self).setdefault("width", 0)
        vars(self).setdefault("height", 0)
        vars(self).setdefault("name", None)
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("backgroundColor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        self.y: int = CommonButtons.getInstance().STANDARD_BUTTON_SIZE + 17
        if "primitiveLongUtil" not in vars(self): self.primitiveLongUtil: PrimitiveLongUtil = None
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        if "x" not in vars(self): self.x: int = 0
        if "textX" not in vars(self): self.textX: int = 0
        if "imageX" not in vars(self): self.imageX: int = 0
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        if "color" not in vars(self): self.color: int = 0
        if "width" not in vars(self): self.width: int = 0
        if "height" not in vars(self): self.height: int = 0
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.backgroundColor: int = int(BasicColorFactory.getInstance().GREY)
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        super().__init__()
        __class__._init_fields(self)
        self.update()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(10000)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        commonButtons: CommonButtons = CommonButtons.getInstance()
        font: Font = graphics.getFont()
        self.setHeight(commonButtons.STANDARD_BUTTON_SIZE + font.getHeight())
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def update(self) -> None:
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
        commonButtons: CommonButtons = CommonButtons.getInstance()
        touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
        displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.x = commonButtons.STANDARD_BUTTON_SIZE + touchButtonLocationHelper.getColumnsRemainderHalf()
        self.textX = self.getX() + 4
        self.width = displayInfoSingleton.getLastWidth() - self.getX() * 2
        self.imageX = self.getWidth() + touchButtonLocationHelper.getColumnsRemainderHalf() - 10
        self.myFontProcessor = self.updateMyFontProcessor
    

    def updateSelectionInfo(self) -> None:
        pass
    

    def updateInfo(self) -> None:
        pass
    

    def getPrimitiveLongUtil(self) -> PrimitiveLongUtil:
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        return self.primitiveLongUtil
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        from org.allbinary.animation.Animation import Animation
        self.animationInterface = animationInterface
    

    def getAnimationInterface(self) -> Animation:
        from org.allbinary.animation.Animation import Animation
        return self.animationInterface
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.basicColor = basicColor
        self.setColor(int(basicColor))
    

    def getBasicColorP(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return self.basicColor
    

    def setColor(self, color: int) -> None:
        self.color = color
    

    def getColor(self) -> int:
        return self.color
    

    def getWidth(self) -> int:
        return self.width
    

    def setHeight(self, height: int) -> None:
        self.height = height
    

    def getHeight(self) -> int:
        return self.height
    

    def getX(self) -> int:
        return self.x
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        graphics.setColor(self.backgroundColor)
        graphics.drawRect(self.getX(), self.y, self.getWidth(), self.getHeight())
        graphics.setColor(self.getColor())
        graphics.drawString(self.getName(), self.textX, self.y, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.input.motion.button.CommonButtons import CommonButtons
# from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
# from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


