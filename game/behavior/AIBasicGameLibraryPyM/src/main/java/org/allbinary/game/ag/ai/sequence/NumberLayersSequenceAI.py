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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.ag.ai.sequence.SequenceAI import SequenceAI


@java_inherited_overloads
class NumberLayersSequenceAI(SequenceAI):
    def _java_defaults(self):
        vars(self).setdefault("numberOfLayersLeft", 0)

    def _init_fields(self) -> None:
        if "numberOfLayersLeft" not in vars(self): self.numberOfLayersLeft: int = 0
    

    def __init__(self, numberOfEnemiesLeft: int, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(artificialIntelligenceInterface, ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        self.numberOfLayersLeft = numberOfEnemiesLeft
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        if self.getIndex() == 0:
            if allBinaryLayerManager.getSize() < self.numberOfLayersLeft:
                self.setIndex(1)
        java_super_call(super(), "processAI", allBinaryLayerManager)
# from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


