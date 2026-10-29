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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.media.audio.NoSound import NoSound


class WaypointBase(EventListenerInterface):
    NULL_WAYPOINT_BASE: WaypointBase = None

    def _init_fields(self) -> None:
        self.connectedWaypointList: BasicArrayList = BasicArrayListD()
        self.sound: Sound = None
        self.allBinaryGameLayerManagerP: AllBinaryGameLayerManager = AllBinaryGameLayerManager.getNullInstance()
    

    def __init__(self, sound: Sound) -> None:
        self._init_fields()
        self.sound = sound
    

    def getSound(self) -> Sound:
        return self.sound
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        self.allBinaryGameLayerManagerP = allBinaryGameLayerManager
    

    def getConnectedWaypointList(self) -> BasicArrayList:
        return self.connectedWaypointList
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def getPathFindingInfo(self, geographicMapCellPosition: GeographicMapCellPosition) -> PathFindingInfo:
        raise RuntimeError()
    

    # throws Exception
    def getPathsList(self, geographicMapCellPosition: GeographicMapCellPosition, pathFindingInfo: PathFindingInfo, multipassState: MultipassState) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def getPathsListRunnable(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def getPathsListFromCacheOnly(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def visit(self, unitLayer: PathFindingLayerInterface) -> None:
        pass
    

    def reset(self) -> None:
        pass
    

    def getType(self) -> int:
        return 0
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.pathfinding.MultipassState import MultipassState
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


WaypointBase.NULL_WAYPOINT_BASE = WaypointBase(NoSound.getInstance())

