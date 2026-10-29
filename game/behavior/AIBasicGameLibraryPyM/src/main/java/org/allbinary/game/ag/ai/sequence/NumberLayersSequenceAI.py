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


class NumberLayersSequenceAI(SequenceAI):

    def _init_fields(self) -> None:
        self.numberOfLayersLeft: int = None
    

    def __init__(self, numberOfEnemiesLeft: int, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(artificialIntelligenceInterface, ownerLayerInterface, gameInput)
        self._init_fields()
        self.numberOfLayersLeft = numberOfEnemiesLeft
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.getIndex() == 0:
            if allBinaryLayerManager.getSize() < self.numberOfLayersLeft:
                self.setIndex(1)
        super().processAI(allBinaryLayerManager)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


