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



class BasicHighScoresGameInfoFactory:
    SINGLETON: BasicHighScoresGameInfoFactory = None

    def _init_fields(self) -> None:
        self.MULTI_PLAYER_SERVER: GameInfo = GameInfo(GameTypeFactory.getInstance().MULTI_PLAYER, GameMode.SERVER, PlayerTypesFactory.getInstance().PLAYER_TYPE_ONE, 0, 0)
        self.SINGLE_PLAYER_SERVER: GameInfo = GameInfo(GameTypeFactory.getInstance().SINGLE_PLAYER, GameMode.SERVER, PlayerTypesFactory.getInstance().PLAYER_TYPE_ONE, 0, 0)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicHighScoresGameInfoFactory:
        return BasicHighScoresGameInfoFactory.SINGLETON
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.GameMode import GameMode
from org.allbinary.game.PlayerTypesFactory import PlayerTypesFactory


BasicHighScoresGameInfoFactory.SINGLETON = BasicHighScoresGameInfoFactory()

