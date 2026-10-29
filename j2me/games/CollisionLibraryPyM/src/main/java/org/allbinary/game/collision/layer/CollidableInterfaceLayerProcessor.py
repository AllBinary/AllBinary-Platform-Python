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
# package org.allbinary.game.collision.layer

from __future__ import annotations

from org.allbinary.layer.LayerProcessor import LayerProcessor


class CollidableInterfaceLayerProcessor(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.game.collision.layer.CollidableInterfaceLayerManager import CollidableInterfaceLayerManager
        super().__init__(CollidableInterfaceLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, index: int) -> None:
        from org.allbinary.game.collision.layer.AllBinaryCollisionManager import AllBinaryCollisionManager
        collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface = layerInterface
        if collidableInterfaceCompositeInterface.getCollidableInferface().isCollidable(collidableInterfaceCompositeInterface):
            AllBinaryCollisionManager.getInstance().process(self.getLayerManager(), collidableInterfaceCompositeInterface, index)
    

    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsCollidableInterface():
            return True
        else:
            return False
from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


