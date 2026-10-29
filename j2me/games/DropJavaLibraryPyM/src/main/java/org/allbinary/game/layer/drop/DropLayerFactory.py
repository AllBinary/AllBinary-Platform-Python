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



class DropLayerFactory:
    DROP_LAYER_FACTORY: DropLayerFactory = None

    def _init_fields(self) -> None:
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
        return self.basicArrayListUtil.getRandom(self.list_)
    

    def add(self, layerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface) -> None:
        self.list_.add(layerInterfaceFactoryInterface)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


DropLayerFactory.DROP_LAYER_FACTORY = DropLayerFactory()

