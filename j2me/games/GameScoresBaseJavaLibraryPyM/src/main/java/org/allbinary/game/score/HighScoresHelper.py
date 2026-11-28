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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase


@java_inherited_overloads
class HighScoresHelper(HighScoresHelperBase):
    def _java_defaults(self):
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("lastIndex", 0)

    def _init_fields(self) -> None:
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(0, 0)
        self.lastIndex: int = -1

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setHighScoresArray(self, highScoresArrayP: list[HighScores]) -> None:
        java_super_call(super(), "setHighScoresArray", highScoresArrayP)
        self.circularIndexUtil.setSize(len(self.highScoresArrayP))
    

    def getNextHighScores(self) -> HighScores:
        highScores: HighScores = self.highScoresArrayP[self.circularIndexUtil.getIndex()]
        index: int = 0
        while (highScores.getTotal() < 1 or self.lastIndex == self.circularIndexUtil.getIndex()) and index < len(self.highScoresArrayP):
            self.circularIndexUtil.next()
            highScores = self.highScoresArrayP[self.circularIndexUtil.getIndex()]
            index += 1
        self.lastIndex = self.circularIndexUtil.getIndex()
        return highScores
    

    def isAnyHighScores(self) -> bool:
        if len(self.highScoresArrayP) < 1:
            return False
        anyScores: bool = False
        highScores: HighScores = None
        for index in range(len(self.highScoresArrayP) - 1, 0 - 1, -1):
            highScores = self.highScoresArrayP[index]
            if highScores.getTotal() > 0:
                anyScores = True
        return anyScores
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


