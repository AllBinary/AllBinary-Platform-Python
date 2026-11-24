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
# package org.allbinary.media.graphics.geography.map.racetrack.drop

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class RaceTrackAdjacentDropLayerFactory:
    DROP_LAYER_FACTORY: RaceTrackAdjacentDropLayerFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        self.list_: BasicArrayList = BasicArrayListD()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def clear(self) -> None:
        self.list_.clear()
    

    @staticmethod
    def getInstance() -> RaceTrackAdjacentDropLayerFactory:
        return RaceTrackAdjacentDropLayerFactory.DROP_LAYER_FACTORY
    

    def getSize(self) -> int:
        return self.list_.size()
    

    def getRandomInstance(self) -> LayerInterfaceFactoryInterface:
        from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
        return self.basicArrayListUtil.getRandom(self.list_)
    

    def add(self, layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> None:
        from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
        self.list_.add(layerInterfaceFactoryInterface)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
# from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface


def _RaceTrackAdjacentDropLayerFactory_DROP_LAYER_FACTORY() -> object:
    return RaceTrackAdjacentDropLayerFactory()

lazy_static(RaceTrackAdjacentDropLayerFactory, "DROP_LAYER_FACTORY", _RaceTrackAdjacentDropLayerFactory_DROP_LAYER_FACTORY)

