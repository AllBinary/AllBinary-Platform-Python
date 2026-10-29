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
# package org.allbinary.game.ag.ai.sequence

from __future__ import annotations

from org.allbinary.game.ag.ai.sequence.SequenceAI import SequenceAI


class ComboSequenceAI(SequenceAI):
    

    def __init__(self, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(artificialIntelligenceInterface, ownerLayerInterface, gameInput)
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        artificialIntelligenceInterfaceArray: list[ArtificialIntelligenceInterface] = self.getArtificialIntelligenceInterface()
        size: int = len(artificialIntelligenceInterfaceArray)
        for index in range(0, size):
            self.setIndex(index)
            super().processAI(allBinaryLayerManager)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


