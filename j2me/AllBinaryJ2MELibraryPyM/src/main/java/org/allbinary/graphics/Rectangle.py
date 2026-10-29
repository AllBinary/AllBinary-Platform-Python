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
# package org.allbinary.graphics

from __future__ import annotations



class Rectangle:

    def _init_fields(self) -> None:
        self.point: GPoint = None
        self.width: int = None
        self.height: int = None
    

    def __init__(self, point: GPoint, width: int, height: int) -> None:
        self._init_fields()
        self.point = point
        self.width = width
        self.height = height
    

    def getPoint(self) -> GPoint:
        return self.point
    

    def setPoint(self, point: GPoint) -> None:
        self.point = point
    

    def getMaxX(self) -> int:
        return self.point.getX() + self.width
    

    def getMaxY(self) -> int:
        return self.point.getY() + self.height
    

    def getWidth(self) -> int:
        return self.width
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def getHeight(self) -> int:
        return self.height
    

    def setHeight(self, height: int) -> None:
        self.height = height
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(self.getPoint()))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(CommonLabels.getInstance().WIDTH_LABEL)
        stringBuffer.appendint(self.getWidth())
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(CommonLabels.getInstance().HEIGHT_LABEL)
        stringBuffer.appendint(self.getHeight())
        stringBuffer.append(" MaxX: ")
        stringBuffer.appendint(self.getMaxX())
        stringBuffer.append(" MaxY: ")
        stringBuffer.appendint(self.getMaxY())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps


