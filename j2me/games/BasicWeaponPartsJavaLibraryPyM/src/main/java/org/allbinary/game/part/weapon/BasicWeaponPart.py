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

from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.part.PartInterface import PartInterface
from org.allbinary.game.part.weapon.SalvoInterface import SalvoInterface


class BasicWeaponPart(PartInterface, SalvoInterface):
    NULL_BASIC_WEAPON_PART: BasicWeaponPart = None

    def _init_fields(self) -> None:
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.ownerLayerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
        self.weaponProperties: WeaponProperties = WeaponProperties.NULL_WEAPON_PROPERTIES
        self.scoreableInterface: ScoreableInterface = NoScoreable.getInstance()
        self.relativeRelationship: RelativeRelationship = RelativeRelationship.NULL_RELATIVE_RELATIONSHIP
    

    @staticmethod
    def createBasicWeaponPart(animationInterface: Animation) -> BasicWeaponPart:
        return BasicWeaponPart(animationInterface, AllBinaryLayer.NULL_ALLBINARY_LAYER, WeaponProperties.NULL_WEAPON_PROPERTIES, NoScoreable.getInstance(), RelativeRelationship.NULL_RELATIVE_RELATIONSHIP)
    

    def __init__(self, animationInterface: Animation, sourceLayerInterface: AllBinaryLayer, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> None:
        self._init_fields()
        self.init(sourceLayerInterface, weaponProperties, scoreableInterface, relativeRelationship)
        self.setAnimationInterface(animationInterface)
    

    def init(self, sourceLayerInterface: AllBinaryLayer, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface, relativeRelationship: RelativeRelationship) -> None:
        self.setOwnerLayerInterface(sourceLayerInterface)
        self.setWeaponProperties(weaponProperties)
        self.scoreableInterface = scoreableInterface
        self.relativeRelationship = relativeRelationship
    

    # throws Exception
    def process(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int) -> None:
        self.processScore(allbinaryLayerManager, angle, otherAngle, self.getWeaponProperties(), self.scoreableInterface)
    

    # throws Exception
    def processScore(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface) -> None:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def getOwnerLayerInterface(self) -> AllBinaryLayer:
        return self.ownerLayerInterface
    

    def setOwnerLayerInterface(self, ownerLayerInterface: AllBinaryLayer) -> None:
        self.ownerLayerInterface = ownerLayerInterface
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        self.animationInterface = animationInterface
    

    def paint(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getOwnerLayerInterface().getViewPosition()
        viewX: int = viewPosition.getX()
        viewY: int = viewPosition.getY()
        self.animationInterface.paintXY(graphics, viewX, viewY)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def getWeaponProperties(self) -> WeaponProperties:
        return self.weaponProperties
    

    def setWeaponProperties(self, weaponProperties: WeaponProperties) -> None:
        self.weaponProperties = weaponProperties
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.score.NoScoreable import NoScoreable
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.view.ViewPositionBase import ViewPositionBase


BasicWeaponPart.NULL_BASIC_WEAPON_PART = BasicWeaponPart.createBasicWeaponPart(NullAnimationFactory.getFactoryInstance().getInstance(0))

