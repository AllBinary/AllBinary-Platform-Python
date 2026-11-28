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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.ag.ai.scroller.PacePatrolAI import PacePatrolAI


@java_inherited_overloads
class TerrainPatrolAI(PacePatrolAI):
    def _java_defaults(self):
        vars(self).setdefault("terrainEventListener", None)
        vars(self).setdefault("DOWN", None)
        vars(self).setdefault("CLIFF", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo
        from org.allbinary.game.terrain.TerrainEventListener import TerrainEventListener
        from org.allbinary.math.AngleFactory import AngleFactory
        self.terrainEventListener: TerrainEventListener = TerrainEventListener()
        self.DOWN: Angle = AngleFactory.getInstance().DOWN
        self.CLIFF: BasicTerrainInfo = BasicTerrainInfo(self.DOWN)
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.game.terrain.TerrainEventCircularStaticPool import TerrainEventCircularStaticPool
        from org.allbinary.game.terrain.TerrainEventHandler import TerrainEventHandler
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.ABHashtable import ABHashtable
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        TerrainEventHandler.getInstance(ownerLayerInterface).addListener(self.terrainEventListener)
        self.terrainEventListener.onTerrainEvent(TerrainEventCircularStaticPool.getInstance().getNext(self.CLIFF))
    

    def update(self) -> None:
        java_super_call(super(), "update")
        self.changeDirectionIfCliffReached()
    

    def changeDirectionIfCliffReached(self) -> None:
        from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo
        from org.allbinary.game.terrain.TerrainEvent import TerrainEvent
        from org.allbinary.math.Angle import Angle
        from org.allbinary.util.BasicArrayList import BasicArrayList
        list_: BasicArrayList = self.terrainEventListener.getList()
        size: int = list_.size()
        for index in range(0, size):
            terrainEvent: TerrainEvent = list_.removeAt(index)
            basicTerrainInfo: BasicTerrainInfo = terrainEvent.getBasicTerrainInfo()
            angle: Angle = basicTerrainInfo.getAngle()
            if angle == self.DOWN:
                self.nextDirection()
                if not (self.isFollowLimitedByTerrain):
                    self.logUtil.putF("Following Limited", self, "onTerrainEvent")
                    self.isFollowLimitedByTerrain = True
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo
# from org.allbinary.game.terrain.TerrainEvent import TerrainEvent
# from org.allbinary.game.terrain.TerrainEventCircularStaticPool import TerrainEventCircularStaticPool
# from org.allbinary.game.terrain.TerrainEventHandler import TerrainEventHandler
# from org.allbinary.game.terrain.TerrainEventListener import TerrainEventListener
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.math.Angle import Angle
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList


