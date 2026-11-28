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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


@java_inherited_overloads
class AllBinaryAndroidImageRotationAnimationFactory(BaseImageAnimationFactory):
    def _java_defaults(self):
        vars(self).setdefault("angleIncrement", 0)
        vars(self).setdefault("resizeCanvasForRotation", False)

    def _init_fields(self) -> None:
        if "angleIncrement" not in vars(self): self.angleIncrement: int = 0
        if "resizeCanvasForRotation" not in vars(self): self.resizeCanvasForRotation: bool = False
    

    # throws Exception
    @staticmethod
    def createFactory(image: Image, width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinaryAndroidImageRotationAnimationFactory:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        from org.allbinary.math.AngleFactory import AngleFactory
        return AllBinaryAndroidImageRotationAnimationFactory(image, width, height, ((int((java_divide(AngleFactory.getInstance().TOTAL_ANGLE, GameConfigurationCentral.getInstance().getGameControlFidelity()))) + 32768) % 65536 - 32768), animationBehaviorFactory, False)
    

    # throws Exception
    @staticmethod
    def createFactoryA(image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinaryAndroidImageRotationAnimationFactory:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        return AllBinaryAndroidImageRotationAnimationFactory(image, width, height, angleIncrement, animationBehaviorFactory, False)
    

    # throws Exception
    @staticmethod
    def createFactoryU(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinaryAndroidImageRotationAnimationFactory:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        from org.allbinary.math.AngleFactory import AngleFactory
        androidImageRotationAnimationFactory: AllBinaryAndroidImageRotationAnimationFactory = AllBinaryAndroidImageRotationAnimationFactory(image, image.getWidth(), image.getHeight(), ((int((java_divide(AngleFactory.getInstance().TOTAL_ANGLE, GameConfigurationCentral.getInstance().getGameControlFidelity()))) + 32768) % 65536 - 32768), animationBehaviorFactory, False)
        androidImageRotationAnimationFactory.init(-image.getWidth() >> 2, -image.getHeight() >> 2)
        return androidImageRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createFactoryDXYU(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinaryAndroidImageRotationAnimationFactory:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        from org.allbinary.math.AngleFactory import AngleFactory
        androidImageRotationAnimationFactory: AllBinaryAndroidImageRotationAnimationFactory = AllBinaryAndroidImageRotationAnimationFactory(image, image.getWidth(), image.getHeight(), ((int((java_divide(AngleFactory.getInstance().TOTAL_ANGLE, GameConfigurationCentral.getInstance().getGameControlFidelity()))) + 32768) % 65536 - 32768), animationBehaviorFactory, False)
        androidImageRotationAnimationFactory.init(dx, dy)
        return androidImageRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createFactoryADXY(image: Image, width: int, height: int, dx: int, dy: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory, resizeCanvasForRotation: bool) -> AllBinaryAndroidImageRotationAnimationFactory:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        androidImageRotationAnimationFactory: AllBinaryAndroidImageRotationAnimationFactory = AllBinaryAndroidImageRotationAnimationFactory(image, width, height, angleIncrement, animationBehaviorFactory, resizeCanvasForRotation)
        androidImageRotationAnimationFactory.init(dx, dy)
        return androidImageRotationAnimationFactory
    

    def init(self, dx: int, dy: int) -> None:
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
        self.animationFactoryInitializationVisitor.originalDx = dx
        self.animationFactoryInitializationVisitor.originalDy = dy
    

    def __init__(self, image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory, resizeCanvasForRotation: bool) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        __class__._init_fields(self)
        self.angleIncrement = angleIncrement
        self.resizeCanvasForRotation = resizeCanvasForRotation
    

    # throws Exception
    def getCanvasImage(self) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
        features: Features = Features.getInstance()
        if self.resizeCanvasForRotation and not (features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL)):
            return ImageCopyUtil.getInstance().createImageScale(self.getImage(), 1.44, False)
        else:
            return self.getImage()
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.AllBinaryFlickerAndroidImageRotationAnimation import AllBinaryFlickerAndroidImageRotationAnimation
        from org.allbinary.animation.image.AllBinaryAdjustedAndroidImageRotationAnimation import AllBinaryAdjustedAndroidImageRotationAnimation
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.math.AngleInfo import AngleInfo
        canvasImage: Image = self.getCanvasImage()
        scaledImage: Image = self.animationFactoryImageScaleUtil.createImage(canvasImage, self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        copyOfScaledImage: Image = ImageCopyUtil.getInstance().createImage(scaledImage)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AllBinaryAdjustedAndroidImageRotationAnimation(scaledImage, copyOfScaledImage, AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return AllBinaryFlickerAndroidImageRotationAnimation(scaledImage, copyOfScaledImage, AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationBehaviorFactory.getOrCreateInstance())
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
# from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo


