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

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from playn.core.Callback import Callback


class ImageModifierUtil:
    class ImageCopyCallback(Callback):

        def _init_fields(self) -> None:
            if "imageModifierUtil" not in vars(self): self.imageModifierUtil: ImageModifierUtil = None
            if "imageArray" not in vars(self): self.imageArray: list[Image] = None
            if "index" not in vars(self): self.index: int = 0
            if "image" not in vars(self): self.image: Image = None
            if "image3" not in vars(self): self.image3: CoreImage = None
        

        def __init__(self, imageModifierUtil: ImageModifierUtil, imageArray: list[Image], index: int, image: Image, image3: CoreImage) -> None:
            from javax.microedition.lcdui.Image import Image
            from playn.core.CoreImage import CoreImage
            __class__._init_fields(self)
            self.imageModifierUtil = imageModifierUtil
            self.imageArray = imageArray
            self.index = index
            self.image = image
            self.image3 = image3
        

        def onSuccess(self, resource: object) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.microemu.device.ResourceCallbackStrings import ResourceCallbackStrings
            logUtil: LogUtil = LogUtil.getInstance()
            resourceCallbackStrings: ResourceCallbackStrings = self.imageModifierUtil.resourceCallbackStrings
            logUtil.putF(str(resourceCallbackStrings.DONE) + self.image.getName(), self, resourceCallbackStrings.HANDLE_IMAGE)
            self.imageModifierUtil.copy(self.imageArray, self.index, self.image, self.image3)
        

        def onFailure(self, e: BaseException) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.logic.string.StringMaker import StringMaker
            from org.microemu.device.ResourceCallbackStrings import ResourceCallbackStrings
            logUtil: LogUtil = LogUtil.getInstance()
            resourceCallbackStrings: ResourceCallbackStrings = self.imageModifierUtil.resourceCallbackStrings
            logUtil.put(str(StringMaker().append(self.imageModifierUtil.commonStrings.EXCEPTION_LABEL).append(resourceCallbackStrings.ERROR).append(self.image.getName())), self, resourceCallbackStrings.HANDLE_IMAGE, e)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.microemu.device.ResourceCallbackStrings import ResourceCallbackStrings
        from playn.html.HTMLPlaynUtil import HTMLPlaynUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.resourceCallbackStrings: ResourceCallbackStrings = ResourceCallbackStrings.getInstance()
        self.playnUtil: HTMLPlaynUtil = HTMLPlaynUtil.getInstance()
        if "alphaArray" not in vars(self): self.alphaArray: list[bool] = None

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstanceOrCreate() -> ImageModifierUtil:
        return ImageModifierUtil()
    

    def setColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def changeColor(self, unusedOriginalImage: Image, image: Image, imageIndex: int, basicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def setAlpha(self, originalImage: Image, image: Image, imageIndex: int, alpha: int) -> None:
        from javax.microedition.lcdui.Image import Image
        alphaF: float = float(alpha)
        alphaFloat: float = alphaF / 255.0
        self.setAlphaF(originalImage, image, imageIndex, alphaFloat)
    

    def setAlphaF(self, originalImage: Image, image: Image, imageIndex: int, alpha: float) -> None:
        from javax.microedition.lcdui.Image import Image
        if self.alphaArray[imageIndex]:
            self.alphaArray[imageIndex] = False
            self.setAlpha2(originalImage, image, imageIndex, alpha)
    

    def setAlpha2(self, originalImage: Image, image: Image, imageIndex: int, alpha: float) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.microemu.device.playn.PlaynImage import PlaynImage
        from playn.core.Canvas import Canvas
        from playn.core.CoreImage import CoreImage
        from playn.core.ImageImpl import ImageImpl
        htmlImage: PlaynImage = image
        canvasImage: ImageImpl = htmlImage.getImage()
        originalPlaynImage: CoreImage = (originalImage).getImage()
        canvas: Canvas = self.playnUtil.getCanvas(canvasImage)
        canvas.clear()
        canvas.setAlpha(alpha)
        canvas.draw(originalPlaynImage, 0, 0)
    

    def setAlpha3(self, image: Image, alpha: float) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.microemu.device.playn.PlaynImage import PlaynImage
        from playn.core.Canvas import Canvas
        from playn.core.ImageImpl import ImageImpl
        alphaF: float = alpha
        alphaFloat: float = alphaF / 255.0
        htmlImage: PlaynImage = image
        canvasImage: ImageImpl = htmlImage.getImage()
        canvas: Canvas = self.playnUtil.getCanvas(canvasImage)
        canvas.setAlpha(alphaFloat)
    

    def getImageArray(self, originalImageArray: list[Image]) -> list[Image]:
        from javax.microedition.lcdui.Image import Image
        size: int = len(originalImageArray)
        self.alphaArray = [False] * (size)
        imageArray: list[Image] = [None] * (size)
        for index in range(0, size):
            imageArray[index] = originalImageArray[index]
            self.handleImage(imageArray, index, originalImageArray[index])
        return imageArray
    

    def handleImage(self, imageArray: list[Image], index: int, image: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.microemu.device.playn.PlaynImage import PlaynImage
        from playn.core.CoreImage import CoreImage
        image3: CoreImage = (image).getImage()
        if image3 is not None:
            if java_predicate(image3, "isReady") or image3.width() + image3.height() <= 0 or image.getName() == self.resourceCallbackStrings.FROM_DATA:
                self.copy(imageArray, index, image, image3)
            else:
                callback: Callback = java_new_inner(self, ImageModifierUtil.ImageCopyCallback, self, imageArray, index, image, image3)
                image3.addCallback(callback)
        else:
            self.logUtil.putF(self.resourceCallbackStrings.NULL + java_predicate(image, "isMutable"), self, self.resourceCallbackStrings.HANDLE_IMAGE)
    

    def copy(self, imageArray: list[Image], index: int, image: Image, image3: CoreImage) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.Anchor import Anchor
        from playn.core.CoreImage import CoreImage
        try:
            image2: Image = Image.createImageWH(int(image3.width()), int(image3.height()))
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
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.microemu.device.playn.PlaynImage import PlaynImage
# from org.microemu.device.ResourceCallbackStrings import ResourceCallbackStrings
# from playn.core.Canvas import Canvas
# from playn.core.CoreImage import CoreImage
# from playn.core.ImageImpl import ImageImpl
# from playn.html.HTMLPlaynUtil import HTMLPlaynUtil


