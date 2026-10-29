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
from org.allbinary.game.score.remote.RemoteHighScoresSubmissionProcessorInterface import RemoteHighScoresSubmissionProcessorInterface


class RemoteHighScoresSubmissionProcessor(RemoteHighScoresSubmissionProcessorInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.noCrypt: NoCrypt = NoCrypt()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def process(self, remoteHighScores: RemoteHighScores, abeClientInformation: AbeClientInformationInterface, highScore: HighScore) -> None:
        with self._lock:
            return self._process_unlocked(remoteHighScores, abeClientInformation, highScore)

    def _process_unlocked(self, remoteHighScores: RemoteHighScores, abeClientInformation: AbeClientInformationInterface, highScore: HighScore) -> None:
        from org.allbinary.game.score.remote.RemoteHighScoresData import RemoteHighScoresData
        from org.allbinary.game.score.remote.RemoteHighScoresData import RemoteHighScoresData
        from org.allbinary.game.score.remote.RemoteHighScoresData import RemoteHighScoresData
        from org.allbinary.game.score.remote.RemoteHighScoresData import RemoteHighScoresData
        from org.allbinary.game.score.remote.XmlRpcRemoteHighScoresClient import XmlRpcRemoteHighScoresClient
        try:
            self.logUtil.putF("Begin Remote HighScores Submission", self, self.commonStrings.PROCESS)
            gameInfoData: GameInfoData = GameInfoData.getInstance()
            hashtable: ABHashtable[object, object] = abeClientInformation.toHashtable()
            HashtableUtil.getInstance().putAll(highScore.getGameInfo().toHashtable(), hashtable)
            hashtable.put(RemoteHighScoresData.getInstance().CUSTOMER_USER_NAME, "None")
            hashtable.put(RemoteHighScoresData.getInstance().DISPLAY_NAME, highScore.getName())
            hashtable.put(gameInfoData.SOFTWARE_INFORMATION, str(remoteHighScores.getSoftwareInformation()))
            hashtable.put(remoteHighScores.ASCENDING, str(remoteHighScores.getAscending()))
            displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
            hashtable.put(displayInfoSingleton.ORIENTATION, BooleanFactory.getInstance().toStringb(displayInfoSingleton.isPortrait()))
            hashtable.put(RemoteHighScoresData.getInstance().GAME_CONFIGURATION, str(GameConfigurationCentral.getInstance()))
            hashtable.put(RemoteHighScoresData.getInstance().SCORE, str(highScore.getScore()))
            if XmlRpcAbeClient.isOnline:
                resultHashtable: ABHashtable[object, object] = XmlRpcRemoteHighScoresClient(abeClientInformation, "highscoresubmissionservicessl.php", "HighScoreSubmissionService.process").get(hashtable, self.noCrypt)
                remoteHighScores.update(resultHashtable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
from org.allbinary.game.GameInfoData import GameInfoData
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.game.score.HighScore import HighScore
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.xmlrpc.XmlRpcAbeClient import XmlRpcAbeClient
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.system.security.crypt.jcehelper.NoCrypt import NoCrypt
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.HashtableUtil import HashtableUtil


