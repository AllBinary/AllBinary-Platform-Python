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

from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactory import PickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactoryInterface import CountedPickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.pickup.PickedUpLayerTypeFactory import PickedUpLayerTypeFactory
from org.allbinary.game.layer.pickup.IconLayer import IconLayer


class CountedPickedUpLayerInterfaceFactory(PickedUpLayerInterfaceFactory, CountedPickedUpLayerInterfaceFactoryInterface):
    NULL_COUNTED_PICKUP_LAYER_FACTORY: CountedPickedUpLayerInterfaceFactory = None

    def _init_fields(self) -> None:
        self.id: int = None
    

    def __init__(self, pickeUpLayerType: PickedUpLayerType, iconLayer: IconLayer, animationInterface: Animation) -> None:
        from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactoryPool import CountedPickedUpLayerInterfaceFactoryPool
        super().__init__(pickeUpLayerType, iconLayer, animationInterface)
        self._init_fields()
        list_: BasicArrayList = CountedPickedUpLayerInterfaceFactoryPool.getInstance().getList()
        self.id = list_.size()
        list_.add(self)
    

    # throws Exception
    def getNextInstance(self, hashtable: ABHashtable[object, object], x: int, y: int, z: int) -> AllBinaryLayer:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def getTotal(self) -> int:
        return -1
    

    def getId(self) -> int:
        return self.id
from org.allbinary.animation.Animation import Animation
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY = CountedPickedUpLayerInterfaceFactory(PickedUpLayerTypeFactory.getInstance().NONE, IconLayer.NULL_ICON_LAYER, NullAnimationFactory.getFactoryInstance().getInstance(0))

