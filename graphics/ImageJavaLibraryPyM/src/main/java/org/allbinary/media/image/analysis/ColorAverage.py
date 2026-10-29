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



class ColorAverage:

    def _init_fields(self) -> None:
        self.avgRed: float = 0.0
        self.avgGreen: float = 0.0
        self.avgBlue: float = 0.0
    

    def __init__(self) -> None:
        self._init_fields()
        self.setAvgRed(0)
        self.setAvgGreen(0)
        self.setAvgBlue(0)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("getAvgRed(): ")
        stringBuffer.appendfloat(self.getAvgRed())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getAvgRed(): ")
        stringBuffer.appendfloat(self.getAvgRed())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append("getAvgGreen(): ")
        stringBuffer.appendfloat(self.getAvgGreen())
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getAvgRed(self) -> float:
        return self.avgRed
    

    def setAvgRed(self, avgRed: float) -> None:
        self.avgRed = avgRed
    

    def getAvgGreen(self) -> float:
        return self.avgGreen
    

    def setAvgGreen(self, avgGreen: float) -> None:
        self.avgGreen = avgGreen
    

    def getAvgBlue(self) -> float:
        return self.avgBlue
    

    def setAvgBlue(self, avgBlue: float) -> None:
        self.avgBlue = avgBlue
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


