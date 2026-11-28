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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


@java_inherited_overloads
class LevelHudWidget(*java_bases(BasicHud, PaintableInterface)):
    def _java_defaults(self):
        vars(self).setdefault("level", 0)
        vars(self).setdefault("maxlevel", 0)
        vars(self).setdefault("levelString", None)
        vars(self).setdefault("levelNumberCharArray", None)
        vars(self).setdefault("levelNumberTotalDigits", 0)
        vars(self).setdefault("offset", 0)
        vars(self).setdefault("primitiveLongUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        if "level" not in vars(self): self.level: int = 0
        if "maxlevel" not in vars(self): self.maxlevel: int = 0
        if "levelString" not in vars(self): self.levelString: list[str] = None
        self.levelNumberCharArray: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        if "levelNumberTotalDigits" not in vars(self): self.levelNumberTotalDigits: int = 0
        if "offset" not in vars(self): self.offset: int = 0
        if "primitiveLongUtil" not in vars(self): self.primitiveLongUtil: PrimitiveLongUtil = None
    

    # throws Exception
    @staticmethod
    def createHud(maxlevel: int, location: int, direction: int) -> LevelHudWidget:
        return LevelHudWidget(maxlevel, location, direction)
    

    def __init__(self, maxlevel: int, location: int, direction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        super().__init__(location, direction, 2, BasicColorFactory.getInstance().GREY)
        __class__._init_fields(self)
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(1000)
        LEVEL: str = "Lv "
        self.levelString = list(LEVEL)
        self.maxlevel = maxlevel
        self.level = maxlevel
        self.update()
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * 4
        self.offset = font.charsWidth(self.levelString, 0, len(self.levelString)) + font.getSize()
        java_super_call(super(), "updateMeasurement", graphics)
    

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
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintDX", graphics, self.levelString, 0, len(self.levelString), self.levelNumberCharArray, 0, self.levelNumberTotalDigits, self.offset)
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


