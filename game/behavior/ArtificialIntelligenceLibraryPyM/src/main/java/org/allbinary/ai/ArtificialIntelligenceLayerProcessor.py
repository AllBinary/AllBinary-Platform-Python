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
# package org.allbinary.ai

from __future__ import annotations

from org.allbinary.layer.LayerProcessor import LayerProcessor


class ArtificialIntelligenceLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.ai.ArtificialIntelligenceLayerManager import ArtificialIntelligenceLayerManager
        super().__init__(ArtificialIntelligenceLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        artificialIntelligenceCompositeInterface: ArtificialIntelligenceCompositeInterface = layerInterface
        artificialIntelligenceCompositeInterface.getArtificialIntelligenceInterface().processAI(allBinaryLayerManager)
    

    # throws Exception
    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsArtificialIntelligenceCompositeInterface():
            return True
        else:
            return False
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


