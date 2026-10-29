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
# package org.allbinary.input.automation.module

from __future__ import annotations

from org.allbinary.media.image.comparison.motion.MotionRectangleConstraintsInterface import MotionRectangleConstraintsInterface


class MotionRectangleConstraints(MotionRectangleConstraintsInterface):

    def _init_fields(self) -> None:
        self.minDimension: Dimension = None
        self.maxDimension: Dimension = None
        self.maxMotionRectangles: int = 0
        self.minArea: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getMinDimension(self) -> Dimension:
        return self.minDimension
    

    def getMaxDimension(self) -> Dimension:
        return self.maxDimension
    

    def isTooSmall(self, rectangle: Rectangle) -> bool:
        if rectangle.width < self.getMinDimension().width or rectangle.height < self.getMinDimension().height:
            return True
        else:
            return False
    

    def isAreaTooSmall(self, rectangle: Rectangle) -> bool:
        if rectangle.width * rectangle.height < self.getMinArea():
            return True
        else:
            return False
    

    def isTooBig(self, rectangle: Rectangle) -> bool:
        if rectangle.width > self.getMaxDimension().width or rectangle.height > self.getMaxDimension().height:
            return True
        else:
            return False
    

    # throws Exception
    def isValid(self, frame: int, bufferedImage: BufferedImage, rectangle: Rectangle) -> bool:
        raise RuntimeError()
    

    def setMinDimension(self, minDimension: Dimension) -> None:
        self.minDimension = minDimension
    

    def setMaxDimension(self, maxDimension: Dimension) -> None:
        self.maxDimension = maxDimension
    

    def getMaxMotionRectangles(self) -> int:
        return self.maxMotionRectangles
    

    def setMaxMotionRectangles(self, maxMotionRectangles: int) -> None:
        self.maxMotionRectangles = maxMotionRectangles
    

    def getMinArea(self) -> int:
        return self.minArea
    

    def setMinArea(self, minArea: int) -> None:
        self.minArea = minArea
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage


