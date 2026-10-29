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

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


class BasicPopupMenuPaintable(Paintable, UpdateMyFontInterface):
    NAME: str = "MENU"

    def _init_fields(self) -> None:
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.drawStringUtil: DrawVerticalStringUtil = DrawVerticalStringUtil.getInstance()
        self.label: str = None
        self.foregroundBasicColor: BasicColor = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.rectangle: Rectangle = None
        self.BORDER: int = 0
        self.heightOffset: int = 0
        self.offset: int = 0
        self.animationInterface: Animation = None
    

    def __init__(self, rectangle: Rectangle, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.foregroundBasicColor = foregroundBasicColor
        self.label = BasicPopupMenuPaintable.NAME
        self.rectangle = rectangle
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            self.animationInterface = NullAnimationFactory.getFactoryInstance().getInstance(0)
        else:
            self.animationInterface = RectangleFilledAnimation(self.rectangle.getWidth(), self.rectangle.getHeight(), BasicColorFactory.getInstance().TRANSPARENT_GREY)
        self.init(rectangle)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        features: Features = Features.getInstance()
        isOpenGL: bool = features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)
        self.drawStringUtil.updateMeasurement(graphics, self.label)
        BORDER: int = 0
        if J2MEUtil.isHTML() or isOpenGL:
            BORDER = MyFontProcessor.defaultCharWidth(font) / 2
        elif AndroidUtil.isAndroid() or J2MEUtil.isJ2SE() or SWTUtil.isSWT:
            BORDER = MyFontProcessor.defaultCharWidth(font)
        else:
            BORDER = MyFontProcessor.defaultCharWidth(font) * 2
        self.BORDER = BORDER
        self.heightOffset = self.rectangle.getHeight() - (font.getHeight() * BasicPopupMenuPaintable.NAME.length())
        if OpenGLFeatureUtil.getInstance().isAnyThreed():
            self.heightOffset -= font.getHeight() + 2
            if AndroidUtil.isAndroid():
                self.heightOffset = font.getHeight()
            else:
                self.heightOffset -= font.getHeight() + 2
        self.offset = (self.heightOffset >> 1) + ((4 if SWTJOGLProcessor.getInstance().isJOGL() else 0))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    # throws Exception
    def init(self, rectangle: Rectangle) -> None:
        self.rectangle = rectangle
        width: int = self.rectangle.getWidth()
        height: int = self.rectangle.getHeight()
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            pass
        else:
            rectangleFilledAnimation: RectangleFilledAnimation = self.animationInterface
            rectangleFilledAnimation.setWidth(width)
            rectangleFilledAnimation.setHeight(height)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        point: GPoint = self.rectangle.getPoint()
        x: int = point.getX()
        y: int = point.getY()
        width: int = self.rectangle.getWidth()
        height: int = self.rectangle.getHeight()
        self.animationInterface.paintXY(graphics, x, y)
        self.basicSetColorUtil.setBasicColorP(graphics, self.foregroundBasicColor)
        self.drawStringUtil.paintVerticle(graphics, self.label, x + self.BORDER, y + self.offset, 0)
        graphics.drawRect(x, y, width, height)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.layer.SWTUtil import SWTUtil
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.graphics.draw.DrawVerticalStringUtil import DrawVerticalStringUtil
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor


