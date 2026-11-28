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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.game.health.HealthListenerInterface import HealthListenerInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


@java_inherited_overloads
class HealthHudWidget(*java_bases(BasicHud, PaintableInterface, HealthListenerInterface)):
    def _java_defaults(self):
        vars(self).setdefault("healthScale", 0)
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("healthInterface", None)
        vars(self).setdefault("max", 0)
        vars(self).setdefault("xArray", None)
        vars(self).setdefault("gameTickTimeDelayHelper", None)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("slowBeatTimeDelayHelper", None)
        vars(self).setdefault("mediumBeatTimeDelayHelper", None)
        vars(self).setdefault("fastBeatTimeDelayHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        from org.allbinary.time.NoTimeDelayHelper import NoTimeDelayHelper
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        if "healthScale" not in vars(self): self.healthScale: int = 0
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
        if "healthInterface" not in vars(self): self.healthInterface: Health = None
        if "max" not in vars(self): self.max: int = 0
        if "xArray" not in vars(self): self.xArray: list[int] = None
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.timeDelayHelper: TimeDelayHelper = NoTimeDelayHelper.SINGLETON
        self.slowBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(1280)
        self.mediumBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(640)
        self.fastBeatTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(320)
    

    def __init__(self, animationInterface: Animation, healthInterface: Health, location: int, direction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.game.health.Health import Health
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().WHITE)
        __class__._init_fields(self)
        self.animationInterface = animationInterface
        self.healthInterface = healthInterface
        self.healthInterface.addListener(self)
        self.healthScale = (java_divide(self.healthInterface.getMaxHealth(), 6)) + 1
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
        java_super_call(super(), "setX", x)
        self.update()
    

    def onHealthChange(self) -> None:
        from org.allbinary.time.NoTimeDelayHelper import NoTimeDelayHelper
        self.max = (java_divide(self.healthInterface.getHealth(), self.healthScale))
        self.timeDelayHelper = NoTimeDelayHelper.SINGLETON
        if self.max <= 1 and java_predicate(self.healthInterface, "isAlive"):
            self.max = 1
            if self.healthScale - self.healthInterface.getHealth() > int((self.healthScale * 2) / 3):
                self.timeDelayHelper = self.slowBeatTimeDelayHelper
            elif self.healthScale - self.healthInterface.getHealth() > int(self.healthScale / 3):
                self.timeDelayHelper = self.mediumBeatTimeDelayHelper
            else:
                self.timeDelayHelper = self.fastBeatTimeDelayHelper
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        for index in range(0, self.max):
            if self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
                self.animationInterface.paintXY(graphics, self.xArray[index], self.getY())
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.game.health.Health import Health
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.NoTimeDelayHelper import NoTimeDelayHelper
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


