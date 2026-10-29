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
# package org.allbinary.game.ag.layer.weapon.mine

from __future__ import annotations

from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory


class MineCountedPickedUpLayerInterfaceFactory(CountedPickedUpLayerInterfaceFactory):
    pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface = CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY

    def _init_fields(self) -> None:
        self.weaponLayerCircularStaticPool: WeaponLayerCircularPool = MineLayerCircularStaticPool.getInstance()
        self.weaponProperties: WeaponProperties = WeaponProperties(-1, -1, 0, 8000, ((int(10) + 32768) % 65536 - 32768))
        self.smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
    

    # throws Exception
    @staticmethod
    def init() -> None:
        MineCountedPickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface = MineCountedPickedUpLayerInterfaceFactory()
    

    def __init__(self) -> None:
        from org.allbinary.game.ag.layer.weapon.mine.MineWeaponResources import MineWeaponResources
        from org.allbinary.game.ag.layer.weapon.mine.MineWeaponResources import MineWeaponResources
        super().__init__(PickedUpLayerTypeFactory.getInstance().MINE, IconLayerFactory.getInstance(FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(MineWeaponResources.getInstance().DROP_ICON_RESOURCE).getInstance(0), 10, 10), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(MineWeaponResources.getInstance().DROP_RESOURCE).getInstance(0))
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PickedUpLayerInterfaceFactoryInterface:
        return MineCountedPickedUpLayerInterfaceFactory.pickedUpLayerInterfaceFactoryInterface
    

    def getTotal(self) -> int:
        return 3
    

    # throws Exception
    def getNextInstance(self, hashtable: ABHashtable[object, object], x: int, y: int, z: int) -> AllBinaryLayer:
        sourceLayerInterface: AllBinaryLayer = hashtable.get(self.smallIntegerSingletonFactory.getAt(0))
        angle: int = hashtable.get(self.smallIntegerSingletonFactory.getAt(1))
        scoreableInterface: ScoreableInterface = sourceLayerInterface
        return self.weaponLayerCircularStaticPool.getInstanceWeaponLayer(sourceLayerInterface, x, y, z, int(int(angle)), 0, self.weaponProperties, scoreableInterface)
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.layer.pickup.IconLayerFactory import IconLayerFactory
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.pickup.PickedUpLayerTypeFactory import PickedUpLayerTypeFactory
from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.game.ag.layer.weapon.mine.MineLayerCircularStaticPool import MineLayerCircularStaticPool


