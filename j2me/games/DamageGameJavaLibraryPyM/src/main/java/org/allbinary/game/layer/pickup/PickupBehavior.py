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

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.layer.pickup.PickupBehaviorInterface import PickupBehaviorInterface


class PickupBehavior(PickupBehaviorInterface):
    NULL_PICKUP_BEHAVIOR: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.countedIndex: int = None
        self.ownerLayerInterface: CollidableCompositeLayer = None
    

    @staticmethod
    def getNullInstance() -> PickupBehavior:
        if PickupBehavior.NULL_PICKUP_BEHAVIOR == NullUtil.getInstance().NULL_OBJECT:
            PickupBehavior.NULL_PICKUP_BEHAVIOR = PickupBehavior(CollidableCompositeLayer.getNullInstance(), 0)
        return PickupBehavior.NULL_PICKUP_BEHAVIOR
    

    def __init__(self, ownerLayerInterface: CollidableCompositeLayer, countedIndex: int) -> None:
        self._init_fields()
        self.ownerLayerInterface = ownerLayerInterface
        self.countedIndex = countedIndex
    

    def doPickup(self, pickupProcessorInterface: PickupProcessorInterface) -> None:
        try:
            healthInterfaceCompositeInterface: HealthInterfaceCompositeInterface = self.ownerLayerInterface
            if healthInterfaceCompositeInterface.getHealthInterface().isAlive():
                pickupProcessorInterface.process(self.ownerLayerInterface)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "doPickup", e)
    

    def doPickupLayer(self, pickupLayerInterface: PickedUpLayerInterface) -> None:
        from org.allbinary.game.layer.pickup.PickedUpLayerTypeFactory import PickedUpLayerTypeFactory
        try:
            pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = pickupLayerInterface.getPickedUpLayerInterfaceFactoryInterface()
            pickedUpLayerType: PickedUpLayerType = pickedUpLayerInterfaceFactoryInterface.getPickedUpLayerType()
            pickedUpLayerTypeFactory: PickedUpLayerTypeFactory = PickedUpLayerTypeFactory.getInstance()
            if pickedUpLayerType == pickedUpLayerTypeFactory.BEAM or pickedUpLayerType == pickedUpLayerTypeFactory.MINE or pickedUpLayerType == pickedUpLayerTypeFactory.PROJECTILE or pickedUpLayerType == pickedUpLayerTypeFactory.ENHANCEMENT:
                self.add(pickedUpLayerInterfaceFactoryInterface)
            elif pickedUpLayerInterfaceFactoryInterface.getPickedUpLayerType() == pickedUpLayerTypeFactory.PART:
                collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = self.ownerLayerInterface
                collidableDestroyableDamageableLayer.addPart(pickedUpLayerInterfaceFactoryInterface)
            elif pickedUpLayerType == pickedUpLayerTypeFactory.NONE:
                pass
            else:
                pickupProcessorInterface: PickupProcessorInterface = pickedUpLayerInterfaceFactoryInterface
                self.doPickup(pickupProcessorInterface)
            pickupLayerInterface.setPickedUp()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, "doPickup", e)
    

    def add(self, countedPickedUpLayerInterfaceFactoryInterface: CountedPickedUpLayerInterfaceFactoryInterface) -> None:
        partIndex: int = countedPickedUpLayerInterfaceFactoryInterface.getId() + self.countedIndex
        self.addAt(countedPickedUpLayerInterfaceFactoryInterface, partIndex)
    

    def addAt(self, countedPickedUpLayerInterfaceFactoryInterface: CountedPickedUpLayerInterfaceFactoryInterface, partIndex: int) -> None:
        collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = self.ownerLayerInterface
        countedLayerInterfaceFactory: CountedLayerInterfaceFactoryPart = collidableDestroyableDamageableLayer.getPartInterfaceArray()[partIndex]
        countedLayerInterfaceFactory.setTotal(countedLayerInterfaceFactory.getTotal() + countedPickedUpLayerInterfaceFactoryInterface.getTotal())
    

    def getFirstAvailableCountedLayerInterfaceFactory(self, pickedUpLayerTypeArray: list[PickedUpLayerType]) -> CountedLayerInterfaceFactoryPart:
        collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = self.ownerLayerInterface
        partInterfaceArray: list[PartInterface] = collidableDestroyableDamageableLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        nextCountedLayerInterfaceFactory: CountedLayerInterfaceFactoryPart = None
        countedPickedUpLayerInterfaceFactory: CountedPickedUpLayerInterfaceFactory = None
        for index in range(self.countedIndex, size):
            nextCountedLayerInterfaceFactory = collidableDestroyableDamageableLayer.getPartInterfaceArray()[index]
            countedPickedUpLayerInterfaceFactory = nextCountedLayerInterfaceFactory.getCountedPickedUpLayerInterfaceFactory()
            index2 = len(pickedUpLayerTypeArray)
            while (index2 := index2 - 1) >= 0:
                if countedPickedUpLayerInterfaceFactory.getPickedUpLayerType() == pickedUpLayerTypeArray[index2]:
                    if nextCountedLayerInterfaceFactory.getTotal() > 0:
                        return nextCountedLayerInterfaceFactory
        return CountedLayerInterfaceFactoryPart.NULL_COUNTED_LAYER_INTERFACE_FACTORY
    

    # throws Exception
    def getCountedLayerInterfaceFactoryForSlot(self, slotIndex: int) -> CountedLayerInterfaceFactoryPart:
        currentSlot: int = 0
        collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = self.ownerLayerInterface
        partInterfaceArray: list[PartInterface] = collidableDestroyableDamageableLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        nextCountedLayerInterfaceFactory: CountedLayerInterfaceFactoryPart = None
        for index in range(self.countedIndex, size):
            nextCountedLayerInterfaceFactory = collidableDestroyableDamageableLayer.getPartInterfaceArray()[index]
            if nextCountedLayerInterfaceFactory.getTotal() > 0:
                if currentSlot == slotIndex:
                    return nextCountedLayerInterfaceFactory
                else:
                    currentSlot += 1
        return CountedLayerInterfaceFactoryPart.NULL_COUNTED_LAYER_INTERFACE_FACTORY
    

    def getCountedIndex(self) -> int:
        return self.countedIndex
from org.allbinary.game.health.HealthInterfaceCompositeInterface import HealthInterfaceCompositeInterface
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.part.CountedLayerInterfaceFactoryPart import CountedLayerInterfaceFactoryPart
from org.allbinary.game.part.PartInterface import PartInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings


