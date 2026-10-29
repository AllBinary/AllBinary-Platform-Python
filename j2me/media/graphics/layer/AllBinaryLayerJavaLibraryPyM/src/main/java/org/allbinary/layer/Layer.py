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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


class Layer:
    ID: int = SmallIntegerSingletonFactory.getInstance().getAt(0)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.x: int = 0
        self.y: int = 0
        self.z: int = 3
        self.width: int = 0
        self.height: int = 0
        self.visible: bool = True
    

    def __init__(self, width: int, height: int) -> None:
        self._init_fields()
        self.setLayerWidth(width)
        self.setLayerHeight(height)
    

    def setPosition(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
    

    def moveDXY(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
    

    def moveDXYZ(self, dx: int, dy: int, dz: int) -> None:
        self.x += dx
        self.y += dy
        self.z += dz
    

    def getXP(self) -> int:
        return self.x
    

    def getYP(self) -> int:
        return self.y
    

    def getZP(self) -> int:
        return self.z
    

    def getWidth(self) -> int:
        return self.width
    

    def getHeight(self) -> int:
        return self.height
    

    def getDepth(self) -> int:
        return 0
    

    def setVisible(self, visible: bool) -> None:
        self.visible = visible
    

    def isVisible(self) -> bool:
        return self.visible
    

    def paint(self, graphics: Graphics) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.logUtil.putF(commonStrings.NOT_IMPLEMENTED, self, canvasStrings.PAINT)
    

    def setLayerWidth(self, width: int) -> None:
        if width < 0:
            raise ValueError()
        self.width = width
    

    def setLayerHeight(self, height: int) -> None:
        if height < 0:
            raise ValueError()
        self.height = height
    

    def toStringAppend(self, stringBuffer: StringMaker) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


