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

import math


class ImageComparator:

    def _init_fields(self) -> None:
        self.imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface = None
    

    def __init__(self, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface) -> None:
        self._init_fields()
        self.imageComparatorConstraintsInterface = imageComparatorConstraintsInterface
    

    # throws Exception
    def process(self, imageComparisonInfo: ImageComparisonResult, point: GPoint) -> None:
        isCollsionWithAvoidRectangles: bool = self.imageComparatorConstraintsInterface.isCollisionWithAvoidRectangles(point)
        if not isCollsionWithAvoidRectangles:
            rgb1: int = imageComparisonInfo.getBufferedImages()[0].getRGB(point.getX(), point.getY())
            rgb2: int = imageComparisonInfo.getBufferedImages()[1].getRGB(point.getX(), point.getY())
            automaticCacheInterface: AutomaticCacheInterface = ColorCacheFactory.getInstance()
            colorInteger: int = str(rgb1)
            colorCacheable: ColorCacheable = automaticCacheInterface.get(colorInteger)
            color: Color = colorCacheable.getColor()
            colorInteger2: int = str(rgb2)
            colorCacheable2: ColorCacheable = automaticCacheInterface.get(colorInteger)
            color2: Color = colorCacheable.getColor()
            if self.imageComparatorConstraintsInterface.isColorAllowed(0, point, color) or self.imageComparatorConstraintsInterface.isColorAllowed(1, point, color2):
                if abs(rgb1 - rgb2) <= imageComparisonInfo.getTolerance():
                    imageComparisonInfo.pixelsThatMatch += 1
                else:
                    imageComparisonInfo.add(PixelDeltaFactory.getInstance(point.getX(), point.getY(), rgb1, rgb2))
        else:
            imageComparisonInfo.pixelsIgnored += 1
    

    # throws Exception
    def compare(self, bufferedImage1: BufferedImage, bufferedImage2: BufferedImage, frameOne: int, frameTwo: int, tolerance: int) -> ImageComparisonResult:
        return self.compare(bufferedImage1, bufferedImage2, frameOne, frameTwo, tolerance, StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def compare(self, bufferedImage1: BufferedImage, bufferedImage2: BufferedImage, frameOne: int, frameTwo: int, tolerance: int, name: str) -> ImageComparisonResult:
        from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
        if bufferedImage1 is None or bufferedImage2 is None:
            raise Exception("Input images must not be null.")
        imageComparisonInfo: ImageComparisonResult = ImageComparisonResult(name, bufferedImage1, bufferedImage2, frameOne, frameTwo, tolerance)
        for indexY in range(0, imageComparisonInfo.imageHeight):
            for indexX in range(0, imageComparisonInfo.imageWidth):
                self.process(imageComparisonInfo, PointFactory.getInstance().createXY(indexX, indexY))
                if imageComparisonInfo.getNonMatchingPixelVector().size() > self.imageComparatorConstraintsInterface.getMaxNonMatchingPixelDeltas():
                    break
        return imageComparisonInfo
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.media.image.comparison.pixel.PixelDeltaFactory import PixelDeltaFactory


