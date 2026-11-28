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

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInitVisitorInterface import GeographicMapCellPositionFactoryInitVisitorInterface


class BasePathFindingInfoFactory:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def init(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
        from org.allbinary.string.CommonSeps import CommonSeps
        class RaceTrackGeographicMapCellPositionFactoryInitVisitor(GeographicMapCellPositionFactoryInitVisitorInterface):

            def _init_fields(self) -> None:
                if "startLineId" not in vars(self): self.startLineId: int = 0
                if "finishLineId" not in vars(self): self.finishLineId: int = 0
                if "pathFindingInfoFactory" not in vars(self): self.pathFindingInfoFactory: BasePathFindingInfoFactory = None
                if "geographicMapInterface" not in vars(self): self.geographicMapInterface: BasicGeographicMap = None
                if "pathFindingInfo" not in vars(self): self.pathFindingInfo: PathFindingInfo = None
                if "mapArray" not in vars(self): self.mapArray: list[list[int]] = None
            

            def __init__(self, pathFindingInfoFactory: BasePathFindingInfoFactory, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
                from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
                from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
                from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
                __class__._init_fields(self)
                self.pathFindingInfoFactory = pathFindingInfoFactory
                self.geographicMapInterface = geographicMapInterface
                self.pathFindingInfo = pathFindingInfo
                self.mapArray = mapArray
                raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = geographicMapInterface.getGeographicMapCellTypeFactory()
                self.startLineId = raceTrackGeographicMapCellTypeFactory.getStartType()
                self.finishLineId = raceTrackGeographicMapCellTypeFactory.getEndType()
            

            # throws Exception
            def visit(self, tiledLayer: AllBinaryTiledLayer, cellPosition: GeographicMapCellPosition) -> None:
                from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
                from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
                from org.allbinary.logic.string.StringMaker import StringMaker
                from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
                from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
                from org.allbinary.string.CommonSeps import CommonSeps
                row: int = cellPosition.getRow()
                column: int = cellPosition.getColumn()
                try:
                    cellTypeId: int = self.mapArray[row][column]
                    geographicCellType: int = self.geographicMapInterface.getCellTypeFromMapCellTypeInt(cellTypeId)
                    if geographicCellType == self.startLineId:
                        self.pathFindingInfoFactory.addStartPathFindingNode(self.pathFindingInfo, cellPosition)
                    if geographicCellType == self.finishLineId:
                        if geographicCellType == self.startLineId:
                            self.pathFindingInfoFactory.addEndPathFindingNode(self.pathFindingInfo, self.geographicMapInterface.getGeographicMapCellPositionFactoryInterface().getInstance(self.geographicMapInterface, cellPosition.getColumn(), cellPosition.getRow(), tiledLayer.getColumns(), tiledLayer.getRows(), tiledLayer.getCellWidth(), tiledLayer.getCellHeight()))
                        else:
                            self.pathFindingInfoFactory.addEndPathFindingNode(self.pathFindingInfo, cellPosition)
                    raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = self.geographicMapInterface.getGeographicMapCellTypeFactory()
                    geographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
                    if raceTrackGeographicMapCellTypeFactory.isPath(geographicMapCellTypeFactory.get(geographicCellType)):
                        RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance().track(cellPosition)
                    else:
                        pass
                except Exception as e:
                    commonSeps: CommonSeps = CommonSeps.getInstance()
                    self.pathFindingInfoFactory.logUtil.put(str(StringMaker().append(commonSeps.BRACKET_OPEN).appendint(row).append(commonSeps.BRACKET_CLOSE).append(commonSeps.BRACKET_OPEN).appendint(column).append("] in [").appendint(len(self.mapArray)).append(commonSeps.BRACKET_CLOSE).append(commonSeps.BRACKET_OPEN).appendint(len(self.mapArray[0])).append(commonSeps.BRACKET_CLOSE)), self, "visit", e)
                    raise e
        geographicMapInterface.getGeographicMapCellPositionFactory().visit(java_new_inner(self, RaceTrackGeographicMapCellPositionFactoryInitVisitor, self, geographicMapInterface, pathFindingInfo, mapArray))
    

    # throws Exception
    def addStartPathFindingNode(self, pathFindingInfo: PathFindingInfo, startGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
        pathFindingInfo.addStartPathFindingNode(PathFindingNode(NullUtil.getInstance().NULL_OBJECT, startGeographicMapCellPosition))
    

    # throws Exception
    def addEndPathFindingNode(self, pathFindingInfo: PathFindingInfo, endGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
        pathFindingInfo.addEndPathFindingNode(PathFindingNode(NullUtil.getInstance().NULL_OBJECT, endGeographicMapCellPosition))
    

    # throws Exception
    def getInstancePathFindingInfo(self, geographicMapInterface: BasicGeographicMap, graphArray: list[list[int]]) -> PathFindingInfo:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
        raise RuntimeError()
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
# from org.allbinary.string.CommonSeps import CommonSeps


