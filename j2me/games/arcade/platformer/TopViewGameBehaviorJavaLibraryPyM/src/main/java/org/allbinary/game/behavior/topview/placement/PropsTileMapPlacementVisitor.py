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


class PropsTileMapPlacementVisitor(TileMapPlacementVisitor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.randomFactory: MyRandomFactory = MyRandomFactory.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def visit(self, lastMap: TiledMap, mapData: list[list[int]]) -> None:
        layerIndex: int = 0
        tileLayer: TileLayer = (lastMap.getLayer(layerIndex))
        mapArray: list[list[int]] = tileLayer.getMapArray()
        size: int = len(mapData)
        size2: int = len(mapData[0])
        for index in range(0, size):
            for index2 in range(0, size2):
                if mapArray[index][index2] == 14:
                    pass
                else:
                    self.visit2(mapArray, mapData, index, index2)
                if index % 7 == 0:
                    if mapArray[index][index2] == 19:
                        randomInt: int = self.randomFactory.getAbsoluteNextIntAllowZero(3)
                        if randomInt == 0:
                            mapData[index][index2] = 1
                        elif randomInt == 1:
                            mapData[index][index2] = 81
                        elif randomInt == 2:
                            mapData[index][index2] = 97
                    elif mapArray[index][index2] == 17:
                        randomInt: int = self.randomFactory.getAbsoluteNextIntAllowZero(3)
                        if randomInt == 0:
                            mapData[index][index2] = 17
                        elif randomInt == 1:
                            mapData[index][index2] = 81
                        elif randomInt == 2:
                            mapData[index][index2] = 97
                if index2 % 7 == 0:
                    if mapArray[index][index2] == 34:
                        randomInt: int = self.randomFactory.getAbsoluteNextIntAllowZero(4)
                        if randomInt == 0:
                            mapData[index][index2] = 33
                        elif randomInt == 1:
                            mapData[index][index2] = 65
                        elif randomInt == 2:
                            mapData[index][index2] = 81
                        elif randomInt == 3:
                            mapData[index][index2] = 97
    

    def visit2(self, mapArray: list[list[int]], mapData: list[list[int]], index: int, index2: int) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        countX: int = 0
        countY: int = 0
        index3: int = index - 1
        for index4 in range(index2 - 1, 0, -1):
            index3 -= 1
            if index3 < 0 or index4 < 0:
                return
            if mapArray[index3][index4] != 14 or mapData[index3][index4] != 0:
                if countX > 10 and countY > 10:
                    for index5 in range(index3 + 1, index - 1):
                        for index6 in range(index4 + 1, index2 - 1):
                            if mapArray[index5][index6] != 14 or mapData[index5][index6] != 0:
                                return
                    x: int = index - (int(countX / 2))
                    y: int = index2 - (int(countY / 2))
                    if x >= 0 and y >= 0 and x < len(mapData) and y < len(mapData[0]):
                        pass
                return
            countY += 1
            countX += 1
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.mapeditor.core.TileLayer import TileLayer
from org.mapeditor.core.TiledMap import TiledMap


