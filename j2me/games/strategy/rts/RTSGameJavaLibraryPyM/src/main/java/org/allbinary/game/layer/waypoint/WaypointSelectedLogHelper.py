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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.waypoint.WaypointLogHelper import WaypointLogHelper


class WaypointSelectedLogHelper(WaypointLogHelper):
    instanceC: WaypointSelectedLogHelper = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WaypointSelectedLogHelper:
        return WaypointSelectedLogHelper.instanceC
    

    def onWaypointEvent(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" onWaypointEvent: ")
        stringBuffer.append(advancedRTSGameLayer.getName())
        if advancedRTSGameLayer.getParentLayer() is not None:
            stringBuffer.append(" With Parent: ")
            stringBuffer.append(advancedRTSGameLayer.getParentLayer().getName())
        self.logUtil.putF(str(stringBuffer), self, "onWaypointEvent")
    

    def addWaypointFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Adding Waypoint: ")
        stringBuffer.append(advancedRTSGameLayer.getName())
        if advancedRTSGameLayer.getParentLayer() is not None:
            stringBuffer.append(" With Parent: ")
            stringBuffer.append(advancedRTSGameLayer.getParentLayer().getName())
        self.logUtil.putF(str(stringBuffer), self, "selected: onWaypointEvent")
    

    def addWaypointFromBuildingList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface, list_: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Waypoints: ")
        stringBuffer.append(self.stringUtil.toString(list_))
        self.logUtil.putF(str(stringBuffer), self, "selected: onWaypointEvent")
    

    def insertWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(waypointName)
        stringBuffer.append(" Insert: ")
        stringBuffer.append(rtsLayer.getName())
        stringBuffer.append(" for Waypoint: ")
        self.logUtil.putF(str(stringBuffer), self, "selected: insertWaypoint")
    

    def insertWaypointList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str, list_: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(waypointName)
        stringBuffer.append(" Insert: ")
        stringBuffer.append(rtsLayer.getName())
        stringBuffer.append(" Waypoints: ")
        stringBuffer.append(self.stringUtil.toString(list_))
        self.logUtil.putF(str(stringBuffer), self, "selected: insertWaypoint")
    

    def setRandomGeographicMapCellHistoryList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, pathsList: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        size: int = pathsList.size()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(CommonLabels.getInstance().START)
        stringBuffer.appendint(size)
        stringBuffer.append(" -> ")
        stringBuffer.append(self.stringUtil.toString(pathsList))
        self.logUtil.putF(str(stringBuffer), self, "selected: setRandomGeographicMapCellHistory")
    

    def moveAwayFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" Trying to move away from building")), self, "selected: moveAwayFromBuilding")
    

    def needToMove(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior: WaypointBehaviorBase) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(unitWaypointBehavior.getMovementLogicAsString())), self, "needToMove")
    

    def setRandomGeographicMapCellHistory(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" pathsList is null")), self, "setRandomGeographicMapCellHistory")
    

    def setCurrentPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingCurrentPathGeographicMapCellPosition: GeographicMapCellPosition, currentPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        if existingCurrentPathGeographicMapCellPosition is None:
            self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" currentPathGeographicMapCellPosition: ").append(self.stringUtil.toString(currentPathGeographicMapCellPosition))), self, "setCurrentPathGeographicMapCellPosition")
    

    def setNextUnvisitedPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingNextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition, nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        if existingNextUnvisitedPathGeographicMapCellPosition != nextUnvisitedPathGeographicMapCellPosition:
            self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" nextUnvisitedPathGeographicMapCellPosition: ").append(self.stringUtil.toString(nextUnvisitedPathGeographicMapCellPosition))), self, "setNextUnvisitedPathGeographicMapCellPosition")
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _WaypointSelectedLogHelper_instanceC() -> object:
    return WaypointSelectedLogHelper()

lazy_static(WaypointSelectedLogHelper, "instanceC", _WaypointSelectedLogHelper_instanceC)

