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
# package org.allbinary.game.layer.drop

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class DropLayerFactory:
    DROP_LAYER_FACTORY: DropLayerFactory = None

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
    def getInstance() -> DropLayerFactory:
        return DropLayerFactory.DROP_LAYER_FACTORY
    

    def getSize(self) -> int:
        return self.list_.size()
    

    def getRandomInstance(self) -> PickedUpLayerInterfaceFactoryInterface:
        from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
        return self.basicArrayListUtil.getRandom(self.list_)
    

    def add(self, layerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface) -> None:
        from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
        self.list_.add(layerInterfaceFactoryInterface)
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
# from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


def _DropLayerFactory_DROP_LAYER_FACTORY() -> object:
    return DropLayerFactory()

lazy_static(DropLayerFactory, "DROP_LAYER_FACTORY", _DropLayerFactory_DROP_LAYER_FACTORY)

