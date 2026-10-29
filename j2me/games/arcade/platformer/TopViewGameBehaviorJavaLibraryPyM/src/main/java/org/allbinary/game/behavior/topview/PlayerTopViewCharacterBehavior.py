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
# package org.allbinary.game.behavior.topview

from __future__ import annotations

from org.allbinary.game.behavior.topview.TopViewCharacterBehavior import TopViewCharacterBehavior


class PlayerTopViewCharacterBehavior(TopViewCharacterBehavior):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def terrainEvent(self, layer: AllBinaryLayer, direction: Direction, x: int, y: int, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        TrackingEventHandler.getInstance().fireEvent(TrackingEventCircularStaticPool.getInstance().getNextInstance(layer))
    

    def terrainMove(self, layer: AllBinaryLayer, geographicMapInterfaceArray: list[BasicGeographicMap], x: int, y: int) -> None:
        basicGeographicMapUtil: BasicGeographicMapUtil = BasicGeographicMapUtil.getInstance()
        basicGeographicMapUtil.setPosition(geographicMapInterfaceArray, x, y)
    

    def moveIfOnScreen(self, layer: AllBinaryLayer, ax: int, ay: int) -> None:
        pass
    

    def isTiledLayerMoveable(self, terrainTiledLayer: AllBinaryTiledLayer, x: int, y: int) -> bool:
        return (terrainTiledLayer.getXP() + DisplayInfoSingleton.getInstance().getLastWidth() < terrainTiledLayer.getWidth() or x < 0) and (terrainTiledLayer.getXP() > 0 or x > 0)
from org.allbinary.direction.Direction import Direction
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.tracking.TrackingEventCircularStaticPool import TrackingEventCircularStaticPool
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapUtil import BasicGeographicMapUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


