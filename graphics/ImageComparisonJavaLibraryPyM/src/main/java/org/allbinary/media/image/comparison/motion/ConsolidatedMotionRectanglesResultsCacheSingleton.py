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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations



class ConsolidatedMotionRectanglesResultsCacheSingleton:
    cacheInterface: CacheInterface = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def _static_init() -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        instance: str = "MotionRectanglesResultsCacheSingleton"
        try:
            logUtil.putF(commonStrings.START, instance, STATIC_BLOCK)
            ConsolidatedMotionRectanglesResultsCacheSingleton.cacheInterface = CacheInterfaceFactory.getInstance(CacheTypeFactory.getInstance().CACHE, CachePolicyFactory.getInstance().ONE_MINUTE_FIVE_MAX)
            logUtil.putF(commonStrings.END, instance, STATIC_BLOCK)
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, instance, STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CacheInterface:
        return ConsolidatedMotionRectanglesResultsCacheSingleton.cacheInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.CacheInterface import CacheInterface
from org.allbinary.logic.util.cache.CacheInterfaceFactory import CacheInterfaceFactory
from org.allbinary.logic.util.cache.CachePolicyFactory import CachePolicyFactory
from org.allbinary.logic.util.cache.CacheTypeFactory import CacheTypeFactory
from org.allbinary.string.CommonStrings import CommonStrings


ConsolidatedMotionRectanglesResultsCacheSingleton._static_init()

