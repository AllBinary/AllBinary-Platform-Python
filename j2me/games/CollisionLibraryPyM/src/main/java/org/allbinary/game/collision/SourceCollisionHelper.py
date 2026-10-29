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

from org.allbinary.game.collision.CollisionHelper import CollisionHelper


class SourceCollisionHelper(CollisionHelper):
    

    def __init__(self, layerInterface: AllBinaryLayer) -> None:
        super().__init__(layerInterface)
    

    def isCollidable(self, layerInterface: CollidableCompositeLayer) -> bool:
        if self.sourceLayerInterface != layerInterface:
            return True
        return False
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


