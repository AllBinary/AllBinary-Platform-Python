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
# package org.allbinary.animation.image.sprite

from __future__ import annotations

from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface


class SpriteIndexedAnimation(IndexedAnimation, ColorCompositeInterface):

    def _init_fields(self) -> None:
        self.sprite: Sprite = None
        self.image: Image = None
        self.basicColorArray: list[BasicColor] = None
    

    def __init__(self, sprite: Sprite, image: Image, basicColorArray: list[BasicColor], animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.sprite = sprite
        self.image = image
        self.basicColorArray = basicColorArray
        if len(self.basicColorArray) != 0 and self.getSize() != len(self.basicColorArray):
            raise Exception(str(StringMaker().append(CommonLabels.getInstance().TOTAL_LABEL).appendint(self.getSize()).append("!=").appendint(len(self.basicColorArray))))
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        for index in range(0, len(self.basicColorArray)):
            if basicColor == self.basicColorArray[index]:
                self.setFrame(index)
                break
    

    def getBasicColorP(self) -> BasicColor:
        if len(self.basicColorArray) < self.getFrame():
            return self.basicColorArray[self.getFrame()]
        else:
            return BasicColorFactory.getInstance().WHITE
    

    def paintFrame(self, graphics: Graphics, frame: int, x: int, y: int) -> None:
        self.setFrame(frame)
        self.sprite.setPosition(x, y)
        self.sprite.paint(graphics)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.sprite.setPosition(x, y)
        self.sprite.paint(graphics)
    

    def paint(self, graphics: Graphics) -> None:
        self.sprite.paint(graphics)
    

    def nextFrame(self) -> None:
        self.sprite.nextFrame()
    

    def previousFrame(self) -> None:
        self.sprite.prevFrame()
    

    def getSize(self) -> int:
        return self.sprite.getRawFrameCount()
    

    def setFrame(self, frame: int) -> None:
        self.sprite.setFrame(frame)
    

    def getFrame(self) -> int:
        return self.sprite.getFrame()
    

    def isLastFrame(self) -> bool:
        if self.sprite.getFrame() == self.getSize() - 1:
            return True
        else:
            return False
    

    def getLastFrame(self) -> int:
        return self.getSize()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    # throws Exception
    def close(self) -> None:
        pass
    

    # throws Throwable
    def finalize(self) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels


