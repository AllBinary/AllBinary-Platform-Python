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
# package org.allbinary.game.ag.layer.hud.basic.level

from __future__ import annotations

from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class LevelHudWidget(BasicHud, PaintableInterface):

    def _init_fields(self) -> None:
        self.level: int = None
        self.maxlevel: int = None
        self.levelString: list[str] = None
        self.levelNumberCharArray: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        self.levelNumberTotalDigits: int = 0
        self.offset: int = 0
        self.primitiveLongUtil: PrimitiveLongUtil = None
    

    # throws Exception
    @staticmethod
    def createHud(maxlevel: int, location: int, direction: int) -> LevelHudWidget:
        return LevelHudWidget(maxlevel, location, direction)
    

    def __init__(self, maxlevel: int, location: int, direction: int) -> None:
        from org.allbinary.game.ag.layer.hud.basic.level.LEVEL import LEVEL
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().GREY)
        self._init_fields()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(1000)
        LEVEL: str = "Lv "
        self.levelString = list(LEVEL)
        self.maxlevel = maxlevel
        self.level = maxlevel
        self.update()
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * 4
        self.offset = font.charsWidth(self.levelString, 0, len(self.levelString)) + font.getSize()
        super().updateMeasurement(graphics)
    

    def update(self) -> None:
        self.levelNumberCharArray = self.primitiveLongUtil.getCharArray(self.level)
        self.levelNumberTotalDigits = self.primitiveLongUtil.getCurrentTotalDigits()
    

    def setLevel(self, level: int) -> None:
        self.level = level
        self.update()
    

    def nextLevel(self) -> None:
        self.level += 1
        self.update()
    

    def previousLevel(self) -> None:
        self.level -= 1
        if self.level < 0:
            self.level = 0
        self.update()
    

    def isComplete(self) -> bool:
        if self.level <= self.maxlevel:
            return False
        else:
            return True
    

    def paint(self, graphics: Graphics) -> None:
        super().paintDX(graphics, self.levelString, 0, len(self.levelString), self.levelNumberCharArray, 0, self.levelNumberTotalDigits, self.offset)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


