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
# package org.allbinary.game.ag.layer.hud.basic.life

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


@java_inherited_overloads
class LivesHudWidget(*java_bases(BasicHud, PaintableInterface)):
    def _java_defaults(self):
        vars(self).setdefault("lifeInterface", None)
        vars(self).setdefault("xArray", None)
        vars(self).setdefault("animationInterface", None)

    def _init_fields(self) -> None:
        if "lifeInterface" not in vars(self): self.lifeInterface: Life = None
        if "xArray" not in vars(self): self.xArray: list[int] = None
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation, lifeInterface: Life, location: int, direction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.game.ag.life.Life import Life
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().WHITE)
        __class__._init_fields(self)
        self.lifeInterface = lifeInterface
        size: int = int(self.getLifeInterface().getMaxlives())
        self.xArray = [0] * (size)
        self.animationInterface = animationInterface
        self.updateMaxWidth = self.lifeInterface.getMaxlives() * 16
        self.updateMaxHeight = 16
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "updateMeasurement", graphics)
        maxLives: int = int(self.getLifeInterface().getMaxlives())
        for index in range(0, maxLives):
            self.xArray[index] = self.getX() + (index * 16)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
        java_super_call(super(), "onDisplayChangeEvent", displayChangeEvent)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def setX(self, x: int) -> None:
        java_super_call(super(), "setX", x)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        index = int(self.getLifeInterface().get())
        while (index := index - 1) >= 0:
            self.animationInterface.paintXY(graphics, self.xArray[index], self.getY())
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def getLifeInterface(self) -> Life:
        from org.allbinary.game.ag.life.Life import Life
        return self.lifeInterface
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.game.ag.life.Life import Life
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent


