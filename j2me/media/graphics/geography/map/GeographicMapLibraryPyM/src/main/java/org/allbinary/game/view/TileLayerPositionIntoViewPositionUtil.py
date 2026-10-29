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
# package org.allbinary.game.view

from __future__ import annotations



class TileLayerPositionIntoViewPositionUtil:
    

    @staticmethod
    def init(gameCanvasInterface: AllBinaryGameCanvas, viewPosition: TileLayerPositionIntoViewPosition) -> None:
        geographicMapCompositeInterface: GeographicMapCompositeInterface = gameCanvasInterface.getLayerManager()
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        viewPosition.setTiledLayer(tiledLayer)
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface


