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
# package org.allbinary.game.score.displayable

from __future__ import annotations

# from javax.microedition.lcdui.Command import Command
from org.allbinary.game.score.HighScoresResultsListener import HighScoresResultsListener
from org.allbinary.logic.string.StringUtil import StringUtil


class HighScoreUtil(HighScoresResultsListener):
    SUBMIT_TEXTBOX_COMMAND: Command = Command("Submit", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.highScoresFactoryInterface: HighScoresFactoryInterface = None
        self.highScoresArray: list[HighScores] = None
        self.highScore: HighScore = None
        self.abeClientInformation: AbeClientInformationInterface = None
        self.gameInfo: GameInfo = None
        self.highScoresHelper: HighScoresHelperBaseInterface = None
        self.firstTime: bool = True
    

    def __init__(self, highScoresFactoryInterface: HighScoresFactoryInterface, highScoresHelper: HighScoresHelperBaseInterface, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, cmdListener: CommandListener, name: str, highScore: HighScore) -> None:
        self._init_fields()
        self.highScoresFactoryInterface = highScoresFactoryInterface
        self.highScoresHelper = highScoresHelper
        self.highScoresArray = self.highScoresHelper.getHighScoresArray()
        self.highScore = highScore
        self.abeClientInformation = abeClientInformation
        self.gameInfo = gameInfo
    

    def setHighScoresArray(self, highScoresArray: list[HighScores]) -> None:
        self.highScoresArray = highScoresArray
        self.firstTime = False
        self.saveHighScore()
    

    def update(self, name: str) -> None:
        HighScoreNamePersistanceSingleton.getInstance().save(self.abeClientInformation, self.gameInfo, name)
        self.highScore.setName(name)
    

    def saveHighScore(self) -> None:
        self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(StringUtil.getInstance().toString(self.highScore))), self, "saveHighScore")
        size: int = len(self.highScoresArray)
        if self.firstTime and size == 0:
            self.logUtil.putF("Games canvas did not give us any HighScores", self, "saveHighScore")
            self.highScoresFactoryInterface.fetchHighScores(self.gameInfo, self)
            return
        highScores: HighScores = None
        highScoresAsString: str = None
        for index in range(0, size):
            highScores = self.highScoresArray[index]
            highScores.addHighScore(self.highScore)
            highScoresAsString = str(highScores)
            self.logUtil.putF(str(StringMaker().append("Added/Adding Score: ").append(highScoresAsString)), self, "saveHighScore")
        self.highScoresHelper.setHighScoresArray(self.highScoresArray)
    

    def submit(self, myCanvas: MyCanvas) -> None:
        commandListener: CommandListener = myCanvas.getCustomCommandListener()
        commandListener.commandAction(HighScoreUtil.SUBMIT_TEXTBOX_COMMAND, myCanvas)
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.score.HighScore import HighScore
from org.allbinary.game.score.HighScoreNamePersistanceSingleton import HighScoreNamePersistanceSingleton
from org.allbinary.game.score.HighScores import HighScores
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.game.score.HighScoresHelperBaseInterface import HighScoresHelperBaseInterface
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


