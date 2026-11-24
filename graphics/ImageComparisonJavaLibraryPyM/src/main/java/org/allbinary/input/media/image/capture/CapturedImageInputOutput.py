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
# package org.allbinary.input.media.image.capture

from __future__ import annotations

from org.allbinary.media.image.io.ImageIOInterface import ImageIOInterface


class CapturedImageInputOutput(ImageIOInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def save_j1(self, frame: int) -> None:
        from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
        from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
        from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
        from org.allbinary.string.CommonStrings import CommonStrings
        commonStrings: CommonStrings = CommonStrings.getInstance()
        capturedBufferedImageCacheable: BufferedImageFrameCacheable = ((CapturedBufferedImagesCacheSingleton.getInstance()).get(frame))
        self.logUtil.putF(("Saving: " + str(capturedBufferedImageCacheable)), self, commonStrings.SAVE)
        self.save(capturedBufferedImageCacheable.getBufferedImage(), frame)
    

    def save_j2(self, bufferedImage: BufferedImage, frame: int) -> None:
        from org.allbinary.input.automation.ImageOutputData import ImageOutputData
        from org.allbinary.logic.java.number.LongUtil import LongUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
        from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
        from org.allbinary.media.image.ImageUtil import ImageUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        commonStrings: CommonStrings = CommonStrings.getInstance()
        imageUtil: ImageUtil = ImageUtil.getInstance()
        filePathStringBuffer: StringMaker = StringMaker()
        filePathStringBuffer.append(ImageOutputData.SAVE_PATH)
        filePathStringBuffer.append(LongUtil.fillIn(str(frame)))
        filePathStringBuffer.append(MediaDataFactory.getInstance().JPG.getExtension())
        filePath: str = str(filePathStringBuffer)
        self.logUtil.putF(("Image File Path: " + filePath + imageUtil.toString(bufferedImage)), self, commonStrings.SAVE)
        imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
        imagePersistanceUtil.saveWithImageIO(filePath, bufferedImage)

    def save(self, *args):
        return getattr(self, "save_j" + str(len(args)))(*args)
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.input.automation.ImageOutputData import ImageOutputData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.number.LongUtil import LongUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
# from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
# from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
# from org.allbinary.media.image.ImageUtil import ImageUtil
# from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
# from org.allbinary.string.CommonStrings import CommonStrings


