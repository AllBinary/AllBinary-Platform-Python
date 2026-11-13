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
# package org.allbinary.game.layer.pickup

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class CountedPickedUpLayerInterfaceFactoryPool:
    SINGLETON: CountedPickedUpLayerInterfaceFactoryPool = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.list_: BasicArrayList = None
    

    def __init__(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self._init_fields()
        self.list_ = BasicArrayListD()
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    @staticmethod
    def getInstance() -> CountedPickedUpLayerInterfaceFactoryPool:
        return CountedPickedUpLayerInterfaceFactoryPool.SINGLETON
    

    @staticmethod
    def init() -> None:
        CountedPickedUpLayerInterfaceFactoryPool.SINGLETON = CountedPickedUpLayerInterfaceFactoryPool()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _CountedPickedUpLayerInterfaceFactoryPool_SINGLETON() -> object:
    return CountedPickedUpLayerInterfaceFactoryPool()

lazy_static(CountedPickedUpLayerInterfaceFactoryPool, "SINGLETON", _CountedPickedUpLayerInterfaceFactoryPool_SINGLETON)

