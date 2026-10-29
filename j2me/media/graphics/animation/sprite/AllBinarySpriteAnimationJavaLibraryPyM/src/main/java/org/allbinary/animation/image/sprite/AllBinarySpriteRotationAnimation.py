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

from org.allbinary.animation.image.sprite.HackRotationSpriteIndexedAnimation import HackRotationSpriteIndexedAnimation


class AllBinarySpriteRotationAnimation(HackRotationSpriteIndexedAnimation):
    

    def __init__(self, sprite: Sprite, image: Image, animationBehavior: AnimationBehavior) -> None:
        super().__init__(sprite, image, AngleInfo.getInstance(((int((AngleFactory.getInstance().TOTAL_ANGLE / sprite.getRawFrameCount())) + 32768) % 65536 - 32768)), animationBehavior)
        self.angleInfo.adjustAngle(self.sprite.getFrame())
    

    def nextRotation(self) -> None:
        self.sprite.nextFrame()
        self.angleInfo.adjustAngle(self.sprite.getFrame())
    

    def previousRotation(self) -> None:
        self.sprite.prevFrame()
        self.angleInfo.adjustAngle(self.sprite.getFrame())
    

    def setFrameByDirection(self, direction: Direction) -> None:
        angle: Angle = self.directionUtil.getFrameAngle(direction)
        self.adjustFrameToAngle(angle)
    

    def setFrameToAngle(self, angle: Angle) -> None:
        self.adjustFrameToAngle(angle)
    

    def setFrame(self, index: int) -> None:
        self.sprite.setFrame(index)
        self.angleInfo.adjustAngle(self.getFrame())
    

    def adjustFrameToAngle(self, angle: Angle) -> None:
        self.adjustFrame(angle.getValue())
    

    def adjustFrame(self, angle: int) -> None:
        self.setFrame(self.frameUtil.getFrameForAngle(angle, int(self.angleInfo.getAngleIncrementInfo().getAngleIncrement())))
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.direction.Direction import Direction
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo


