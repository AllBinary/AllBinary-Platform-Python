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


class StraightMultiProjectileWeaponPart(BasicWeaponPart):

    def _init_fields(self) -> None:
        self.weaponLayerCircularStaticPool: WeaponLayerCircularPool = None
        self.total: int = None
        self.noDecimalTrigTable: NoDecimalTrigTable = NoDecimalTrigTable.getInstance()
    

    @staticmethod
    def createStraightMultiProjectileWeaponPart(animationInterface: Animation, weaponLayerCircularStaticPool: WeaponLayerCircularPool) -> StraightMultiProjectileWeaponPart:
        return StraightMultiProjectileWeaponPart(animationInterface, AllBinaryLayer.NULL_ALLBINARY_LAYER, weaponLayerCircularStaticPool, 2, WeaponProperties.NULL_WEAPON_PROPERTIES, NoScoreable.getInstance(), RelativeRelationship.NULL_RELATIVE_RELATIONSHIP)
    

    def __init__(self, animationInterface: Animation, sourceLayerInterface: AllBinaryLayer, weaponLayerCircularStaticPool: WeaponLayerCircularPool, total: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> None:
        super().__init__(animationInterface, sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)
        self._init_fields()
        self.total = total
        self.weaponLayerCircularStaticPool = weaponLayerCircularStaticPool
    

    # throws Exception
    def processScore(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface) -> None:
        sourceLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        reducedWidth: int = (sourceLayerInterface.getWidth() * 8 / 10)
        halfWidth: int = (reducedWidth >> 1)
        x: int = self.relativeRelationship.getX()
        y: int = self.relativeRelationship.getY()
        sine: int = 0
        beamX: int = 0
        cosine: int = 0
        beamY: int = 0
        weaponLayer: WeaponLayer = None
        increment: int = int(reducedWidth / (self.total - 1))
        next: int = -halfWidth
        for index in range(0, self.total):
            sine = int((next * self.noDecimalTrigTable.sin(angle)))
            beamX = int((sine / self.noDecimalTrigTable.SCALE))
            cosine = int((next * self.noDecimalTrigTable.cos(angle)))
            beamY = -int((cosine / self.noDecimalTrigTable.SCALE))
            weaponLayer = self.weaponLayerCircularStaticPool.getInstanceWeaponLayer(sourceLayerInterface, x + beamX, y + beamY, 0, angle, otherAngle, weaponProperties, scoreableInterface)
            allbinaryLayerManager.append(weaponLayer)
            next += increment
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.layer.weapon.WeaponLayer import WeaponLayer
from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
from org.allbinary.game.score.NoScoreable import NoScoreable
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.math.NoDecimalTrigTable import NoDecimalTrigTable


