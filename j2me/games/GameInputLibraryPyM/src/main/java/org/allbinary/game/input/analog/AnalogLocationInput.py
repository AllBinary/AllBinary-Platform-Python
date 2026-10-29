# Generated Code Do Not Modify
# package org.allbinary.game.input.analog

from __future__ import annotations



class AnalogLocationInput:
    NULL_ANALOG_LOCATION_INPUT: AnalogLocationInput = None

    def _init_fields(self) -> None:
        self.playerId: int = None
        self.customGPoint: CustomGPoint = None
        self.rz: int = 0
        self.rightTrigger: int = 0
        self.leftTrigger: int = 0
    

    def __init__(self, playerId: int) -> None:
        self._init_fields()
        self.playerId = playerId
        self.customGPoint = CustomGPoint(0, 0, 0)
    

    def getPlayerId(self) -> int:
        return self.playerId
    

    def getCustomGPoint(self) -> CustomGPoint:
        return self.customGPoint
    

    def getRz(self) -> int:
        return self.rz
    

    def setRz(self, rz: int) -> None:
        self.rz = rz
    

    def getRightTrigger(self) -> int:
        return self.rightTrigger
    

    def setRightTrigger(self, rightTrigger: int) -> None:
        self.rightTrigger = rightTrigger
    

    def getLeftTrigger(self) -> int:
        return self.leftTrigger
    

    def setLeftTrigger(self, leftTrigger: int) -> None:
        self.leftTrigger = leftTrigger
from org.allbinary.graphics.CustomGPoint import CustomGPoint


AnalogLocationInput.NULL_ANALOG_LOCATION_INPUT = AnalogLocationInput(-1)

