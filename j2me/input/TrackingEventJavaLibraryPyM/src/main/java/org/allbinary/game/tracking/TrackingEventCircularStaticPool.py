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
# package org.allbinary.game.tracking

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import lazy_static


class TrackingEventCircularStaticPool:
    instance: TrackingEventCircularStaticPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventCircularPool import AllBinaryEventCircularPool
        self.EVENT_POOL: AllBinaryEventCircularPool = AllBinaryEventCircularPool(20)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TrackingEventCircularStaticPool:
        return TrackingEventCircularStaticPool.instance
    

    def init(self) -> None:
        from org.allbinary.game.tracking.TrackingEventFactory import TrackingEventFactory
        self.EVENT_POOL.initAllBinaryEventCircularPool(TrackingEventFactory())
    

    # throws Exception
    def getNextInstance(self, layerInterface: AllBinaryLayer) -> TrackingEvent:
        with self._lock:
            return self._getNextInstance_unlocked(layerInterface)

    def _getNextInstance_unlocked(self, layerInterface: AllBinaryLayer) -> TrackingEvent:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        trackingEvent: TrackingEvent = self.EVENT_POOL.getNextInstance()
        trackingEvent.setLayerInterfaceForCircularStaticPool(layerInterface)
        return trackingEvent
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.util.event.AllBinaryEventCircularPool import AllBinaryEventCircularPool


def _TrackingEventCircularStaticPool_instance() -> object:
    return TrackingEventCircularStaticPool()

lazy_static(TrackingEventCircularStaticPool, "instance", _TrackingEventCircularStaticPool_instance)

