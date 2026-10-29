# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.behavior.topview.placement

from __future__ import annotations

from org.allbinary.game.behavior.topview.placement.TileMapPlacementVisitor import TileMapPlacementVisitor


class AllAnimationsEverywhereTileMapPlacementVisitor(TileMapPlacementVisitor):

    def __init__(self) -> None:
        super().__init__()
    

    def visit(self, lastMap: TiledMap, mapData: list[list[int]]) -> None:
        size: int = len(mapData)
        size2: int = len(mapData[0]) - 7
        for index in range(0, size):
            for index2 in range(0, size2, 7):
                mapData[index][index2] = 1
                mapData[index][index2 + 1] = 17
                mapData[index][index2 + 2] = 33
                mapData[index][index2 + 3] = 49
                mapData[index][index2 + 4] = 65
                mapData[index][index2 + 5] = 81
                mapData[index][index2 + 6] = 97
from org.mapeditor.core.TiledMap import TiledMap


