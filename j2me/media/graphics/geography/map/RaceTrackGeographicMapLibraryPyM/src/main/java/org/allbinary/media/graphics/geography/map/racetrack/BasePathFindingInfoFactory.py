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



class BasePathFindingInfoFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def init(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellPositionFactoryInitVisitor import RaceTrackGeographicMapCellPositionFactoryInitVisitor
        class RaceTrackGeographicMapCellPositionFactoryInitVisitor(GeographicMapCellPositionFactoryInitVisitorInterface):

            def _init_fields(self) -> None:
                self.startLineId: int = None
                self.finishLineId: int = None
            

            def __init__(self) -> None:
                self._init_fields()
                raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = self.geographicMapInterface.getGeographicMapCellTypeFactory()
                self.startLineId = raceTrackGeographicMapCellTypeFactory.getStartType()
                self.finishLineId = raceTrackGeographicMapCellTypeFactory.getEndType()
            

            # throws Exception
            def visit(self, tiledLayer: AllBinaryTiledLayer, cellPosition: GeographicMapCellPosition) -> None:
                from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
                row: int = cellPosition.getRow()
                column: int = cellPosition.getColumn()
                try:
                    cellTypeId: int = self.mapArray[row][column]
                    geographicCellType: int = self.geographicMapInterface.getCellTypeFromMapCellTypeInt(cellTypeId)
                    if geographicCellType == self.startLineId:
                        self.addStartPathFindingNode(self.pathFindingInfo, cellPosition)
                    if geographicCellType == self.finishLineId:
                        if geographicCellType == self.startLineId:
                            self.addEndPathFindingNode(self.pathFindingInfo, self.geographicMapInterface.getGeographicMapCellPositionFactoryInterface().getInstance(self.geographicMapInterface, cellPosition.getColumn(), cellPosition.getRow(), tiledLayer.getColumns(), tiledLayer.getRows(), tiledLayer.getCellWidth(), tiledLayer.getCellHeight()))
                        else:
                            self.addEndPathFindingNode(self.pathFindingInfo, cellPosition)
                    raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = self.geographicMapInterface.getGeographicMapCellTypeFactory()
                    geographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
                    if raceTrackGeographicMapCellTypeFactory.isPath(geographicMapCellTypeFactory.get(geographicCellType)):
                        RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance().track(cellPosition)
                    else:
                        pass
                except Exception as e:
                    commonSeps: CommonSeps = CommonSeps.getInstance()
                    self.logUtil.put(str(StringMaker().append(commonSeps.BRACKET_OPEN).appendint(row).append(commonSeps.BRACKET_CLOSE).append(commonSeps.BRACKET_OPEN).appendint(column).append("] in [").appendint(len(self.mapArray)).append(commonSeps.BRACKET_CLOSE).append(commonSeps.BRACKET_OPEN).appendint(len(self.mapArray[0])).append(commonSeps.BRACKET_CLOSE)), self, "visit", e)
                    raise e
        geographicMapInterface.getGeographicMapCellPositionFactory().visit(RaceTrackGeographicMapCellPositionFactoryInitVisitor())
    

    # throws Exception
    def addStartPathFindingNode(self, pathFindingInfo: PathFindingInfo, startGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        pathFindingInfo.addStartPathFindingNode(PathFindingNode(NullUtil.getInstance().NULL_OBJECT, startGeographicMapCellPosition))
    

    # throws Exception
    def addEndPathFindingNode(self, pathFindingInfo: PathFindingInfo, endGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        pathFindingInfo.addEndPathFindingNode(PathFindingNode(NullUtil.getInstance().NULL_OBJECT, endGeographicMapCellPosition))
    

    # throws Exception
    def getInstancePathFindingInfo(self, geographicMapInterface: BasicGeographicMap, graphArray: list[list[int]]) -> PathFindingInfo:
        raise RuntimeError()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInitVisitorInterface import GeographicMapCellPositionFactoryInitVisitorInterface
from org.allbinary.string.CommonSeps import CommonSeps


