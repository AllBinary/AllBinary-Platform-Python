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


class BasicHighScoresFactory(HighScoresBase):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
        self.softwareInformation: SoftwareInformation = None
        self.highScoresArray: list[HighScores] = [None] * (2)
        self.TOP: str = "Top"
        self.SCORES: str = "Scores"
        self.PERSONAL_HIGH_SCORES: str = "Personal Top Scores"
        self.WORLD_TOP_SCORES: str = "World Top Scores"
        self.FETCH: str = "fetchHighScores"
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation) -> None:
        super().__init__()
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.softwareInformation = softwareInformation
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        self.logUtil.putF("Getting Remote/Local HighScores", self, self.FETCH)
        self.fetchHighScoresPreload(gameInfo, highScoresResultsListener, True)
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
        from org.allbinary.game.score.ScoreComparator import ScoreComparator
        from org.allbinary.game.score.LastFetchHighScoresFactory import LastFetchHighScoresFactory
        SecondaryThreadPool.getInstance().runTask((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
#                 from org.allbinary.game.score.ScoreComparator import ScoreComparator
#                 from org.allbinary.game.score.LastFetchHighScoresFactory import LastFetchHighScoresFactory
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     logUtil.putF(self.commonStrings.START, self, self.FETCH)
#                     self.highScoresArray[0] = RecordStoreHighScores.getInstance(self.abeClientInformation, gameInfo, self.TOP, self.PERSONAL_HIGH_SCORES, self.SCORES, ScoreComparator(True))
#                     gameType: GameType = gameInfo.getGameType()
#                     gameTypeFactory: GameTypeFactory = GameTypeFactory.getInstance()
#                     gameInfo2: GameInfo = gameInfo
#                     if gameType == gameTypeFactory.SINGLE_PLAYER or gameType == gameTypeFactory.BOT:
#                         gameInfo2 = BasicHighScoresGameInfoFactory.getInstance().SINGLE_PLAYER_SERVER
#                     elif gameType == gameTypeFactory.MULTI_PLAYER:
#                         gameInfo2 = BasicHighScoresGameInfoFactory.getInstance().MULTI_PLAYER_SERVER
#                     self.highScoresArray[1] = RemoteHighScores.getInstancePreload(self.abeClientInformation, self.softwareInformation, gameInfo2, self.WORLD_TOP_SCORES, self.SCORES, BooleanFactory.getInstance().FALSE, preload)
#                     logUtil.putF(self.commonStrings.END, self, self.FETCH)
#                     LastFetchHighScoresFactory.getInstance().highScoresArray = self.highScoresArray
#                     highScoresResultsListener.setHighScoresArray(self.highScoresArray)
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.FETCH, e)
))
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        from org.allbinary.game.score.HighScoresHelper2 import HighScoresHelper2
        return HighScoresHelper2()
    

    @staticmethod
    def loaded(index2: int) -> bool:
        if index2 >= 0:
            return True
        return False
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.game.BasicHighScoresGameInfoFactory import BasicHighScoresGameInfoFactory
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.GameType import GameType
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.score.remote.RemoteHighScores import RemoteHighScores
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool


