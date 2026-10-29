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
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
        self.colorArray: list[int] = [0] * (1)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil.instance
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        pass
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        newBufferedImage: BufferedImage = self.imageUtil.getBufferedImage(image)
        r: int = basicColor.red
        g: int = basicColor.green
        b: int = basicColor.blue
        width: int = image.getWidth()
        height: int = image.getHeight()
        colorModel: ColorModel = None
        dataElements: object = None
        ax: int = 0
        rx: int = 0
        gx: int = 0
        bx: int = 0
        for index in range(0, width):
            for index2 in range(0, height):
                colorModel = newBufferedImage.getColorModel()
                dataElements = newBufferedImage.getRaster().getDataElements(index, index2, None)
                ax = colorModel.getAlpha(dataElements)
                rx = colorModel.getRed(dataElements)
                gx = colorModel.getGreen(dataElements)
                bx = colorModel.getBlue(dataElements)
                if rx != 0 or gx != 0 or bx != 0:
                    newBufferedImage.setRGB(index, index2, (ax << 24) | (r << 16) | (g << 8) | (b))
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        newBufferedImage: BufferedImage = self.imageUtil.getBufferedImage(image)
        MAX: float = 255.0
        r: float = (float(basicColor.red)) / MAX
        g: float = (float(basicColor.green)) / MAX
        b: float = (float(basicColor.blue)) / MAX
        width: int = image.getWidth()
        height: int = image.getHeight()
        colorModel: ColorModel = None
        dataElements: object = None
        ax: int = 0
        rx: int = 0
        gx: int = 0
        bx: int = 0
        for index in range(0, width):
            for index2 in range(0, height):
                colorModel = newBufferedImage.getColorModel()
                dataElements = newBufferedImage.getRaster().getDataElements(index, index2, None)
                ax = colorModel.getAlpha(dataElements)
                rx = colorModel.getRed(dataElements)
                gx = colorModel.getGreen(dataElements)
                bx = colorModel.getBlue(dataElements)
                rx = int(rx * r)
                gx = int(gx * g)
                bx = int(bx * b)
                newBufferedImage.setRGB(index, index2, (ax << 24) | (rx << 16) | (gx << 8) | (bx))
    

    def setAlpha(self, unusedOriginalImage: Image, image: Image, imageIndex: int, alphaInt: int) -> None:
        alpha: int = ((int(alphaInt) + 128) % 256 - 128)
        newBufferedImage: BufferedImage = self.imageUtil.getBufferedImage(image)
        width: int = image.getWidth()
        height: int = image.getHeight()
        raster: WritableRaster = newBufferedImage.getAlphaRaster()
        for index in range(0, width):
            for index2 in range(0, height):
                raster.getPixel(index, index2, self.colorArray)
                self.colorArray[0] = alpha & self.colorArray[0]
                raster.setPixel(index, index2, self.colorArray)
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil
        try:
            newImageArray: list[Image] = [None] * (len(originalImageArray))
            size: int = len(newImageArray)
            originalImage: Image = None
            for index in range(0, size):
                originalImage = originalImageArray[index]
                image: Image = ImageCreationUtil.getInstance().createImageWH(originalImage.getWidth(), originalImage.getHeight())
                image.getGraphics().drawImage(originalImage, 0, 0, Anchor.TOP_LEFT)
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
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.ColorModel import ColorModel
# from java.awt.image.WritableRaster import WritableRaster
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.image.ImageUtil import ImageUtil


ImageModifierUtil.instance = ImageModifierUtil()

