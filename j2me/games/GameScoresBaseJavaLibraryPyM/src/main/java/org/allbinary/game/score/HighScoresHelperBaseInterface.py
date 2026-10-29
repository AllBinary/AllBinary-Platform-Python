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

from org.allbinary.game.score.HighScoresResultsListener import HighScoresResultsListener


# Java interface
class HighScoresHelperBaseInterface(HighScoresResultsListener):
    

    def setSelectedHighScores(self, selectedHighScores: HighScores) -> None:
        raise NotImplementedError()
    

    def getHighScoresArray(self) -> list[HighScores]:
        raise NotImplementedError()
    

    def getSelectedHighScores(self) -> HighScores:
        raise NotImplementedError()


