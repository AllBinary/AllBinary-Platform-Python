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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations



class RaceTrackStartPointUtil:
    

    # throws Exception
    @staticmethod
    def get(geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, index: int) -> GPoint:
        list_: BasicArrayList = pathFindingInfo.getStartPathFindingNodeList()
        startPathFindingNode: PathFindingNode = list_.get(index)
        geographicMapCellPosition: GeographicMapCellPosition = startPathFindingNode.geographicMapCellPosition
        point: GPoint = geographicMapCellPosition.getPoint()
        return PointFactory.getInstance().createXY(point.getX(), point.getY() + geographicMapInterface.getAllBinaryTiledLayer().getHalfCellHeight())
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode


