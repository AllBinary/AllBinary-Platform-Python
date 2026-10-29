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
# package org.allbinary.game

from __future__ import annotations

from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.GameMode import GameMode
from org.allbinary.game.PlayerTypesFactory import PlayerTypesFactory


class GameInfo:
    NONE: GameInfo = None
    LEVEL_NAME: str = "LEVEL"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameInfoData: GameInfoData = GameInfoData.getInstance()
        self.gameType: GameType = None
        self.gameMode: GameMode = None
        self.playerType: PlayerType = None
        self.highestLevel: int = 0
        self.currentLevel: int = None
        self.NEW_LEVEL: str = "New Level: "
        self.SET_CURRENT_LEVEL: str = "setCurrentLevel"
        self.NEXT_GAME_LEVEL: str = "nextGameLevel"
    

    def __init__(self, gameType: GameType, gameMode: GameMode, playerType: PlayerType, highestLevel: int, currentLevel: int) -> None:
        self._init_fields()
        self.gameType = gameType
        self.gameMode = gameMode
        self.setHighestLevel(highestLevel)
        self.currentLevel = currentLevel
        self.playerType = playerType
    

    def getGameType(self) -> GameType:
        return self.gameType
    

    def getGameMode(self) -> GameMode:
        return self.gameMode
    

    def getPlayerType(self) -> PlayerType:
        return self.playerType
    

    def getHighestLevel(self) -> int:
        return self.highestLevel
    

    def setHighestLevel(self, highestLevel: int) -> None:
        self.highestLevel = highestLevel
    

    def getCurrentLevel(self) -> int:
        return self.currentLevel
    

    def setCurrentLevel(self, currentLevel: int) -> None:
        self.currentLevel = currentLevel
        self.logUtil.putF(str(StringMaker().append(self.NEW_LEVEL).appendint(self.getCurrentLevel())), self, self.SET_CURRENT_LEVEL)
    

    def nextGameLevel(self) -> None:
        if self.getCurrentLevel() < self.getHighestLevel():
            self.currentLevel += 1
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().NEXT).append(CommonSeps.getInstance().SPACE).append(self.NEW_LEVEL).appendint(self.getCurrentLevel())), self, self.NEXT_GAME_LEVEL)
    

    def previousGameLevel(self) -> None:
        if self.getCurrentLevel() > 1:
            self.currentLevel -= 1
    

    def isLastLevel(self) -> bool:
        if self.getCurrentLevel() >= self.getHighestLevel():
            return True
        else:
            return False
    

    def toHashtable(self) -> ABHashtable[object, object]:
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        hashtable.put(self.gameInfoData.GAME_TYPE, str(self.getGameType()))
        hashtable.put(self.gameInfoData.GAME_MODE, str(self.gameMode))
        hashtable.put(self.gameInfoData.PLAYER_TYPE, str(self.playerType))
        hashtable.put(self.gameInfoData.HIGHEST_LEVEL, str(self.getHighestLevel()))
        hashtable.put(self.gameInfoData.CURRENT_LEVEL, str(self.currentLevel))
        return hashtable
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append(self.gameInfoData.GAME_TYPE)
        stringBuffer.append(commonSeps.EQUALS)
        stringBuffer.append(str(self.getGameType()))
        stringBuffer.append(commonSeps.COMMA_SEP)
        stringBuffer.append(self.gameInfoData.GAME_MODE)
        stringBuffer.append(commonSeps.EQUALS)
        stringBuffer.append(str(self.gameMode))
        stringBuffer.append(commonSeps.COMMA_SEP)
        stringBuffer.append(self.gameInfoData.PLAYER_TYPE)
        stringBuffer.append(commonSeps.EQUALS)
        stringBuffer.append(StringUtil.getInstance().toString(self.playerType))
        stringBuffer.append(commonSeps.COMMA_SEP)
        stringBuffer.append(self.gameInfoData.HIGHEST_LEVEL)
        stringBuffer.append(commonSeps.EQUALS)
        stringBuffer.appendint(self.getHighestLevel())
        stringBuffer.append(commonSeps.COMMA_SEP)
        stringBuffer.append(self.gameInfoData.CURRENT_LEVEL)
        stringBuffer.append(commonSeps.EQUALS)
        stringBuffer.appendint(self.currentLevel)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.game.GameInfoData import GameInfoData


GameInfo.NONE = GameInfo(GameTypeFactory.getInstance().NONE, GameMode.NONE, PlayerTypesFactory.getInstance().PLAYER_TYPE_ONE, -1, -1)

