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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.RTSLayer2LogHelper import RTSLayer2LogHelper


@java_inherited_overloads
class RTSLayer2SelectedLogHelper(RTSLayer2LogHelper):
    instanceC: RTSLayer2SelectedLogHelper = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("TRACK_TO_FIRE_OR_MOVE", None)
        vars(self).setdefault("BUILDING_CHASE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.TRACK_TO_FIRE_OR_MOVE: str = "trackTo:fireOrMove"
        self.BUILDING_CHASE: str = "buildingChase"

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> RTSLayer2SelectedLogHelper:
        return RTSLayer2SelectedLogHelper.instanceC
    

    def steeringUp(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Up")), self, self.TRACK_TO_FIRE_OR_MOVE)
    

    def steeringFireOrStop(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Fire/All Stop")), self, self.TRACK_TO_FIRE_OR_MOVE)
    

    def buildingAbove(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Above")), self, self.BUILDING_CHASE)
    

    def buildingChaseLeft(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Left: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingChaseRight(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Right: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingDown(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Below")), self, self.BUILDING_CHASE)
    

    def buildingChaseDown(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Down: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingChaseUp(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" steering - Going Up: ").appendint(angle)), self, self.BUILDING_CHASE)
    

    def buildingLeft(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Left")), self, self.BUILDING_CHASE)
    

    def buildingRight(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(" Building Right")), self, self.BUILDING_CHASE)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


def _RTSLayer2SelectedLogHelper_instanceC() -> object:
    return RTSLayer2SelectedLogHelper()

lazy_static(RTSLayer2SelectedLogHelper, "instanceC", _RTSLayer2SelectedLogHelper_instanceC)

