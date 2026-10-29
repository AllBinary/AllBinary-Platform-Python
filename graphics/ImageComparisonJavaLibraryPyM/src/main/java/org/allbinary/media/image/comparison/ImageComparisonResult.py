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
# package org.allbinary.media.image.comparison

from __future__ import annotations



class ImageComparisonResult:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.bufferedImages: list[BufferedImage] = [None] * (2)
        self.name: str = None
        self.isSameHeight: bool = False
        self.isSameWidth: bool = False
        self.imageHeight: int = None
        self.imageWidth: int = None
        self.nonMatchingPixelVector: BasicArrayList = None
        self.frameOne: int = None
        self.frameTwo: int = None
        self.pixelsThatMatch: int = 0
        self.pixelsIgnored: int = 0
        self.tolerance: int = 0
        self.matchingPercent: float = float(-1)
    

    def __init__(self, name: str, bufferedImage: BufferedImage, bufferedImage2: BufferedImage, frameOne: int, frameTwo: int, tolerance: int) -> None:
        self._init_fields()
        self.name = name
        self.nonMatchingPixelVector = BasicArrayListD()
        self.bufferedImages[0] = bufferedImage
        self.bufferedImages[1] = bufferedImage2
        self.frameOne = frameOne
        self.frameTwo = frameTwo
        self.setTolerance(0)
        imageHeight: int = bufferedImage.getHeight()
        imageWidth: int = bufferedImage.getWidth()
        if bufferedImage.getHeight() != bufferedImage2.getHeight():
            self.isSameHeight = False
            if imageHeight > bufferedImage2.getHeight():
                imageHeight = bufferedImage2.getHeight()
        else:
            self.isSameHeight = True
        if bufferedImage.getWidth() != bufferedImage2.getWidth():
            self.isSameWidth = False
            if imageWidth > bufferedImage2.getWidth():
                imageWidth = bufferedImage2.getWidth()
        else:
            self.isSameWidth = True
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        if not self.isSameWidth or not self.isSameHeight:
            imageUtil: ImageUtil = ImageUtil.getInstance()
            self.logUtil.putF("Images were not the same size? Most likely a resolution change.", self, self.commonStrings.CONSTRUCTOR)
            self.logUtil.putF("1: " + imageUtil.toString(bufferedImage), self, self.commonStrings.CONSTRUCTOR)
            self.logUtil.putF("2: " + imageUtil.toString(bufferedImage2), self, self.commonStrings.CONSTRUCTOR)
    

    def getMatchingPercent(self) -> float:
        if self.matchingPercent == float(-1):
            self.matchingPercent = float(self.pixelsThatMatch) / float((self.imageWidth * self.imageHeight))
        return self.matchingPercent
    

    def add(self, pixel: PixelDelta) -> None:
        self.nonMatchingPixelVector.add(pixel)
    

    def getNonMatchingPixelVector(self) -> BasicArrayList:
        return self.nonMatchingPixelVector
    

    def toString(self) -> str:
        return str(StringMaker().append("ImageComparisonInfo: ").append(self.name).append(" Number Of Matching Pixels: ").appendint(self.pixelsThatMatch).append("\nNumber Of Non-Matching Pixels: ").appendint(self.getNonMatchingPixelVector().size()).append("\nNumber Of Pixels Ignored: ").appendint(self.pixelsIgnored).append("\nMatching Percentage: ").appendfloat(self.getMatchingPercent()))

    def __str__(self) -> str:
        return self.toString()
    

    def getBufferedImages(self) -> list[BufferedImage]:
        return self.bufferedImages
    

    def getTolerance(self) -> int:
        return self.tolerance
    

    def setTolerance(self, tolerance: int) -> None:
        self.tolerance = tolerance
    

    def getFrameOne(self) -> int:
        return self.frameOne
    

    def getFrameTwo(self) -> int:
        return self.frameTwo
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.media.image.comparison.pixel.PixelDelta import PixelDelta
from org.allbinary.string.CommonStrings import CommonStrings


