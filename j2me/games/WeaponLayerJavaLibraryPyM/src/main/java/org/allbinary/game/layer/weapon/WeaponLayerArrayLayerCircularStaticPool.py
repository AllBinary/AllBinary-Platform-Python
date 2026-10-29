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

import threading


class WeaponLayerArrayLayerCircularStaticPool:
    instance: WeaponLayerArrayLayerCircularStaticPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.MAX: int = 5
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(self.MAX)
        self.ALL_WEAPONLAYER_ARRAY: list[list[list[object]]] = [None] * (4)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WeaponLayerArrayLayerCircularStaticPool:
        return WeaponLayerArrayLayerCircularStaticPool.instance
    

    def init(self) -> None:
        WEAPONLAYER_ARRAY: list[list[object]] = [None] * (self.MAX * 2)
        TWO_WEAPONLAYER_ARRAY: list[list[object]] = [None] * (self.MAX)
        THREE_WEAPONLAYER_ARRAY: list[list[object]] = [None] * (self.MAX)
        for index in range(0, self.MAX):
            WEAPONLAYER_ARRAY[index] = [None] * (1)
            TWO_WEAPONLAYER_ARRAY[index] = [None] * (2)
            THREE_WEAPONLAYER_ARRAY[index] = [None] * (3)
        self.ALL_WEAPONLAYER_ARRAY[1] = WEAPONLAYER_ARRAY
        self.ALL_WEAPONLAYER_ARRAY[2] = TWO_WEAPONLAYER_ARRAY
        self.ALL_WEAPONLAYER_ARRAY[3] = THREE_WEAPONLAYER_ARRAY
    

    # throws Exception
    def getInstanceArray(self, size: int) -> list[WeaponLayer]:
        with self._lock:
            return self._getInstanceArray_unlocked(size)

    def _getInstanceArray_unlocked(self, size: int) -> list[WeaponLayer]:
        weaponLayerArray: list[WeaponLayer] = self.ALL_WEAPONLAYER_ARRAY[size][self.circularIndexUtil.getIndex()]
        self.circularIndexUtil.next()
        return weaponLayerArray
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


WeaponLayerArrayLayerCircularStaticPool.instance = WeaponLayerArrayLayerCircularStaticPool()

