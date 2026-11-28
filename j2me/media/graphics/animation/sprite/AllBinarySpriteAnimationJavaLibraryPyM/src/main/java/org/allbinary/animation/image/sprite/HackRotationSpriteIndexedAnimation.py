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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.RotationAnimation import RotationAnimation


@java_inherited_overloads
class HackRotationSpriteIndexedAnimation(RotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("sprite", None)
        vars(self).setdefault("image", None)

    def _init_fields(self) -> None:
        if "sprite" not in vars(self): self.sprite: Sprite = None
        if "image" not in vars(self): self.image: Image = None
    

    def __init__(self, sprite: Sprite, image: Image, angleInfo: AngleInfo, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.game.Sprite import Sprite
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(angleInfo, CircularIndexUtil.createInstance(java_divide(360, angleInfo.getAngleIncrementInfo().getAngleIncrement())), animationBehavior)
        __class__._init_fields(self)
        self.sprite = sprite
        self.image = image
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def paintFrame(self, g: Graphics, frame: int, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.setFrame(frame)
        self.paintXY(g, x, y)
    

    def paintXY(self, g: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.sprite.setPosition(x, y)
        self.paint(g)
    

    def paint(self, g: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
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
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        return PrimitiveIntUtil.getArrayInstance()
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


