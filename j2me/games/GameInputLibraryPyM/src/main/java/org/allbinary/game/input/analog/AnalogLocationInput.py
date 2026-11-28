# Generated Code Do Not Modify
# package org.allbinary.game.input.analog

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class AnalogLocationInput:
    NULL_ANALOG_LOCATION_INPUT: AnalogLocationInput = None

    def _init_fields(self) -> None:
        if "playerId" not in vars(self): self.playerId: int = 0
        if "customGPoint" not in vars(self): self.customGPoint: CustomGPoint = None
        if "rz" not in vars(self): self.rz: int = 0
        if "rightTrigger" not in vars(self): self.rightTrigger: int = 0
        if "leftTrigger" not in vars(self): self.leftTrigger: int = 0
    

    def __init__(self, playerId: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        __class__._init_fields(self)
        self.playerId = playerId
        self.customGPoint = CustomGPoint(0, 0, 0)
    

    def getPlayerId(self) -> int:
        return self.playerId
    

    def getCustomGPoint(self) -> CustomGPoint:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
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
# from org.allbinary.graphics.CustomGPoint import CustomGPoint


def _AnalogLocationInput_NULL_ANALOG_LOCATION_INPUT() -> object:
    return AnalogLocationInput(-1)

lazy_static(AnalogLocationInput, "NULL_ANALOG_LOCATION_INPUT", _AnalogLocationInput_NULL_ANALOG_LOCATION_INPUT)

