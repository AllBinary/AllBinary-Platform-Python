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

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


class SelectionHudPaintable(InitUpdatePaintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.y: int = CommonButtons.getInstance().STANDARD_BUTTON_SIZE + 17
        self.primitiveLongUtil: PrimitiveLongUtil = None
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.x: int = 0
        self.textX: int = 0
        self.imageX: int = 0
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        self.color: int = 0
        self.width: int = 0
        self.height: int = 0
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.backgroundColor: int = int(BasicColorFactory.getInstance().GREY)
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.update()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(10000)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        commonButtons: CommonButtons = CommonButtons.getInstance()
        font: Font = graphics.getFont()
        self.setHeight(commonButtons.STANDARD_BUTTON_SIZE + font.getHeight())
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def update(self) -> None:
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
        return self.primitiveLongUtil
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        self.animationInterface = animationInterface
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
        self.setColor(int(basicColor))
    

    def getBasicColorP(self) -> BasicColor:
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
        self.myFontProcessor.process(graphics)
        graphics.setColor(self.backgroundColor)
        graphics.drawRect(self.getX(), self.y, self.getWidth(), self.getHeight())
        graphics.setColor(self.getColor())
        graphics.drawString(self.getName(), self.textX, self.y, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.input.motion.button.CommonButtons import CommonButtons
from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


