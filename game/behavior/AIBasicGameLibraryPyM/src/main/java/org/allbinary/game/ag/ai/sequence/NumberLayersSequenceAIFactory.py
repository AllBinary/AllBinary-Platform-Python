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



class NumberLayersSequenceAIFactory:
    

    def getInstance(self, numberOfEnemiesLeft: int, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.sequence.NumberLayersSequenceAI import NumberLayersSequenceAI
        return NumberLayersSequenceAI(numberOfEnemiesLeft, artificialIntelligenceInterface, ownerLayerInterface, gameInput)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


