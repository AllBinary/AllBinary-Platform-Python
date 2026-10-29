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

from org.allbinary.game.ai.ArtificialIntelligenceInterfaceFactoryInterface import ArtificialIntelligenceInterfaceFactoryInterface


class DiveAndDirectionalTrackingAIFactory(ArtificialIntelligenceInterfaceFactoryInterface):
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.ThrustAIVisitorFactory import ThrustAIVisitorFactory
        from org.allbinary.game.ag.ai.BasicProbabilityAIDataFactory import BasicProbabilityAIDataFactory
        from org.allbinary.game.ag.ai.LastKeyAIVisitorFactory import LastKeyAIVisitorFactory
        from org.allbinary.game.ag.ai.DiveAndDirectionalTrackingAI import DiveAndDirectionalTrackingAI
        visitorCanBeNull: object = hashtable.get(BasicAI.AI_VISITOR)
        if visitorCanBeNull is None:
            visitorCanBeNull = ThrustAIVisitorFactory.getInstance()
        hashtable2: ABHashtable[object, object] = BasicProbabilityAIDataFactory().getInstance()
        hashtable2.put(BasicAI.AI_VISITOR, LastKeyAIVisitorFactory.getInstance())
        artificialIntelligenceInterface: ArtificialIntelligenceInterface = BasicRandomAIFactory().getInstance(hashtable2, ownerLayerInterface, gameInput)
        return DiveAndDirectionalTrackingAI(ownerLayerInterface, artificialIntelligenceInterface, gameInput, visitorCanBeNull)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.ag.ai.tactical.BasicRandomAIFactory import BasicRandomAIFactory
from org.allbinary.game.ai.BasicAI import BasicAI
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.util.ABHashtable import ABHashtable


