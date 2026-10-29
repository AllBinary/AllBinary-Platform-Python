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
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.form.item.ABTextItem import ABTextItem


class SelectableTextItem(ABTextItem):
    

    def __init__(self, label: str, layout: int, altText: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(label, layout, altText, backgroundBasicColor, foregroundBasicColor)
    

    def isFocusable(self) -> bool:
        return True
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        stringComponent: ABStringComponent = self.getLabelStringComponent()
        if stringComponent is not None:
            graphics.setColor(int(stringComponent.getForegroundBasicColor()))
        graphics.drawString(self.getLabel(), x + 2, y, 0)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


