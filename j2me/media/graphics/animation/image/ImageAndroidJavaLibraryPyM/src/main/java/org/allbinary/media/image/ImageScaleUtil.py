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



class ImageScaleUtil:
    instance: ImageScaleUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.anchor: int = Anchor.TOP_LEFT
        self.imageBasicArrayList: BasicArrayList = BasicArrayListD()
        self.scaledImageBasicArrayList: BasicArrayList = BasicArrayListD()
        self.scaleXBasicArrayList: BasicArrayList = BasicArrayListD()
        self.scaleYBasicArrayList: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> ImageScaleUtil:
        return ImageScaleUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createImage2(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool) -> Image:
        return self.createImage3(imageCache, originalImage, scaleNominatorX, scaleDenominatorX, scaleNominatorY, scaleDenominatorY, cached, True)
    

    # throws Exception
    def createImage3(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool, mutable: bool) -> Image:
        scaleX: float = scaleNominatorX / scaleDenominatorX
        scaleY: float = scaleNominatorY / scaleDenominatorY
        return self.createImage(imageCache, originalImage, scaleX, scaleY, cached)
    

    # throws Exception
    def createImage(self, imageCache: ImageCache, originalImage: Image, scaleX: float, scaleY: float, cached: bool) -> Image:
        originalAndroidImage: AndroidImageInterface = originalImage
        originalBitmap: Bitmap = originalAndroidImage.getBitmap()
        width: int = int((originalBitmap.getWidth() * scaleX))
        height: int = int((originalBitmap.getHeight() * scaleY))
        index: int = self.imageBasicArrayList.indexOf(originalImage)
        alreadyAvailable: bool = False
        if index >= 0:
            scaleX2Float: float = self.scaleXBasicArrayList.get(index)
            scaleX2: float = float(scaleX2Float)
            scaleY2Float: float = self.scaleYBasicArrayList.get(index)
            scaleY2: float = float(scaleY2Float)
            if scaleX2 == scaleX and scaleY2 == scaleY:
                alreadyAvailable = True
        if alreadyAvailable:
            return self.scaledImageBasicArrayList.get(index)
        else:
            scaledImage: Image = self.getScaledImage(imageCache, originalImage, scaleX, scaleY, width, height, cached)
            self.imageBasicArrayList.add(originalImage)
            self.scaledImageBasicArrayList.add(scaledImage)
            self.scaleXBasicArrayList.add(scaleX)
            self.scaleYBasicArrayList.add(scaleY)
            return scaledImage
    

    # throws Exception
    def getScaledImage(self, imageCache: ImageCache, originalImage: Image, scaleX: float, scaleY: float, width: int, height: int, cached: bool) -> Image:
        image: Image = NullImage.NULL_IMAGE
        if cached:
            image = imageCache.get(type(self).__module__ + "." + type(self).__qualname__, width, height)
        else:
            image = imageCache.get(self.commonStrings.CREATE_IMAGE, width, height)
        if image.isMutable():
            matrix: Matrix = Matrix()
            self.scale(image, matrix, scaleX, scaleY)
            image.getGraphics().drawImage(originalImage, 0, 0, self.anchor)
            return image
        else:
            raise Exception("Not Mutable")
    

    def scale(self, image: Image, matrix: Matrix, scaleX: float, scaleY: float) -> None:
        matrix.setScale(scaleX, scaleY)
        canvas: Canvas = (image).getCanvas()
        canvas.concat(matrix)
from android.graphics.Bitmap import Bitmap
from android.graphics.Canvas import Canvas
from android.graphics.Matrix import Matrix
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface


ImageScaleUtil.instance = ImageScaleUtil()

