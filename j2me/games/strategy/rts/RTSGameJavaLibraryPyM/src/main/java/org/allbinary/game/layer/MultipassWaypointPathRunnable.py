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

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.game.layer.WaypointPathRunnableBase import WaypointPathRunnableBase


@java_inherited_overloads
class MultipassWaypointPathRunnable(WaypointPathRunnableBase):
    @java_inherited_overloads
    class FirstRunnable(ARunnable):
        def _java_defaults(self):
            vars(self).setdefault("multipassWaypointPathRunnable", None)

        def _init_fields(self) -> None:
            if "multipassWaypointPathRunnable" not in vars(self): self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processFirstRunnable()
    #    private boolean first = true;
    @java_inherited_overloads
    class SecondRunnable(ARunnable):
        def _java_defaults(self):
            vars(self).setdefault("multipassWaypointPathRunnable", None)

        def _init_fields(self) -> None:
            if "multipassWaypointPathRunnable" not in vars(self): self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processSecondRunnable()
    @java_inherited_overloads
    class EndRunnable(ARunnable):
        def _java_defaults(self):
            vars(self).setdefault("multipassWaypointPathRunnable", None)

        def _init_fields(self) -> None:
            if "multipassWaypointPathRunnable" not in vars(self): self.multipassWaypointPathRunnable: MultipassWaypointPathRunnable = None
        

        def __init__(self, multipassWaypointPathRunnable: MultipassWaypointPathRunnable) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.multipassWaypointPathRunnable = multipassWaypointPathRunnable
        

        def run(self) -> None:
            self.multipassWaypointPathRunnable.processEndRunnable()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicArrayListUtil", None)
        vars(self).setdefault("multipassState", None)
        vars(self).setdefault("done", False)
        vars(self).setdefault("list_", None)
        vars(self).setdefault("pathFindingInfo", None)
        vars(self).setdefault("FIRST_RUNNABLE", None)
        vars(self).setdefault("SECOND_RUNNABLE", None)
        vars(self).setdefault("END_RUNNABLE", None)
        vars(self).setdefault("ALREADY_ENDED_RUNNABLE", None)
        vars(self).setdefault("currentPassRunnable", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.graphics.geography.pathfinding.MultipassState import MultipassState
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.multipassState: MultipassState = MultipassState()
        self.done: bool = False
        self.list_: BasicArrayList = self.basicArrayListUtil.getImmutableInstance()
        self.pathFindingInfo: object = NullUtil.getInstance().NULL_OBJECT
        self.FIRST_RUNNABLE: object = java_new_inner(self, FirstRunnable, self)
        self.SECOND_RUNNABLE: object = java_new_inner(self, SecondRunnable, self)
        self.END_RUNNABLE: object = java_new_inner(self, EndRunnable, self)
        _java_listener_owner = self
        class _JavaListenerN66915(ARunnable):
                


            def run(self) -> None:
                raise RuntimeError()
        self.ALREADY_ENDED_RUNNABLE: object = _JavaListenerN66915()
            
        self.currentPassRunnable: object = self.FIRST_RUNNABLE
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setRunning(self, isRunning: bool) -> None:
        self.runningP = isRunning
        if self.runningP:
            self.reset()
            self.done = False
    

    def run(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            self.currentPassRunnable.run()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
    

    def reset2(self) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
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
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
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
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
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
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            waypointBehavior: WaypointBehaviorBase = self.pathFindingLayer.getWaypointBehavior()
            waypointBehavior.setWaypointPathsList(self.list_)
            self.pathFindingLayer.getWaypointRunnableLogHelper().end(self.pathFindingLayer)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
            self.setRunning(False)
        self.finish()
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.media.graphics.geography.pathfinding.MultipassState import MultipassState
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


