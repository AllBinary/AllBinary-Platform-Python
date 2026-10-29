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
# package org.allbinary.game.combat.damage

from __future__ import annotations

from org.allbinary.graphics.paint.Paintable import Paintable


class DamageFloaters(Paintable):
    SINGLETON: DamageFloaters = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> DamageFloaters:
        return DamageFloaters.SINGLETON
    

    def add(self, damage: int) -> None:
        pass


DamageFloaters.SINGLETON = DamageFloaters()

