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



class BufferedImageInfo:

    def _init_fields(self) -> None:
        self.width: int = None
        self.height: int = None
        self.type_: int = None
    

    def __init__(self, width: int, height: int, type_: int) -> None:
        self._init_fields()
        self.width = width
        self.height = height
        self.type_ = type_
    

    def getWidth(self) -> int:
        return self.width
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def getHeight(self) -> int:
        return self.height
    

    def setHeight(self, height: int) -> None:
        self.height = height
    

    def getType(self) -> int:
        return self.type_
    

    def setType(self, type_: int) -> None:
        self.type_ = type_
    

    def toString(self) -> str:
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("BufferedImageInfo -")
        stringBuffer.append(commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(self.getWidth())
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(self.getHeight())
        stringBuffer.append(" Type: ")
        stringBuffer.appendint(self.getType())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels


