# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class DisplayPointScalar:
    instance: DisplayPointScalar = None
    

    @staticmethod
    def getInstance() -> DisplayPointScalar:
        return DisplayPointScalar.instance
    

    def __init__(self) -> None:
        pass
    

    def processX(self, value: int) -> int:
        return value
    

    def processY(self, value: int) -> int:
        return value
    

    def process(self, point: GPoint) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return point
# from org.allbinary.graphics.GPoint import GPoint


def _DisplayPointScalar_instance() -> object:
    return DisplayPointScalar()

lazy_static(DisplayPointScalar, "instance", _DisplayPointScalar_instance)

