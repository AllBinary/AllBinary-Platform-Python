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

from org.allbinary.layer.BasicLayerProcessorInterface import BasicLayerProcessorInterface


# Java interface
class LayerProcessorInterface(BasicLayerProcessorInterface):
    

    def getLayerManager(self) -> LayerManager:
        raise NotImplementedError()
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        raise NotImplementedError()


