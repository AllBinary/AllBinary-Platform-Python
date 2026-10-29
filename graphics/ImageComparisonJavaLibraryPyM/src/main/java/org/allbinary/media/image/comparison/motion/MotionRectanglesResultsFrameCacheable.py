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

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


class MotionRectanglesResultsFrameCacheable(CacheableInterface):

    def _init_fields(self) -> None:
        self.motionRectangles: MotionRectangles = None
        self.frame: int = None
    

    def __init__(self, motionRectangles: MotionRectangles, frame: int) -> None:
        self._init_fields()
        self.frame = frame
        self.setMotionRectangles(motionRectangles)
    

    def getKey(self) -> object:
        return self.frame
    

    def getMotionRectangles(self) -> MotionRectangles:
        return self.motionRectangles
    

    def setMotionRectangles(self, motionRectangles: MotionRectangles) -> None:
        self.motionRectangles = motionRectangles
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(" Frame: ")
        stringBuffer.append(str(self.getKey()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


