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



class BufferedImagePoolSingleton:
    poolInterface: PoolInterface = None
    

    @staticmethod
    def _static_init() -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        instance: str = "BufferedImagePoolSingleton"
        try:
            logUtil.putF(commonStrings.START, instance, STATIC_BLOCK)
            BufferedImagePoolSingleton.poolInterface = PoolInterfaceFactory.getInstance(BufferedImageCacheableFactory(), PoolTypeFactory.getInstance().VECTOR_POOL, CachePolicyFactory.getInstance().MAX_TIME_THOUSAND_MAX)
            logUtil.putF(commonStrings.END, instance, STATIC_BLOCK)
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, instance, STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> PoolInterface:
        return BufferedImagePoolSingleton.poolInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.CachePolicyFactory import CachePolicyFactory
from org.allbinary.logic.util.cache.PoolInterface import PoolInterface
from org.allbinary.logic.util.cache.PoolInterfaceFactory import PoolInterfaceFactory
from org.allbinary.logic.util.cache.PoolTypeFactory import PoolTypeFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.image.cache.BufferedImageCacheableFactory import BufferedImageCacheableFactory


BufferedImagePoolSingleton._static_init()

