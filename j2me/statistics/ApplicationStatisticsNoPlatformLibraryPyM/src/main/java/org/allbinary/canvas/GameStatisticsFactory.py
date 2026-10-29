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


#NoPlatform
class GameStatisticsFactory(BaseGameStatistics):
    instance: GameStatisticsFactory = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> GameStatisticsFactory:
        return GameStatisticsFactory.instance
    

    def add(self, string: str) -> None:
        pass
    

    def toString(self) -> str:
        raise RuntimeError()

    def __str__(self) -> str:
        return self.toString()


GameStatisticsFactory.instance = GameStatisticsFactory()

