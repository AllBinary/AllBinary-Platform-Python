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



class ColorDeltaFactory:
    cacheInterface: AutomaticCacheInterface = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def _static_init() -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        instance: str = "ColorDeltaFactory"
        try:
            logUtil.putF(commonStrings.START, instance, STATIC_BLOCK)
            ColorDeltaFactory.cacheInterface = CacheInterfaceFactory.getInstance(CacheTypeFactory.getInstance().CACHE, CachePolicyFactory.getInstance().THIRTY_MINUTES_TEN_THOUSAND_MAX)
            logUtil.putF(commonStrings.END, instance, STATIC_BLOCK)
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, instance, STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    @staticmethod
    def getInstance(rgb1: int, rgb2: int) -> ColorDelta:
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        from org.allbinary.media.image.comparison.color.ColorDelta import ColorDelta
        colorDelta: ColorDelta = ColorDeltaFactory.cacheInterface.get(ColorDelta.getKey(rgb1, rgb2))
        if colorDelta is None:
            colorDelta = ColorDelta(rgb1, rgb2)
        return colorDelta
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.logic.util.cache.CacheInterfaceFactory import CacheInterfaceFactory
from org.allbinary.logic.util.cache.CachePolicyFactory import CachePolicyFactory
from org.allbinary.logic.util.cache.CacheTypeFactory import CacheTypeFactory
from org.allbinary.string.CommonStrings import CommonStrings


ColorDeltaFactory._static_init()

