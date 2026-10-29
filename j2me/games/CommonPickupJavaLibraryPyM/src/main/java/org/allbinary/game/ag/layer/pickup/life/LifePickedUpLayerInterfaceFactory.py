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
# package org.allbinary.game.ag.layer.pickup.life

from __future__ import annotations

from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactory import PickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.PickupProcessorInterface import PickupProcessorInterface


class LifePickedUpLayerInterfaceFactory(PickedUpLayerInterfaceFactory, PickupProcessorInterface):
    pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY

    def _init_fields(self) -> None:
        self.pool: LifeLayerCircularStaticPool = LifeLayerCircularStaticPool(LifeLayerFactory(), 1)
    

    # throws Exception
    @staticmethod
    def init() -> None:
        LifePickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface = LifePickedUpLayerInterfaceFactory()
    

    def __init__(self) -> None:
        from org.allbinary.game.ag.layer.pickup.life.LifeResources import LifeResources
        from org.allbinary.game.ag.layer.pickup.life.LifeResources import LifeResources
        super().__init__(PickedUpLayerTypeFactory.getInstance().LIFE, IconLayerFactory.getInstance(FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(LifeResources.getInstance().RESOURCE).getInstance(0), 10, 10), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(LifeResources.getInstance().RESOURCE).getInstance(0))
        self._init_fields()
    

    def getTotal(self) -> int:
        return 1
    

    @staticmethod
    def getInstance() -> PickedUpLayerInterfaceFactoryInterface:
        return LifePickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface
    

    # throws Exception
    def process(self, sourceLayerInterface: AllBinaryLayer) -> None:
        self.pool.visit(sourceLayerInterface)
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.game.layer.pickup.IconLayerFactory import IconLayerFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.pickup.PickedUpLayerTypeFactory import PickedUpLayerTypeFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.game.ag.layer.pickup.life.LifeLayerCircularStaticPool import LifeLayerCircularStaticPool
from org.allbinary.game.ag.layer.pickup.life.LifeLayerFactory import LifeLayerFactory


