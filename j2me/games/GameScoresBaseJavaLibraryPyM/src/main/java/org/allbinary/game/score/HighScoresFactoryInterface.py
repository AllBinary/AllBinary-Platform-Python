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



# Java interface
class HighScoresFactoryInterface:
    

    def fetchHighScores(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener) -> None:
        raise NotImplementedError()
    

    def fetchHighScoresPreload(self, gameInfo: GameInfo, highScoresResultsListener: HighScoresResultsListener, preload: bool) -> None:
        raise NotImplementedError()
    

    def createHighScoresHelper(self) -> HighScoresHelperBaseInterface:
        raise NotImplementedError()
from org.allbinary.game.GameInfo import GameInfo


