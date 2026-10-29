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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.animation.special.SpecialAnimationInterface import SpecialAnimationInterface
from org.allbinary.animation.image.ImageArrayAnimation import ImageArrayAnimation


class ImageArraySpecialAnimation(ImageArrayAnimation, SpecialAnimationInterface):

    def _init_fields(self) -> None:
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(270)
        self.loopCount: int = 0
        self.loopCountTotal: int = 1
    

    def __init__(self, imageArray: list[Image], animationBehavior: AnimationBehavior) -> None:
        super().__init__(imageArray, animationBehavior)
        self._init_fields()
        self.reset()
    

    def getLoopCount(self) -> int:
        return self.loopCount
    

    def setLastFrame(self) -> None:
        self.circularIndexUtil.setIndex(self.circularIndexUtil.getSize() - 1)
    

    def reset(self) -> None:
        self.setFrame(self.getSize() - 1)
        self.loopCount = 0
    

    def nextFrame(self) -> None:
        if self.getFrame() > 0:
            if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
                self.previousFrame()
                if self.getFrame() == 0:
                    self.loopCount += 1
    

    def isComplete(self) -> bool:
        if self.loopCount < self.loopCountTotal or self.getFrame() != 0:
            return False
        else:
            return True
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        x = DisplayInfoSingleton.getInstance().getLastHalfWidth() - (self.getImage(self.circularIndexUtil.getIndex()).getWidth() >> 1)
        y = 5
        super().paintXY(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


