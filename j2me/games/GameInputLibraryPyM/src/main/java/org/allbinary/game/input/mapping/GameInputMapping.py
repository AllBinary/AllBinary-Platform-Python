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
# package org.allbinary.game.input.mapping

from __future__ import annotations



class GameInputMapping:

    def _init_fields(self) -> None:
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.gameKey: GameKey = GameKey.NULL_GAME_KEY
    

    def __init__(self, name: str, gameKey: GameKey) -> None:
        self._init_fields()
        self.setName(name)
        self.setGameKey(gameKey)
    

    def setGameKey(self, gameKey: GameKey) -> None:
        self.gameKey = gameKey
    

    def getGameKey(self) -> GameKey:
        return self.gameKey
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.logic.string.StringUtil import StringUtil


