# Generated Code Do Not Modify
# package org.allbinary.game.layer.drop

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class PlacedLayerFactory:
    instance: PlacedLayerFactory = None

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
    def getInstance() -> PlacedLayerFactory:
        return PlacedLayerFactory.instance
    

    def getSize(self) -> int:
        return self.list_.size()
    

    def getRandomInstance(self) -> AllBinaryLayerFactoryInterface:
        from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface
        return self.basicArrayListUtil.getRandom(self.list_)
    

    def add(self, layerInterfaceFactoryInterface: AllBinaryLayerFactoryInterface) -> None:
        from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface
        self.list_.add(layerInterfaceFactoryInterface)
# from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


def _PlacedLayerFactory_instance() -> object:
    return PlacedLayerFactory()

lazy_static(PlacedLayerFactory, "instance", _PlacedLayerFactory_instance)

