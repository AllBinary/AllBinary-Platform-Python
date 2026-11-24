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

from java.lang.JavaRuntimeStatic import lazy_static


class RemoteErrorHighScoresSingletonFactory:
    SINGLETON: HighScores = None
    

    @staticmethod
    def getInstance() -> HighScores:
        return RemoteErrorHighScoresSingletonFactory.SINGLETON
# from org.allbinary.string.CommonStrings import CommonStrings


def _RemoteErrorHighScoresSingletonFactory_SINGLETON() -> object:
    from org.allbinary.game.score.HighScores import HighScores
    from org.allbinary.string.CommonStrings import CommonStrings
    return HighScores(CommonStrings.getInstance().LOADING, "Remote High Scores Did Not Load", CommonStrings.getInstance().PERIODS)

lazy_static(RemoteErrorHighScoresSingletonFactory, "SINGLETON", _RemoteErrorHighScoresSingletonFactory_SINGLETON)

