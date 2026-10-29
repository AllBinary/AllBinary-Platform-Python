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
# package org.allbinary.business.advertisement

from __future__ import annotations



class BottomLimiter:
    instance: BottomLimiter = None

    def _init_fields(self) -> None:
        self.bottom: int = 0
        self.deltaY: int = 0
        self.lower: int = 0
        self.higher: int = 0
    

    @staticmethod
    def getInstance() -> BottomLimiter:
        return BottomLimiter.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, lower: int, higher: int) -> None:
        self.lower = lower
        self.higher = higher
    

    def update(self) -> None:
        from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        gameAdState: GameAdState = GameAdStateFactory.getInstance().getCurrentInstance()
        if gameAdState.isShowingAt():
            self.deltaY = self.higher
        else:
            self.deltaY = self.lower
        self.bottom = displayInfo.getLastHeight() - self.deltaY
    

    def getDeltaY(self) -> int:
        return self.deltaY
    

    def getBottom(self) -> int:
        return self.bottom
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


BottomLimiter.instance = BottomLimiter()

