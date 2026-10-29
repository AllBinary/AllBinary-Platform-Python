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
# package org.allbinary.media.image

from __future__ import annotations



class ImageCopyUtil:
    instance: ImageCopyUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        self.features: Features = Features.getInstance()
        self.openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        self.openGLUtil: OpenGLUtil = OpenGLUtil.getInstance()
        self.openGLESImageExclusionUtil: OpenGLESImageExclusionUtil = OpenGLESImageExclusionUtil.getInstance()
        self.NO_COPY: str = "SWT should not copy images after initial loading as the alpha is not honored"
        self.UNABLE: str = "Unable to scale image without dimensions"
        self.INFORMATION: str = "about_"
        self.LEADERBOARD: str = "leaderboard"
    

    @staticmethod
    def getInstance() -> ImageCopyUtil:
        return ImageCopyUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createImageForRotation(self, originalImage: Image) -> Image:
        if self.features.isFeature(self.openGLFeatureFactory.OPENGL):
            image: Image = originalImage
            image = self.openGLUtil.addImage(image)
            return image
        else:
            return self.createImage(originalImage)
    

    # throws Exception
    def createImage(self, originalImage: Image) -> Image:
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return originalImage
        originalImage2: Image = originalImage
        if self.features.isFeature(self.openGLFeatureFactory.OPENGL):
            if originalImage.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (originalImage)
                originalImage2 = openGLESImage.openGLBitmap.getImage()
        image: Image = None
        if originalImage2.isMutable():
            originalMutableImage: SwtMutableImage = originalImage2
            image = SwtMutableImage(SwtDeviceComponent.createImage(originalMutableImage.image.getImageData()))
        else:
            originalImmutableImage: SwtImmutableImage = originalImage2
            image = SwtMutableImage(SwtDeviceComponent.createImage(originalImmutableImage.image.getImageData()))
        image = self.openGLUtil.addImage(image)
        return image
    

    # throws Exception
    def createImageWH(self, originalImage: Image, width: int, height: int, mutable: bool) -> Image:
        originalImage2: Image = originalImage
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return originalImage
        if self.features.isFeature(self.openGLFeatureFactory.OPENGL):
            if self.openGLESImageExclusionUtil.isCustomScaling(originalImage):
                return self.createImage2(originalImage, width, height, mutable)
            if originalImage.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (originalImage)
                originalImage2 = openGLESImage.openGLBitmap.getImage()
        image: Image = None
        if originalImage2.isMutable() and mutable:
            originalMutableImage: SwtMutableImage = originalImage2
            if originalMutableImage.getImage() is not None:
                imageData2: ImageData = originalMutableImage.image.getImageData()
                imageData: ImageData = imageData2.scaledTo(width, height)
                image = SwtMutableImage(SwtDeviceComponent.createImage(imageData))
            else:
                image = SwtMutableImage(originalMutableImage.getName(), PostLoadSwtMutableImageProcessor(originalMutableImage))
        else:
            originalImmutableImage: SwtImmutableImage = originalImage2
            if originalImmutableImage.getImage() is not None:
                imageData2: ImageData = originalImmutableImage.image.getImageData()
                if width > 0 and height > 0:
                    imageData: ImageData = imageData2.scaledTo(width, height)
                    image = SwtImmutableImage(originalImage.getName(), SwtDeviceComponent.createImage(imageData))
                else:
                    self.logUtil.putF(self.UNABLE, self, self.commonStrings.CONSTRUCTOR)
                    image = SwtImmutableImage(originalImmutableImage.getName(), PostLoadSwtImmutableImageProcessor(originalImmutableImage))
            else:
                image = SwtImmutableImage(originalImmutableImage.getName(), PostLoadSwtImmutableImageProcessor(originalImmutableImage))
        image = self.openGLUtil.addImage(image)
        return image
    

    # throws Exception
    def createImage2(self, originalImage: Image, width: int, height: int, mutable: bool) -> Image:
        originalImage2: Image = originalImage
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return originalImage
        image: Image = None
        if self.features.isFeature(self.openGLFeatureFactory.OPENGL):
            displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
            if originalImage.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (originalImage)
                openGLESImageProperties: OpenGLESImageProperties = openGLESImage.openGLESImageProperties
                openGLWidth: int = openGLESImage.openGLBitmap.getWidth()
                openGLHeight: int = openGLESImage.openGLBitmap.getHeight()
                openGLESImageProperties.scaleX2 = ((float(width)) / float(openGLWidth))
                openGLESImageProperties.scaleX = openGLESImageProperties.scaleX2
                openGLESImageProperties.scaleY2 = ((float(height)) / float(openGLHeight))
                openGLESImageProperties.scaleY = openGLESImageProperties.scaleY2
                openGLESImageProperties.scaleX = openGLESImageProperties.scaleX * 0.75
                openGLESImageProperties.scaleY = openGLESImageProperties.scaleY * 0.75
                if originalImage.getHeight() % 2 != 0:
                    openGLESImageProperties.scaleX2 += 1.0 / float(openGLWidth)
                    openGLESImageProperties.scaleY2 += 1.0 / float(openGLHeight)
                image = openGLESImage
            else:
                image = originalImage
                openGLESImage: OpenGLESImage = self.openGLUtil.addImage(image)
                openGLESImageProperties: OpenGLESImageProperties = openGLESImage.openGLESImageProperties
                openGLESImageProperties.scaleX2 = float(((float(width)) / openGLESImage.getWidth()))
                openGLESImageProperties.scaleX = openGLESImageProperties.scaleX2
                openGLESImageProperties.scaleY2 = float(((float(height)) / openGLESImage.getHeight()))
                openGLESImageProperties.scaleY = openGLESImageProperties.scaleY2
                if image.getName().startsWith(self.INFORMATION):
                    openGLESImage.openGLESImageTranslate = OpenGLESDeviceImageTranslate()
                    openGLESDeviceImageTranslate: OpenGLESDeviceImageTranslate = openGLESImage.openGLESImageTranslate
                    openGLESDeviceImageTranslate.translateX = displayInfoSingleton.getLastWidth() / 1.4 / openGLESImageProperties.scaleX
                    openGLESDeviceImageTranslate.translateY = displayInfoSingleton.getLastHeight() / 4 / openGLESImageProperties.scaleY
                    openGLESImageProperties.scaleX = openGLESImageProperties.scaleX * 0.25
                    openGLESImageProperties.scaleY = openGLESImageProperties.scaleY * 0.25
                else:
                    openGLESImageProperties.scaleX = openGLESImageProperties.scaleX * 0.75
                    openGLESImageProperties.scaleY = openGLESImageProperties.scaleY * 0.75
                    if image.getName().startsWith(self.LEADERBOARD):
                        openGLESImage.openGLESImageTranslate = OpenGLESDeviceImageTranslate()
                        openGLESDeviceImageTranslate: OpenGLESDeviceImageTranslate = openGLESImage.openGLESImageTranslate
                        openGLESDeviceImageTranslate.translateX = -displayInfoSingleton.getLastWidth() / 40 / openGLESImageProperties.scaleX
                    if image.getName().startsWith(self.LEADERBOARD):
                        pass
                    else:
                        openGLESImageProperties.scaleX = 1.0
                        openGLESImageProperties.scaleY = 1.0
                image = openGLESImage
        else:
            if originalImage2.isMutable() and mutable:
                originalMutableImage: SwtMutableImage = originalImage2
                if originalMutableImage.getImage() is not None:
                    imageData2: ImageData = originalMutableImage.image.getImageData()
                    imageData: ImageData = imageData2.scaledTo(width, height)
                    image = SwtMutableImage(SwtDeviceComponent.createImage(imageData))
                else:
                    image = SwtMutableImage(originalMutableImage.getName(), PostLoadSwtMutableImageProcessor(originalMutableImage))
            else:
                originalImmutableImage: SwtImmutableImage = originalImage2
                if originalImmutableImage.getImage() is not None:
                    imageData2: ImageData = originalImmutableImage.image.getImageData()
                    imageData: ImageData = imageData2.scaledTo(width, height)
                    image = SwtImmutableImage(originalImage.getName(), SwtDeviceComponent.createImage(imageData))
                else:
                    image = SwtImmutableImage(originalImmutableImage.getName(), PostLoadSwtImmutableImageProcessor(originalImmutableImage))
            image = self.openGLUtil.addImage(image)
        return image
    

    # throws Exception
    def createImageScale(self, originalImage: Image, canvasScale: float, resize: bool) -> Image:
        if not self.features.isFeature(self.gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION):
            self.logUtil.putF(self.NO_COPY, self, self.commonStrings.CONSTRUCTOR)
            return originalImage
        newWidth: int = int((originalImage.getWidth() * canvasScale))
        newHeight: int = int((originalImage.getHeight() * canvasScale))
        if resize:
            if newWidth < newHeight:
                newWidth = newHeight
            if newHeight < newWidth:
                newHeight = newWidth
        image: Image = self.createImageWH(originalImage, newWidth, newHeight, True)
        if image.isMutable():
            originalImageData: ImageData = (originalImage.getImage()).getImageData()
            mutableImage2: SwtMutableImage = image
            halfWidthDelta: int = (newWidth - originalImage.getWidth()) / 2
            halfHeightDelta: int = (newHeight - originalImage.getHeight()) / 2
            originalPixelArray: list[int] = [0] * (originalImage.getWidth() * originalImage.getHeight())
            newPixelArray: list[int] = [0] * (image.getWidth() * image.getHeight())
            width: int = originalImage.getWidth()
            height: int = originalImage.getHeight()
            for i in range(0, height):
                originalImageData.getPixels(0, i, width, originalPixelArray, (i * width))
            for index in range(halfWidthDelta, width):
                for index2 in range(halfHeightDelta, height):
                    newPixelArray[index + (index2 * width)] = originalPixelArray[(index - halfWidthDelta) + ((index2 - halfHeightDelta) * width)]
            (mutableImage2.getImage()).getImageData().setPixels(0, 0, image.getWidth(), newPixelArray, 0)
            return image
        else:
            originalImmutableImage: SwtImmutableImage = image
            originalImageData: ImageData = (originalImage.getImage()).getImageData()
            halfWidthDelta: int = (newWidth - originalImage.getWidth()) / 2
            halfHeightDelta: int = (newHeight - originalImage.getHeight()) / 2
            originalPixelArray: list[int] = [0] * (originalImage.getWidth() * originalImage.getHeight())
            newPixelArray: list[int] = [0] * (image.getWidth() * image.getHeight())
            width: int = originalImage.getWidth()
            height: int = originalImage.getHeight()
            for i in range(0, height):
                originalImageData.getPixels(0, i, width, originalPixelArray, (i * width))
            for index in range(halfWidthDelta, width):
                for index2 in range(halfHeightDelta, height):
                    newPixelArray[index + (index2 * width)] = originalPixelArray[(index - halfWidthDelta) + ((index2 - halfHeightDelta) * width)]
            (originalImmutableImage.getImage()).getImageData().setPixels(0, 0, image.getWidth(), newPixelArray, 0)
            return image
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
from org.allbinary.image.opengles.OpenGLESDeviceImageTranslate import OpenGLESDeviceImageTranslate
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.image.opengles.OpenGLESImageExclusionUtil import OpenGLESImageExclusionUtil
from org.allbinary.image.opengles.OpenGLESImageProperties import OpenGLESImageProperties
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.eclipse.swt.graphics.ImageData import ImageData
from org.microemu.app.ui.swt.SwtDeviceComponent import SwtDeviceComponent
from org.microemu.device.swt.PostLoadSwtImmutableImageProcessor import PostLoadSwtImmutableImageProcessor
from org.microemu.device.swt.PostLoadSwtMutableImageProcessor import PostLoadSwtMutableImageProcessor
from org.microemu.device.swt.SwtImmutableImage import SwtImmutableImage
from org.microemu.device.swt.SwtMutableImage import SwtMutableImage


ImageCopyUtil.instance = ImageCopyUtil()

