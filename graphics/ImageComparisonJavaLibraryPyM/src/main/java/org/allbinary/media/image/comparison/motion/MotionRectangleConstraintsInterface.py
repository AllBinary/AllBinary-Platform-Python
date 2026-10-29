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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations



# Java interface
class MotionRectangleConstraintsInterface:
    

    def getMaxMotionRectangles(self) -> int:
        raise NotImplementedError()
    

    def getMinDimension(self) -> Dimension:
        raise NotImplementedError()
    

    def getMinArea(self) -> int:
        raise NotImplementedError()
    

    def getMaxDimension(self) -> Dimension:
        raise NotImplementedError()
    

    def isTooSmall(self, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
    

    def isAreaTooSmall(self, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
    

    def isTooBig(self, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def isValid(self, frame: int, bufferedImage: BufferedImage, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage


