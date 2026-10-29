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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.layer.LayerProcessor import LayerProcessor


class GameInputLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.game.input.GameInputLayerManager import GameInputLayerManager
        super().__init__(GameInputLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        gameInputInterface: GameInputInterface = layerInterface
        gameInputInterface.processInput(allBinaryLayerManager)
    

    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsGameInputInterface():
            return True
        else:
            return False
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


