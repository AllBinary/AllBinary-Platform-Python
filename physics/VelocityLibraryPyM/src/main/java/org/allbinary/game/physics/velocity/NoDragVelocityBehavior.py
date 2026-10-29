# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.physics.velocity

from __future__ import annotations

from org.allbinary.game.physics.velocity.VelocityBehaviorBase import VelocityBehaviorBase


class NoDragVelocityBehavior(VelocityBehaviorBase):
    instance: NoDragVelocityBehavior = None

    def __init__(self) -> None:
        super().__init__()


NoDragVelocityBehavior.instance = NoDragVelocityBehavior()

