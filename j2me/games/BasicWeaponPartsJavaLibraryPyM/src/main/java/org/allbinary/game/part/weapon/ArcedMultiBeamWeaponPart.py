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


class ArcedMultiBeamWeaponPart(BasicWeaponPart):

    def _init_fields(self) -> None:
        self.weaponLayerCircularStaticPool: WeaponLayerCircularPool = None
        self.total: int = None
        self.TOTAL_ANGLE: int = int(AngleFactory.getInstance().TOTAL_ANGLE)
    

    def __init__(self, animationInterface: Animation, sourceLayerInterface: AllBinaryLayer, weaponLayerCircularStaticPool: WeaponLayerCircularPool, total: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> None:
        super().__init__(animationInterface, sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)
        self._init_fields()
        self.total = total
        self.weaponLayerCircularStaticPool = weaponLayerCircularStaticPool
    

    # throws Exception
    def processScore(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface) -> None:
        increment: int = ((int((int((self.total - 1) / self.TOTAL_ANGLE))) + 32768) % 65536 - 32768)
        minAngle: int = ((int((angle - ((increment * self.total) >> 1))) + 32768) % 65536 - 32768)
        next: int = 0
        weaponLayer: WeaponLayer = None
        for index in range(0, self.total):
            weaponLayer = self.weaponLayerCircularStaticPool.getInstanceWeaponLayer(self.getOwnerLayerInterface(), self.relativeRelationship.getX(), self.relativeRelationship.getY(), 0, (minAngle + increment), otherAngle, weaponProperties, scoreableInterface)
            allbinaryLayerManager.append(weaponLayer)
            next += increment
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.layer.weapon.WeaponLayer import WeaponLayer
from org.allbinary.game.layer.weapon.WeaponLayerCircularPool import WeaponLayerCircularPool
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.math.AngleFactory import AngleFactory


