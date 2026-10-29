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



class ExplosionResources:
    instance: ExplosionResources = None

    def _init_fields(self) -> None:
        self.EXPLOSION_90_RESOURCE: str = "/explosion_sprite_90_by_90.png"
        self.EXPLOSION_60_RESOURCE: str = "/explosion_sprite_60_by_60.png"
        self.HALF_EXPLOSION_RESOURCE: str = "/explosion_sprite_30_by_30.png"
        self.THIRD_EXPLOSION_RESOURCE: str = "/explosion_sprite_15_by_15.png"
    

    @staticmethod
    def getInstance() -> ExplosionResources:
        return ExplosionResources.instance
    

    def __init__(self) -> None:
        self._init_fields()


ExplosionResources.instance = ExplosionResources()

