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
# package org.allbinary.media.image

from __future__ import annotations



class ImageModifierUtil:
    instance: ImageModifierUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageCopyUtil: ImageCopyUtil = ImageCopyUtil.getInstance()
        self.features: Features = Features.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil.instance
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        pass
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        newBufferedImage: Image = None
        if image.isMutable():
            swtImage: SwtMutableImage = image
            newBufferedImage = swtImage.getImage()
        else:
            swtImage: SwtImmutableImage = image
            newBufferedImage = swtImage.getImage()
        r: int = basicColor.red
        g: int = basicColor.green
        b: int = basicColor.blue
        width: int = image.getWidth()
        height: int = image.getHeight()
        imageData: ImageData = newBufferedImage.getImageData()
        if imageData.depth == 24:
            rx: int = 0
            gx: int = 0
            bx: int = 0
            index3: int = 0
            for index in range(0, width):
                for index2 in range(0, height):
                    index3 = (index2 * imageData.bytesPerLine) + (index * 4)
                    rx = (imageData.data[index3] & 0xFF) << 16
                    gx = (imageData.data[index3 + 1] & 0xFF) << 8
                    bx = (imageData.data[index3 + 2] & 0xFF)
                    if rx != 0 or gx != 0 or bx != 0:
                        imageData.data[index3] = ((int(r) + 128) % 256 - 128)
                        imageData.data[index3 + 1] = ((int(g) + 128) % 256 - 128)
                        imageData.data[index3 + 2] = ((int(b) + 128) % 256 - 128)
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        if self.features.isFeature(OpenGLFeatureFactory.getInstance().OPENGL):
            if image.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (image)
                openGLESImage.imageProcessor = ModifierOpenGLESImageProcessor.getInstance()
                openGLESImage.openGLESImageProperties.redf = basicColor.getRedComponent()
                openGLESImage.openGLESImageProperties.greenf = basicColor.getGreenComponent()
                openGLESImage.openGLESImageProperties.bluef = basicColor.getBlueComponent()
                return
        newBufferedImage: Image = None
        if image.isMutable():
            swtImage: SwtMutableImage = image
            newBufferedImage = swtImage.getImage()
        else:
            swtImage: SwtImmutableImage = image
            newBufferedImage = swtImage.getImage()
        MAX: float = 255.0
        r: float = (float(basicColor.red)) / MAX
        g: float = (float(basicColor.green)) / MAX
        b: float = (float(basicColor.blue)) / MAX
        rx: int = 0
        gx: int = 0
        bx: int = 0
        imageData: ImageData = newBufferedImage.getImageData()
        if imageData.depth == 24:
            size: int = len(imageData.data)
            for index in range(0, size, 4):
                rx = (imageData.data[index] & 0xFF) << 16
                gx = (imageData.data[index + 1] & 0xFF) << 8
                bx = (imageData.data[index + 2] & 0xFF)
                rx = int(rx * r)
                gx = int(gx * g)
                bx = int(bx * b)
                imageData.data[index] = ((int(rx) + 128) % 256 - 128)
                imageData.data[index + 1] = ((int(gx) + 128) % 256 - 128)
                imageData.data[index + 2] = ((int(bx) + 128) % 256 - 128)
    

    def setAlpha(self, unusedOriginalImage: Image, image: Image, imageIndex: int, alphaInt: int) -> None:
        if self.features.isFeature(OpenGLFeatureFactory.getInstance().OPENGL):
            if image.getType() >= OpenGLESImage.TYPE:
                openGLESImage: OpenGLESImage = (image)
                openGLESImage.imageProcessor = ModifierOpenGLESImageProcessor.getInstance()
                openGLESImage.openGLESImageProperties.alphaf = (float(alphaInt)) / 255.0
                return
        self.setAlphaSWT(image, alphaInt)
    

    def setAlphaSWT(self, image: Image, alphaInt: int) -> None:
        alpha: int = ((int(alphaInt) + 128) % 256 - 128)
        newBufferedImage: Image = None
        if image.isMutable():
            swtImage: SwtMutableImage = image
            newBufferedImage = swtImage.getImage()
        else:
            swtImage: SwtImmutableImage = image
            newBufferedImage = swtImage.getImage()
        newBufferedImage.getImageData().alpha = alpha
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        try:
            newImageArray: list[Image] = [None] * (len(originalImageArray))
            size: int = len(newImageArray)
            originalImage: Image = None
            for index in range(0, size):
                originalImage = originalImageArray[index]
                image: Image = self.imageCopyUtil.createImage(originalImage)
                newImageArray[index] = image
            return newImageArray
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, "getImageArray", e)
            return originalImageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        pass
    

    def reset(self) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.image.opengles.ModifierOpenGLESImageProcessor import ModifierOpenGLESImageProcessor
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.eclipse.swt.graphics.ImageData import ImageData
from org.microemu.device.swt.SwtImmutableImage import SwtImmutableImage
from org.microemu.device.swt.SwtMutableImage import SwtMutableImage
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil


ImageModifierUtil.instance = ImageModifierUtil()

