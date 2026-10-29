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

from org.allbinary.game.layer.RTSLayer2LogHelper import RTSLayer2LogHelper


class RTSLayer2SelectedLogHelper(RTSLayer2LogHelper):
    instanceC: RTSLayer2SelectedLogHelper = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.TRACK_TO_FIRE_OR_MOVE: str = "trackTo:fireOrMove"
        self.BUILDING_CHASE: str = "buildingChase"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RTSLayer2SelectedLogHelper:
        return RTSLayer2SelectedLogHelper.instanceC
    

    def steeringUp(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Up")), self, self.TRACK_TO_FIRE_OR_MOVE)
    

    def steeringFireOrStop(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Fire/All Stop")), self, self.TRACK_TO_FIRE_OR_MOVE)
    

    def buildingAbove(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Above")), self, self.BUILDING_CHASE)
    

    def buildingChaseLeft(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Left: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingChaseRight(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Right: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingDown(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Below")), self, self.BUILDING_CHASE)
    

    def buildingChaseDown(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Down: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingChaseUp(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Up: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingLeft(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Left")), self, self.BUILDING_CHASE)
    

    def buildingRight(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Right")), self, self.BUILDING_CHASE)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


RTSLayer2SelectedLogHelper.instanceC = RTSLayer2SelectedLogHelper()

