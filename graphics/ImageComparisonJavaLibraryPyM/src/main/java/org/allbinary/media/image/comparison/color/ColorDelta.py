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
        if "rgb1" not in vars(self): self.rgb1: int = 0
        if "rgb2" not in vars(self): self.rgb2: int = 0
        if "key" not in vars(self): self.key: object = None
    

    def __init__(self, rgb1: int, rgb2: int) -> None:
        __class__._init_fields(self)
        self.setRgb1(rgb1)
        self.setRgb2(rgb2)
        self.key = ColorDelta.getKey_j2(rgb1, rgb2)
            
    

    def getKey_j0(self) -> object:
        return self.key
    

    @staticmethod
    def getKey_j2(rgb1: int, rgb2: int) -> object:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        return str(StringMaker().append(str(rgb1)).append(CommonSeps.getInstance().UNDERSCORE).append(str(rgb2)))

    def getKey(self, *args):
        implementation = __class__.__dict__.get("getKey_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getKey(*args)
    

    def getRgb1(self) -> int:
        return self.rgb1
    

    def setRgb1(self, rgb1: int) -> None:
        self.rgb1 = rgb1
    

    def getRgb2(self) -> int:
        return self.rgb2
    

    def setRgb2(self, rgb2: int) -> None:
        self.rgb2 = rgb2
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        return str(StringMaker().append("ColorDelta: ").append(StringUtil.getInstance().toString(self.getKey())).append(" RGB1: ").appendint(self.getRgb1()).append(" RGB2: ").appendint(self.getRgb2()))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonSeps import CommonSeps


