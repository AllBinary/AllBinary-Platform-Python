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

from org.allbinary.layer.LayerProcessor import LayerProcessor


class SingleLayerLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.layer.SingleLayerLayerManager import SingleLayerLayerManager
        super().__init__(SingleLayerLayerManager())
    

    # throws Exception
    def process(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        layerManager: LayerManager = self.getLayerManager()
        self.processAt(allBinaryLayerManager, layerManager.getLayerAt(0), 0)


