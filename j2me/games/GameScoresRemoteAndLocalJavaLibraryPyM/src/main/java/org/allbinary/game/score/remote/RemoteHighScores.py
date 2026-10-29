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
# package org.allbinary.game.score.remote

from __future__ import annotations

import threading
from org.allbinary.game.score.HighScores import HighScores
from org.allbinary.logic.StdUtil import StdUtil


class RemoteHighScores(HighScores):
    hashTable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
        self.softwareInformation: SoftwareInformation = None
        self.ascending: bool = None
        self.ASCENDING: str = "ASCENDING"
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation, gameInfo: GameInfo, heading: str, columnTwoHeading: str, ascending: bool, preload: bool) -> None:
        from org.allbinary.game.score.remote.RemoteHighScoresProcessorFactory import RemoteHighScoresProcessorFactory
        super().__init__(str(gameInfo), heading, columnTwoHeading)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.softwareInformation = softwareInformation
        self.setAscending(ascending)
        if preload:
            RemoteHighScoresProcessorFactory.getInstance().process(self, self.abeClientInformation, gameInfo)
    

    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation, gameInfo: GameInfo, heading: str, columnTwoHeading: str, isAscending: bool) -> HighScores:
        with RemoteHighScores._lock:
            return RemoteHighScores._getInstance_unlocked(abeClientInformation, softwareInformation, gameInfo, heading, columnTwoHeading, isAscending)

    @staticmethod
    def _getInstance_unlocked(abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation, gameInfo: GameInfo, heading: str, columnTwoHeading: str, isAscending: bool) -> HighScores:
        return RemoteHighScores.getInstancePreload(abeClientInformation, softwareInformation, gameInfo, heading, columnTwoHeading, isAscending, True)
    

    @staticmethod
    def getInstancePreload(abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation, gameInfo: GameInfo, heading: str, columnTwoHeading: str, isAscending: bool, preload: bool) -> HighScores:
        with RemoteHighScores._lock:
            return RemoteHighScores._getInstancePreload_unlocked(abeClientInformation, softwareInformation, gameInfo, heading, columnTwoHeading, isAscending, preload)

    @staticmethod
    def _getInstancePreload_unlocked(abeClientInformation: AbeClientInformationInterface, softwareInformation: SoftwareInformation, gameInfo: GameInfo, heading: str, columnTwoHeading: str, isAscending: bool, preload: bool) -> HighScores:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            highScores: HighScores = RemoteHighScores.hashTable.get(gameInfo)
            if highScores is None:
                highScores = RemoteHighScores(abeClientInformation, softwareInformation, gameInfo, heading, columnTwoHeading, isAscending, preload)
                RemoteHighScores.hashTable.put(gameInfo, highScores)
            return highScores
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, RemoteErrorHighScoresSingletonFactory.getInstance(), commonStrings.GET_INSTANCE, e)
            return RemoteErrorHighScoresSingletonFactory.getInstance()
    

    def addHighScore(self, newHighScore: HighScore) -> None:
        from org.allbinary.game.score.remote.RemoteHighScoresSubmissionProcessorFactory import RemoteHighScoresSubmissionProcessorFactory
        RemoteHighScoresSubmissionProcessorFactory.getInstance().process(self, self.abeClientInformation, newHighScore)
    

    def update(self, hashtable: ABHashtable[object, object]) -> None:
        from org.allbinary.game.score.remote.RemoteHighScoresData import RemoteHighScoresData
        self.getList().clear()
        vector: BasicArrayList = hashtable.get(RemoteHighScoresData.getInstance().HIGH_SCORES)
        if vector is not None:
            size: int = vector.size()
            for index in range(0, size):
                highScoreVector: BasicArrayList = vector.get(index)
                displayName: str = highScoreVector.get(0)
                score: str = highScoreVector.get(1)
                longScore: int = int(score)
                highScore: HighScore = HighScore(-1, displayName, None, longScore)
                self.getList().add(highScore)
        else:
            NEXT_ELEMENT: str = str(StringMaker().append(CommonLabels.getInstance().NEXT).append("Element: "))
            commonStrings: CommonStrings = CommonStrings.getInstance()
            enumeration: Enumeration = hashtable.elements()
            nextElement: object = None
            while self.enumerationUtil.hasMoreElements(enumeration):
                nextElement = self.enumerationUtil.nextElement(enumeration)
                self.logUtil.putF(NEXT_ELEMENT + str(nextElement), self, commonStrings.PROCESS)
    

    def setAscending(self, ascending: bool) -> None:
        self.ascending = ascending
    

    def getAscending(self) -> bool:
        return self.ascending
    

    def getSoftwareInformation(self) -> SoftwareInformation:
        return self.softwareInformation
# from java.util.Enumeration import Enumeration
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.score.HighScore import HighScore
from org.allbinary.game.score.RemoteErrorHighScoresSingletonFactory import RemoteErrorHighScoresSingletonFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.EnumerationUtil import EnumerationUtil


