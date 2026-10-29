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



class ImageCacheBase:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.imageFactory: ImageFactory = ImageFactory.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.SIZE: int = 128
        self.widths: list[int] = [0] * (self.SIZE)
        self.heights: list[int] = [0] * (self.SIZE)
        self.listOfList: list[BasicArrayList] = [None] * (self.SIZE)
        self.availableListOfList: list[BasicArrayList] = [None] * (self.SIZE)
        self.volume: int = 0
        self.nextIndex: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
        for index in range(len(self.listOfList) - 1, 0 - 1, -1):
            self.listOfList[index] = BasicArrayListD()
        for index in range(len(self.availableListOfList) - 1, 0 - 1, -1):
            self.availableListOfList[index] = BasicArrayListD()
    

    def getImage(self, resourceId: object) -> Image:
        imageCanBeNull: object = self.hashtable.get(resourceId)
        if imageCanBeNull is None:
            return NullImage.NULL_IMAGE
        return imageCanBeNull
    

    def releaseAll(self) -> None:
        for index in range(len(self.listOfList) - 1, 0 - 1, -1):
            self.availableListOfList[index].clear()
            self.availableListOfList[index].addAllList(self.listOfList[index])
        self.logUtil.putF(str(StringMaker().append("ImageCache: ").append(str(self))), self, "releaseAll")
    

    def getIndexWH(self, width: int, height: int) -> int:
        foundIndex: int = -1
        size: int = len(self.widths)
        for index in range(0, size):
            if self.widths[index] == width and self.heights[index] == height:
                foundIndex = index
                return foundIndex
        return foundIndex
    

    def getFromAvailable(self, foundIndex: int, width: int, height: int) -> Image:
        if foundIndex != -1:
            if self.availableListOfList[foundIndex].size() > 0:
                list_: BasicArrayList = self.availableListOfList[foundIndex]
                return list_.removeAt(list_.size() - 1)
        return NullImage.NULL_IMAGE
    

    # throws Exception
    def get(self, caller: str, width: int, height: int) -> Image:
        raise RuntimeError()
    

    # throws Exception
    def getWithKey(self, key: object) -> Image:
        raise RuntimeError()
    

    # throws Exception
    def createImage(self, caller: str, width: int, height: int) -> Image:
        return self.imageFactory.createImage(caller, width, height)
    

    # throws Exception
    def createImageFromInputStream(self, key: object, inputStream: InputStream) -> Image:
        return self.imageFactory.createImageFromInputStream(key, inputStream)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        for index in range(self.nextIndex - 1, 0 - 1, -1):
            width: int = self.widths[index]
            height: int = self.heights[index]
            total: int = self.listOfList[index].size()
            totalAvailable: int = self.availableListOfList[index].size()
            stringBuffer.append(" w: ")
            stringBuffer.appendint(width)
            stringBuffer.append(" h: ")
            stringBuffer.appendint(height)
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            stringBuffer.append(CommonLabels.getInstance().TOTAL_LABEL)
            stringBuffer.appendint(total)
            stringBuffer.append(" available: ")
            stringBuffer.appendint(totalAvailable)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getHashtableP(self) -> ABHashtable[object, object]:
        return self.hashtable
    

    def init(self, image: Image) -> None:
        pass
    

    def initProgress(self) -> None:
        pass
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.image.ImageFactory import ImageFactory


