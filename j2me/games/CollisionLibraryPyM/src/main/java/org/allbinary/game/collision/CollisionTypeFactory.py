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



class CollisionTypeFactory:
    SINGLETON: CollisionTypeFactory = None

    def _init_fields(self) -> None:
        self.NONE: CollisionType = CollisionType("None")
        self.DAMAGE: CollisionType = CollisionType("Damage")
        self.PICKUP: CollisionType = CollisionType("Pickup")
        self.COLLISION: CollisionType = CollisionType("Collision")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CollisionTypeFactory:
        return CollisionTypeFactory.SINGLETON
from org.allbinary.game.collision.CollisionType import CollisionType


CollisionTypeFactory.SINGLETON = CollisionTypeFactory()

