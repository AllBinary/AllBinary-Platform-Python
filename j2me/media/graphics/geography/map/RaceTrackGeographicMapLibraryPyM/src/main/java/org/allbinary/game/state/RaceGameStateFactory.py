# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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


class RaceGameStateFactory:
    instance: object = None

    def _init_fields(self) -> None:
        self.START_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("START_GAME_STATE")
        self.YELLOW_LIGHT_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("YELLOW_LIGHT_GAME_STATE")
        self.RED_LIGHT_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("RED_LIGHT_GAME_STATE")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RaceGameStateFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if RaceGameStateFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            RaceGameStateFactory.instance = RaceGameStateFactory()
        return RaceGameStateFactory.instance
# from org.allbinary.logic.NullUtil import NullUtil


def _RaceGameStateFactory_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(RaceGameStateFactory, "instance", _RaceGameStateFactory_instance)

