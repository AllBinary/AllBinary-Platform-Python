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
# package org.allbinary.game.ai.path

from __future__ import annotations



class BasicAIProcessor:

    def _init_fields(self) -> None:
        self.name: str = None
        self.geographicMapCellHistory: GeographicMapCellHistory = None
        self.geographicMapCellPositionBasicArrayList: BasicArrayList = None
        self.geographicMapCellPathHistoryInfo: GeographicMapCellPathHistoryInfo = None
        self.basicAI: BasicDirectionAIHelper = None
        self.geographicMapDirectionUtil: GeographicMapDirectionUtil = GeographicMapDirectionUtil.getInstance()
    

    def __init__(self, name: str, geographicMapCellHistory: GeographicMapCellHistory, geographicMapCellPathHistoryInfo: GeographicMapCellPathHistoryInfo, chosenPathList: BasicArrayList, angleInfo: AngleInfo, seed: int) -> None:
        from org.allbinary.game.ai.path.BasicDirectionAIHelper import BasicDirectionAIHelper
        self._init_fields()
        self.name = name
        self.geographicMapCellHistory = geographicMapCellHistory
        self.geographicMapCellPositionBasicArrayList = chosenPathList
        self.geographicMapCellPathHistoryInfo = geographicMapCellPathHistoryInfo
        self.setName(name)
        self.setNewPath(geographicMapCellHistory, chosenPathList)
        self.basicAI = BasicDirectionAIHelper(self.getName(), angleInfo)
    

    def setNewPath(self, geographicMapCellHistory: GeographicMapCellHistory, chosenPathList: BasicArrayList) -> None:
        self.setGeographicMapCellHistory(geographicMapCellHistory)
        self.geographicMapCellPositionBasicArrayList = chosenPathList
        self.init()
    

    def init(self) -> None:
        self.geographicMapCellPathHistoryInfo = GeographicMapCellPathHistoryInfo()
        self.geographicMapCellPathHistoryInfo.setPreviousOnPathGeographicMapCellPosition(self.geographicMapCellPositionBasicArrayList.get(self.geographicMapCellPositionBasicArrayList.size() - 1))
        self.geographicMapCellPathHistoryInfo.setNextOnPathGeographicMapCellPosition(self.geographicMapCellPositionBasicArrayList.get(self.geographicMapCellPositionBasicArrayList.size() - 1))
        self.update()
    

    # throws Exception
    def goTowardNextChosenOnPathPosition(self, currentGeographicMapCellPosition: GeographicMapCellPosition) -> int:
        keyDirection: int = -1
        goToGeographicMapCellPosition: GeographicMapCellPosition = self.geographicMapCellPathHistoryInfo.getNextChosenOnPathGeographicMapCellPosition()
        geographicMapDirectionData: Direction = self.geographicMapDirectionUtil.getDirectionFromCellPositionToAdjacentCellPosition(currentGeographicMapCellPosition, goToGeographicMapCellPosition)
        if geographicMapDirectionData == DirectionFactory.getInstance().NOT_BORDERED_WITH:
            geographicMapDirectionData = self.geographicMapDirectionUtil.getDirectionFromCellPositionToCellPosition(currentGeographicMapCellPosition, goToGeographicMapCellPosition)
        keyDirection = self.basicAI.getAIKeyPressedFromDirection(geographicMapDirectionData)
        return keyDirection
    

    def update(self) -> None:
        self.geographicMapCellPathHistoryInfo.setNextUnvisitedOnPathGeographicMapCellPosition(self.getGeographicMapCellHistory().getFirstUnvisited())
        self.geographicMapCellPathHistoryInfo.setNextChosenOnPathGeographicMapCellPosition(self.geographicMapCellPathHistoryInfo.getNextUnvisitedOnPathGeographicMapCellPosition())
    

    # throws Exception
    def processAI(self, myManager: AllBinaryLayerManager, currentGeographicMapCellPosition: GeographicMapCellPosition) -> int:
        keyDirection: int = -1
        if self.geographicMapCellPositionBasicArrayList.contains(currentGeographicMapCellPosition):
            self.update()
            keyDirection = self.goTowardNextChosenOnPathPosition(currentGeographicMapCellPosition)
            self.geographicMapCellPathHistoryInfo.setPreviousOnPathGeographicMapCellPosition(currentGeographicMapCellPosition)
        else:
            keyDirection = self.goTowardNextChosenOnPathPosition(currentGeographicMapCellPosition)
        return keyDirection
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getGeographicMapCellPathHistoryInfo(self) -> GeographicMapCellPathHistoryInfo:
        return self.geographicMapCellPathHistoryInfo
    

    def setGeographicMapCellPathHistoryInfo(self, geographicMapCellPathHistoryInfo: GeographicMapCellPathHistoryInfo) -> None:
        self.geographicMapCellPathHistoryInfo = geographicMapCellPathHistoryInfo
    

    def getGeographicMapCellHistory(self) -> GeographicMapCellHistory:
        return self.geographicMapCellHistory
    

    def setGeographicMapCellHistory(self, geographicMapCellHistory: GeographicMapCellHistory) -> None:
        self.geographicMapCellHistory = geographicMapCellHistory
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapDirectionUtil import GeographicMapDirectionUtil
from org.allbinary.media.graphics.geography.pathfinding.GeographicMapCellPathHistoryInfo import GeographicMapCellPathHistoryInfo


