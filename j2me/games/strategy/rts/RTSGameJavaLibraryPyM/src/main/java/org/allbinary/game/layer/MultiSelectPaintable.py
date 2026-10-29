# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


class MultiSelectPaintable(SelectionHudPaintable):

    def _init_fields(self) -> None:
        self.rootNameList: BasicArrayList = BasicArrayListD()
        self.totalCharArray: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        self.rootNamesString: str = StringUtil.getInstance().EMPTY_STRING
        self.TOTAL: str = "Total Selected: "
        self.backgroundColor: int = int(BasicColorFactory.getInstance().GREY)
        self.totalWidth: int = 0
        self.textLine2Y: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        font: Font = graphics.getFont()
        self.totalWidth = font.stringWidth(self.TOTAL)
        self.textLine2Y = (self.y + font.getHeight())
    

    def update(self, list_: BasicArrayList) -> None:
        self.clear()
        size: int = list_.size()
        self.totalCharArray = self.getPrimitiveLongUtil().getCharArray(size)
        for index in range(list_.size() - 1, 0 - 1, -1):
            rtsLayer: RTSLayer = list_.get(index)
            if not self.rootNameList.contains(rtsLayer.getRootName()):
                self.rootNameList.add(rtsLayer.getRootName())
        COMMA_SEP: str = CommonSeps.getInstance().COMMA_SEP
        stringBuffer: StringMaker = StringMaker()
        for index in range(self.rootNameList.size() - 1, 0 - 1, -1):
            rootName: str = self.rootNameList.get(index)
            stringBuffer.append(rootName)
            if index != 0:
                stringBuffer.append(COMMA_SEP)
        self.rootNamesString = str(stringBuffer)
    

    def clear(self) -> None:
        self.rootNameList.clear()
    

    def paint(self, graphics: Graphics) -> None:
        graphics.setColor(self.backgroundColor)
        graphics.drawRect(self.getX(), self.y, self.getWidth(), self.getHeight())
        graphics.setColor(self.getColor())
        graphics.drawString(self.TOTAL, self.textX, self.y, 0)
        graphics.drawChars(self.totalCharArray, 0, self.getPrimitiveLongUtil().getCurrentTotalDigits(), self.textX + self.totalWidth, self.y, 0)
        graphics.drawString(self.rootNamesString, self.textX, self.textLine2Y, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.NullUtil import NullUtil


