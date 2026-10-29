# Generated Code Do Not Modify
# package org.allbinary.game.layer.weapon

from __future__ import annotations

from org.allbinary.game.layer.weapon.SimpleWeaponLayer import SimpleWeaponLayer


class TempExplosionWeaponLayer(SimpleWeaponLayer):

    def _init_fields(self) -> None:
        self.weaponProperties: WeaponProperties = WeaponProperties(-1, -1, 0, 1000, ((int(0) + 32768) % 65536 - 32768))
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(0)
    

    def __init__(self, name: str, movement: Movement, animationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase, timeDelay: int) -> None:
        from org.allbinary.game.layer.weapon.SimpleWeaponLayer import SimpleWeaponLayer
        super().__init__(name, RemoteInfo.REMOTE_INFO, -1, movement, animationInterface, SimpleWeaponLayer.createDestroyed(), rectangle, viewPosition)
        self._init_fields()
        self.timeDelayHelper.delay = timeDelay
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.getCollidableInferface().collide(self, self)
            self.totalDamage = self.getInitDamage() + 1
        super().processTick(allBinaryLayerManager)
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.physics.movement.Movement import Movement
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.view.ViewPositionBase import ViewPositionBase


