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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class BasicPopupMenuPaintable(*java_bases(Paintable, UpdateMyFontInterface)):
    NAME: str = "MENU"
    def _java_defaults(self):
        vars(self).setdefault("basicSetColorUtil", None)
        vars(self).setdefault("drawStringUtil", None)
        vars(self).setdefault("label", None)
        vars(self).setdefault("foregroundBasicColor", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("rectangle", None)
        vars(self).setdefault("BORDER", 0)
        vars(self).setdefault("heightOffset", 0)
        vars(self).setdefault("offset", 0)
        vars(self).setdefault("animationInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
        from org.allbinary.graphics.draw.DrawVerticalStringUtil import DrawVerticalStringUtil
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.drawStringUtil: DrawVerticalStringUtil = DrawVerticalStringUtil.getInstance()
        if "label" not in vars(self): self.label: str = None
        if "foregroundBasicColor" not in vars(self): self.foregroundBasicColor: BasicColor = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        if "rectangle" not in vars(self): self.rectangle: Rectangle = None
        if "BORDER" not in vars(self): self.BORDER: int = 0
        if "heightOffset" not in vars(self): self.heightOffset: int = 0
        if "offset" not in vars(self): self.offset: int = 0
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
    

    def __init__(self, rectangle: Rectangle, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__()
        __class__._init_fields(self)
        self.foregroundBasicColor = foregroundBasicColor
        self.label = BasicPopupMenuPaintable.NAME
        self.rectangle = rectangle
        if java_predicate(J2MEUtil, "isJ2ME") or java_predicate(J2MEUtil, "isHTML"):
            self.animationInterface = NullAnimationFactory.getFactoryInstance().getInstance(0)
        else:
            self.animationInterface = RectangleFilledAnimation(self.rectangle.getWidth(), self.rectangle.getHeight(), BasicColorFactory.getInstance().TRANSPARENT_GREY)
        self.init(rectangle)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.AndroidUtil import AndroidUtil
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.layer.SWTUtil import SWTUtil
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
        from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor
        font: Font = graphics.getFont()
        features: Features = Features.getInstance()
        isOpenGL: bool = features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)
        self.drawStringUtil.updateMeasurement(graphics, self.label)
        BORDER: int = 0
        if java_predicate(J2MEUtil, "isHTML") or isOpenGL:
            BORDER = java_divide(MyFontProcessor.defaultCharWidth(font), 2)
        elif java_predicate(AndroidUtil, "isAndroid") or java_predicate(J2MEUtil, "isJ2SE") or SWTUtil.isSWT:
            BORDER = MyFontProcessor.defaultCharWidth(font)
        else:
            BORDER = MyFontProcessor.defaultCharWidth(font) * 2
        self.BORDER = BORDER
        self.heightOffset = self.rectangle.getHeight() - (font.getHeight() * __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(BasicPopupMenuPaintable.NAME))
        if java_predicate(OpenGLFeatureUtil.getInstance(), "isAnyThreed"):
            self.heightOffset -= font.getHeight() + 2
            if java_predicate(AndroidUtil, "isAndroid"):
                self.heightOffset = font.getHeight()
            else:
                self.heightOffset -= font.getHeight() + 2
        self.offset = (int(self.heightOffset) >> (int(1) & 31)) + ((4 if java_predicate(SWTJOGLProcessor.getInstance(), "isJOGL") else 0))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    # throws Exception
    def init(self, rectangle: Rectangle) -> None:
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation
        from org.allbinary.graphics.Rectangle import Rectangle
        self.rectangle = rectangle
        width: int = self.rectangle.getWidth()
        height: int = self.rectangle.getHeight()
        if java_predicate(J2MEUtil, "isJ2ME") or java_predicate(J2MEUtil, "isHTML"):
            pass
        else:
            rectangleFilledAnimation: RectangleFilledAnimation = self.animationInterface
            rectangleFilledAnimation.setWidth(width)
            rectangleFilledAnimation.setHeight(height)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.GPoint import GPoint
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
# from org.allbinary.AndroidUtil import AndroidUtil
# from org.allbinary.J2MEUtil import J2MEUtil
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
# from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.game.layer.SWTUtil import SWTUtil
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
# from org.allbinary.graphics.draw.DrawVerticalStringUtil import DrawVerticalStringUtil
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
# from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor


