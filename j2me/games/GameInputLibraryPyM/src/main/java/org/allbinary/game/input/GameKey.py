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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.input.Input import Input


class GameKey(Input):
    NULL_GAME_KEY: GameKey = None
    

    def __init__(self, key: int, name: str) -> None:
        super().__init__(key, name)
    

    def toString(self) -> str:
        return str(StringMaker().append("GameKey ").append(str(super())))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


GameKey.NULL_GAME_KEY = GameKey(-1, StringUtil.getInstance().NULL_STRING)

