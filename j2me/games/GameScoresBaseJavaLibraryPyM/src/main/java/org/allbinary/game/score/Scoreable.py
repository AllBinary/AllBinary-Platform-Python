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
# package org.allbinary.game.score

from __future__ import annotations

from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface


class Scoreable(ScoreableInterface):
    ID: int = SmallIntegerSingletonFactory.getInstance().getAt(3)

    def _init_fields(self) -> None:
        self.points: int = None
    

    def __init__(self, points: int) -> None:
        self._init_fields()
        self.points = points
    

    def addPoints(self, points: int) -> None:
        self.points += points
    

    def removePoints(self, points: int) -> None:
        self.points -= points
    

    def setPoints(self, points: int) -> None:
        self.points = points
    

    def getPoints(self) -> int:
        return self.points


