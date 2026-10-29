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

from org.allbinary.game.ag.ai.sequence.SequenceAI import SequenceAI


class NumberOnOwnGroupSequenceAI(SequenceAI):

    def _init_fields(self) -> None:
        self.numberOnSameTeam: list[int] = None
    

    def __init__(self, numberOnSameTeam: list[int], artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(artificialIntelligenceInterface, ownerLayerInterface, gameInput)
        self._init_fields()
        self.numberOnSameTeam = numberOnSameTeam
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        layerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        index: int = self.getIndex()
        if len(self.numberOnSameTeam) > index:
            size: int = GroupLayerManagerListener.getInstance().getGroupSizeFromInterface(layerInterface)
            if int(self.numberOnSameTeam[index]) > size:
                self.next()
        super().processAI(allBinaryLayerManager)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.layer.identification.GroupLayerManagerListener import GroupLayerManagerListener
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


