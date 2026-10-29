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
# package org.allbinary.input.automation.module.generic.constraints

from __future__ import annotations

from org.allbinary.input.automation.module.MotionRectangleConstraints import MotionRectangleConstraints


class NoMotionRectangleConstraints(MotionRectangleConstraints):
    

    def __init__(self) -> None:
        from org.allbinary.input.automation.module.generic.constraints.Dimension import Dimension
        from org.allbinary.input.automation.module.generic.constraints.Dimension import Dimension
        super().__init__()
        self.setMinDimension(Dimension(0, 0))
        self.setMinArea(0)
        self.setMaxDimension(Dimension(2147483647, 2147483647))
        self.setMaxMotionRectangles(2147483647)
    

    def isValid(self, frame: int, bufferedImage: BufferedImage, rectangle: Rectangle) -> bool:
        return True
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage


