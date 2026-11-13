# Generated Code Do Not Modify
# package org.allbinary.logic.util.cache

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class CacheTypeFactory:
    instance: CacheTypeFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.NO_CACHE: CacheType = CacheType(StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING)
        self.CACHE: CacheType = CacheType(StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING)
        self.SET: CacheType = CacheType(StringUtil.getInstance().EMPTY_STRING, "Set")
        self.CACHE_VECTOR: CacheType = CacheType(StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CacheTypeFactory:
        return CacheTypeFactory.instance
# from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.cache.CacheType import CacheType


def _CacheTypeFactory_instance() -> object:
    return CacheTypeFactory()

lazy_static(CacheTypeFactory, "instance", _CacheTypeFactory_instance)

