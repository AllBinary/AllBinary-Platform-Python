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
# package org.allbinary.game.combat.destroy

from __future__ import annotations

from org.allbinary.layer.BasicLayerProcessor import BasicLayerProcessor


class DestroyedLayerProcessor(BasicLayerProcessor):
    DESTROYED_LAYER_PROCESSOR: BasicLayerProcessor = BasicLayerProcessor.NULL_LAYER_PROCESSOR
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def init() -> None:
        DestroyedLayerProcessor.DESTROYED_LAYER_PROCESSOR = DestroyedLayerProcessor()
    

    @staticmethod
    def getInstance() -> BasicLayerProcessor:
        return DestroyedLayerProcessor.DESTROYED_LAYER_PROCESSOR
    

    # throws Exception
    def process(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        list_: BasicArrayList = self.getList()
        size: int = list_.size()
        destroyedEventHandler: DestroyedEventHandler = DestroyedEventHandler.getInstance()
        destroyEventCircularStaticPool: DestroyEventCircularStaticPool = DestroyEventCircularStaticPool.getInstance()
        destroyedEvent: DestroyedEvent = None
        layerInterface: AllBinaryLayer = None
        for index in range(0, size):
            layerInterfaceCanBeNull: object = list_.objectArray[index]
            if layerInterfaceCanBeNull is not None:
                layerInterface = layerInterfaceCanBeNull
                allBinaryLayerManager.remove(layerInterface)
                destroyedEvent = destroyEventCircularStaticPool.getInstanceForLayer(layerInterface)
                destroyedEventHandler.fireEvent(destroyedEvent)
            else:
                commonStrings: CommonStrings = CommonStrings.getInstance()
        list_.clear()
from org.allbinary.game.combat.destroy.event.DestroyEventCircularStaticPool import DestroyEventCircularStaticPool
from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
from org.allbinary.game.combat.destroy.event.DestroyedEventHandler import DestroyedEventHandler
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


