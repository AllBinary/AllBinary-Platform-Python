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



class GameTypeFactory:
    instance: GameTypeFactory = None

    def _init_fields(self) -> None:
        self.NULL_GAME_TYPE_ARRAY: list[GameType] = [None] * (0)
        self.NONE: GameType = GameType(StringUtil.getInstance().NULL_STRING)
        self.SINGLE_PLAYER: GameType = GameType("Single Player")
        self.MULTI_PLAYER: GameType = GameType("Multi Player")
        self.BOT: GameType = GameType("Artificial Player")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameTypeFactory:
        return GameTypeFactory.instance
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.GameType import GameType


GameTypeFactory.instance = GameTypeFactory()

