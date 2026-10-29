# Generated Code Do Not Modify
# package org.allbinary.game.score

from __future__ import annotations

from org.allbinary.game.score.HighScoresBase import HighScoresBase


class BasicHighScoresFactory(HighScoresBase):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
        self.highScoresArray: list[HighScores] = [None] * (1)
        self.TOP: str = "Top"
        self.SCORES: str = "Scores"
        self.PERSONAL_HIGH_SCORES: str = "Personal Top Scores"
        self.FETCH: str = "fetchHighScores"
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation) -> None:
        super().__init__()
        self._init_fields()
        self.abeClientInformation = abeClientInformation
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        self.logUtil.putF("Getting Local HighScores", self, self.FETCH)
        self.fetchHighScoresPreload(gameInfo, highScoresResultsListener, True)
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
        from org.allbinary.game.score.ScoreComparator import ScoreComparator
        try:
            self.highScoresArray[0] = RecordStoreHighScores.getInstance(self.abeClientInformation, gameInfo, self.TOP, self.PERSONAL_HIGH_SCORES, self.SCORES, ScoreComparator(True))
            highScoresResultsListener.setHighScoresArray(self.highScoresArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.FETCH, e)
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        from org.allbinary.game.score.HighScoresHelper2 import HighScoresHelper2
        return HighScoresHelper2()
    

    @staticmethod
    def loaded(index2: int) -> bool:
        if index2 >= 0:
            return True
        return False
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


