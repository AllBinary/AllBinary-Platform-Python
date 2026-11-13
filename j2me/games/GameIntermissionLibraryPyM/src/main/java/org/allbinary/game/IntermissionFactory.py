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

from java.lang.JavaRuntimeStatic import lazy_static


class IntermissionFactory:
    instance: IntermissionFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.game.state.GameState import GameState
        from org.allbinary.game.state.GameStateFactory import GameStateFactory
        self.START_LEVEL_INTERMISSION_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("START_LEVEL_INTERMISSION_GAME_STATE")
        self.WAIT_LEVEL_INTERMISSION_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("WAIT_LEVEL_INTERMISSION_GAME_STATE")
        self.SHOW_RESULTS_LEVEL_INTERMISSION_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("SHOW_RESULTS_LEVEL_INTERMISSION_GAME_STATE")
        self.SHOW_HIGH_SCORE_LEVEL_INTERMISSION_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("SHOW_HIGH_SCORE_LEVEL_INTERMISSION_GAME_STATE")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> IntermissionFactory:
        return IntermissionFactory.instance
# from org.allbinary.game.state.GameState import GameState
# from org.allbinary.game.state.GameStateFactory import GameStateFactory


def _IntermissionFactory_instance() -> object:
    return IntermissionFactory()

lazy_static(IntermissionFactory, "instance", _IntermissionFactory_instance)

