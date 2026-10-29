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


class ArrayAI(BasicAI):

    def _init_fields(self) -> None:
        self.artificialIntelligenceInterfaceArray: list[ArtificialIntelligenceInterface] = None
    

    def __init__(self, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.artificialIntelligenceInterfaceArray = artificialIntelligenceInterface
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        size: int = len(self.artificialIntelligenceInterfaceArray)
        for index in range(0, size):
            self.artificialIntelligenceInterfaceArray[index].processAI(allBinaryLayerManager)
    

    def getArtificialIntelligenceInterface(self) -> list[ArtificialIntelligenceInterface]:
        return self.artificialIntelligenceInterfaceArray
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


