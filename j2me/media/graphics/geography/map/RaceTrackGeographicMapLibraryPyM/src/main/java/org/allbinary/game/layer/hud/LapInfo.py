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
# package org.allbinary.game.layer.hud

from __future__ import annotations



class LapInfo:
    NULL_LAP_INFO: LapInfo = None

    def _init_fields(self) -> None:
        self.numberOfLaps: int = None
        self.totalLaps: int = None
    

    def __init__(self, totalLaps: int) -> None:
        self._init_fields()
        self.totalLaps = totalLaps
        self.numberOfLaps = 1
    

    def add(self) -> None:
        self.numberOfLaps += 1
    

    def getCurrentLap(self) -> int:
        return self.numberOfLaps
    

    def getTotalLaps(self) -> int:
        return self.totalLaps
    

    def isDone(self) -> bool:
        if self.numberOfLaps >= self.totalLaps:
            return True
        return False
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("isDone: ")
        stringBuffer.appendboolean(self.isDone())
        stringBuffer.append(" CurrentLap: ")
        stringBuffer.appendint(self.getCurrentLap())
        stringBuffer.append(" Total Laps: ")
        stringBuffer.appendint(self.getTotalLaps())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


LapInfo.NULL_LAP_INFO = LapInfo(-1)

