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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.ai.BasicAI import BasicAI


@java_inherited_overloads
class ArrayAI(BasicAI):
    def _java_defaults(self):
        vars(self).setdefault("artificialIntelligenceInterfaceArray", None)

    def _init_fields(self) -> None:
        if "artificialIntelligenceInterfaceArray" not in vars(self): self.artificialIntelligenceInterfaceArray: list[ArtificialIntelligenceInterface] = None
    

    def __init__(self, artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        self.artificialIntelligenceInterfaceArray = artificialIntelligenceInterface
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        size: int = len(self.artificialIntelligenceInterfaceArray)
        for index in range(0, size):
            self.artificialIntelligenceInterfaceArray[index].processAI(allBinaryLayerManager)
    

    def getArtificialIntelligenceInterface(self) -> list[ArtificialIntelligenceInterface]:
        from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
        return self.artificialIntelligenceInterfaceArray
# from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


