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

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class ImageComparisonResultFrameCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.frame: int = None
        self.imageComparisonResult: ImageComparisonResult = None
    

    def __init__(self, imageComparisonResult: ImageComparisonResult, frame: int) -> None:
        self._init_fields()
        self.setImageComparisonResult(imageComparisonResult)
        self.frame = frame
    

    def getKey(self) -> object:
        return self.frame
    

    def getFrame(self) -> int:
        return self.frame
    

    def setFrame(self, frame: int) -> None:
        self.frame = frame
    

    def getImageComparisonResult(self) -> ImageComparisonResult:
        return self.imageComparisonResult
    

    def setImageComparisonResult(self, imageComparisonResult: ImageComparisonResult) -> None:
        self.imageComparisonResult = imageComparisonResult
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(" Frame: ")
        stringBuffer.appendlong(self.getFrame())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


