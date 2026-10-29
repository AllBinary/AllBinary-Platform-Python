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
# package org.allbinary.game.ag.layer.hud.basic.health

from __future__ import annotations

from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.game.health.HealthListenerInterface import HealthListenerInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class HealthHudWidget(BasicHud, PaintableInterface, HealthListenerInterface):

    def _init_fields(self) -> None:
        self.healthScale: int = None
        self.animationInterface: Animation = None
        self.healthInterface: Health = None
        self.max: int = 0
        self.xArray: list[int] = None
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.timeDelayHelper: TimeDelayHelper = NoTimeDelayHelper.SINGLETON
        self.slowBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(1280)
        self.mediumBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(640)
        self.fastBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(320)
    

    def __init__(self, animationInterface: Animation, healthInterface: Health, location: int, direction: int) -> None:
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().WHITE)
        self._init_fields()
        self.animationInterface = animationInterface
        self.healthInterface = healthInterface
        self.healthInterface.addListener(self)
        self.healthScale = (self.healthInterface.getMaxHealth() / 6) + 1
        self.onHealthChange()
        self.updateMaxWidth = healthInterface.getMaxHealth() * 16
        self.updateMaxHeight = 16
        self.xArray = [0] * (30)
        self.update()
    

    def update(self) -> None:
        if self.xArray is not None:
            for index in range(0, len(self.xArray)):
                self.xArray[index] = self.getX() + (index * 16)
    

    def setX(self, x: int) -> None:
        super().setX(x)
        self.update()
    

    def onHealthChange(self) -> None:
        self.max = (self.healthInterface.getHealth() / self.healthScale)
        self.timeDelayHelper = NoTimeDelayHelper.SINGLETON
        if self.max <= 1 and self.healthInterface.isAlive():
            self.max = 1
            if self.healthScale - self.healthInterface.getHealth() > int((self.healthScale * 2) / 3):
                self.timeDelayHelper = self.slowBeatTimeDelayHelper
            elif self.healthScale - self.healthInterface.getHealth() > int(self.healthScale / 3):
                self.timeDelayHelper = self.mediumBeatTimeDelayHelper
            else:
                self.timeDelayHelper = self.fastBeatTimeDelayHelper
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        for index in range(0, self.max):
            if self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
                self.animationInterface.paintXY(graphics, self.xArray[index], self.getY())
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.health.Health import Health
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.NoTimeDelayHelper import NoTimeDelayHelper
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


