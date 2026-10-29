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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.game.layer.waypoint.Waypoint import Waypoint


class WorkWaypoint(Waypoint):
    ID: int = SmallIntegerSingletonFactory.getInstance().getAt(25)
    

    def __init__(self, ownerLayer: PathFindingLayerInterface) -> None:
        super().__init__(ownerLayer, WorkSound.getInstance())
    

    # throws Exception
    def visit(self, unitLayer: UnitLayer) -> None:
        if unitLayer.getGroupInterface()[0] != self.ownerLayer.getGroupInterface()[0]:
            return
        size: int = self.getConnectedWaypointList().size()
        if size > 0:
            occupyList: BasicArrayList = self.ownerLayer.getGeographicMapCellPositionArea().getOccupyingGeographicMapCellPositionList()
            outOfResources: bool = True
            geologicalGeographicMapCellPosition: GeologicalGeographicMapCellPosition = None
            geologicalResource: GeologicalResource = None
            index = occupyList.size()
            while (index := index - 1) >= 0:
                geologicalGeographicMapCellPosition = occupyList.get(index)
                geologicalResource = geologicalGeographicMapCellPosition.getGeologicalResource()
                if geologicalResource.getTotal() >= 1:
                    outOfResources = False
                    maxResourceLoad: int = int(unitLayer.getMaxResourceLoad())
                    geologicalResource.remove(maxResourceLoad)
                    unitLayer.setLoad(maxResourceLoad)
            waypointInfoHudPaintable: WaypointInfoHudPaintable = self.ownerLayer.getHudPaintable()
            if self.ownerLayer == waypointInfoHudPaintable.getRtsLayer():
                waypointInfoHudPaintable.updateSelectionInfo()
            if not outOfResources:
                unitWaypointBehavior: UnitWaypointBehavior = unitLayer.getWaypointBehavior()
                rtsLayer: RTSLayer = None
                while self.getConnectedWaypointList().size() > 0:
                    rtsLayer = self.getConnectedWaypointList().get(0)
                    if rtsLayer.isDestroyed():
                        self.getConnectedWaypointList().remove(rtsLayer)
                    else:
                        unitWaypointBehavior.insertWaypoint(0, rtsLayer)
                        break
    

    def getType(self) -> int:
        return 2
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.geological.resources.GeologicalGeographicMapCellPosition import GeologicalGeographicMapCellPosition
from org.allbinary.game.layer.geological.resources.GeologicalResource import GeologicalResource
from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
from org.allbinary.media.audio.WorkSound import WorkSound
from org.allbinary.util.BasicArrayList import BasicArrayList


