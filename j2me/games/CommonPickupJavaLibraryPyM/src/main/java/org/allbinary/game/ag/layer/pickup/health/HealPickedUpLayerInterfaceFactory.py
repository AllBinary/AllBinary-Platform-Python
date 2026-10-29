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
# package org.allbinary.game.ag.layer.pickup.health

from __future__ import annotations

from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactory import PickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.PickupProcessorInterface import PickupProcessorInterface


class HealPickedUpLayerInterfaceFactory(PickedUpLayerInterfaceFactory, PickupProcessorInterface):
    pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY

    def _init_fields(self) -> None:
        self.pool: HealLayerCircularStaticPool = HealLayerCircularStaticPool(HealLayerFactory(), 1)
    

    # throws Exception
    @staticmethod
    def init() -> None:
        HealPickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface = HealPickedUpLayerInterfaceFactory()
    

    def __init__(self) -> None:
        from org.allbinary.game.ag.layer.pickup.health.HealthResources import HealthResources
        from org.allbinary.game.ag.layer.pickup.health.HealthResources import HealthResources
        super().__init__(PickedUpLayerTypeFactory.getInstance().HEAL, IconLayerFactory.getInstance(FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(HealthResources.getInstance().RESOURCE).getInstance(0), 10, 10), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(HealthResources.getInstance().RESOURCE).getInstance(0))
        self._init_fields()
    

    def getTotal(self) -> int:
        return 1
    

    @staticmethod
    def getInstance() -> PickedUpLayerInterfaceFactoryInterface:
        return HealPickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface
    

    # throws Exception
    def process(self, sourceLayerInterface: AllBinaryLayer) -> None:
        self.pool.visit(sourceLayerInterface)
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.game.layer.pickup.IconLayerFactory import IconLayerFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.pickup.PickedUpLayerTypeFactory import PickedUpLayerTypeFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.game.ag.layer.pickup.health.HealLayerCircularStaticPool import HealLayerCircularStaticPool
from org.allbinary.game.ag.layer.pickup.health.HealLayerFactory import HealLayerFactory


