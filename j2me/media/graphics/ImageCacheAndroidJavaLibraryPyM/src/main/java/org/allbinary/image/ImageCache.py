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
# package org.allbinary.image

from __future__ import annotations

import time
import threading
from org.allbinary.image.ImageCacheBase import ImageCacheBase


class ImageCache(ImageCacheBase):
    NULL_IMAGE_CACHE: ImageCache = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, renderer: object) -> None:
        pass
    

    def getIndex(self, key: object) -> int:
        gdResources: GDResources = GDResources.getInstance()
        resourceStringArray: list[str] = gdResources.resourceStringArray
        size: int = len(resourceStringArray)
        for index in range(0, size):
            if resourceStringArray[index] == key:
                return index
        self.logUtil.putF(str(StringMaker().append("unable to find key: ").append(StringUtil.getInstance().toString(key))), self, self.commonStrings.RUN)
        raise RuntimeError()
    

    # throws Exception
    def get(self, caller: str, width: int, height: int) -> Image:
        foundIndex: int = self.getIndexWH(width, height)
        image: Image = self.getFromAvailable(foundIndex, width, height)
        if image == NullImage.NULL_IMAGE:
            self.volume += width * height
            if self.volume > 32000:
                self.tsUtil.gc()
                self.volume = 0
            image = self.createImage(caller, width, height)
            if foundIndex == -1:
                foundIndex = self.nextIndex
                self.widths[self.nextIndex] = width
                self.heights[self.nextIndex] = height
                self.nextIndex += 1
            self.listOfList[foundIndex].add(image)
        return image
    

    # throws Exception
    def getWithKey(self, key: object) -> Image:
        resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        resourceId: int = resourceUtil.getResourceId(key)
        image: Image = self.getImage(resourceId)
        if image == NullImage.NULL_IMAGE:
            inputStream: InputStream = resourceUtil.getResourceAsStream(key)
            try:
                self.logUtil.putF(Memory.getInfo(), self, self.commonStrings.GET)
                image = self.createImageFromInputStream(key, inputStream)
            except Exception as e:
                self.logUtil.put("Exception: Trying Again After GC", self, self.commonStrings.GET, e)
                self.logUtil.putF(str(StringMaker().append("InputStream: ").append(StringUtil.getInstance().toString(inputStream))), self, self.commonStrings.GET)
                self.tsUtil.gc()
                self.tsUtil.gc()
                self.logUtil.putF(Memory.getInfo(), self, self.commonStrings.GET)
                time.sleep((100) / 1000)
                image = self.createImageFromInputStream(key, inputStream)
            inputStream.close()
            self.hashtable.put(resourceId, image)
        return image
    

    def runTask(self) -> None:
        pass
    

    def isLazy(self) -> bool:
        return False
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.TsUtil import TsUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.game.gd.resource.GDResources import GDResources
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.system.Memory import Memory


ImageCache.NULL_IMAGE_CACHE = ImageCache()

