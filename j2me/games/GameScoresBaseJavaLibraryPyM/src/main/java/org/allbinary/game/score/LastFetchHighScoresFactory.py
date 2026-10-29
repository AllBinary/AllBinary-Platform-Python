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

from org.allbinary.logic.NullUtil import NullUtil


class LastFetchHighScoresFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.highScoresArray: list[HighScores] = NoHighScoresFactory.getInstance().NO_HIGH_SCORES

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LastFetchHighScoresFactory:
        if LastFetchHighScoresFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            LastFetchHighScoresFactory.instance = LastFetchHighScoresFactory()
        return LastFetchHighScoresFactory.instance
from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory


