# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.game.score.HighScoresHelperBaseInterface import HighScoresHelperBaseInterface


class HighScoresHelperBase(HighScoresHelperBaseInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.highScoresArrayP: list[HighScores] = LastFetchHighScoresFactory.getInstance().highScoresArray

    def __init__(self) -> None:
        self._init_fields()
    

    def setHighScoresArray(self, highScoresArrayP: list[HighScores]) -> None:
        if highScoresArrayP is not None:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(str(StringMaker().append(commonStrings.START).appendint(len(highScoresArrayP))), self, "setHighScoresArray")
        else:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, "setHighScoresArray")
        self.highScoresArrayP = highScoresArrayP
    

    def getNextHighScores(self) -> HighScores:
        from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
        return NullHighScoresSingletonFactory.getInstance()
    

    def isAnyHighScores(self) -> bool:
        raise RuntimeError()
    

    def setSelectedHighScores(self, selectedHighScores: HighScores) -> None:
        pass
    

    def getSelectedHighScores(self) -> HighScores:
        from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
        return NullHighScoresSingletonFactory.getInstance()
    

    def getHighScoresArray(self) -> list[HighScores]:
        return self.highScoresArrayP
    

    def selectHighScores(self) -> None:
        pass
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.score.LastFetchHighScoresFactory import LastFetchHighScoresFactory


