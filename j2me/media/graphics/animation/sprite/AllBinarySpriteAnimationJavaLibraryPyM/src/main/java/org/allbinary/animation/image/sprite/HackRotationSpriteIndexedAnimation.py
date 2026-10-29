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

from org.allbinary.animation.RotationAnimation import RotationAnimation


class HackRotationSpriteIndexedAnimation(RotationAnimation):

    def _init_fields(self) -> None:
        self.sprite: Sprite = None
        self.image: Image = None
    

    def __init__(self, sprite: Sprite, image: Image, angleInfo: AngleInfo, animationBehavior: AnimationBehavior) -> None:
        super().__init__(angleInfo, CircularIndexUtil.createInstance(360 / angleInfo.getAngleIncrementInfo().getAngleIncrement()), animationBehavior)
        self._init_fields()
        self.sprite = sprite
        self.image = image
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def paintFrame(self, g: Graphics, frame: int, x: int, y: int) -> None:
        self.setFrame(frame)
        self.paintXY(g, x, y)
    

    def paintXY(self, g: Graphics, x: int, y: int) -> None:
        self.sprite.setPosition(x, y)
        self.paint(g)
    

    def paint(self, g: Graphics) -> None:
        self.sprite.paint(g)
    

    def nextRotation(self) -> None:
        self.sprite.nextFrame()
    

    def previousRotation(self) -> None:
        self.sprite.prevFrame()
    

    def getSize(self) -> int:
        return self.sprite.getRawFrameCount()
    

    def setFrame(self, frame: int) -> None:
        self.sprite.setFrame(frame)
    

    def getFrame(self) -> int:
        return self.sprite.getFrame()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


