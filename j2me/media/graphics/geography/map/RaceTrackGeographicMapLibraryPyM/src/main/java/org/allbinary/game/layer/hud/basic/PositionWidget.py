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


#super.paint(graphics, positionString, currentPostString, offset2, offset);
@java_inherited_overloads
class PositionWidget(BasicHud):
    def _java_defaults(self):
        vars(self).setdefault("position", 0)
        vars(self).setdefault("positionString", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        if "position" not in vars(self): self.position: int = 0
        self.positionString: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, position: int, location: int, direction: int, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(location, direction, 2, basicColor)
        __class__._init_fields(self)
        self.updateMaxHeight = 10
        self.updateMaxWidth = 40
    

    def get(self) -> int:
        return self.position
    

    def set(self, position: int) -> None:
        self.position = position
        self.positionString = PositionWidget.toString(self.get())
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintString", graphics, self.positionString)
    

    @staticmethod
    def toString(position: int) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(position))
        if position == 1:
            stringBuffer.append("st")
        elif position == 2:
            stringBuffer.append("nd")
        elif position == 3:
            stringBuffer.append("rd")
        else:
            stringBuffer.append("th")
        return str(stringBuffer)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.graphics.color.BasicColor import BasicColor


