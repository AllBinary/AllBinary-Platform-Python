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

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class BaseImageAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationFactoryImageScaleUtil: AnimationFactoryImageScaleUtil = AnimationFactoryImageScaleUtil.getInstance()
        self.image: Image = None
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
        self.sequenceArray: list[int] = None
        self.animationFactoryInitializationVisitor: AnimationFactoryInitializationVisitor = None
        self.scaleProperties: ScaleProperties = ScaleProperties.instance
    

    # throws Exception
    @staticmethod
    def createFactoryBase(image: Image, sequenceArray: list[int], width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> BaseImageAnimationFactory:
        return BaseImageAnimationFactory(image, sequenceArray, width, height, 0, 0, animationBehaviorFactory)
    

    def __init__(self, image: Image, sequenceArray: list[int], width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        from org.allbinary.animation.image.AnimationFactoryInitializationVisitor import AnimationFactoryInitializationVisitor
        self._init_fields()
        self.animationFactoryInitializationVisitor = AnimationFactoryInitializationVisitor()
        self.image = image
        self.animationFactoryInitializationVisitor.width = width
        self.animationFactoryInitializationVisitor.height = height
        self.animationBehaviorFactory = animationBehaviorFactory
        self.sequenceArray = sequenceArray
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        return NullAnimationFactory.getFactoryInstance().getInstance(instanceId)
    

    def getImage(self) -> Image:
        return self.image
    

    def getSequenceArray(self) -> list[int]:
        return self.sequenceArray
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        self.scaleProperties = scaleProperties
        if self.scaleProperties.shouldScale:
            self.scaleProperties.scaleWidth = int((self.animationFactoryInitializationVisitor.width * self.scaleProperties.scaleX))
            self.scaleProperties.scaleHeight = int((self.animationFactoryInitializationVisitor.height * self.scaleProperties.scaleY))
        else:
            pass
    

    def getAnimationFactoryInitializationVisitorP(self) -> AnimationFactoryInitializationVisitor:
        return self.animationFactoryInitializationVisitor
    

    def getScalePropertiesP(self) -> ScaleProperties:
        return self.scaleProperties
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(int(self.image.getHeight()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(str(self.animationFactoryInitializationVisitor))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.image.AnimationFactoryImageScaleUtil import AnimationFactoryImageScaleUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps


