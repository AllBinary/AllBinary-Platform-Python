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
# package org.allbinary.game.physics.acceleration

from __future__ import annotations



class GravityUtil:
    instance: GravityUtil = None

    def _init_fields(self) -> None:
        self.GAME_GRAVITY_VELOCITY: int = 1800
        self.MAX_GAME_VELOCITY: int = 18000

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GravityUtil:
        return GravityUtil.instance
    

    def process(self, velocityProperties: BasicVelocityProperties, customGravity: int) -> None:
        velocityProperties.getVelocityYBasicDecimalP().addint(customGravity)
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties


GravityUtil.instance = GravityUtil()

