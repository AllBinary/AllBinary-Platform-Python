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

import sys


class ChangedPixelsUtil:
    START_X: int = 0
    START_Y: int = 0
    OFFSET: int = 0
    SCAN_SIZE: int = 0
    CLEAR_INT_ARRAY: list[int] = [0] * (1800 * 1600)
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def generateBufferedImageChacheables(imageComparisonInfo: ImageComparisonResult) -> list[BufferedImageCacheable]:
        bufferedImageCacheables: list[BufferedImageCacheable] = None
        originalBufferedImage: BufferedImage = imageComparisonInfo.getBufferedImages()[0]
        bufferedImageCacheables = [None] * (2)
        bufferedImageInfo: BufferedImageInfo = BufferedImageInfoFactory.getInstance(imageComparisonInfo.imageWidth, imageComparisonInfo.imageHeight, originalBufferedImage.getType())
        poolInterface: PoolInterface = BufferedImagePoolSingleton.getInstance()
        for index in range(0, len(bufferedImageCacheables)):
            bufferedImageCacheable: BufferedImageCacheable = poolInterface.remove(bufferedImageInfo)
            bufferedImageCacheables[index] = bufferedImageCacheable
            bufferedImageCacheables[index].getBufferedImage().setRGB(ChangedPixelsUtil.START_X, ChangedPixelsUtil.START_Y, bufferedImageInfo.getWidth(), bufferedImageInfo.getHeight(), ChangedPixelsUtil.CLEAR_INT_ARRAY, ChangedPixelsUtil.OFFSET, ChangedPixelsUtil.SCAN_SIZE)
        vector: BasicArrayList = imageComparisonInfo.getNonMatchingPixelVector()
        size: int = vector.size()
        for index in range(0, size):
            pixelDelta: PixelDelta = vector.get(index)
            if pixelDelta.getColorDelta() is None:
                print("ColorDelta", end="")
                sys.exit(0)
            bufferedImageCacheables[0].getBufferedImage().setRGB(pixelDelta.getPoint().getX(), pixelDelta.getPoint().getY(), pixelDelta.getColorDelta().getRgb1())
            bufferedImageCacheables[1].getBufferedImage().setRGB(pixelDelta.getPoint().getX(), pixelDelta.getPoint().getY(), pixelDelta.getColorDelta().getRgb2())
        return bufferedImageCacheables
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.util.cache.PoolInterface import PoolInterface
from org.allbinary.media.image.cache.BufferedImageCacheable import BufferedImageCacheable
from org.allbinary.media.image.cache.BufferedImageInfo import BufferedImageInfo
from org.allbinary.media.image.cache.BufferedImageInfoFactory import BufferedImageInfoFactory
from org.allbinary.media.image.cache.BufferedImagePoolSingleton import BufferedImagePoolSingleton
from org.allbinary.media.image.comparison.pixel.PixelDelta import PixelDelta


