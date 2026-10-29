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

from org.allbinary.game.ag.ai.ArrayAI import ArrayAI


class SequenceAI(ArrayAI):
    SEQUENCE_AI: str = "Sequence AI"

    def _init_fields(self) -> None:
        self.index: int = 0
    

    def __init__(self, artificialIntelligenceInterfaceArray: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(artificialIntelligenceInterfaceArray, ownerLayerInterface, gameInput)
        self._init_fields()
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        self.getArtificialIntelligenceInterface()[self.index].processAI(allBinaryLayerManager)
    

    def next(self) -> None:
        self.index += 1
        artificialIntelligenceInterface: ArtificialIntelligenceInterface = self.getSelectedArtificialIntelligenceInterface()
        if artificialIntelligenceInterface.getId() == ArtificialIntelligence.AI_ID:
            artificialIntelligenceTransitionInterface: ArtificialIntelligenceTransitionInterface = artificialIntelligenceInterface
            artificialIntelligenceTransitionInterface.transition()
    

    def getIndex(self) -> int:
        return self.index
    

    def setIndex(self, index: int) -> None:
        self.index = index
    

    def getSelectedArtificialIntelligenceInterface(self) -> ArtificialIntelligenceInterface:
        return self.getArtificialIntelligenceInterface()[self.index]
    

    def getName(self) -> str:
        return SequenceAI.SEQUENCE_AI
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        stringBuffer.append(" Selected AI: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getSelectedArtificialIntelligenceInterface()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.ai.ArtificialIntelligenceTransitionInterface import ArtificialIntelligenceTransitionInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


