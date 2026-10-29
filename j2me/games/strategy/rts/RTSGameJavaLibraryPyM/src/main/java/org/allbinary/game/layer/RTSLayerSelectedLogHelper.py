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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.RTSLayerLogHelper import RTSLayerLogHelper


class RTSLayerSelectedLogHelper(RTSLayerLogHelper):
    instanceC: RTSLayerSelectedLogHelper = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.positionStrings: PositionStrings = PositionStrings.getInstance()
        self.TRACKTO_TURNTO: str = "trackTo:turnTo"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RTSLayerSelectedLogHelper:
        return RTSLayerSelectedLogHelper.instanceC
    

    def setClosestGeographicMapCellHistory(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, pathsList: BasicArrayList) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(CommonLabels.getInstance().START)
        stringBuffer.appendint(pathsList.size())
        stringBuffer.append(" -> ")
        stringBuffer.append(StringUtil.getInstance().toString(pathsList))
        self.logUtil.putF(str(stringBuffer), self, "selected: setClosestGeographicMapCellHistory")
    

    def trackTo(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition, dx: int, dy: int, reason: str) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(StringUtil.getInstance().toString(nextUnvisitedPathGeographicMapCellPosition))
        stringBuffer.append(self.positionStrings.DX_LABEL)
        stringBuffer.appendint(dx)
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.positionStrings.DY_LABEL)
        stringBuffer.appendint(dy)
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(reason)
        self.logUtil.putF(str(stringBuffer), self, "selected: trackTo")
    

    def turnTo(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int, angleInfo: AngleInfo, angle: int, movementAngle: NamedAngle, evading: bool, targetAngle: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" steering - ")
        stringBuffer.append(self.positionStrings.DX_LABEL)
        stringBuffer.appendint(dx)
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.positionStrings.DY_LABEL)
        stringBuffer.appendint(dy)
        stringBuffer.append(" angle: ")
        stringBuffer.appendint(angle)
        stringBuffer.append(" movementAngle: ")
        stringBuffer.append(movementAngle.name)
        stringBuffer.append(self.commonSeps.FORWARD_SLASH)
        stringBuffer.appendshort(((int(movementAngle.getValue()) + 32768) % 65536 - 32768))
        if angleInfo is not None:
            angleIncrement: int = angleInfo.getAngleIncrementInfo().getAngleIncrement()
            stringBuffer.append(" angleIncrement: ")
            stringBuffer.appendshort(angleIncrement)
        stringBuffer.append(" Evading: ")
        stringBuffer.appendboolean(evading)
        self.logUtil.putF(str(stringBuffer), self, self.TRACKTO_TURNTO)
    

    def doneMoving(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - done moving 0,0")), self, self.TRACKTO_TURNTO)
    

    def closeEnough(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - close enough")), self, self.TRACKTO_TURNTO)
    

    def movingLeft(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - allow movingLeft")), self, self.TRACKTO_TURNTO)
    

    def movingRight(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - allow movingRight")), self, self.TRACKTO_TURNTO)
    

    def movingUp(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - allow movingUp")), self, self.TRACKTO_TURNTO)
    

    def movingDown(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - allow movingDown")), self, self.TRACKTO_TURNTO)
    

    def currentMoveEnded(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - correct angle, but movement not needed for current deltas so reseting movement angle")), self, self.TRACKTO_TURNTO)
    

    def evade(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - evade")), self, self.TRACKTO_TURNTO)
    

    def rotateLeft(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - rotating left")), self, self.TRACKTO_TURNTO)
    

    def rotateRight(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - rotating right")), self, self.TRACKTO_TURNTO)
    

    def handle(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, movementAngle: NamedAngle) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - movementAngle: ").append(movementAngle.name).append(self.commonSeps.FORWARD_SLASH).appendshort(((int(movementAngle.getValue()) + 32768) % 65536 - 32768))), self, self.TRACKTO_TURNTO)
    

    def noRotation(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" steering - Do not rotate")), self, self.TRACKTO_TURNTO)
    

    def notOnPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, geographicMapCellHistory: GeographicMapCellHistory, currentGeographicMapCellPosition: GeographicMapCellPosition, pathList: BasicArrayList) -> None:
        stringUtil: StringUtil = StringUtil.getInstance()
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(CommonSeps.getInstance().SPACE).appendint(int(geographicMapCellHistory.getTotalVisited())).append(CommonSeps.getInstance().SPACE).append(stringUtil.toString(currentGeographicMapCellPosition)).append(" - trying to move but not on path: ").append(stringUtil.toString(pathList))), self, "turnTo")
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.math.NamedAngle import NamedAngle
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList


RTSLayerSelectedLogHelper.instanceC = RTSLayerSelectedLogHelper()

