# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.view

from __future__ import annotations

from org.allbinary.view.ViewPositionBase import ViewPositionBase


class ViewPosition(ViewPositionBase):

    def _init_fields(self) -> None:
        self.allbinaryLayer: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    @staticmethod
    def getInstanceD() -> ViewPosition:
        return ViewPosition(0, 0, 0)
    

    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y, z)
        self._init_fields()
    

    def getX(self) -> int:
        return self.allbinaryLayer.getXP()
    

    def getY(self) -> int:
        return self.allbinaryLayer.getYP()
    

    def getZ(self) -> int:
        return self.allbinaryLayer.getZP()
    

    def getX2(self) -> int:
        return self.getX() + self.allbinaryLayer.getWidth()
    

    def getY2(self) -> int:
        return self.getY() + self.allbinaryLayer.getHeight()
    

    def getZ2(self) -> int:
        return int((self.getZ() + self.allbinaryLayer.getDepth()))
    

    def setAllbinaryLayer(self, allbinaryLayer: object) -> None:
        self.allbinaryLayer = allbinaryLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


