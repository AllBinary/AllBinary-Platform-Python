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

from java.lang.JavaRuntimeStatic import lazy_static


class MineLayerCircularStaticPool:
    WEAPON_LAYER_CIRCULAR_STATIC_POOL: WeaponLayerCircularPool = None
    

    # throws Exception
    @staticmethod
    def init(viewPositionFactoryInterface: ViewPositionFactoryInterface) -> None:
        from org.allbinary.game.ag.layer.weapon.mine.MineCountedPickedUpLayerInterfaceFactory import MineCountedPickedUpLayerInterfaceFactory
        from org.allbinary.game.ag.layer.weapon.mine.MineLayerFactory import MineLayerFactory
        from org.allbinary.view.ViewPositionFactoryInterface import ViewPositionFactoryInterface
        MineCountedPickedUpLayerInterfaceFactory.init()
        MineLayerCircularStaticPool.WEAPON_LAYER_CIRCULAR_STATIC_POOL.initAllBinaryLayerCircularPool(MineLayerFactory(viewPositionFactoryInterface), 20)
    

    @staticmethod
    def getInstance() -> WeaponLayerCircularPool:
        from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
        return MineLayerCircularStaticPool.WEAPON_LAYER_CIRCULAR_STATIC_POOL
# from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
# from org.allbinary.view.ViewPositionFactoryInterface import ViewPositionFactoryInterface


def _MineLayerCircularStaticPool_WEAPON_LAYER_CIRCULAR_STATIC_POOL() -> object:
    from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
    return WeaponLayerCircularPool()

lazy_static(MineLayerCircularStaticPool, "WEAPON_LAYER_CIRCULAR_STATIC_POOL", _MineLayerCircularStaticPool_WEAPON_LAYER_CIRCULAR_STATIC_POOL)

