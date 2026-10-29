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

from org.allbinary.game.collision.CollidableNeverCollideBehavior import CollidableNeverCollideBehavior


class CollidableAlwaysPickupNeverCollideBehavior(CollidableNeverCollideBehavior):
    

    def __init__(self) -> None:
        super().__init__(True)
    

    def getCollisionTypeWith(self, layerInterface: AllBinaryLayer) -> CollisionType:
        from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
        return CollisionTypeFactory.getInstance().PICKUP
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


