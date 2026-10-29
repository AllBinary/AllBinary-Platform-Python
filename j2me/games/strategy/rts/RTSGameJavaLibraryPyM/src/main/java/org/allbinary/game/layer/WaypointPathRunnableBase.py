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

import threading
from org.allbinary.thread.PriorityRunnable import PriorityRunnable
from org.allbinary.thread.RunnableInterface import RunnableInterface


class WaypointPathRunnableBase(RunnableInterface, PriorityRunnable):

    def _init_fields(self) -> None:
        self.layerDistanceUtil: LayerDistanceUtil = LayerDistanceUtil.getInstance()
        self.pathFindingLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.targetPathFindingLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.priorityP: int = 2147483647
        self.runningP: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    def isRunning(self) -> bool:
        return self.runningP
    

    def setRunning(self, isRunning: bool) -> None:
        self.runningP = isRunning
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        pass
    

    def setTargetLayer(self, waypointLayer: PathFindingLayerInterface) -> None:
        self.targetPathFindingLayer = waypointLayer
        self.setPriority()
    

    def setPriority(self) -> None:
        pathFindingLayer: AllBinaryLayer = self.pathFindingLayer
        targetLayer: AllBinaryLayer = self.targetPathFindingLayer
        if targetLayer is not None:
            distance: int = self.layerDistanceUtil.getDistance(targetLayer, pathFindingLayer)
            distanceCategory: int = int(distance / 70)
            self.priorityP = distanceCategory
    

    def getTargetLayer(self) -> PathFindingLayerInterface:
        return self.targetPathFindingLayer
    

    def setUnitLayer(self, unitLayer: PathFindingLayerInterface) -> None:
        self.pathFindingLayer = unitLayer
    

    def getPriority(self) -> int:
        return self.priorityP
    

    def isDone(self) -> bool:
        return True
    

    def run(self) -> None:
        pass
    

    def reset(self) -> None:
        pass
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.math.LayerDistanceUtil import LayerDistanceUtil
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer


