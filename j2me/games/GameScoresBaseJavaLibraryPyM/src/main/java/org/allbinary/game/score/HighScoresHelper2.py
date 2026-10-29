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

from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase


class HighScoresHelper2(HighScoresHelperBase):

    def _init_fields(self) -> None:
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstanceAt(0, 0)
        self.selectedHighScores: HighScores = NullHighScoresSingletonFactory.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setSelectedHighScores(self, selectedHighScores: HighScores) -> None:
        self.selectedHighScores = selectedHighScores
    

    def getSelectedHighScores(self) -> HighScores:
        return self.selectedHighScores
    

    def setHighScoresArray(self, highScoresArrayP: list[HighScores]) -> None:
        super().setHighScoresArray(highScoresArrayP)
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
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory


