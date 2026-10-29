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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations



class MyFormUtil:
    instance: MyFormUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.popupMenuRectangle: Rectangle = RectangleFactory.SINGLETON

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MyFormUtil:
        return MyFormUtil.instance
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        features: Features = Features.getInstance()
        isOpenGL: bool = features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)
        TOTAL_CHAR_WIDTH: int = (2 if SWTJOGLProcessor.getInstance().isJOGL() and isOpenGL else 3)
        width: int = MyFontProcessor.defaultStringWidth(font, TOTAL_CHAR_WIDTH)
        pointFactory: PointFactory = PointFactory.getInstance()
        if displayInfo.getLastHeight() < 320:
            self.popupMenuRectangle = Rectangle(pointFactory.createXY(0, 25), width, (font.getHeight() * 4) + 2)
        else:
            self.popupMenuRectangle = Rectangle(pointFactory.createXY(0, displayInfo.getLastHalfHeight() - 70), width, (font.getHeight() * 5))
    

    def getPopupMenuRectangle(self) -> Rectangle:
        return self.popupMenuRectangle
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


MyFormUtil.instance = MyFormUtil()

