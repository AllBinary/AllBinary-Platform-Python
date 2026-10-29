# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class TiledLayerUtil:
    instance: TiledLayerUtil = None
    

    @staticmethod
    def getInstance() -> TiledLayerUtil:
        return TiledLayerUtil.instance
    

    def keepOnBorderdMapX(self, terrainTiledLayer: AllBinaryTiledLayer, x: int, width: int, mapBorderBufferWidth: int) -> int:
        newX: int = x
        maxRight: int = terrainTiledLayer.getWidth() - width - mapBorderBufferWidth
        if x + width > maxRight:
            newX = maxRight
        if x < mapBorderBufferWidth:
            newX = mapBorderBufferWidth
        return newX
    

    def keepOnBorderdMapY(self, terrainTiledLayer: AllBinaryTiledLayer, y: int, height: int, mapBorderBufferHeight: int) -> int:
        newY: int = y
        maxBottom: int = terrainTiledLayer.getHeight() - height - mapBorderBufferHeight
        if y + height > maxBottom:
            newY = maxBottom
        if y < mapBorderBufferHeight:
            newY = mapBorderBufferHeight
        return newY
    

    def keepOnMapX(self, terrainTiledLayer: AllBinaryTiledLayer, x: int, width: int) -> int:
        newX: int = x
        maxRight: int = terrainTiledLayer.getWidth() - width
        if x >= maxRight:
            newX = maxRight
        if x < 0:
            newX = 0
        return newX
    

    def keepOnMapY(self, terrainTiledLayer: AllBinaryTiledLayer, y: int, height: int) -> int:
        newY: int = y
        maxBottom: int = terrainTiledLayer.getHeight() - height
        if y >= maxBottom:
            newY = maxBottom
        if y < 0:
            newY = 0
        return newY


TiledLayerUtil.instance = TiledLayerUtil()

