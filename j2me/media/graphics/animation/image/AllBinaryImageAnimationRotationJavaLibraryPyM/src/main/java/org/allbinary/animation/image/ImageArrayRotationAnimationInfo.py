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
# package org.allbinary.animation.image

from __future__ import annotations



class ImageArrayRotationAnimationInfo:

    def _init_fields(self) -> None:
        self.imageArray: list[Image] = None
        self.angleIncrement: int = None
        self.totalAngle: int = None
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, imageArray: list[Image], angleIncrement: int, totalAngle: int, dx: int, dy: int) -> None:
        self._init_fields()
        self.imageArray = imageArray
        self.angleIncrement = angleIncrement
        self.totalAngle = totalAngle
        self.dx = dx
        self.dy = dy
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        self.imageArray = imageArray
    

    def getImageArray(self) -> list[Image]:
        return self.imageArray
    

    def getAngleInfoP(self) -> AngleInfo:
        return AngleInfo.getInstance(((int(self.angleIncrement) + 32768) % 65536 - 32768))
    

    def setTotalAngle(self, totalAngle: int) -> None:
        self.totalAngle = totalAngle
    

    def getTotalAngle(self) -> int:
        return self.totalAngle
    

    def setDx(self, dx: int) -> None:
        self.dx = dx
    

    def getDx(self) -> int:
        return self.dx
    

    def setDy(self, dy: int) -> None:
        self.dy = dy
    

    def getDy(self) -> int:
        return self.dy
# from javax.microedition.lcdui.Image import Image
from org.allbinary.math.AngleInfo import AngleInfo


