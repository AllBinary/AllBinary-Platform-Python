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
# package org.allbinary.game.terrain

from __future__ import annotations

import threading


class TerrainEventCircularStaticPool:
    instance: TerrainEventCircularStaticPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.EVENT_POOL: AllBinaryEventCircularPool = AllBinaryEventCircularPool(20)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TerrainEventCircularStaticPool:
        return TerrainEventCircularStaticPool.instance
    

    def init(self) -> None:
        from org.allbinary.game.terrain.TerrainEventFactory import TerrainEventFactory
        self.EVENT_POOL.initAllBinaryEventCircularPool(TerrainEventFactory())
    

    # throws Exception
    def getNext(self, basicTerrainInfo: BasicTerrainInfo) -> TerrainEvent:
        with self._lock:
            return self._getNext_unlocked(basicTerrainInfo)

    def _getNext_unlocked(self, basicTerrainInfo: BasicTerrainInfo) -> TerrainEvent:
        trackingEvent: TerrainEvent = self.EVENT_POOL.getNextInstance()
        trackingEvent.setBasicTerrainInfoForCircularStaticPool(basicTerrainInfo)
        return trackingEvent
from org.allbinary.logic.util.event.AllBinaryEventCircularPool import AllBinaryEventCircularPool


TerrainEventCircularStaticPool.instance = TerrainEventCircularStaticPool()

