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

from org.allbinary.game.ai.BasicAI import BasicAI


class StopAtEdgeAI(BasicAI):
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = (ownerLayerInterface)
        velocityProperties: BasicVelocityProperties = velocityInterfaceCompositeInterface.getVelocityProperties()
        x: int = ownerLayerInterface.getXP()
        y: int = ownerLayerInterface.getYP()
        x2: int = ownerLayerInterface.getX2()
        y2: int = ownerLayerInterface.getY2()
        width: int = ownerLayerInterface.getWidth()
        height: int = ownerLayerInterface.getHeight()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if x2 + velocityProperties.getVelocityXBasicDecimalP().getScaled() > displayInfo.getLastWidth():
            ownerLayerInterface.setPosition(displayInfo.getLastWidth() - width, y, ownerLayerInterface.getZP())
            velocityProperties.getVelocityYBasicDecimalP().setint(0)
        if y2 + velocityProperties.getVelocityYBasicDecimalP().getScaled() > displayInfo.getLastHeight():
            ownerLayerInterface.setPosition(x, displayInfo.getLastHeight() - height, ownerLayerInterface.getZP())
            velocityProperties.getVelocityXBasicDecimalP().setint(0)
        if x + velocityProperties.getVelocityXBasicDecimalP().getScaled() < 0:
            ownerLayerInterface.setPosition(0, y, ownerLayerInterface.getZP())
            velocityProperties.getVelocityYBasicDecimalP().setint(0)
        if y + velocityProperties.getVelocityYBasicDecimalP().getScaled() < 0:
            ownerLayerInterface.setPosition(x, 0, ownerLayerInterface.getZP())
            velocityProperties.getVelocityXBasicDecimalP().setint(0)
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


