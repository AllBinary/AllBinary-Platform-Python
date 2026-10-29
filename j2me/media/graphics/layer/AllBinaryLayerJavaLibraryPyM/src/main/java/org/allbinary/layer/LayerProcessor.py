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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.layer.LayerProcessorInterface import LayerProcessorInterface


class LayerProcessor(LayerProcessorInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.layerManager: LayerManager = None
    

    def __init__(self, layerManager: LayerManager) -> None:
        self._init_fields()
        self.layerManager = layerManager
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def getLayerManager(self) -> LayerManager:
        return self.layerManager
    

    # throws Exception
    def process(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        layerManager: LayerManager = self.getLayerManager()
        size: int = layerManager.getSize()
        for index in range(0, size):
            self.processAt(allBinaryLayerManager, layerManager.getLayerAt(index), index)
from org.allbinary.string.CommonStrings import CommonStrings


