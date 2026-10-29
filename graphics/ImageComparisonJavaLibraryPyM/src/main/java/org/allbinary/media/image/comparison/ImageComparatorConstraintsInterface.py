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
# package org.allbinary.media.image.comparison

from __future__ import annotations



# Java interface
class ImageComparatorConstraintsInterface:
    

    def getMaxNonMatchingPixelDeltas(self) -> int:
        raise NotImplementedError()
    

    def isCollisionWithAvoidRectangles(self, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def isCollisionWithAvoidRectangles(self, point: GPoint) -> bool:
        raise NotImplementedError()
    

    def isColorAllowed(self, frame: int, point: GPoint, color: Color) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def isImageValid(self, bufferedImage: BufferedImage) -> bool:
        raise NotImplementedError()
    

    def isFrameAllowed(self, frame: int) -> bool:
        raise NotImplementedError()
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.graphics.GPoint import GPoint


