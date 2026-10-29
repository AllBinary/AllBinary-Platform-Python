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
# package org.allbinary.game.ag.ai.tactical

from __future__ import annotations

from org.allbinary.game.ai.ArtificialIntelligenceInterfaceFactoryInterface import ArtificialIntelligenceInterfaceFactoryInterface


class BasicRandomAIFactory(ArtificialIntelligenceInterfaceFactoryInterface):
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.tactical.BasicRandomAI import BasicRandomAI
        visitor: Visitor = hashtable.get(BasicAI.AI_VISITOR)
        if visitor is None:
            raise Exception("No Visitor Provided")
        inputProbability: InputProbability = hashtable.get(InputProbability.INPUT_PROBABILITY)
        return BasicRandomAI(ownerLayerInterface, gameInput, inputProbability, visitor)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.ai.BasicAI import BasicAI
from org.allbinary.game.ag.ai.InputProbability import InputProbability
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.util.ABHashtable import ABHashtable


