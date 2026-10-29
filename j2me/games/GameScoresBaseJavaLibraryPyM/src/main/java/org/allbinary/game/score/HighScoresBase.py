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

from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface


class HighScoresBase(HighScoresFactoryInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        raise RuntimeError()
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        raise RuntimeError()
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        raise RuntimeError()
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.string.CommonStrings import CommonStrings


