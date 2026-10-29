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

from org.allbinary.input.automation.module.ImageComparatorConstraints import ImageComparatorConstraints


class NoImageComparatorConstraints(ImageComparatorConstraints):
    

    def __init__(self) -> None:
        super().__init__(1)
        self.setMaxNonMatchingPixelDeltas(2147483647)
    

    def isColorAllowed(self, frame: int, point: GPoint, color: Color) -> bool:
        return True
    

    def isImageValid(self, bufferedImage: BufferedImage) -> bool:
        return True
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.graphics.GPoint import GPoint


