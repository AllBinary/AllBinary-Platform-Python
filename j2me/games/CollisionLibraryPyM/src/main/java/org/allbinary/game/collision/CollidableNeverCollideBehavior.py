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

from org.allbinary.game.collision.CollidableBaseBehavior import CollidableBaseBehavior


class CollidableNeverCollideBehavior(CollidableBaseBehavior):
    

    def __init__(self, isCollidable: bool) -> None:
        super().__init__(isCollidable)
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, allbinaryCollidableLayer: CollidableCompositeLayer) -> bool:
        return False
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, allbinaryCollidableLayer: CollidableCompositeLayer) -> None:
        pass
    

    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        pass
    

    def isCollisionInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> bool:
        return False
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer


