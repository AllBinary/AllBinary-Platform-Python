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
# package org.allbinary.game.ag.layer.hud.basic.time

from __future__ import annotations



class Timer:

    def _init_fields(self) -> None:
        self.startTime: int = -1
        self.hundredthTime: int = 0
        self.maxTime: int = None
        self.modifier: int = 0
        self.hundrethsString: list[str] = PrimitiveLongSingleton.getInstance().ZERO
        self.totalDigits: int = 1
        self.primitiveLongUtil: PrimitiveLongUtil = None
        self.MAX: list[str] = ['L', 'O', 'L']
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
    

    def __init__(self, maxTime: int) -> None:
        self._init_fields()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(maxTime)
        self.maxTime = maxTime
    

    def start(self) -> None:
        self.hundredthTime = 0
        self.startTime = self.gameTickTimeDelayHelper.startTime
    

    def get(self) -> int:
        return self.hundredthTime
    

    def update(self) -> None:
        lastLowerTime: int = self.hundredthTime
        currentTime: int = ((self.modifier + self.gameTickTimeDelayHelper.startTime) - self.startTime)
        if currentTime < 0:
            currentTime = 0
        self.hundredthTime = int(currentTime / 100)
        if self.hundredthTime >= self.maxTime:
            if self.startTime > 0:
                self.hundrethsString = self.MAX
        elif lastLowerTime != self.hundredthTime:
            self.hundrethsString = self.primitiveLongUtil.getCharArray(self.hundredthTime)
            self.totalDigits = self.primitiveLongUtil.getCurrentTotalDigits()
    

    def reduce(self, value: int) -> None:
        self.modifier -= value
    

    def add(self, value: int) -> None:
        self.modifier += value
    

    def getTimeChars(self) -> list[str]:
        return self.hundrethsString
    

    def getCurrentTotalDigits(self) -> int:
        return self.totalDigits
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory


