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


class UpDownVectorAI(BasicAI):

    def _init_fields(self) -> None:
        self.velocityInterface: BasicVelocityProperties = None
        self.index: int = 0
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        velocityInterfaceCompositeInterface: VelocityInterfaceCompositeInterface = self.getOwnerLayerInterface()
        self.velocityInterface = velocityInterfaceCompositeInterface.getVelocityProperties()
        self.velocityInterface.getVelocityYBasicDecimalP().setint(0)
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        y: int = self.getOwnerLayerInterface().getHeight() * 270
        if self.index < 5:
            basicDecimal: BasicDecimal = self.velocityInterface.getVelocityYBasicDecimalP()
            basicDecimal.setint(0)
            basicDecimal.addint(y)
            self.index += 1
        elif self.index < 10:
            basicDecimal: BasicDecimal = self.velocityInterface.getVelocityYBasicDecimalP()
            basicDecimal.setint(0)
            basicDecimal.subtractint(y)
            self.index += 1
        else:
            self.index = 0
            self.processAI(allBinaryLayerManager)
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.physics.velocity.BasicVelocityProperties import BasicVelocityProperties
from org.allbinary.game.physics.velocity.VelocityInterfaceCompositeInterface import VelocityInterfaceCompositeInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


