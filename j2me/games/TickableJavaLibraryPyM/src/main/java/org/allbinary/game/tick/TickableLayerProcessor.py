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
# package org.allbinary.game.tick

from __future__ import annotations

from org.allbinary.layer.LayerProcessor import LayerProcessor


class TickableLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.game.tick.TickableLayerManager import TickableLayerManager
        super().__init__(TickableLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        tickableInterface: TickableInterface = layerInterface
        tickableInterface.processTick(allBinaryLayerManager)
    

    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsTickableInterface():
            return True
        else:
            return False
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


