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
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_divide


class Line:

    def _init_fields(self) -> None:
        if "p1" not in vars(self): self.p1: GPoint = None
        if "p2" not in vars(self): self.p2: GPoint = None
        if "deltaX" not in vars(self): self.deltaX: float = 0.0
        if "deltaY" not in vars(self): self.deltaY: float = 0.0
    

    def __init__(self, p1: GPoint, p2: GPoint) -> None:
        from org.allbinary.graphics.PointFactory import PointFactory
        __class__._init_fields(self)
        self.p1 = PointFactory.getInstance().ZERO_ZERO
        self.p2 = self.p1
        self.setP1(p1)
        self.setP2(p2)
    

    def getGradient(self) -> float:
        return self.getDeltaY() / self.getDeltaX()
    

    def update(self) -> None:
        self.deltaX = float(self.getP1().getX()) - self.getP2().getX()
        self.deltaY = float(self.getP1().getY()) - self.getP2().getY()
    

    def getDeltaX(self) -> float:
        return self.deltaX
    

    def getDeltaY(self) -> float:
        return self.deltaY
    

    def getP1(self) -> GPoint:
        return self.p1
    

    def getP2(self) -> GPoint:
        return self.p2
    

    def setP1(self, p1: GPoint) -> None:
        self.p1 = p1
        self.update()
    

    def setP2(self, p2: GPoint) -> None:
        self.p2 = p2
        self.update()


