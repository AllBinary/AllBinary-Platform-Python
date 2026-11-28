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
# package org.allbinary.graphics.j2me.workarea.canvas

from __future__ import annotations



class Grid:

    def _init_fields(self) -> None:
        if "grid" not in vars(self): self.grid: GPoint = None
        self.isGridOn: bool = True
        self.isGridPossible: bool = False
        self.zoom: int = 3
        self.isChanged: bool = True

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor1(self, grid: Grid) -> None:
        __class__._init_fields(self)
        self.grid = grid.grid
        self.showGrid(grid.isGridOn)
        self.isGridPossible = grid.isGridPossible
        self.setZoom(grid.getZoom())
    

    def isGridOn(self) -> bool:
        return self.isGridOn
    

    def isGridPossible(self) -> bool:
        return self.isGridPossible
    

    def getGrid(self) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return self.grid
    

    def getZoom(self) -> int:
        return self.zoom
    

    def showGrid(self, value: bool) -> None:
        self.isGridOn = value
    

    def setZoom(self, zoom: int) -> None:
        self.zoom = zoom
        if self.zoom < 1:
            zoom = 1
        self.isChanged = True
# from org.allbinary.graphics.GPoint import GPoint


