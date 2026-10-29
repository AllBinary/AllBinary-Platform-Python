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
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface
from org.allbinary.animation.AnimationInterface import AnimationInterface


class Animation(AnimationInterface, OpenGLSurfaceChangedInterface):

    def _init_fields(self) -> None:
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.colorP: int = 0
        self.changeBasicColorP: BasicColor = BasicColorFactory.getInstance().NULL_COLOR
        self.changeColorP: int = 0
        self.alphaP: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
    

    def setAlpha(self, alpha: int) -> None:
        self.alphaP = alpha
    

    # throws Exception
    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        pass
    

    def isThreed(self) -> bool:
        return False
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
        self.colorP = int(self.basicColor)
    

    def setBackgroundBasicColorP(self, basicColor: BasicColor) -> None:
        pass
    

    def getChangeBasicColor(self) -> BasicColor:
        return self.changeBasicColorP
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        self.changeBasicColorP = basicColor
        self.changeColorP = int(self.changeBasicColorP)
    

    def getChangeColor(self) -> int:
        return self.changeColorP
    

    def getColor(self) -> int:
        return self.colorP
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        pass
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        pass
    

    # throws Exception
    def set(self, gl: GL) -> None:
        pass
    

    def setDx(self, dx: int) -> None:
        pass
    

    def getDx(self) -> int:
        return 0
    

    def setDy(self, dy: int) -> None:
        pass
    

    def getDy(self) -> int:
        return 0
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil


