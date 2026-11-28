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
# package org.allbinary.vector

from __future__ import annotations



class VectorInfo:

    def _init_fields(self) -> None:
        if "width" not in vars(self): self.width: int = 0
        if "height" not in vars(self): self.height: int = 0
        if "points" not in vars(self): self.points: list[list[int]] = None
        if "totalFrames" not in vars(self): self.totalFrames: int = 0
    

    def __init__(self, width: int, height: int, points: list[list[int]], totalFrames: int) -> None:
        __class__._init_fields(self)
        self.width = width
        self.height = height
        self.points = points
        self.totalFrames = totalFrames
    

    def getWidth(self) -> int:
        return self.width
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def getHeight(self) -> int:
        return self.height
    

    def setHeight(self, height: int) -> None:
        self.height = height
    

    def getPoints(self) -> list[list[int]]:
        return self.points
    

    def setPoints(self, points: list[list[int]]) -> None:
        self.points = points
    

    def getTotalFrames(self) -> int:
        return self.totalFrames
    

    def setTotalFrames(self, totalFrames: int) -> None:
        self.totalFrames = totalFrames


