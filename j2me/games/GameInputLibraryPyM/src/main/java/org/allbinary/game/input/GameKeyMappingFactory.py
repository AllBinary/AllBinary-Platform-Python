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

from org.allbinary.logic.NullUtil import NullUtil


class GameKeyMappingFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.intKeyToGameKey: list[GameKey] = [None] * (InputFactory.getInstance().MAX)
    

    @staticmethod
    def getInstance() -> GameKeyMappingFactory:
        if GameKeyMappingFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GameKeyMappingFactory.instance = GameKeyMappingFactory()
        return GameKeyMappingFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
        self._init_fields()
        gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
        self.setGameKey(gameKeyFactory.NONE)
        self.setGameKey(gameKeyFactory.UP)
        self.setGameKey(gameKeyFactory.DOWN)
        self.setGameKey(gameKeyFactory.LEFT)
        self.setGameKey(gameKeyFactory.RIGHT)
        self.setGameKey(gameKeyFactory.KEY_POUND)
        self.setGameKey(gameKeyFactory.KEY_STAR)
        self.setGameKey(gameKeyFactory.KEY_NUM0)
        self.setGameKey(gameKeyFactory.KEY_NUM1)
        self.setGameKey(gameKeyFactory.KEY_NUM2)
        self.setGameKey(gameKeyFactory.KEY_NUM3)
        self.setGameKey(gameKeyFactory.KEY_NUM4)
        self.setGameKey(gameKeyFactory.KEY_NUM5)
        self.setGameKey(gameKeyFactory.KEY_NUM6)
        self.setGameKey(gameKeyFactory.KEY_NUM7)
        self.setGameKey(gameKeyFactory.KEY_NUM8)
        self.setGameKey(gameKeyFactory.KEY_NUM9)
        self.setGameKey(gameKeyFactory.GAME_A)
        self.setGameKey(gameKeyFactory.GAME_B)
        self.setGameKey(gameKeyFactory.GAME_C)
        self.setGameKey(gameKeyFactory.GAME_D)
        self.setGameKey(gameKeyFactory.FIRE)
        self.setGameKey(gameKeyFactory.LEVEL_DOWN)
        self.setGameKey(gameKeyFactory.LEVEL_UP)
    

    def getGameKey(self, key: int) -> GameKey:
        return self.intKeyToGameKey[key]
    

    def setGameKey(self, gameKey: GameKey) -> None:
        self.intKeyToGameKey[gameKey.getId()] = gameKey
from org.allbinary.game.input.InputFactory import InputFactory


