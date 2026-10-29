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

from org.allbinary.game.part.weapon.BasicWeaponPart import BasicWeaponPart


class BasicProjectileWeaponPart(BasicWeaponPart):

    def _init_fields(self) -> None:
        self.weaponLayerCircularStaticPool: WeaponLayerCircularPool = None
    

    @staticmethod
    def createBasicProjectileWeaponPart(animationInterface: Animation, weaponLayerCircularStaticPool: WeaponLayerCircularPool) -> BasicProjectileWeaponPart:
        return BasicProjectileWeaponPart(animationInterface, AllBinaryLayer.NULL_ALLBINARY_LAYER, weaponLayerCircularStaticPool, WeaponProperties.NULL_WEAPON_PROPERTIES, NoScoreable.getInstance(), RelativeRelationship.NULL_RELATIVE_RELATIONSHIP)
    

    def __init__(self, animationInterface: Animation, sourceLayerInterface: AllBinaryLayer, weaponLayerCircularStaticPool: WeaponLayerCircularPool, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> None:
        super().__init__(animationInterface, sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)
        self._init_fields()
        self.weaponLayerCircularStaticPool = weaponLayerCircularStaticPool
    

    # throws Exception
    def processScore(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface) -> None:
        weaponLayer: WeaponLayer = self.weaponLayerCircularStaticPool.getInstanceWeaponLayer(self.getOwnerLayerInterface(), self.relativeRelationship.getX(), self.relativeRelationship.getY(), self.relativeRelationship.getZ(), angle, otherAngle, weaponProperties, scoreableInterface)
        allbinaryLayerManager.append(weaponLayer)
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.layer.weapon.WeaponLayer import WeaponLayer
from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
from org.allbinary.game.score.NoScoreable import NoScoreable
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


