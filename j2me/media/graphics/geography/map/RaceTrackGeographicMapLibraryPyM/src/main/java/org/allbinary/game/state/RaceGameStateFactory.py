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

from org.allbinary.logic.NullUtil import NullUtil


class RaceGameStateFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.START_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("START_GAME_STATE")
        self.YELLOW_LIGHT_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("YELLOW_LIGHT_GAME_STATE")
        self.RED_LIGHT_GAME_STATE: GameState = GameStateFactory.getInstance().createGameState("RED_LIGHT_GAME_STATE")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RaceGameStateFactory:
        if RaceGameStateFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            RaceGameStateFactory.instance = RaceGameStateFactory()
        return RaceGameStateFactory.instance
from org.allbinary.game.state.GameStateFactory import GameStateFactory


