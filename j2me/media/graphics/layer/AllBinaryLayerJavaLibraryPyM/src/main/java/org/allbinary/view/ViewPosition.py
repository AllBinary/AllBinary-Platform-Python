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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.view.ViewPositionBase import ViewPositionBase


@java_inherited_overloads
class ViewPosition(ViewPositionBase):
    def _java_defaults(self):
        vars(self).setdefault("allbinaryLayer", None)

    def _init_fields(self) -> None:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        self.allbinaryLayer: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    @staticmethod
    def getInstanceD() -> ViewPosition:
        return ViewPosition(0, 0, 0)
    

    def __init__(self, x: int, y: int, z: int) -> None:
        __class__._java_defaults(self)
        super().__init__(x, y, z)
        __class__._init_fields(self)
    

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
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        self.allbinaryLayer = allbinaryLayer
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


