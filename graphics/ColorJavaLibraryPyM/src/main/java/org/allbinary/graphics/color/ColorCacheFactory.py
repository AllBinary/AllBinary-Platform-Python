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
# package org.allbinary.graphics.color

from __future__ import annotations



class ColorCacheFactory:
    cacheInterface: AutomaticCacheInterface = None
    

    @staticmethod
    def _static_init() -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        try:
            logUtil.putF(commonStrings.START, ColorCacheFactory, STATIC_BLOCK)
            ColorCacheFactory.cacheInterface = AutomaticCacheInterfaceFactory.getInstance(ColorCacheableFactory(), CacheTypeFactory.getInstance().CACHE, CachePolicyFactory.getInstance().THIRTY_MINUTES_TEN_THOUSAND_MAX)
            logUtil.putF(commonStrings.END, ColorCacheFactory, STATIC_BLOCK)
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, ColorCacheFactory, STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> AutomaticCacheInterface:
        return ColorCacheFactory.cacheInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.logic.util.cache.AutomaticCacheInterfaceFactory import AutomaticCacheInterfaceFactory
from org.allbinary.logic.util.cache.CachePolicyFactory import CachePolicyFactory
from org.allbinary.logic.util.cache.CacheTypeFactory import CacheTypeFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.graphics.color.ColorCacheableFactory import ColorCacheableFactory


ColorCacheFactory._static_init()

