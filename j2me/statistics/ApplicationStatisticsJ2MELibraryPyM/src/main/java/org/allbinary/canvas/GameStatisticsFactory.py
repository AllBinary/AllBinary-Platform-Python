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
# package org.allbinary.canvas

from __future__ import annotations

from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics


#ActualPlatform
class GameStatisticsFactory(BaseGameStatistics):
    instance: GameStatisticsFactory = None

    def _init_fields(self) -> None:
        self.stringBuffer: StringMaker = StringMaker()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameStatisticsFactory:
        return GameStatisticsFactory.instance
    

    def add(self, string: str) -> None:
        if self.stringBuffer.length() > 12000:
            self.stringBuffer.delete(0, self.stringBuffer.length())
            self.stringBuffer.append("Old Stats Cleared")
        self.stringBuffer.append(string)
    

    def toString(self) -> str:
        return str(StringMaker().append(str(super())).append(str(self.stringBuffer)))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


GameStatisticsFactory.instance = GameStatisticsFactory()

