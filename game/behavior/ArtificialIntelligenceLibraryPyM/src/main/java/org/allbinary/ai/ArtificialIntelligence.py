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
# package org.allbinary.ai

from __future__ import annotations

from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface


class ArtificialIntelligence(ArtificialIntelligenceInterface):
    AI_ID: int = 2
    instance: ArtificialIntelligence = None
    

    @staticmethod
    def getInstance() -> ArtificialIntelligence:
        return ArtificialIntelligence.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def processAI(self, layerManager: AllBinaryLayerManager) -> None:
        pass
    

    def getId(self) -> int:
        return 1
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


ArtificialIntelligence.instance = ArtificialIntelligence()

