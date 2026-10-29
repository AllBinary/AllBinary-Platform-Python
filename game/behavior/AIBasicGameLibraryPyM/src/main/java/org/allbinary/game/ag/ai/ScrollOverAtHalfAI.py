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


class ScrollOverAtHalfAI(BasicAI):
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        x: int = ownerLayerInterface.getXP()
        y: int = ownerLayerInterface.getYP()
        halfWidth: int = ownerLayerInterface.getHalfWidth()
        halfHeight: int = ownerLayerInterface.getHalfHeight()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if x > displayInfo.getLastWidth() - halfWidth:
            ownerLayerInterface.setPosition(halfWidth + 1, y, ownerLayerInterface.getZP())
        if y > displayInfo.getLastHeight() - halfHeight:
            ownerLayerInterface.setPosition(x, halfHeight + 1, ownerLayerInterface.getZP())
        if x < -halfWidth:
            ownerLayerInterface.setPosition(displayInfo.getLastWidth() - halfWidth, y, ownerLayerInterface.getZP())
        if y < -halfHeight:
            ownerLayerInterface.setPosition(x, displayInfo.getLastHeight() - halfHeight, ownerLayerInterface.getZP())
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


