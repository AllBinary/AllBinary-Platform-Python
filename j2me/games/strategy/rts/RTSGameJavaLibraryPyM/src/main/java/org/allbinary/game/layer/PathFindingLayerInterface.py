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

from org.allbinary.game.combat.destroy.DestroyableInterface import DestroyableInterface
from org.allbinary.game.identification.GroupInterfaceCompositeInterface import GroupInterfaceCompositeInterface
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.game.layer.waypoint.WaypointLayerInterface import WaypointLayerInterface


# Java interface
class PathFindingLayerInterface(WaypointLayerInterface, GameKeyEventSourceInterface, GroupInterfaceCompositeInterface, DestroyableInterface):
    

    # throws Exception
    def getEndGeographicMapCellPositionList(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def shouldHandleStartSameAsEnd(self) -> bool:
        raise NotImplementedError()
    

    def getGeographicMapCellPositionArea(self) -> GeographicMapCellPositionAreaBase:
        raise NotImplementedError()
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        raise NotImplementedError()
    

    # throws Exception
    def handleCost(self, ownerLayer: PathFindingLayerInterface) -> None:
        raise NotImplementedError()
    

    def getParentLayer(self) -> PathFindingLayerInterface:
        raise NotImplementedError()
    

    def getRTSLayer2LogHelper(self) -> RTSLayer2LogHelper:
        raise NotImplementedError()
    

    # throws Exception
    def setTarget(self, targetGameLayer: PathFindingLayerInterface) -> None:
        raise NotImplementedError()
from org.allbinary.util.BasicArrayList import BasicArrayList


