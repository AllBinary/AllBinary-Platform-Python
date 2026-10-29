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

from org.allbinary.game.score.HighScoresBase import HighScoresBase


class NoHighScoresFactory(HighScoresBase):
    instance: NoHighScoresFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.NO_HIGH_SCORES: list[HighScores] = [None] * (0)
    

    @staticmethod
    def getInstance() -> NoHighScoresFactory:
        return NoHighScoresFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        self.logUtil.putF("Getting No HighScores", self, "fetchHighScores")
        highScoresResultsListener.setHighScoresArray(self.NO_HIGH_SCORES)
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
        return HighScoresHelperBase()
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil


NoHighScoresFactory.instance = NoHighScoresFactory()

