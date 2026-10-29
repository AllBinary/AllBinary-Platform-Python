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
# package org.allbinary.game.ag.ai.scroller

from __future__ import annotations

from org.allbinary.game.ai.ArtificialIntelligenceInterfaceFactoryInterface import ArtificialIntelligenceInterfaceFactoryInterface


class RandomPatrolFlockingFiringAIFactory(ArtificialIntelligenceInterfaceFactoryInterface):
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.scroller.RandomPatrolAI import RandomPatrolAI
        from org.allbinary.game.ag.ai.scroller.TimedFireAI import TimedFireAI
        artificialIntelligenceInterface: list[ArtificialIntelligenceInterface] = [None] * (2)
        artificialIntelligenceInterface[0] = RandomPatrolAI(hashtable, ownerLayerInterface, gameInput)
        artificialIntelligenceInterface[1] = TimedFireAI(1800, ownerLayerInterface, gameInput)
        return ArrayAI(artificialIntelligenceInterface, ownerLayerInterface, gameInput)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.ag.ai.ArrayAI import ArrayAI
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.util.ABHashtable import ABHashtable


