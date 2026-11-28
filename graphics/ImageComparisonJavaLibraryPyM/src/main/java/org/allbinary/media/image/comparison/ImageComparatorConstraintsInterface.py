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
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def isCollisionWithAvoidRectangles_j1_1(self, rectangle: Rectangle) -> bool:
        raise NotImplementedError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def isCollisionWithAvoidRectangles_j1_2(self, point: GPoint) -> bool:
        from org.allbinary.graphics.GPoint import GPoint
        raise NotImplementedError()

    def isCollisionWithAvoidRectangles(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Rectangle" for base in type(args[0]).__mro__)):
            return __class__.__dict__["isCollisionWithAvoidRectangles_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["isCollisionWithAvoidRectangles_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("isCollisionWithAvoidRectangles_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isCollisionWithAvoidRectangles(*args)
    

    def isColorAllowed(self, frame: int, point: GPoint, color: Color) -> bool:
        from org.allbinary.graphics.GPoint import GPoint
        raise NotImplementedError()
    

    # throws Exception
    def isImageValid(self, bufferedImage: BufferedImage) -> bool:
        raise NotImplementedError()
    

    def isFrameAllowed(self, frame: int) -> bool:
        raise NotImplementedError()
# from java.awt.Rectangle import Rectangle
# from java.awt.Color import Color
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.graphics.GPoint import GPoint


