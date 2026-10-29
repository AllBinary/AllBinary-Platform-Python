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



class AllBinaryCollisionManager:
    allBinaryCollisionManager: AllBinaryCollisionManager = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> AllBinaryCollisionManager:
        return AllBinaryCollisionManager.allBinaryCollisionManager
    

    # throws Exception
    def process(self, layerManager: LayerManager, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface, startIndex: int) -> None:
        size: int = layerManager.getSize()
        for index in range(startIndex + 1, size):
            collidableInterfaceCompositeInterface2: CollidableInterfaceCompositeInterface = layerManager.getLayerAt(index)
            self.collide(layerManager, collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2)
    

    # throws Exception
    def collide(self, layerManager: LayerManager, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2: CollidableInterfaceCompositeInterface) -> None:
        collidableBase2: CollidableBaseBehavior = collidableInterfaceCompositeInterface2.getCollidableInferface()
        collidableBase: CollidableBaseBehavior = collidableInterfaceCompositeInterface.getCollidableInferface()
        if collidableBase2.isCollidable(collidableInterfaceCompositeInterface):
            if collidableBase.isCollisionInterface(collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2):
                collidableBase.collideInterface(collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface2)
                collidableBase2.collideInterface(collidableInterfaceCompositeInterface, collidableInterfaceCompositeInterface)
from org.allbinary.game.collision.CollidableBaseBehavior import CollidableBaseBehavior
from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.LayerManager import LayerManager


AllBinaryCollisionManager.allBinaryCollisionManager = AllBinaryCollisionManager()

