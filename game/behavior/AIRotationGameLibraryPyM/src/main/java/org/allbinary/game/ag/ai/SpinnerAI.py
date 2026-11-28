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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.ai.BasicAI import BasicAI


@java_inherited_overloads
class SpinnerAI(BasicAI):
    def _java_defaults(self):
        vars(self).setdefault("isEven", False)
        vars(self).setdefault("direction", None)

    def _init_fields(self) -> None:
        if "isEven" not in vars(self): self.isEven: bool = False
        if "direction" not in vars(self): self.direction: list[int] = None
    

    def __init__(self, direction: list[int], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__(ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        self.direction = direction
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        if self.isEven:
            java_super_call(super(), "processKeyAI", self.direction[0])
            self.isEven = False
        else:
            java_super_call(super(), "processKeyAI", Canvas.KEY_NUM1)
            self.isEven = True
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


