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
# package org.allbinary.game.collision

from __future__ import annotations

from org.allbinary.layer.LayerProcessor import LayerProcessor


class OptimizedAllBinaryCollisionLayerProcessorForCollidableLayer(LayerProcessor):
    

    def __init__(self) -> None:
        from org.allbinary.game.collision.OptimizedAllBinaryCollisionLayerManager import OptimizedAllBinaryCollisionLayerManager
        super().__init__(OptimizedAllBinaryCollisionLayerManager())
    

    # throws Exception
    def processAt(self, allBinaryLayerManager: AllBinaryLayerManager, layerInterface: AllBinaryLayer, startIndex: int) -> None:
        collidableInterfaceCompositeInterface: CollidableCompositeLayer = layerInterface
        collidableBase: CollidableBaseBehavior = collidableInterfaceCompositeInterface.getCollidableInferface()
        if collidableBase.isCollidable(collidableInterfaceCompositeInterface):
            layerManager: LayerManager = self.getLayerManager()
            size: int = layerManager.getSize()
            collidableInterfaceCompositeInterface2: CollidableCompositeLayer = None
            collidableBase2: CollidableBaseBehavior = None
            for index in range(startIndex + 1, size):
                collidableInterfaceCompositeInterface2 = layerManager.getLayerAt(index)
                collidableBase2 = collidableInterfaceCompositeInterface2.getCollidableInferface()
                if collidableBase2.isCollidable(collidableInterfaceCompositeInterface) and collidableBase.isCollision(collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2):
                    collidableBase.collide(collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2)
                    collidableBase2.collide(collidableInterfaceCompositeInterface2, collidableInterfaceCompositeInterface)
    

    def isProcessorLayer(self, layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.implmentsCollidableInterface():
            return True
        else:
            return False
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.LayerManager import LayerManager


