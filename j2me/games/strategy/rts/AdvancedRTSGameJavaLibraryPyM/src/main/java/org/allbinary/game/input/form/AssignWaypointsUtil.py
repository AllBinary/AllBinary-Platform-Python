# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.input.form

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class AssignWaypointsUtil:
    instance: AssignWaypointsUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
        from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.WAYPOINT_EVENT: RTSLayerEvent = RTSLayerEvent(NullPathFindingLayer.NULL_PATH_FINDING_LAYER)

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AssignWaypointsUtil:
        return AssignWaypointsUtil.instance
    

    def set(self, unitLayer: UnitLayer, ownerAdvancedRTSGameLayer: AdvancedRTSGameLayer) -> None:
        from org.allbinary.game.input.form.PrimaryWaypointHelper import PrimaryWaypointHelper
        from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
        from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.RTSLayer import RTSLayer
        from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
        from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            list_: BasicArrayList = ownerAdvancedRTSGameLayer.getWaypointBehavior().getOwnedWaypointList()
            unitWaypointBehavior: UnitWaypointBehavior = unitLayer.getWaypointBehavior()
            for index in range(list_.size() - 1, 0 - 1, -1):
                ownedWaypointLayer: RTSLayer = list_.get(index)
                self.WAYPOINT_EVENT.setRtsLayer(ownedWaypointLayer)
                unitWaypointBehavior.onWaypointEvent(self.WAYPOINT_EVENT)
            waypointLayer: PathFindingLayerInterface = PrimaryWaypointHelper.getInstance().getWaypointLayer()
            if waypointLayer != NullPathFindingLayer.NULL_PATH_FINDING_LAYER:
                self.WAYPOINT_EVENT.setRtsLayer(waypointLayer)
                unitWaypointBehavior.onWaypointEvent(self.WAYPOINT_EVENT)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "set", e)
# from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
# from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.game.layer.RTSLayer import RTSLayer
# from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
# from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
# from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _AssignWaypointsUtil_instance() -> object:
    return AssignWaypointsUtil()

lazy_static(AssignWaypointsUtil, "instance", _AssignWaypointsUtil_instance)

