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
class HighScoresHelper2(HighScoresHelperBase):
    def _java_defaults(self):
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("selectedHighScores", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(0, 0)
        self.selectedHighScores: HighScores = NullHighScoresSingletonFactory.getInstance()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setSelectedHighScores(self, selectedHighScores: HighScores) -> None:
        self.selectedHighScores = selectedHighScores
    

    def getSelectedHighScores(self) -> HighScores:
        return self.selectedHighScores
    

    def setHighScoresArray(self, highScoresArrayP: list[HighScores]) -> None:
        java_super_call(super(), "setHighScoresArray", highScoresArrayP)
        self.circularIndexUtil.setSize(len(self.highScoresArrayP))
        self.selectHighScores()
    

    def selectHighScores(self) -> None:
        from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
        if len(self.highScoresArrayP) == 0:
            self.setSelectedHighScores(NullHighScoresSingletonFactory.getInstance())
            return
        self.circularIndexUtil.next()
        highScores: HighScores = self.highScoresArrayP[self.circularIndexUtil.getIndex()]
        index: int = 0
        while highScores.getTotal() < 1 and index < len(self.highScoresArrayP):
            highScores = self.highScoresArrayP[self.circularIndexUtil.next()]
            index += 1
        self.setSelectedHighScores(highScores)
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory


