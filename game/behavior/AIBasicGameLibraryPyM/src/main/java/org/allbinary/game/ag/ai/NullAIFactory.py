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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.ai.ArtificialIntelligenceInterfaceFactoryInterface import ArtificialIntelligenceInterfaceFactoryInterface


class NullAIFactory(ArtificialIntelligenceInterfaceFactoryInterface):
    NULL_AI: NullAI = None
    

    def getInstance(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.ABHashtable import ABHashtable
        return NullAIFactory.NULL_AI
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance() -> ArtificialIntelligenceInterface:
        from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
        return NullAIFactory.NULL_AI
# from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.util.ABHashtable import ABHashtable


def _NullAIFactory_NULL_AI() -> object:
    from org.allbinary.game.ag.ai.NullAI import NullAI
    return NullAI()

lazy_static(NullAIFactory, "NULL_AI", _NullAIFactory_NULL_AI)

