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

from org.allbinary.layer.NamedInterface import NamedInterface


# Java interface
class CollidableInterface(NamedInterface):
    

    # throws Exception
    def isCollidable(self, ownerLayer: CollidableCompositeLayer) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def isCollision(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        raise NotImplementedError()
    

    def getCollisionTypeWith(self, layerInterface: AllBinaryLayer) -> CollisionType:
        raise NotImplementedError()
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


