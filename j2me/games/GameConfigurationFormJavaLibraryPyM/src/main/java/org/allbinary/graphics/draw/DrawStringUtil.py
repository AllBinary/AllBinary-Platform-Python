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
# package org.allbinary.graphics.draw

from __future__ import annotations



class DrawStringUtil:
    instance: DrawStringUtil = None

    def _init_fields(self) -> None:
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.anchor: int = Anchor.TOP_LEFT

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> DrawStringUtil:
        return DrawStringUtil.instance
    

    def drawCenterString(self, graphics: Graphics, string: str, offset: int, length: int, x: int, y: int) -> None:
        width: int = (graphics.getFont().substringWidth(string, offset, length) >> 1)
        try:
            graphics.drawSubstring(string, offset, length, x - width, y, self.anchor)
        except Exception as e:
            PreLogUtil.put(str(StringMaker().append("Exception: stringLength: ").appendint(len(string)).append(" offset: ").appendint(offset).append(" currentLength: ").appendint(length)), self, "drawCenterString")
    

    def drawCenterStrings(self, graphics: Graphics, stringArray: list[str], maxWidth: int, charHeight: int, x: int, y: int) -> None:
        extraLines: int = 0
        for index in range(0, len(stringArray)):
            string: str = stringArray[index]
            if string != self.EMPTY_STRING:
                width: int = graphics.getFont().stringWidth(string)
                minTotalLines: int = 1
                if width > maxWidth:
                    minTotalLines = (int(width / maxWidth)) + 1
                linePortion: int = int(len(string) / minTotalLines)
                offset: int = 0
                currentLength: int = linePortion
                size: int = len(string)
                while offset < size:
                    if offset + currentLength > size:
                        currentLength = size - offset
                    if offset + currentLength != size:
                        while currentLength > 0 and stringArray[index].charAt(offset + currentLength) != ' ':
                            currentLength -= 1
                        if currentLength <= 4:
                            currentLength = linePortion
                    self.drawCenterString(graphics, string, offset, currentLength, x, y + ((index + ((extraLines := extraLines + 1) - 1)) * charHeight))
                    offset = offset + currentLength
                    currentLength = linePortion
                extraLines -= 1
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


DrawStringUtil.instance = DrawStringUtil()

