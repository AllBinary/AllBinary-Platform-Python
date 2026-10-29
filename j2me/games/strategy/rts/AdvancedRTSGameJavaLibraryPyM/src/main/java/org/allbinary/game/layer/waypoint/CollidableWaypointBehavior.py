# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.game.layer.CollidableRTSBehavior import CollidableRTSBehavior


class CollidableWaypointBehavior(CollidableRTSBehavior):
    

    def __init__(self, collidable: bool) -> None:
        super().__init__(collidable)
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> bool:
        return False
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> None:
        pass
    

    def isCollisionInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterface: CollidableInterfaceCompositeInterface) -> bool:
        return False
    

    # throws Exception
    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterface: CollidableInterfaceCompositeInterface) -> None:
        pass
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface


