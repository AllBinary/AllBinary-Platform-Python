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


class OptimizedTickableLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.game.tick.OptimizedTickableLayerManager import OptimizedTickableLayerManager
        super().__init__(OptimizedTickableLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        tickableInterface: AllBinaryGameLayer = layerInterface
        tickableInterface.processTick(allBinaryLayerManager)
    

    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsTickableInterface():
            return True
        else:
            return False
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


