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

from org.allbinary.game.collision.CollidableBaseBehaviorFactory import CollidableBaseBehaviorFactory


class CollidableAlwaysPickupNeverCollideBehaviorFactory(CollidableBaseBehaviorFactory):
    instanceC: CollidableAlwaysPickupNeverCollideBehaviorFactory = None

    def _init_fields(self) -> None:
        self.instance: CollidableAlwaysPickupNeverCollideBehavior = CollidableAlwaysPickupNeverCollideBehavior()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CollidableAlwaysPickupNeverCollideBehaviorFactory:
        return CollidableAlwaysPickupNeverCollideBehaviorFactory.instanceC
    

    def createBehavior(self) -> CollidableBaseBehavior:
        return self.instance
from org.allbinary.game.collision.CollidableAlwaysPickupNeverCollideBehavior import CollidableAlwaysPickupNeverCollideBehavior


CollidableAlwaysPickupNeverCollideBehaviorFactory.instanceC = CollidableAlwaysPickupNeverCollideBehaviorFactory()

