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
# package org.allbinary.game.state

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameStateFactory:
    instance: object = None

    def _init_fields(self) -> None:
        self.index: int = 0
        self.NO_GAME_STATE: GameState = self.createGameState("NO_GAME_STATE")
        self.PLAYING_GAME_STATE: GameState = self.createGameState("PLAYING_GAME_STATE")
        self.SHOW_END_RESULT_GAME_STATE: GameState = self.createGameState("SHOW_END_RESULT_GAME_STATE")
        self.SHOW_HIGH_SCORE_GAME_STATE: GameState = self.createGameState("SHOW_HIGH_SCORE_GAME_STATE")
    

    @staticmethod
    def getInstance() -> GameStateFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if GameStateFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GameStateFactory.instance = GameStateFactory()
        return GameStateFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def createGameState(self, name: str) -> GameState:
        from org.allbinary.game.state.GameState import GameState
        return GameState(name, ((setattr(self, "index", self.index + 1) or self.index) - 1))
# from org.allbinary.logic.NullUtil import NullUtil


def _GameStateFactory_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(GameStateFactory, "instance", _GameStateFactory_instance)

