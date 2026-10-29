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



class PixelDeltaFactory:
    cacheInterface: AutomaticCacheInterface = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def _static_init() -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        instance: str = "PixelDeltaFactory"
        try:
            logUtil.putF(commonStrings.START, instance, STATIC_BLOCK)
            PixelDeltaFactory.cacheInterface = CacheInterfaceFactory.getInstance(CacheTypeFactory.getInstance().CACHE, CachePolicyFactory.getInstance().THIRTY_MINUTES_TEN_THOUSAND_MAX)
            logUtil.putF(commonStrings.END, instance, STATIC_BLOCK)
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, instance, STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    @staticmethod
    def getInstance(x: int, y: int, rgb1: int, rgb2: int) -> PixelDelta:
        from org.allbinary.media.image.comparison.pixel.PixelDelta import PixelDelta
        from org.allbinary.media.image.comparison.pixel.PixelDelta import PixelDelta
        point: GPoint = PointFactory.getInstance().createXY(x, y)
        colorDelta: ColorDelta = ColorDeltaFactory.getInstance(rgb1, rgb2)
        pixelDelta: PixelDelta = PixelDeltaFactory.cacheInterface.get(PixelDelta.getKey(point, colorDelta))
        if pixelDelta is None:
            pixelDelta = PixelDelta(point, colorDelta)
        return pixelDelta
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.logic.util.cache.CacheInterfaceFactory import CacheInterfaceFactory
from org.allbinary.logic.util.cache.CachePolicyFactory import CachePolicyFactory
from org.allbinary.logic.util.cache.CacheTypeFactory import CacheTypeFactory
from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
from org.allbinary.media.image.comparison.color.ColorDeltaFactory import ColorDeltaFactory
from org.allbinary.string.CommonStrings import CommonStrings


PixelDeltaFactory._static_init()

