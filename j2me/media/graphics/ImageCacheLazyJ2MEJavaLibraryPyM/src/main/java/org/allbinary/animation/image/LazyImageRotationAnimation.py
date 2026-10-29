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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.animation.RotationAnimation import RotationAnimation


class LazyImageRotationAnimation(RotationAnimation):
    SET_REAL_ANIMATION: str = "setRealAnimation"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.layoutIndex: int = None
        self.instanceId: int = None
        self.animationInterfaceFactoryInterface: BaseImageAnimationFactory = None
        self.NULL_INDEX_ANIMATION: IndexedAnimation = None
        self.animation: IndexedAnimation = None
        self.scaleProperties: ScaleProperties = ScaleProperties.instance
    

    def __init__(self, layoutIndex: int, instanceId: int, scaleProperties: ScaleProperties, animationInterfaceFactoryInterface: BaseImageAnimationFactory, animationBehavior: AnimationBehavior) -> None:
        from org.allbinary.animation.image.ActualRotationAnimation import ActualRotationAnimation
        super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), animationBehavior)
        self._init_fields()
        self.layoutIndex = layoutIndex
        self.instanceId = instanceId
        self.animationInterfaceFactoryInterface = animationInterfaceFactoryInterface
        imageCache: ImageCache = ImageCacheFactory.getInstance()
        imageCache.add(self)
        self.scaleProperties = scaleProperties
        self.NULL_INDEX_ANIMATION = NullRotationAnimationFactory.getFactoryInstance().getInstance(0)
        class ActualRotationAnimation(RotationAnimation):

            def _init_fields(self) -> None:
                self.lazyImageRotationAnimation: LazyImageRotationAnimation = None
                self.index: int = 0
            

            def __init__(self, lazyImageRotationAnimation: LazyImageRotationAnimation) -> None:
                super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), self.animationBehavior)
                self._init_fields()
                self.lazyImageRotationAnimation = lazyImageRotationAnimation
            

            def setFrame(self, index: int) -> None:
                self.index = index
            

            def getFrame(self) -> int:
                return self.index
            

            def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
                try:
                    ImageCacheFactory.getInstance().insertFirst(self)
                    self.lazyImageRotationAnimation.animation = self.lazyImageRotationAnimation.NULL_INDEX_ANIMATION
                except Exception as e:
                    logUtil: LogUtil = LogUtil.getInstance()
                    logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
            

            def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
                try:
                    ImageCacheFactory.getInstance().insertFirst(self)
                    self.lazyImageRotationAnimation.animation = self.lazyImageRotationAnimation.NULL_INDEX_ANIMATION
                except Exception as e:
                    logUtil: LogUtil = LogUtil.getInstance()
                    logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
        self.animation = ActualRotationAnimation(self)
    

    def setRealAnimation(self) -> None:
        try:
            animation: IndexedAnimation = self.animation
            self.animationInterfaceFactoryInterface.setInitialScale(self.scaleProperties)
            self.animation = self.animationInterfaceFactoryInterface.getInstance(self.instanceId)
            self.animation.setState(animation)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, LazyImageRotationAnimation.SET_REAL_ANIMATION, e)
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        self.animation.setScale(scaleX, scaleY)
    

    def getAnimationBehavior(self) -> AnimationBehavior:
        return self.animation.getAnimationBehavior()
    

    # throws Exception
    def set(self, gl: GL) -> None:
        self.animation.set(gl)
    

    def setAlpha(self, alpha: int) -> None:
        self.animation.setAlpha(alpha)
    

    def setDx(self, dx: int) -> None:
        self.animation.setDx(dx)
    

    def setDy(self, dy: int) -> None:
        self.animation.setDy(dy)
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        self.animation.setMaxScale(maxScaleX, maxScaleY)
    

    def nextRotation(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.nextRotation()
    

    def previousRotation(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.previousRotation()
    

    def nextRotationX(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.nextRotationX()
    

    def previousRotationX(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.previousRotationX()
    

    def nextRotationZ(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.nextRotationZ()
    

    def previousRotationZ(self) -> None:
        rotationAnimation: RotationAnimation = (self.animation)
        rotationAnimation.previousRotationZ()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        self.animation.changeBasicColor(basicColor)
    

    def getBasicColorP(self) -> BasicColor:
        return self.animation.getBasicColorP()
    

    def getChangeBasicColor(self) -> BasicColor:
        return self.animation.getChangeBasicColor()
    

    def getChangeColor(self) -> int:
        return self.animation.getChangeColor()
    

    def getColor(self) -> int:
        return self.animation.getColor()
    

    def getDx(self) -> int:
        return self.animation.getDx()
    

    def getDy(self) -> int:
        return self.animation.getDy()
    

    def isThreed(self) -> bool:
        return self.animation.isThreed()
    

    # throws Exception
    def nextFrame(self) -> None:
        self.animation.nextFrame()
    

    def reset(self) -> None:
        self.animation.reset()
    

    def setFrame(self, index: int) -> None:
        self.animation.setFrame(index)
    

    def getFrame(self) -> int:
        return self.animation.getFrame()
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.animation.getAnimationSize()
    

    def getSize(self) -> int:
        return self.animation.getSize()
    

    def previousFrame(self) -> None:
        self.animation.previousFrame()
    

    def isLastFrame(self) -> bool:
        return self.animation.isLastFrame()
    

    def setSequence(self, sequence: list[int]) -> None:
        self.animation.setSequence(sequence)
    

    def getSequence(self) -> list[int]:
        return self.animation.getSequence()
    

    def getWidth(self) -> int:
        return self.animation.getWidth()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        try:
            self.animation.paintXY(graphics, x, y)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        try:
            self.animation.paintThreedXYZ(graphics, x, y, z)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        image: Image = self.animationInterfaceFactoryInterface.getImage()
        return str(StringMaker().append(str(super())).append(commonSeps.SPACE).append(image.getName()).append(commonSeps.SPACE).appendint(int(image.getWidth())).append(commonSeps.SPACE).appendint(int(image.getHeight())))

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.NullRotationAnimationFactory import NullRotationAnimationFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


