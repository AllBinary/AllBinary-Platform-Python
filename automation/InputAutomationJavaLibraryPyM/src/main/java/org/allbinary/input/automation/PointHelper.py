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
# package org.allbinary.input.automation

from __future__ import annotations



class PointHelper:
    two: float = 2.0
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getCenterPoint(rectangle: Rectangle) -> Point:
        from org.allbinary.input.automation.PointFactory import PointFactory
        x: float = rectangle.getX() + rectangle.getWidth() / PointHelper.two
        y: float = rectangle.getY() + rectangle.getHeight() / PointHelper.two
        return PointFactory.getInstance(int(x), int(y))
# from java.awt import *


