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
# package org.allbinary.view

from __future__ import annotations

from org.allbinary.graphics.GPoint import GPoint


class ViewPositionBase(GPoint):
    NULL_VIEW_POSITION: ViewPositionBase = None
    

    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y, z)
    

    def getX2(self) -> int:
        return self.getX()
    

    def getY2(self) -> int:
        return self.getY()
    

    def getZ2(self) -> int:
        return self.getZ()
    

    def setAllbinaryLayer(self, allbinaryLayer: object) -> None:
        pass


ViewPositionBase.NULL_VIEW_POSITION = ViewPositionBase(0, 0, 0)

