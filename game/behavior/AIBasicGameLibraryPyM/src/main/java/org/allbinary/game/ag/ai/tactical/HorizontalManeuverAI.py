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

from org.allbinary.game.ai.BasicAI import BasicAI


class HorizontalManeuverAI(BasicAI):

    def _init_fields(self) -> None:
        self.currentRelativeAngle: int = 0
        self.currentSpeed: int = None
    

    def __init__(self, ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        self.currentSpeed = 5
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        x: int = ownerLayerInterface.getXP()
        if ownerLayerInterface.getXP() - self.currentSpeed <= 0:
            self.reverse()
            self.drop()
        if ownerLayerInterface.getX2() + self.currentSpeed > DisplayInfoSingleton.getInstance().getLastWidth():
            self.reverse()
            self.accelerate()
            self.drop()
        if self.currentRelativeAngle == 0:
            x += self.currentSpeed
        elif self.currentRelativeAngle == 180:
            x -= self.currentSpeed
        ownerLayerInterface.setPosition(x, ownerLayerInterface.getYP(), ownerLayerInterface.getZP())
        if self.currentRelativeAngle == 0:
            super().processKeyAI(Canvas.KEY_NUM0)
        elif self.currentRelativeAngle == 180:
            super().processKeyAI(Canvas.KEY_POUND)
    

    def reverse(self) -> None:
        if self.currentRelativeAngle == 180:
            self.currentRelativeAngle = 0
        elif self.currentRelativeAngle == 0:
            self.currentRelativeAngle = 180
    

    def accelerate(self) -> None:
        if self.currentSpeed < 20:
            self.currentSpeed += 1
    

    def drop(self) -> None:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        y: int = ownerLayerInterface.getYP()
        if ownerLayerInterface.getY2() + ownerLayerInterface.getHeight() > DisplayInfoSingleton.getInstance().getLastHeight():
            y = 0
        else:
            y += ownerLayerInterface.getHeight() + 1
        ownerLayerInterface.setPosition(ownerLayerInterface.getXP(), y, ownerLayerInterface.getZP())
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


