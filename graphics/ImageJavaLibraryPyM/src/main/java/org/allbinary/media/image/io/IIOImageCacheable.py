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
# package org.allbinary.media.image.io

from __future__ import annotations

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class IIOImageCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.key: str = None
        self.iioImage: IIOImage = None
    

    def __init__(self, key: str) -> None:
        self._init_fields()
        self.key = key
    

    def getKey(self) -> object:
        return self.key
    

    def setBufferedImage(self, bufferedImage: BufferedImage) -> None:
        self.setIioImage(IIOImage(bufferedImage, None, None))
    

    def getIioImage(self) -> IIOImage:
        return self.iioImage
    

    def setIioImage(self, iioImage: IIOImage) -> None:
        self.iioImage = iioImage
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(" Reusable IIOImage")
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
# from javax.imageio.IIOImage import IIOImage
from org.allbinary.logic.string.StringMaker import StringMaker


