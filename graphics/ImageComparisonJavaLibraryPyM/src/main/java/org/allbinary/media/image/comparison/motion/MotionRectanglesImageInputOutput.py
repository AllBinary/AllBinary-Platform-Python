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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations

from org.allbinary.media.image.io.ImageIOInterface import ImageIOInterface


class MotionRectanglesImageInputOutput(ImageIOInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.NUMBER_OF_IMAGES: int = 1
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def save(self, frame: int) -> None:
        from org.allbinary.media.image.comparison.motion.AllMotionRectanglesResultsCacheSingleton import AllMotionRectanglesResultsCacheSingleton
        from org.allbinary.media.image.comparison.motion.ConsolidatedMotionRectanglesResultsCacheSingleton import ConsolidatedMotionRectanglesResultsCacheSingleton
        from org.allbinary.media.image.comparison.motion.ConstrainedMotionRectanglesResultsCacheSingleton import ConstrainedMotionRectanglesResultsCacheSingleton
        commonStrings: CommonStrings = CommonStrings.getInstance()
        motionRectanglesResultsFrameCacheable: MotionRectanglesResultsFrameCacheable = (AllMotionRectanglesResultsCacheSingleton.getInstance()).get(frame)
        if motionRectanglesResultsFrameCacheable is not None:
            motionRectangles: MotionRectangles = motionRectanglesResultsFrameCacheable.getMotionRectangles()
            self.save(motionRectangles, frame)
            motionRectanglesResultsFrameCacheable = (ConsolidatedMotionRectanglesResultsCacheSingleton.getInstance()).get(frame)
            motionRectangles = motionRectanglesResultsFrameCacheable.getMotionRectangles()
            self.save(motionRectangles, frame)
            motionRectanglesResultsFrameCacheable = (ConstrainedMotionRectanglesResultsCacheSingleton.getInstance()).get(frame)
            motionRectangles = motionRectanglesResultsFrameCacheable.getMotionRectangles()
            self.save(motionRectangles, frame)
        else:
            self.logUtil.putF("No Motion Rectangle Results for Frame: " + str(frame), self, commonStrings.SAVE)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def save(self, motionRectangles: MotionRectangles, frame: int) -> None:
        from org.allbinary.media.image.comparison.motion.Color import Color
        commonStrings: CommonStrings = CommonStrings.getInstance()
        filePathStringBuffer: StringMaker = StringMaker()
        filePathStringBuffer.append(ImageOutputData.SAVE_PATH)
        filePathStringBuffer.append(LongUtil.fillIn(str(frame)))
        filePathStringBuffer.append("_")
        filePathStringBuffer.append(motionRectangles.getName())
        filePathStringBuffer1: StringMaker = StringMaker()
        filePathStringBuffer1.append(str(filePathStringBuffer))
        filePathStringBuffer1.append("_1")
        filePathStringBuffer1.append(MediaDataFactory.getInstance().JPG.getExtension())
        filePathStringBuffer2: StringMaker = StringMaker()
        filePathStringBuffer2.append(str(filePathStringBuffer))
        filePathStringBuffer2.append("_2")
        filePathStringBuffer2.append(MediaDataFactory.getInstance().JPG.getExtension())
        filePathStringBuffer3: StringMaker = StringMaker()
        filePathStringBuffer3.append(str(filePathStringBuffer))
        filePathStringBuffer3.append(MediaDataFactory.getInstance().JPG.getExtension())
        self.logUtil.putF("Motion Image File Path 1: " + str(filePathStringBuffer1), self, commonStrings.SAVE)
        self.logUtil.putF("Motion Image File Path 2: " + str(filePathStringBuffer2), self, commonStrings.SAVE)
        self.logUtil.putF("Motion Image File Path 2: " + str(filePathStringBuffer3), self, commonStrings.SAVE)
        bufferedImageCacheables: list[BufferedImageCacheable] = [None] * (self.NUMBER_OF_IMAGES)
        imageComparisonInfo: ImageComparisonResult = motionRectangles.getImageComparisonResult()
        originalBufferedImage: BufferedImage = imageComparisonInfo.getBufferedImages()[0]
        bufferedImageInfo: BufferedImageInfo = BufferedImageInfoFactory.getInstance(imageComparisonInfo.imageWidth, imageComparisonInfo.imageHeight, originalBufferedImage.getType())
        poolInterface: PoolInterface = BufferedImagePoolSingleton.getInstance()
        for index in range(0, self.NUMBER_OF_IMAGES):
            bufferedImageCacheables[index] = poolInterface.remove(bufferedImageInfo)
        bufferedImageCacheables[0].getBufferedImage().setData(imageComparisonInfo.getBufferedImages()[1].getData())
        if self.NUMBER_OF_IMAGES > 1:
            bufferedImageCacheables[1].getBufferedImage().setData(imageComparisonInfo.getBufferedImages()[1].getData())
        bufferedImageGraphicsArray: list[Graphics] = None
        bufferedImageGraphicsArray = [None] * (self.NUMBER_OF_IMAGES)
        for index in range(0, self.NUMBER_OF_IMAGES):
            bufferedImageGraphicsArray[index] = bufferedImageCacheables[index].getBufferedImage().getGraphics()
        rectangelList: BasicArrayList = motionRectangles.getVector()
        size: int = rectangelList.size()
        for index2 in range(0, size):
            motionRectangle: MotionRectangle = rectangelList.get(index2)
            rectangle: Rectangle = motionRectangle.getRectangle()
            for index in range(0, self.NUMBER_OF_IMAGES):
                bufferedImageGraphicsArray[index].setColor(Color.ORANGE)
                bufferedImageGraphicsArray[index].drawRect(rectangle.x, rectangle.y, rectangle.width, rectangle.height)
        imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
        if self.NUMBER_OF_IMAGES > 1:
            imagePersistanceUtil.saveWithImageIO(str(filePathStringBuffer1), bufferedImageCacheables[1].getBufferedImage())
        imagePersistanceUtil.saveWithImageIO(str(filePathStringBuffer2), bufferedImageCacheables[0].getBufferedImage())
        if self.NUMBER_OF_IMAGES > 2:
            imagePersistanceUtil.saveWithImageIO(str(filePathStringBuffer3), bufferedImageCacheables[2].getBufferedImage())
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.ImageOutputData import ImageOutputData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.number.LongUtil import LongUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.logic.util.cache.PoolInterface import PoolInterface
from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
from org.allbinary.media.image.cache.BufferedImageCacheable import BufferedImageCacheable
from org.allbinary.media.image.cache.BufferedImageInfo import BufferedImageInfo
from org.allbinary.media.image.cache.BufferedImageInfoFactory import BufferedImageInfoFactory
from org.allbinary.media.image.cache.BufferedImagePoolSingleton import BufferedImagePoolSingleton
from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
from org.allbinary.string.CommonStrings import CommonStrings


