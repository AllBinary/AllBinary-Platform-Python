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



class RTSLayerLogHelper:
    instance: RTSLayerLogHelper = None
    

    @staticmethod
    def getInstance() -> RTSLayerLogHelper:
        return RTSLayerLogHelper.instance
    

    def setClosestGeographicMapCellHistory(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, pathsList: BasicArrayList) -> None:
        pass
    

    def trackTo(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition, dx: int, dy: int, reason: str) -> None:
        pass
    

    def turnTo(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int, angleInfo: AngleInfo, angle: int, movementAngle: NamedAngle, evading: bool, targetAngle: int) -> None:
        pass
    

    def doneMoving(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def closeEnough(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def movingLeft(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def movingRight(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def movingUp(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def movingDown(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def currentMoveEnded(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def evade(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def rotateLeft(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def rotateRight(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def handle(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, movementAngle: NamedAngle) -> None:
        pass
    

    def noRotation(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def notOnPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, geographicMapCellHistory: GeographicMapCellHistory, currentGeographicMapCellPosition: GeographicMapCellPosition, pathList: BasicArrayList) -> None:
        pass
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.math.NamedAngle import NamedAngle
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList


RTSLayerLogHelper.instance = RTSLayerLogHelper()

