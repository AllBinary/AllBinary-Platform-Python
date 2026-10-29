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


class BufferedImageFrameCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.frame: int = None
        self.bufferedImage: BufferedImage = None
    

    def __init__(self, bufferedImage: BufferedImage, frame: int) -> None:
        self._init_fields()
        self.frame = frame
        self.setBufferedImage(bufferedImage)
    

    def getKey(self) -> object:
        return self.frame
    

    def getBufferedImage(self) -> BufferedImage:
        return self.bufferedImage
    

    def setBufferedImage(self, bufferedImage: BufferedImage) -> None:
        self.bufferedImage = bufferedImage
    

    def getFrame(self) -> int:
        return self.frame
    

    def setFrame(self, frame: int) -> None:
        self.frame = frame
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(" Frame: ")
        stringBuffer.appendlong(self.getFrame())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.string.StringMaker import StringMaker


