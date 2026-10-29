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

from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class LivesHudWidget(BasicHud, PaintableInterface):

    def _init_fields(self) -> None:
        self.lifeInterface: Life = None
        self.xArray: list[int] = None
        self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation, lifeInterface: Life, location: int, direction: int) -> None:
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().WHITE)
        self._init_fields()
        self.lifeInterface = lifeInterface
        size: int = int(self.getLifeInterface().getMaxlives())
        self.xArray = [0] * (size)
        self.animationInterface = animationInterface
        self.updateMaxWidth = self.lifeInterface.getMaxlives() * 16
        self.updateMaxHeight = 16
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        maxLives: int = int(self.getLifeInterface().getMaxlives())
        for index in range(0, maxLives):
            self.xArray[index] = self.getX() + (index * 16)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        super().onDisplayChangeEvent(displayChangeEvent)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def setX(self, x: int) -> None:
        super().setX(x)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        index = int(self.getLifeInterface().get())
        while (index := index - 1) >= 0:
            self.animationInterface.paintXY(graphics, self.xArray[index], self.getY())
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def getLifeInterface(self) -> Life:
        return self.lifeInterface
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.ag.life.Life import Life
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent


