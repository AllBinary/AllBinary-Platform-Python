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
# package org.allbinary.game.combat.destroy.event

from __future__ import annotations



class DestroyEventCircularStaticPool:
    instance: DestroyEventCircularStaticPool = None

    def _init_fields(self) -> None:
        self.EVENT_POOL: AllBinaryEventCircularPool = AllBinaryEventCircularPool(20)
    

    @staticmethod
    def getInstance() -> DestroyEventCircularStaticPool:
        return DestroyEventCircularStaticPool.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, combatGameCanvas: AllBinaryGameCanvas) -> None:
        from org.allbinary.game.combat.destroy.event.DestroyEventFactory import DestroyEventFactory
        self.EVENT_POOL.initAllBinaryEventCircularPool(DestroyEventFactory(combatGameCanvas))
    

    # throws Exception
    def getInstanceForLayer(self, layerInterface: AllBinaryLayer) -> DestroyedEvent:
        destroyedEvent: DestroyedEvent = self.EVENT_POOL.getNextInstance()
        destroyedEvent.setLayerInterfaceForCircularStaticPool(layerInterface)
        return destroyedEvent
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.util.event.AllBinaryEventCircularPool import AllBinaryEventCircularPool


DestroyEventCircularStaticPool.instance = DestroyEventCircularStaticPool()

