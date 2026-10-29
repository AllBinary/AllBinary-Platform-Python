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
# package org.allbinary.media.image.cache

from __future__ import annotations

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class BufferedImageCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.key: BufferedImageInfo = None
        self.bufferedImage: BufferedImage = None
    

    def __init__(self, key: BufferedImageInfo) -> None:
        self._init_fields()
        self.key = key
        self.setBufferedImage(BufferedImage(key.getWidth(), key.getHeight(), key.getType()))
    

    def getKey(self) -> object:
        return self.key
    

    def getBufferedImage(self) -> BufferedImage:
        return self.bufferedImage
    

    def setBufferedImage(self, bufferedImage: BufferedImage) -> None:
        self.bufferedImage = bufferedImage
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(" ")
        stringBuffer.append(str(self.getKey()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.string.StringMaker import StringMaker


