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
from org.allbinary.game.layer.waypoint.WaypointRunnableLogHelper import WaypointRunnableLogHelper


class WaypointRunnableSelectedLogHelper(WaypointRunnableLogHelper):
    instanceC: WaypointRunnableSelectedLogHelper = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WaypointRunnableSelectedLogHelper:
        return WaypointRunnableSelectedLogHelper.instanceC
    

    def start(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(self.commonStrings.START_RUNNABLE)), self, self.commonStrings.RUN)
    

    def end(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.logUtil.putF(str(StringMaker().append(pathFindingLayerInterface.getName()).append(self.commonStrings.END_RUNNABLE)), self, self.commonStrings.RUN)
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.string.StringMaker import StringMaker


def _WaypointRunnableSelectedLogHelper_instanceC() -> object:
    return WaypointRunnableSelectedLogHelper()

lazy_static(WaypointRunnableSelectedLogHelper, "instanceC", _WaypointRunnableSelectedLogHelper_instanceC)

