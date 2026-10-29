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

from org.allbinary.layer.AllBinaryLayerCircularPool import AllBinaryLayerCircularPool


class PickupLayerCircularStaticPool(AllBinaryLayerCircularPool):
    SINGLETON: PickupLayerCircularStaticPool = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> PickupLayerCircularStaticPool:
        return PickupLayerCircularStaticPool.SINGLETON
    

    # throws Exception
    def getInstanceXYZ(self, pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface, x: int, y: int, z: int) -> PickedUpLayerInterface:
        pickupLayer: PickupLayer = self.getNextInstance()
        pickupLayer.initXYZ(x, y, z)
        pickupLayer.init(pickedUpLayerInterfaceFactoryInterface, pickedUpLayerInterfaceFactoryInterface.getAnimationInterface())
        return pickupLayer


PickupLayerCircularStaticPool.SINGLETON = PickupLayerCircularStaticPool()

