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
# package org.allbinary.media.image.analysis

from __future__ import annotations



# Java interface
class ColorRangeInterface:
    

    def getMinRed(self) -> int:
        raise NotImplementedError()
    

    def setMinRed(self, minRed: int) -> None:
        raise NotImplementedError()
    

    def getMaxRed(self) -> int:
        raise NotImplementedError()
    

    def setMaxRed(self, maxRed: int) -> None:
        raise NotImplementedError()
    

    def getMinGreen(self) -> int:
        raise NotImplementedError()
    

    def setMinGreen(self, minGreen: int) -> None:
        raise NotImplementedError()
    

    def getMaxGreen(self) -> int:
        raise NotImplementedError()
    

    def setMaxGreen(self, maxGreen: int) -> None:
        raise NotImplementedError()
    

    def getMinBlue(self) -> int:
        raise NotImplementedError()
    

    def setMinBlue(self, minBlue: int) -> None:
        raise NotImplementedError()
    

    def getMaxBlue(self) -> int:
        raise NotImplementedError()
    

    def setMaxBlue(self, maxBlue: int) -> None:
        raise NotImplementedError()
    

    def isInRange(self, color: Color) -> bool:
        raise NotImplementedError()
# from java.awt import *


