# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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

import time
import threading
from org.allbinary.game.layer.WaypointPathRunnableBase import WaypointPathRunnableBase


class WaypointPathRunnable(WaypointPathRunnableBase):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def run(self) -> None:
        try:
            self.pathFindingLayer.getWaypointRunnableLogHelper().start(self.pathFindingLayer)
            waypointBehavior: WaypointBehaviorBase = self.pathFindingLayer.getWaypointBehavior()
            geographicMapCellPosition: GeographicMapCellPosition = self.pathFindingLayer.getCurrentGeographicMapCellPosition()
            if geographicMapCellPosition is None:
                raise Exception("Should never be running here")
            waypointBehavior.setWaypointPathsList(self.targetPathFindingLayer.getWaypointBehavior().getWaypoint().getPathsListRunnable(geographicMapCellPosition))
            self.pathFindingLayer.getWaypointRunnableLogHelper().end(self.pathFindingLayer)
            time.sleep((15 + (self.priorityP * 2)) / 1000)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
    

    def isDone(self) -> bool:
        return True
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


