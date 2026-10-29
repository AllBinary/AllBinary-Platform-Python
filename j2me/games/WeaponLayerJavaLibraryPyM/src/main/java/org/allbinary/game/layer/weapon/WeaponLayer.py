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

from org.allbinary.game.multiplayer.layer.MultiPlayerGameLayer import MultiPlayerGameLayer
from org.allbinary.game.tick.TickableInterface import TickableInterface


class WeaponLayer(MultiPlayerGameLayer, TickableInterface):

    def _init_fields(self) -> None:
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.initAnimationInterface: Animation = None
        self.destroyedAnimationInterface: Animation = None
        self.sourceLayerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
        self.totalDamage: int = 0
        self.initDamage: int = 0
        self.destroyed: bool = True
        self.scoreableInterface: ScoreableInterface = NoScoreable.getInstance()
        self.movement: Movement = None
        self.weaponProperties: WeaponProperties = WeaponProperties.NULL_WEAPON_PROPERTIES
        self.multiPlayerType: int = None
        self.collidableWeaponBehavior: CollidableWeaponBehavior = CollidableWeaponBehavior.getNullInstance()
    

    def __init__(self, name: str, remoteInfo: RemoteInfo, multiPlayerType: int, movement: Movement, animationInterface: Animation, destroyedAnimationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(remoteInfo, BasicGroupFactory.getInstance().NONE_ARRAY, name, rectangle, viewPosition)
        self._init_fields()
        self.initAnimationInterface = animationInterface
        self.setAnimationInterface(animationInterface)
        self.destroyedAnimationInterface = destroyedAnimationInterface
        self.movement = movement
        self.multiPlayerType = multiPlayerType
    

    def setCollidableInferface(self, collidableInferface: CollidableBaseBehavior) -> None:
        super().setCollidableInferface(collidableInferface)
        self.collidableWeaponBehavior = self.getCollidableInferface()
    

    # throws Exception
    def initXYZ(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
    

    # throws Exception
    def init(self, sourceLayerInterface: AllBinaryLayer, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreable: ScoreableInterface) -> None:
        self.setWeaponPropertiesP(weaponProperties)
        self.setReadyForExplosion(False)
        self.setAnimationInterface(self.getInitAnimationInterfaceP())
        self.setOwnerLayerInterface(sourceLayerInterface)
        self.collidableWeaponBehavior.init(sourceLayerInterface)
        self.setGroupInterfaces()
        if scoreable is not None:
            self.scoreableInterface = scoreable
        self.totalDamage = 0
        self.initDamage = weaponProperties.getDamage()
        self.setDestroyed(False)
        self.movement.init(weaponProperties.getSpeed(), angle, otherAngle)
    

    def setGroupInterfaces(self) -> None:
        basicGroupFactory: BasicGroupFactory = BasicGroupFactory.getInstance()
        if self.sourceLayerInterface.getGroupInterface()[0] == basicGroupFactory.ENEMY:
            self.setGroupInterface(basicGroupFactory.ENEMY_ARRAY)
        else:
            self.setGroupInterface(self.sourceLayerInterface.getGroupInterface())
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.isExhausted() and not self.isDestroyed():
            if self.isReadyForExplosion():
                indexedAnimationInterface: IndexedAnimation = self.getAnimationInterface()
                currentFrame: int = indexedAnimationInterface.getFrame()
                if currentFrame < indexedAnimationInterface.getAnimationSize() - 1:
                    indexedAnimationInterface.nextFrame()
                else:
                    self.setDestroyed(True)
            else:
                collidableWeaponBehavior: CollidableWeaponBehavior = self.getCollidableInferface()
                if collidableWeaponBehavior.isCollided():
                    self.setAnimationInterface(self.destroyedAnimationInterface)
                    self.getMovement().stop()
                    self.setReadyForExplosion(True)
                else:
                    self.setDestroyed(True)
        self.movement.process(self)
        self.totalDamage += self.weaponProperties.getDissipation()
    

    def isDestroyed(self) -> bool:
        return self.destroyed
    

    def damage(self, damage: int, damageType: int) -> None:
        self.totalDamage += damage * damage
    

    def givePoints(self, total: int) -> None:
        self.scoreableInterface.addPoints(GameConfigurationUtil.getInstance().getCompetitionValue() * total)
    

    def isExhausted(self) -> bool:
        if self.totalDamage > self.getInitDamage() or self.totalDamage < 0:
            return True
        else:
            return False
    

    def getDamage(self, damageType: int) -> int:
        if not self.isExhausted():
            total: int = self.getInitDamage() - self.totalDamage
            self.givePoints(total)
            return total
        return 0
    

    def setDestroyed(self, destroyed: bool) -> None:
        self.destroyed = destroyed
        if self.isDestroyed():
            self.scoreableInterface = NoScoreable.getInstance()
            DestroyedLayerProcessor.getInstance().add(self)
    

    def getInitDamage(self) -> int:
        return self.initDamage
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        self.animationInterface = animationInterface
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
    

    def getInitAnimationInterfaceP(self) -> Animation:
        return self.initAnimationInterface
    

    def setInitAnimationInterfaceP(self, initAnimationInterface: Animation) -> None:
        self.initAnimationInterface = initAnimationInterface
    

    def getDestroyedAnimationInterface(self) -> Animation:
        return self.destroyedAnimationInterface
    

    def getOwnerLayerInterface(self) -> AllBinaryLayer:
        return self.sourceLayerInterface
    

    def setOwnerLayerInterface(self, sourceLayerInterface: AllBinaryLayer) -> None:
        self.sourceLayerInterface = sourceLayerInterface
    

    def paint(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getViewPosition()
        self.animationInterface.paintXY(graphics, viewPosition.getX() - self.getHalfWidth(), viewPosition.getY() - self.getHalfHeight())
    

    def paintThreed(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getViewPosition()
        self.animationInterface.paintThreedXYZ(graphics, viewPosition.getX() - self.getHalfWidth(), viewPosition.getY() - self.getHalfHeight(), viewPosition.getZ() - self.getHalfDepth())
    

    def getMovement(self) -> Movement:
        return self.movement
    

    def setMovement(self, movement: Movement) -> None:
        self.movement = movement
    

    def getType(self) -> int:
        return WeaponLayer.getStaticType()
    

    @staticmethod
    def getStaticType() -> int:
        return 0
    

    def getMultiPlayerType(self) -> int:
        return self.multiPlayerType
    

    def setWeaponPropertiesP(self, weaponProperties: WeaponProperties) -> None:
        self.weaponProperties = weaponProperties
    

    def getWeaponPropertiesP(self) -> WeaponProperties:
        return self.weaponProperties
    

    def implmentsTickableInterface(self) -> bool:
        return True
    

    # throws Exception
    def set(self, gl: GL) -> None:
        self.initAnimationInterface.set(gl)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.collision.CollidableBaseBehavior import CollidableBaseBehavior
from org.allbinary.game.combat.destroy.DestroyedLayerProcessor import DestroyedLayerProcessor
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.game.score.NoScoreable import NoScoreable
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.physics.movement.Movement import Movement
from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.game.layer.weapon.CollidableWeaponBehavior import CollidableWeaponBehavior


