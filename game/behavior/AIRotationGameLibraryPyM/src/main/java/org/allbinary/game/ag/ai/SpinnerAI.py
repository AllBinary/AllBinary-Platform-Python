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

from org.allbinary.game.ai.BasicAI import BasicAI


class SpinnerAI(BasicAI):

    def _init_fields(self) -> None:
        self.isEven: bool = False
        self.direction: list[int] = None
    

    def __init__(self, direction: list[int], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.direction = direction
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.isEven:
            super().processKeyAI(self.direction[0])
            self.isEven = False
        else:
            super().processKeyAI(Canvas.KEY_NUM1)
            self.isEven = True
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


