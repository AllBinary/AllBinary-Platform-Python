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
# package org.allbinary.animation.caption

from __future__ import annotations

from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase


class CaptionAnimationHelper(CaptionAnimationHelperBase):

    def _init_fields(self) -> None:
        self.timeHelper: TimeDelayHelper = TimeDelayHelper(620)
        self.textAnimation: TextAnimation = TextAnimation(StringUtil.getInstance().EMPTY_STRING, AnimationBehavior.getInstance())
        self.captionAnimation: Animation = None
        self.animation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def __init__(self, captionAnimation: Animation, captionDx: int, captionDy: int, dx: int, dy: int) -> None:
        from org.allbinary.animation.caption.CaptionAnimation import CaptionAnimation
        super().__init__()
        self._init_fields()
        self.captionAnimation = CaptionAnimation(captionAnimation, self.textAnimation, captionDx, captionDy, dx, dy)
    

    def isShowing(self) -> bool:
        if self.animation == self.captionAnimation:
            return True
        else:
            return False
    

    def tick(self) -> None:
        if self.timeHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def update(self, message: str, basicColor: BasicColor) -> None:
        self.textAnimation.setBasicColorP(basicColor)
        self.textAnimation.setText(message)
        self.animation = self.captionAnimation
        self.timeHelper.setStartTimeTNT()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.animation.paintXY(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.text.TextAnimation import TextAnimation
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


