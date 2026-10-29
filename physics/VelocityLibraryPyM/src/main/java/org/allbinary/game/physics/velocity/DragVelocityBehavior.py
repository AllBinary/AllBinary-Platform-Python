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
# package org.allbinary.game.physics.velocity

from __future__ import annotations

from org.allbinary.game.physics.velocity.VelocityBehaviorBase import VelocityBehaviorBase


class DragVelocityBehavior(VelocityBehaviorBase):
    instance: DragVelocityBehavior = None

    def __init__(self) -> None:
        super().__init__()
    

    def reduce(self, velocityProperties: BasicVelocityProperties, nominator: int, denominator: int) -> None:
        if velocityProperties.getVelocityXBasicDecimalP().getUnscaled() != 0:
            basicDecimal: BasicDecimal = velocityProperties.getVelocityXBasicDecimalP()
            basicDecimal.multiplyint(nominator)
            basicDecimal.divideint(denominator)
        if velocityProperties.getVelocityYBasicDecimalP().getUnscaled() != 0:
            basicDecimal: BasicDecimal = velocityProperties.getVelocityYBasicDecimalP()
            basicDecimal.multiplyint(nominator)
            basicDecimal.divideint(denominator)
    

    def reduceX(self, velocityProperties: BasicVelocityProperties, nominator: int, denominator: int) -> None:
        basicDecimal: BasicDecimal = velocityProperties.getVelocityXBasicDecimalP()
        if basicDecimal.getUnscaled() != 0:
            basicDecimal.multiplyint(nominator)
            basicDecimal.divideint(denominator)
    

    def reduceY(self, velocityProperties: BasicVelocityProperties, nominator: int, denominator: int) -> None:
        if velocityProperties.getVelocityYBasicDecimalP().getUnscaled() != 0:
            basicDecimal: BasicDecimal = velocityProperties.getVelocityYBasicDecimalP()
            basicDecimal.multiplyint(nominator)
            basicDecimal.divideint(denominator)
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


DragVelocityBehavior.instance = DragVelocityBehavior()

