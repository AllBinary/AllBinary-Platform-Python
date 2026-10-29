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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from org.allbinary.bounds.BoundsVisitorInterface import BoundsVisitorInterface


class ReverseVelocityBoundsVisitor(BoundsVisitorInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.velocityInterface: VelocityInterface = None
        self.layerInterface: LayerInterface = None
    

    def __init__(self, layerInterface: LayerInterface) -> None:
        self._init_fields()
        self.layerInterface = layerInterface
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = layerInterface
        self.velocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
    

    def getX(self) -> int:
        return self.layerInterface.getXP()
    

    def getY(self) -> int:
        return self.layerInterface.getYP()
    

    def minX(self) -> None:
        if self.velocityInterface.getVelocityXBasicDecimalP().getUnscaled() < 0:
            self.velocityInterface.getVelocityXBasicDecimalP().multiplyint(-1)
    

    def maxX(self) -> None:
        if self.velocityInterface.getVelocityXBasicDecimalP().getUnscaled() > 0:
            self.velocityInterface.getVelocityXBasicDecimalP().multiplyint(-1)
    

    def minY(self) -> None:
        if self.velocityInterface.getVelocityYBasicDecimalP().getUnscaled() < 0:
            self.velocityInterface.getVelocityYBasicDecimalP().multiplyint(-1)
    

    def maxY(self) -> None:
        if self.velocityInterface.getVelocityYBasicDecimalP().getUnscaled() > 0:
            self.velocityInterface.getVelocityYBasicDecimalP().multiplyint(-1)
from org.allbinary.game.physics.velocity.VelocityInterface import VelocityInterface
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.layer.LayerInterface import LayerInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil


