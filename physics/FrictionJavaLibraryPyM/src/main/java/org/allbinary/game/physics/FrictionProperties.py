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
# package org.allbinary.game.physics

from __future__ import annotations



class FrictionProperties:
    

    def __init__(self) -> None:
        pass
    

    def friction(self, velocityProperties: VelocityProperties, nominator: int) -> None:
        DragVelocityBehavior.instance.reduce(velocityProperties, nominator, FrictionData.getFrictionDenominator())
from org.allbinary.game.physics.friction.FrictionData import FrictionData
from org.allbinary.game.physics.velocity.DragVelocityBehavior import DragVelocityBehavior
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties


