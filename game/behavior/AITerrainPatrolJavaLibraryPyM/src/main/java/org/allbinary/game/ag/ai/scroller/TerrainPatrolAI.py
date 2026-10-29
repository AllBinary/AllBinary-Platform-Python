#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.game.ag.ai.scroller

from __future__ import annotations

from org.allbinary.game.ag.ai.scroller.PacePatrolAI import PacePatrolAI


class TerrainPatrolAI(PacePatrolAI):

    def _init_fields(self) -> None:
        self.terrainEventListener: TerrainEventListener = TerrainEventListener()
        self.DOWN: Angle = AngleFactory.getInstance().DOWN
        self.CLIFF: BasicTerrainInfo = BasicTerrainInfo(self.DOWN)
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        self._init_fields()
        TerrainEventHandler.getInstance(ownerLayerInterface).addListener(self.terrainEventListener)
        self.terrainEventListener.onTerrainEvent(TerrainEventCircularStaticPool.getInstance().getNext(self.CLIFF))
    

    def update(self) -> None:
        super().update()
        self.changeDirectionIfCliffReached()
    

    def changeDirectionIfCliffReached(self) -> None:
        list_: BasicArrayList = self.terrainEventListener.getList()
        size: int = list_.size()
        for index in range(0, size):
            terrainEvent: TerrainEvent = list_.removeAt(index)
            basicTerrainInfo: BasicTerrainInfo = terrainEvent.getBasicTerrainInfo()
            angle: Angle = basicTerrainInfo.getAngle()
            if angle == self.DOWN:
                self.nextDirection()
                if not self.isFollowLimitedByTerrain:
                    self.logUtil.putF("Following Limited", self, "onTerrainEvent")
                    self.isFollowLimitedByTerrain = True
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo
from org.allbinary.game.terrain.TerrainEvent import TerrainEvent
from org.allbinary.game.terrain.TerrainEventCircularStaticPool import TerrainEventCircularStaticPool
from org.allbinary.game.terrain.TerrainEventHandler import TerrainEventHandler
from org.allbinary.game.terrain.TerrainEventListener import TerrainEventListener
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


