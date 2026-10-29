# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.animation.text

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class CustomTextAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        self.text: str = None
        self.initScaleHeight: int = None
        self.dx: int = 0
        self.dy: int = 0
        self.font: Font = None
        self.scaleProperties: ScaleProperties = None
    

    @staticmethod
    def createDXY(text: str, fontSize: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> CustomTextAnimationFactory:
        customTextAnimationFactory: CustomTextAnimationFactory = CustomTextAnimationFactory(text, fontSize, animationBehaviorFactory)
        customTextAnimationFactory.dx = dx
        customTextAnimationFactory.dy = dy
        return customTextAnimationFactory
    

    def __init__(self, text: str, fontSize: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.scaleProperties = ScaleProperties()
        self.text = text
        self.scaleProperties.scaleHeight = fontSize - (int(fontSize / 4))
        self.initScaleHeight = self.scaleProperties.scaleHeight
        self.animationBehaviorFactory = animationBehaviorFactory
        self.font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, self.initScaleHeight)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.text.CustomTextAnimation import CustomTextAnimation
        from org.allbinary.animation.text.AdjustCustomTextAnimation import AdjustCustomTextAnimation
        customTextAnimation: CustomTextAnimation = None
        if self.dx != 0 or self.dy != 0:
            customTextAnimation = AdjustCustomTextAnimation(self.text, self.scaleProperties.scaleHeight, self.dx, self.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            customTextAnimation = CustomTextAnimation(self.text, self.scaleProperties.scaleHeight, self.animationBehaviorFactory.getOrCreateInstance())
        customTextAnimation.setBasicColorP(self.basicColor)
        return customTextAnimation
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
    

    def getWidth(self) -> int:
        return self.font.stringWidth(self.text)
    

    def getHeight(self) -> int:
        return self.font.getHeight()
# from javax.microedition.lcdui.Font import Font
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


