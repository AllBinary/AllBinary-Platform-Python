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

from org.allbinary.game.layer.WaypointPathRunnableBase import WaypointPathRunnableBase


class MultipassWaypointPathRunnable(WaypointPathRunnableBase):
    class FirstRunnable(ARunnable):

        def _init_fields(self) -> None:
            self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            super().__init__()
            self._init_fields()
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processFirstRunnable()
    #    private boolean first = true;
    class SecondRunnable(ARunnable):

        def _init_fields(self) -> None:
            self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            super().__init__()
            self._init_fields()
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processSecondRunnable()
    class EndRunnable(ARunnable):

        def _init_fields(self) -> None:
            self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            super().__init__()
            self._init_fields()
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processEndRunnable()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.multipassState: MultipassState = MultipassState()
        self.done: bool = False
        self.list_: BasicArrayList = self.basicArrayListUtil.getImmutableInstance()
        self.pathFindingInfo: object = NullUtil.getInstance().NULL_OBJECT
        self.FIRST_RUNNABLE: object = FirstRunnable(self)
        self.SECOND_RUNNABLE: object = SecondRunnable(self)
        self.END_RUNNABLE: object = EndRunnable(self)
        self.ALREADY_ENDED_RUNNABLE: object = (ARunnable()  # Java anonymous class body:
#         
# 
#         def run(self) -> None:
#             raise RuntimeError()
)
        self.currentPassRunnable: object = self.FIRST_RUNNABLE
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setRunning(self, isRunning: bool) -> None:
        self.runningP = isRunning
        if self.runningP:
            self.reset()
            self.done = False
    

    def run(self) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            self.currentPassRunnable.run()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
    

    def reset2(self) -> None:
        self.multipassState.step = 0
        self.multipassState.iteration = 0
        self.multipassState.iteration2 = 0
        self.pathFindingInfo = NullUtil.getInstance().NULL_OBJECT
    

    def finish(self) -> None:
        self.reset2()
        self.currentPassRunnable = self.ALREADY_ENDED_RUNNABLE
        self.done = True
    

    def isDone(self) -> bool:
        return self.done
    

    def reset(self) -> None:
        self.reset2()
        self.currentPassRunnable = self.FIRST_RUNNABLE
        self.done = False
    

    def processFirstRunnable(self) -> None:
        try:
            self.pathFindingLayer.getWaypointRunnableLogHelper().start(self.pathFindingLayer)
            self.reset2()
            geographicMapCellPosition: GeographicMapCellPosition = self.pathFindingLayer.getCurrentGeographicMapCellPosition()
            if geographicMapCellPosition is None:
                raise Exception("Should never be running here")
            self.pathFindingInfo = self.targetPathFindingLayer.getWaypointBehavior().getWaypoint().getPathFindingInfo(geographicMapCellPosition)
            localPathFindingInfo: PathFindingInfo = self.pathFindingInfo
            self.list_ = self.targetPathFindingLayer.getWaypointBehavior().getWaypoint().getPathsList(geographicMapCellPosition, localPathFindingInfo, self.multipassState)
            if self.list_ != self.basicArrayListUtil.getImmutableInstance():
                self.END_RUNNABLE.run()
            else:
                self.currentPassRunnable = self.SECOND_RUNNABLE
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
            self.finish()
    

    def processSecondRunnable(self) -> None:
        try:
            geographicMapCellPosition: GeographicMapCellPosition = self.pathFindingLayer.getCurrentGeographicMapCellPosition()
            localPathFindingInfo: PathFindingInfo = self.pathFindingInfo
            self.list_ = self.targetPathFindingLayer.getWaypointBehavior().getWaypoint().getPathsList(geographicMapCellPosition, localPathFindingInfo, self.multipassState)
            if self.list_ != self.basicArrayListUtil.getImmutableInstance():
                self.END_RUNNABLE.run()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
            self.finish()
    

    def processEndRunnable(self) -> None:
        try:
            waypointBehavior: WaypointBehaviorBase = self.pathFindingLayer.getWaypointBehavior()
            waypointBehavior.setWaypointPathsList(self.list_)
            self.pathFindingLayer.getWaypointRunnableLogHelper().end(self.pathFindingLayer)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
        self.finish()
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.pathfinding.MultipassState import MultipassState
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.game.layer.FirstRunnable import FirstRunnable
from org.allbinary.game.layer.SecondRunnable import SecondRunnable
from org.allbinary.game.layer.EndRunnable import EndRunnable


