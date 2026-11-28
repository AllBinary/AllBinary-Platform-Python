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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.score.HighScoresBase import HighScoresBase


@java_inherited_overloads
class BasicHighScoresFactory(HighScoresBase):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("abeClientInformation", None)
        vars(self).setdefault("softwareInformation", None)
        vars(self).setdefault("highScoresArray", None)
        vars(self).setdefault("TOP", None)
        vars(self).setdefault("SCORES", None)
        vars(self).setdefault("PERSONAL_HIGH_SCORES", None)
        vars(self).setdefault("WORLD_TOP_SCORES", None)
        vars(self).setdefault("FETCH", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "abeClientInformation" not in vars(self): self.abeClientInformation: AbeClientInformationInterface = None
        if "softwareInformation" not in vars(self): self.softwareInformation: SoftwareInformation = None
        self.highScoresArray: list[HighScores] = [None] * (2)
        self.TOP: str = "Top"
        self.SCORES: str = "Scores"
        self.PERSONAL_HIGH_SCORES: str = "Personal Top Scores"
        self.WORLD_TOP_SCORES: str = "World Top Scores"
        self.FETCH: str = "fetchHighScores"
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        super().__init__()
        __class__._init_fields(self)
        self.abeClientInformation = abeClientInformation
        self.softwareInformation = softwareInformation
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        from org.allbinary.game.GameInfo import GameInfo
        self.logUtil.putF("Getting Remote/Local HighScores", self, self.FETCH)
        self.fetchHighScoresPreload(gameInfo, highScoresResultsListener, True)
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
        from org.allbinary.game.score.ScoreComparator import ScoreComparator
        from org.allbinary.game.score.LastFetchHighScoresFactory import LastFetchHighScoresFactory
        from org.allbinary.thread.ARunnable import ARunnable
        from org.allbinary.game.BasicHighScoresGameInfoFactory import BasicHighScoresGameInfoFactory
        from org.allbinary.game.GameInfo import GameInfo
        from org.allbinary.game.GameType import GameType
        from org.allbinary.game.GameTypeFactory import GameTypeFactory
        from org.allbinary.game.score.remote.RemoteHighScores import RemoteHighScores
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool
        _java_listener_owner = self
        class _JavaListenerN66612(ARunnable):
            
            

            def run(self) -> None:
                from org.allbinary.game.score.RecordStoreHighScores import RecordStoreHighScores
                from org.allbinary.game.score.ScoreComparator import ScoreComparator
                from org.allbinary.game.score.LastFetchHighScoresFactory import LastFetchHighScoresFactory
                from org.allbinary.game.BasicHighScoresGameInfoFactory import BasicHighScoresGameInfoFactory
                from org.allbinary.game.GameInfo import GameInfo
                from org.allbinary.game.GameType import GameType
                from org.allbinary.game.GameTypeFactory import GameTypeFactory
                from org.allbinary.game.score.remote.RemoteHighScores import RemoteHighScores
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    logUtil.putF(_java_listener_owner.commonStrings.START, self, _java_listener_owner.FETCH)
                    _java_listener_owner.highScoresArray[0] = RecordStoreHighScores.getInstance(_java_listener_owner.abeClientInformation, gameInfo, _java_listener_owner.TOP, _java_listener_owner.PERSONAL_HIGH_SCORES, _java_listener_owner.SCORES, ScoreComparator(True))
                    gameType: GameType = gameInfo.getGameType()
                    gameTypeFactory: GameTypeFactory = GameTypeFactory.getInstance()
                    gameInfo2: GameInfo = gameInfo
                    if gameType == gameTypeFactory.SINGLE_PLAYER or gameType == gameTypeFactory.BOT:
                        gameInfo2 = BasicHighScoresGameInfoFactory.getInstance().SINGLE_PLAYER_SERVER
                    elif gameType == gameTypeFactory.MULTI_PLAYER:
                        gameInfo2 = BasicHighScoresGameInfoFactory.getInstance().MULTI_PLAYER_SERVER
                    _java_listener_owner.highScoresArray[1] = RemoteHighScores.getInstancePreload(_java_listener_owner.abeClientInformation, _java_listener_owner.softwareInformation, gameInfo2, _java_listener_owner.WORLD_TOP_SCORES, _java_listener_owner.SCORES, BooleanFactory.getInstance().FALSE, preload)
                    logUtil.putF(_java_listener_owner.commonStrings.END, self, _java_listener_owner.FETCH)
                    LastFetchHighScoresFactory.getInstance().highScoresArray = _java_listener_owner.highScoresArray
                    highScoresResultsListener.setHighScoresArray(_java_listener_owner.highScoresArray)
                except Exception as e:
                    logUtil.put((self if hasattr(self, "commonStrings") else _java_listener_owner).commonStrings.EXCEPTION, self, _java_listener_owner.FETCH, e)
        SecondaryThreadPool.getInstance().runTask(_JavaListenerN66612()
            )
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        from org.allbinary.game.score.HighScoresHelper2 import HighScoresHelper2
        return HighScoresHelper2()
    

    @staticmethod
    def loaded(index2: int) -> bool:
        if index2 >= 0:
            return True
        return False
# from org.allbinary.thread.ARunnable import ARunnable
# from org.allbinary.game.BasicHighScoresGameInfoFactory import BasicHighScoresGameInfoFactory
# from org.allbinary.game.GameInfo import GameInfo
# from org.allbinary.game.GameType import GameType
# from org.allbinary.game.GameTypeFactory import GameTypeFactory
# from org.allbinary.game.score.remote.RemoteHighScores import RemoteHighScores
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool


