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



class RaceTrackAdjacentDropLayerFactory:
    DROP_LAYER_FACTORY: RaceTrackAdjacentDropLayerFactory = None

    def _init_fields(self) -> None:
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
        return self.basicArrayListUtil.getRandom(self.list_)
    

    def add(self, layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> None:
        self.list_.add(layerInterfaceFactoryInterface)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface


RaceTrackAdjacentDropLayerFactory.DROP_LAYER_FACTORY = RaceTrackAdjacentDropLayerFactory()

