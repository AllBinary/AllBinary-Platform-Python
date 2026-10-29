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

from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class AllBinaryJ2SEImageRotationAnimationFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.angleIncrementP: int = None
        self.resizeCanvasForRotation: bool = None
    

    # throws Exception
    @staticmethod
    def createDXY(image: Image, width: int, height: int, dx: int, dy: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory, resizeCanvasForRotation: bool) -> AllBinaryJ2SEImageRotationAnimationFactory:
        imageRotationAnimationFactory: AllBinaryJ2SEImageRotationAnimationFactory = AllBinaryJ2SEImageRotationAnimationFactory(image, width, height, angleIncrement, animationBehaviorFactory, resizeCanvasForRotation)
        imageRotationAnimationFactory.animationFactoryInitializationVisitor.dx = dx
        imageRotationAnimationFactory.animationFactoryInitializationVisitor.dy = dy
        imageRotationAnimationFactory.animationFactoryInitializationVisitor.originalDx = dx
        imageRotationAnimationFactory.animationFactoryInitializationVisitor.originalDy = dy
        return imageRotationAnimationFactory
    

    def __init__(self, image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory, resizeCanvasForRotation: bool) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        self._init_fields()
        self.angleIncrementP = angleIncrement
        self.resizeCanvasForRotation = resizeCanvasForRotation
    

    # throws Exception
    def getCanvasImage(self) -> Image:
        features: Features = Features.getInstance()
        if self.resizeCanvasForRotation and not features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            return ImageCopyUtil.getInstance().createImageScale(self.getImage(), 1.44, False)
        else:
            return self.getImage()
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.AllBinaryJ2SEImageRotationAnimation import AllBinaryJ2SEImageRotationAnimation
        from org.allbinary.animation.image.AllBinaryAdjustedJ2SEImageRotationAnimation import AllBinaryAdjustedJ2SEImageRotationAnimation
        imageCopyUtil: ImageCopyUtil = ImageCopyUtil.getInstance()
        canvasImage: Image = self.getCanvasImage()
        scaledImage: Image = self.animationFactoryImageScaleUtil.createImage(canvasImage, self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        openGLUtil: OpenGLUtil = OpenGLUtil.getInstance()
        scaledImage = openGLUtil.addImage(scaledImage)
        copyOfScaledImage: Image = imageCopyUtil.createImageForRotation(scaledImage)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AllBinaryAdjustedJ2SEImageRotationAnimation(scaledImage, copyOfScaledImage, AngleInfo.getInstance(self.angleIncrementP), AngleFactory.getInstance().TOTAL_ANGLE, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return AllBinaryJ2SEImageRotationAnimation(scaledImage, copyOfScaledImage, AngleInfo.getInstance(self.angleIncrementP), AngleFactory.getInstance().TOTAL_ANGLE, self.animationBehaviorFactory.getOrCreateInstance())
    

    def getAngleIncrement(self) -> int:
        return self.angleIncrementP
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil


