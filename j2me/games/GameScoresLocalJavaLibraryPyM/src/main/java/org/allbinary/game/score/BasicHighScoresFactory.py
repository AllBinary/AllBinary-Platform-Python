# Generated Code Do Not Modify
# package org.allbinary.game.score

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.score.HighScoresBase import HighScoresBase


@java_inherited_overloads
class BasicHighScoresFactory(HighScoresBase):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("abeClientInformation", None)
        vars(self).setdefault("highScoresArray", None)
        vars(self).setdefault("TOP", None)
        vars(self).setdefault("SCORES", None)
        vars(self).setdefault("PERSONAL_HIGH_SCORES", None)
        vars(self).setdefault("FETCH", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "abeClientInformation" not in vars(self): self.abeClientInformation: AbeClientInformationInterface = None
        self.highScoresArray: list[HighScores] = [None] * (1)
        self.TOP: str = "Top"
        self.SCORES: str = "Scores"
        self.PERSONAL_HIGH_SCORES: str = "Personal Top Scores"
        self.FETCH: str = "fetchHighScores"
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        super().__init__()
        __class__._init_fields(self)
        self.abeClientInformation = abeClientInformation
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        from org.allbinary.game.GameInfo import GameInfo
        self.logUtil.putF("Getting Local HighScores", self, self.FETCH)
        self.fetchHighScoresPreload(gameInfo, highScoresResultsListener, True)
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
        from org.allbinary.game.score.ScoreComparator import ScoreComparator
        from org.allbinary.game.GameInfo import GameInfo
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
# from org.allbinary.game.GameInfo import GameInfo
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


