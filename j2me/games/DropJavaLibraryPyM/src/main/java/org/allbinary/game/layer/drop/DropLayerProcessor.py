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
# package org.allbinary.game.layer.drop

from __future__ import annotations

from org.allbinary.layer.BasicLayerProcessor import BasicLayerProcessor


class DropLayerProcessor(BasicLayerProcessor):
    LAYER_PROCESSOR: BasicLayerProcessor = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> BasicLayerProcessor:
        return DropLayerProcessor.LAYER_PROCESSOR
    

    # throws Exception
    def process(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        list_: BasicArrayList = self.getList()
        size: int = list_.size()
        layerInterface: AllBinaryLayer = None
        dropLayerInterface: DropLayerInterface = None
        for index in range(0, size):
            layerInterface = list_.objectArray[index]
            dropLayerInterface = layerInterface
            layerInterface = dropLayerInterface.getDroppedLayer()
            allBinaryLayerManager.append(layerInterface)
        list_.clear()
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.util.BasicArrayList import BasicArrayList


DropLayerProcessor.LAYER_PROCESSOR = DropLayerProcessor()

