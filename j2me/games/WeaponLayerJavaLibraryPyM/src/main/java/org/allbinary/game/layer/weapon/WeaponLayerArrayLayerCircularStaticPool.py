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
# package org.allbinary.game.layer.weapon

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class WeaponLayerArrayLayerCircularStaticPool:
    instance: WeaponLayerArrayLayerCircularStaticPool = None

    def _init_fields(self) -> None:
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.MAX: int = 5
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(self.MAX)
        self.WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = None
        self.TWO_WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = None
        self.THREE_WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = None

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WeaponLayerArrayLayerCircularStaticPool:
        return WeaponLayerArrayLayerCircularStaticPool.instance
    

    def init(self) -> None:
        WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = [None] * (self.MAX * 2)
        TWO_WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = [None] * (self.MAX)
        THREE_WEAPONLAYER_ARRAY: list[list[WeaponLayer]] = [None] * (self.MAX)
        for index in range(0, self.MAX):
            WEAPONLAYER_ARRAY[index] = [None] * (1)
            TWO_WEAPONLAYER_ARRAY[index] = [None] * (2)
            THREE_WEAPONLAYER_ARRAY[index] = [None] * (3)
        self.WEAPONLAYER_ARRAY = WEAPONLAYER_ARRAY
        self.TWO_WEAPONLAYER_ARRAY = TWO_WEAPONLAYER_ARRAY
        self.THREE_WEAPONLAYER_ARRAY = THREE_WEAPONLAYER_ARRAY
    

    def getWeaponLayerArrays(self, size: int) -> list[list[WeaponLayer]]:
        if size == 1:
            return self.WEAPONLAYER_ARRAY
        elif size == 2:
            return self.TWO_WEAPONLAYER_ARRAY
        elif size == 3:
            return self.THREE_WEAPONLAYER_ARRAY
        raise RuntimeError()
    

    # throws Exception
    def getInstanceArray(self, size: int) -> list[WeaponLayer]:
        weaponLayerArray: list[WeaponLayer] = self.getWeaponLayerArrays(size)[self.circularIndexUtil.getIndex()]
        self.circularIndexUtil.next()
        return weaponLayerArray
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


def _WeaponLayerArrayLayerCircularStaticPool_instance() -> object:
    return WeaponLayerArrayLayerCircularStaticPool()

lazy_static(WeaponLayerArrayLayerCircularStaticPool, "instance", _WeaponLayerArrayLayerCircularStaticPool_instance)

