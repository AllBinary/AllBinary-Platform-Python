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
# package org.allbinary.game.part.weapon

from __future__ import annotations

import threading


class BasicWeaponPartCircularPool:
    NULL_BASIC_WEAPON_PART_CIRCULAR_POOL: BasicWeaponPartCircularPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.basicWeaponPart: BasicWeaponPart = BasicWeaponPart.NULL_BASIC_WEAPON_PART

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def init(self, basicWeaponPartFactoryInterface: BasicWeaponPartFactoryInterface) -> None:
        self.basicWeaponPart = basicWeaponPartFactoryInterface.getInstance()
    

    # throws Exception
    def getInstance(self, sourceLayerInterface: AllBinaryLayer, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> BasicWeaponPart:
        with self._lock:
            return self._getInstance_unlocked(sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)

    def _getInstance_unlocked(self, sourceLayerInterface: AllBinaryLayer, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> BasicWeaponPart:
        self.basicWeaponPart.init(sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)
        return self.basicWeaponPart
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.game.part.weapon.BasicWeaponPart import BasicWeaponPart


BasicWeaponPartCircularPool.NULL_BASIC_WEAPON_PART_CIRCULAR_POOL = BasicWeaponPartCircularPool()

