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
# package org.allbinary.physics.movement

from __future__ import annotations



class NoMovementFactory:
    instance: NoMovementFactory = None

    def _init_fields(self) -> None:
        self.movement: Movement = Movement()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NoMovementFactory:
        return NoMovementFactory.instance
    

    def getMovmentInstance(self) -> Movement:
        return self.movement
from org.allbinary.physics.movement.Movement import Movement


NoMovementFactory.instance = NoMovementFactory()

