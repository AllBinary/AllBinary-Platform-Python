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
# package org.allbinary.game.layer.hud.basic

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.graphics.hud.BasicHud import BasicHud


@java_inherited_overloads
class LapWidget(BasicHud):
    def _java_defaults(self):
        vars(self).setdefault("LAP_STR", None)
        vars(self).setdefault("OF_STR", None)
        vars(self).setdefault("string", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.LAP_STR: str = "Lap "
        self.OF_STR: str = " of "
        self.string: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, location: int, direction: int, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(location, direction, 2, basicColor)
        __class__._init_fields(self)
        self.updateMaxHeight = 15
        self.updateMaxWidth = 40
    

    def update(self, lapInfo: LapInfo) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.game.layer.hud.LapInfo import LapInfo
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.LAP_STR)
        stringBuffer.appendint(int(lapInfo.getCurrentLap()))
        stringBuffer.append(self.OF_STR)
        stringBuffer.appendint(int(lapInfo.getTotalLaps()))
        self.string = str(stringBuffer)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintString", graphics, self.string)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.game.layer.hud.LapInfo import LapInfo
# from org.allbinary.graphics.color.BasicColor import BasicColor


