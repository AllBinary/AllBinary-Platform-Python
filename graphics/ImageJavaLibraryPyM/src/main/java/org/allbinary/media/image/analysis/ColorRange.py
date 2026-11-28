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
# package org.allbinary.media.image.analysis

from __future__ import annotations

from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface


class ColorRange(ColorRangeInterface):

    def _init_fields(self) -> None:
        if "minRed" not in vars(self): self.minRed: int = 0
        if "maxRed" not in vars(self): self.maxRed: int = 0
        if "minGreen" not in vars(self): self.minGreen: int = 0
        if "maxGreen" not in vars(self): self.maxGreen: int = 0
        if "minBlue" not in vars(self): self.minBlue: int = 0
        if "maxBlue" not in vars(self): self.maxBlue: int = 0
    

    def __init__(self) -> None:
        __class__._init_fields(self)
        self.minRed = 0
        self.maxRed = 0
        self.minGreen = 0
        self.maxGreen = 0
        self.minBlue = 0
        self.maxBlue = 0
    

    def getMinRed(self) -> int:
        return self.minRed
    

    def setMinRed(self, minRed: int) -> None:
        self.minRed = minRed
    

    def getMaxRed(self) -> int:
        return self.maxRed
    

    def setMaxRed(self, maxRed: int) -> None:
        self.maxRed = maxRed
    

    def getMinGreen(self) -> int:
        return self.minGreen
    

    def setMinGreen(self, minGreen: int) -> None:
        self.minGreen = minGreen
    

    def getMaxGreen(self) -> int:
        return self.maxGreen
    

    def setMaxGreen(self, maxGreen: int) -> None:
        self.maxGreen = maxGreen
    

    def getMinBlue(self) -> int:
        return self.minBlue
    

    def setMinBlue(self, minBlue: int) -> None:
        self.minBlue = minBlue
    

    def getMaxBlue(self) -> int:
        return self.maxBlue
    

    def setMaxBlue(self, maxBlue: int) -> None:
        self.maxBlue = maxBlue
    

    def isInRange(self, color: Color) -> bool:
        if color.getRed() >= self.getMinRed() and color.getRed() <= self.getMaxRed() and color.getGreen() >= self.getMinGreen() and color.getGreen() <= self.getMaxGreen() and color.getBlue() >= self.getMinBlue() and color.getBlue() <= self.getMaxBlue():
            return True
        else:
            return False
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("getMinRed(): ")
        stringBuffer.appendint(self.getMinRed())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getMaxRed(): ")
        stringBuffer.appendint(self.getMaxRed())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getMinGreen(): ")
        stringBuffer.appendint(self.getMinGreen())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getMaxGreen(): ")
        stringBuffer.appendint(self.getMaxGreen())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getMinBlue(): ")
        stringBuffer.appendint(self.getMinGreen())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getMaxBlue(): ")
        stringBuffer.appendint(self.getMaxBlue())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.Color import Color
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


