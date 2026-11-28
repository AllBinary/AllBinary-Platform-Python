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
# package org.allbinary.media.image.comparison.pixel

from __future__ import annotations

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class PixelDelta(CacheableInterface):

    def _init_fields(self) -> None:
        if "point" not in vars(self): self.point: GPoint = None
        if "colorDelta" not in vars(self): self.colorDelta: ColorDelta = None
        if "key" not in vars(self): self.key: object = None
    

    def __init__(self, point: GPoint, colorDelta: ColorDelta) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        __class__._init_fields(self)
        self.setPoint(point)
        self.setColorDelta(colorDelta)
        self.key = PixelDelta.getKey_j2(self.getPoint(), self.getColorDelta())
            
    

    def getKey_j0(self) -> object:
        return self.key
    

    @staticmethod
    def getKey_j2(point: GPoint, colorDelta: ColorDelta) -> object:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.TsUtil import TsUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        from org.allbinary.string.CommonSeps import CommonSeps
        return str(StringMaker().appendint(int(TsUtil.getInstance().hashCode(point))).append(CommonSeps.getInstance().UNDERSCORE).append(str(colorDelta.getKey())))

    def getKey(self, *args):
        implementation = __class__.__dict__.get("getKey_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getKey(*args)
    

    def getPoint(self) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return self.point
    

    def setPoint(self, point: GPoint) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        self.point = point
    

    def getColorDelta(self) -> ColorDelta:
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        return self.colorDelta
    

    def setColorDelta(self, colorDelta: ColorDelta) -> None:
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        self.colorDelta = colorDelta
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        return str(StringMaker().append("PixelDelta: Point: ").append(str(self.point)).append(CommonSeps.getInstance().SPACE).append(str(self.colorDelta)))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.TsUtil import TsUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
# from org.allbinary.string.CommonSeps import CommonSeps


