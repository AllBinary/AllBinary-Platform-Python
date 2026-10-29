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

from org.allbinary.media.image.io.ImageIOInterface import ImageIOInterface


class ComparisonImageInputOutput(ImageIOInterface):
    ROOT_NAME: str = "_Changed_"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def save(self, frame: int) -> None:
        from org.allbinary.media.image.comparison.ImageComparisonResultCacheSingleton import ImageComparisonResultCacheSingleton
        commonStrings: CommonStrings = CommonStrings.getInstance()
        if frame > 0:
            imageComparisonResultFrameCacheable: ImageComparisonResultFrameCacheable = (ImageComparisonResultCacheSingleton.getInstance()).get(frame)
            if imageComparisonResultFrameCacheable is not None:
                imageComparisonResult: ImageComparisonResult = imageComparisonResultFrameCacheable.getImageComparisonResult()
                self.save(imageComparisonResult, imageComparisonResultFrameCacheable.getFrame())
            else:
                self.logUtil.putF("Comparison Results Not Available for Output: " + str(frame), self, commonStrings.SAVE)
        else:
            self.logUtil.putF("No Comparison Results: for first frame: " + str(frame), self, commonStrings.SAVE)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def save(self, imageComparisonResult: ImageComparisonResult, frame: int) -> None:
        from org.allbinary.media.image.comparison.ChangedPixelsUtil import ChangedPixelsUtil
        commonStrings: CommonStrings = CommonStrings.getInstance()
        filePathStringBuffer: StringMaker = StringMaker()
        filePathStringBuffer.append(ImageOutputData.SAVE_PATH)
        filePathStringBuffer.append(LongUtil.fillIn(str(frame)))
        filePathStringBuffer.append(ComparisonImageInputOutput.ROOT_NAME)
        filePathStringBuffer1: StringMaker = StringMaker()
        filePathStringBuffer1.append(str(filePathStringBuffer))
        filePathStringBuffer1.append("_1")
        filePathStringBuffer1.append(MediaDataFactory.getInstance().JPG.getExtension())
        filePath1: str = str(filePathStringBuffer1)
        filePathStringBuffer2: StringMaker = StringMaker()
        filePathStringBuffer2.append(str(filePathStringBuffer))
        filePathStringBuffer2.append("_2")
        filePathStringBuffer2.append(MediaDataFactory.getInstance().JPG.getExtension())
        filePath2: str = str(filePathStringBuffer2)
        bufferedImageCacheables: list[BufferedImageCacheable] = ChangedPixelsUtil.generateBufferedImageChacheables(imageComparisonResult)
        self.logUtil.putF("Comparison Image File Path 1: " + filePath1, self, commonStrings.SAVE)
        self.logUtil.putF("Comparison Image File Path 2: " + filePath2, self, commonStrings.SAVE)
        bufferedImageArray: list[BufferedImage] = [None] * (2)
        bufferedImageArray[0] = bufferedImageCacheables[0].getBufferedImage()
        bufferedImageArray[1] = bufferedImageCacheables[1].getBufferedImage()
        imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
        imagePersistanceUtil.saveWithImageIO(filePath1, bufferedImageArray[0])
        imagePersistanceUtil.saveWithImageIO(filePath2, bufferedImageArray[1])
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.input.automation.ImageOutputData import ImageOutputData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.number.LongUtil import LongUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
from org.allbinary.media.image.cache.BufferedImageCacheable import BufferedImageCacheable
from org.allbinary.string.CommonStrings import CommonStrings


