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
# package org.allbinary.media.image.comparison.color

from __future__ import annotations

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class ColorDelta(CacheableInterface):

    def _init_fields(self) -> None:
        self.rgb1: int = 0
        self.rgb2: int = 0
        self.key: object = None
    

    def __init__(self, rgb1: int, rgb2: int) -> None:
        self._init_fields()
        self.setRgb1(rgb1)
        self.setRgb2(rgb2)
        self.key = ColorDelta.getKey(rgb1, rgb2)
    

    def getKey(self) -> object:
        return self.key
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getKey(rgb1: int, rgb2: int) -> object:
        return str(StringMaker().append(str(rgb1)).append(CommonSeps.getInstance().UNDERSCORE).append(str(rgb2)))
    

    def getRgb1(self) -> int:
        return self.rgb1
    

    def setRgb1(self, rgb1: int) -> None:
        self.rgb1 = rgb1
    

    def getRgb2(self) -> int:
        return self.rgb2
    

    def setRgb2(self, rgb2: int) -> None:
        self.rgb2 = rgb2
    

    def toString(self) -> str:
        return str(StringMaker().append("ColorDelta: ").append(StringUtil.getInstance().toString(self.getKey())).append(" RGB1: ").appendint(self.getRgb1()).append(" RGB2: ").appendint(self.getRgb2()))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


