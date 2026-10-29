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

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.resourceCallbackStrings: ResourceCallbackStrings = ResourceCallbackStrings.getInstance()
        self.alphaArray: list[bool] = None

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil()
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        pass
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        pass
    

    def setAlpha(self, originalImage: Image, image: Image, imageIndex: int, alpha: int) -> None:
        alphaF: float = float(alpha)
        alphaFloat: float = alphaF / 255.0
        self.setAlphaF(originalImage, image, imageIndex, alphaFloat)
    

    def setAlphaF(self, originalImage: Image, image: Image, imageIndex: int, alpha: float) -> None:
        if self.alphaArray[imageIndex]:
            self.alphaArray[imageIndex] = False
            self.setAlpha2(originalImage, image, imageIndex, alpha)
    

    def setAlpha2(self, originalImage: Image, image: Image, imageIndex: int, alpha: float) -> None:
        htmlImage: PlaynImage = image
        canvasImage: CanvasImage = htmlImage.getImage()
        originalPlaynImage: Image = (originalImage).getImage()
        canvas: Canvas = canvasImage.canvas()
        canvas.clear()
        canvas.setAlpha(alpha)
        canvas.drawImage(originalPlaynImage, 0, 0)
    

    def setAlpha3(self, image: Image, alpha: float) -> None:
        alphaF: float = alpha
        alphaFloat: float = alphaF / 255.0
        htmlImage: PlaynImage = image
        canvasImage: CanvasImage = htmlImage.getImage()
        canvas: Canvas = canvasImage.canvas()
        canvas.setAlpha(alphaFloat)
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        size: int = len(originalImageArray)
        self.alphaArray = [False] * (size)
        imageArray: list[Image] = [None] * (size)
        for index in range(0, size):
            imageArray[index] = originalImageArray[index]
            self.handleImage(imageArray, index, originalImageArray[index])
        return imageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        image3: Image = (image).getImage()
        if image3 is not None:
            if image3.isReady() or image3.width() + image3.height() <= 0 or image.getName() == self.resourceCallbackStrings.FROM_DATA:
                self.copy(imageArray, index, image, image3)
            else:
                callback: Callback = (Callback()  # Java anonymous class body:
#                     
# 
#                     def onSuccess(self, resource: object) -> None:
#                         logUtil: LogUtil = LogUtil.getInstance()
#                         logUtil.putF(str(self.resourceCallbackStrings.DONE) + image.getName(), self, self.resourceCallbackStrings.HANDLE_IMAGE)
#                         self.copy(imageArray, index, image, image3)
#                     
# 
#                     def onFailure(self, e: BaseException) -> None:
#                         logUtil: LogUtil = LogUtil.getInstance()
#                         logUtil.putF(str(StringMaker().append(self.commonStrings.EXCEPTION_LABEL).append(self.resourceCallbackStrings.ERROR).append(image.getName())), self, self.resourceCallbackStrings.HANDLE_IMAGE)
)
                image3.addCallback(callback)
        else:
            self.logUtil.putF(self.resourceCallbackStrings.NULL + image.isMutable(), self, self.resourceCallbackStrings.HANDLE_IMAGE)
    

    def copy(self, imageArray: list[Image], index: int, image: Image, image3: Image) -> None:
        try:
            image2: Image = Image.createImage(image3.width(), image3.height())
            graphics: Graphics = image2.getGraphics()
            graphics.drawImage(image, 0, 0, Anchor.TOP_LEFT)
            imageArray[index] = image2
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION_LABEL + self.resourceCallbackStrings.DONE, self, self.resourceCallbackStrings.HANDLE_IMAGE)
    

    def reset(self) -> None:
        size: int = len(self.alphaArray)
        for index in range(0, size):
            self.alphaArray[index] = True
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.microemu.device.playn.PlaynImage import PlaynImage
from org.microemu.device.ResourceCallbackStrings import ResourceCallbackStrings
from playn.core.Canvas import Canvas
from playn.core.CanvasImage import CanvasImage
from playn.core.util.Callback import Callback


