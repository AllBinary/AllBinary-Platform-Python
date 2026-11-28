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
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.image.ImageCacheBase import ImageCacheBase


@java_inherited_overloads
class ImageCache(ImageCacheBase):
    NULL_IMAGE_CACHE: ImageCache = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("systemWrapper", None)
        vars(self).setdefault("tsUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.TsUtil import TsUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws Exception
    def get_j3(self, caller: str, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
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
    def get_j1(self, key: object) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.system.Memory import Memory
        resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        resourceId: int = resourceUtil.getResourceId(key)
        image: Image = self.getImage(resourceId)
        if image == NullImage.NULL_IMAGE:
            inputStream: InputStream = None
            try:
                self.logUtil.putF(Memory.getInfo(), self, self.commonStrings.GET)
                image = self.createImage(key, inputStream)
            except Exception as e:
                self.logUtil.put("Exception: Trying Again After GC", self, self.commonStrings.GET, e)
                self.logUtil.putF(str(StringMaker().append("InputStream: ").append(str(inputStream))), self, self.commonStrings.GET)
                self.tsUtil.gc()
                self.tsUtil.gc()
                self.logUtil.putF(Memory.getInfo(), self, self.commonStrings.GET)
                time.sleep((100) / 1000)
                image = self.createImage(key, inputStream)
            self.hashtable.put(resourceId, image)
        return image

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
    

    def getIndex(self, key: object) -> int:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.game.gd.resource.GDResources import GDResources
        from org.allbinary.logic.string.StringUtil import StringUtil
        gdResources: GDResources = GDResources.getInstance()
        resourceStringArray: list[str] = gdResources.resourceStringArray
        size: int = len(resourceStringArray)
        for index in range(0, size):
            if resourceStringArray[index] == key:
                return index
        self.logUtil.putF(str(StringMaker().append("unable to find key: ").append(StringUtil.getInstance().toString(key))), self, self.commonStrings.RUN)
        raise RuntimeError()
    

    # throws Exception
    def createImage(self, key: object, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        return Image.createImageLater(key, -1, -1)
    _declared_createImage = createImage
    def createImage(self, *args, **kwargs):
        if len(args) + len(kwargs) == 2 and (kwargs or (True and (args[1] is None or any(base.__name__ == "InputStream" for base in type(args[1]).__mro__)))): return __class__._declared_createImage(self, *args, **kwargs)
        return super().createImage(*args, **kwargs)
    

    def isLazy(self) -> bool:
        raise RuntimeError()
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.TsUtil import TsUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.game.gd.resource.GDResources import GDResources
# from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.system.Memory import Memory


def _ImageCache_NULL_IMAGE_CACHE() -> object:
    return ImageCache()

lazy_static(ImageCache, "NULL_IMAGE_CACHE", _ImageCache_NULL_IMAGE_CACHE)

